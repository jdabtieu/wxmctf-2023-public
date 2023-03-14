#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <unistd.h>

typedef unsigned char byte;

#ifndef min
#define min(a,b)            (((a) < (b)) ? (a) : (b))
#endif

struct inst {
    byte a1;
    byte op;
    byte a2;
};

byte term = 0;
struct inst prog[256] = {0};
byte reg[7] = {0, 0, 0, 0, 0, 0, 0};
byte mem[256] = {0};

#define ra 0
#define rb 3
#define rc 1
#define rd 6
#define rs 2
#define ri 5
#define rf 4

void vm_imm(int r, int imm8) {
    reg[r] = (byte) imm8;
}
void vm_add(int r1, int r2) {
    reg[r1] += reg[r2];
}
void vm_sub(int r1, int r2) {
    reg[r1] -= reg[r2];
}
void vm_xor(int r1, int r2) {
    reg[r1] ^= reg[r2];
}
void vm_and(int r1, int r2) {
    reg[r1] &= reg[r2];
}
void vm_or(int r1, int r2) {
    reg[r1] |= reg[r2];
}
void vm_stk(int arg0, int arg1) {
    if (arg0 & 0x10) {
        reg[rs]++;
        mem[reg[rs]] = reg[arg1];
    } else if (arg0 & 0x20) {
        reg[arg1] = mem[reg[rs]];
        reg[rs]--;
    } else {
        reg[arg0] = reg[arg1];
    }
}
void vm_stm(int r1, int r2) {
    mem[reg[r1]] = reg[r2];
}
void vm_ldm(int r1, int r2) {
    reg[r1] = mem[reg[r2]];
}
void vm_cmp(int r1, int r2) {
    reg[rf] = 0;
    byte v1 = reg[r1], v2 = reg[r2];
    if (v1 == v2) reg[rf] |= 0b1;
    if (v1 > v2) reg[rf] |= 0b10;
    if (v1 < v2) reg[rf] |= 0b100;
    if (v1 != v2) reg[rf] |= 0b1000;
}
void vm_jmp(int mask, int dst) {
    if (mask == 0) {
        reg[ri] = dst - 1;
        return;
    } else if (mask == 0b100000) {
        reg[ri] += dst;
        return;
    }
    byte flag = reg[rf];
    byte fmsk = mask & 0b1111;
    if ((flag & fmsk) != fmsk) return;
    if (mask & 0b100000) reg[ri] += dst;
    else reg[ri] = dst - 1;
}
void vm_sys(int sid, int unused) {
    if (sid == 1) {
        int fd = reg[ra];
        void *buf = mem + reg[rb];
        int count = min(reg[rc], 256 - reg[rb]);
        reg[rd] = read(fd, buf, count);
    } else if (sid == 2) {
        int fd = reg[ra];
        void *buf = mem + reg[rb];
        int count = min(reg[rc], 256 - reg[rb]);
        reg[rd] = write(fd, buf, count);
    } else if (sid == 3) {
        term = 1;
    } else {
        printf("Fatal: unknown syscall\n");
        term = 1;
        reg[ra] = 0xff;
    }
}

void (*vm_ops[12])() = {vm_imm, vm_add, vm_sub, vm_xor, vm_and, vm_or, vm_stk, vm_stm, vm_ldm, vm_cmp, vm_jmp, vm_sys};

int vm_loop() {
    while(1) {
        struct inst cur = prog[reg[ri]];
        (*vm_ops[cur.op])(cur.a1, cur.a2);
        if (term) break;
        reg[ri]++;
    }
    return reg[ra];
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: ./vm [prog]\n");
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (f == NULL) {
        printf("Unable to open program file\n");
        return 2;
    }
    byte buf[1030];
    fread(buf, 1, 1030, f);
    if (memcmp(buf, "\x50\x4b\x03\x04\x79\x85", 6)) {
        printf("Invalid program file\n");
        return 3;
    }
    memcpy(prog, buf+6, 256*3);
    memcpy(mem, buf+6+256*3, 256);
    return vm_loop();
}