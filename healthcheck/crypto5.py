from pwn import *
import sys

p = remote(sys.argv[1], int(sys.argv[2]))
p.recvuntil(b"seed")
p.sendline(b"186482063914337")
p.recvuntil(b"Ready")
p.sendline(b"yes")
p.send(b"\x1B[B"*11)
p.sendline(b"\x1B[C"*11)
p.recvuntil(b"Congratulations!")
print(p.recvuntil(b"\n"))
