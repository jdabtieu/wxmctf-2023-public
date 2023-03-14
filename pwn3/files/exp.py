from pwn import *

s = remote("localhost", 5000)
s.send(b"aaaaaaaaaaa\n")
s.recvuntil(b"password: ")
s.sendline(b"970")
s.recvuntil(b"btw\n")
info(s.recvallS())
