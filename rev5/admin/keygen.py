flag = "wxmctf{yan85_my_beloved}"

# subtract adjacent characters, then add key to the 23 paired subs so that they all turn into 0
# then or the 23 pairs, should equal 0
# offset:64, len:23 add pairs (0x100 - sub)
# result stored in offset:97

mem = b"Enter password: Wrong password!\nWelcome, hacker\n"
mem += b"\x00"*(64-len(mem))

print("Y_mov ya, 200") # ya = input ptr
print("Y_mov yb, byte [ya]")
print(f"Y_mov yc, {ord('w')}")
print("Y_sub yb, yc")
print("Y_mov yc, 96")
print("Y_mov byte[yc], yb") # move 0 if first char matches
"""
i = d = 0
for (;;) { // i is d
    char *b = 200
    char *a = b
    char *a += i
    char a = *a
    i++
    *c = b
    *c += i
    char c = *c
    a -= c
    char *b = 96
    *b += i
    *b = a
    mov b, 24
    cmp i, b
    jne loop_start
}
"""
print("Y_xor yd, yd")
print("Y_mov yb, 200") # loop start
print("Y_mov ya, yb")
print("Y_add ya, yd")
print("Y_mov ya, byte [ya]")
print("Y_mov yc, 1")
print("Y_add yd, yc")
print("Y_mov yc, yb")
print("Y_add yc, yd")
print("Y_mov yc, byte [yc]")
print("Y_sub ya, yc")
print("Y_mov yb, 96")
print("Y_add yb, yd")
print("Y_mov byte [yb], ya")
print("Y_mov yb, 24")
print("Y_cmp yd, yb")
print("Y_jne -16")
mem += b"\x00"
for i in range(23):
    subres = (ord(flag[i]) - ord(flag[i+1]) + 0x100) % 0x100
    mem += (0x100 - subres).to_bytes(1, "little")
mem += b"\x00"*(256-len(mem))
# 64, 64+24
# 96, 96+24
print("Y_xor yd, yd")
for i in range(24):
    print(f"Y_mov yb, {64+i}")
    print("Y_mov ya, byte [yb]")
    print(f"Y_mov yb, {96+i}")
    print("Y_mov yb, byte [yb]")
    print("Y_add ya, yb")
    print("Y_or yd, ya")
print("Y_xor ya, ya")
print("Y_cmp yd, ya")
print("Y_je +6")
print("Y_mov ya, 1")
print("Y_mov yb, 16")
print("Y_mov yc, 16")
print("Y_sys [sys_write]") # write(stdout, "Wrong password!\n", 16))
print("Y_xor ya, ya")
print("Y_sys [sys_exit]") # exit(0)
print("Y_mov ya, 1")
print("Y_mov yb, 32")
print("Y_mov yc, 16")
print("Y_sys [sys_write]") # write(stdout, "Welcome, hacker\n", 16))
print("Y_jmp -7")
print(".MEMORY " + mem.hex())