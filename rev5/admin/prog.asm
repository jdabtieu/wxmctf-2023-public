; This is a comment. The following are directives generated by calling yan85decompile.py with the -d flag.
.REGISTER ya 0x0
.REGISTER yb 0x3
.REGISTER yc 0x1
.REGISTER yd 0x6
.REGISTER ystk 0x2
.REGISTER yip 0x5
.REGISTER yflags 0x4
.FLAG lt 0x4
.FLAG gt 0x2
.FLAG eq 0x1
.FLAG ne 0x8
.SYSCALL read 1
.SYSCALL write 2
.SYSCALL exit 3
.INST interpret_imm 0x0
.INST interpret_add 0x1
.INST interpret_sub 0x2
.INST interpret_xor 0x3
.INST interpret_and 0x4
.INST interpret_or 0x5
.INST interpret_stk 0x6
.INST interpret_stm 0x7
.INST interpret_ldm 0x8
.INST interpret_cmp 0x9
.INST interpret_jmp 0xa
.INST interpret_sys 0xb
.ABI OP 1
.ABI ARG1 0
.ABI ARG2 2

Y_jmp +1
Y_sys [sys_exit]
Y_mov ya, 1
Y_xor yb, yb
Y_mov yc, 16
Y_sys [sys_write] ; write(stdout, "Enter password: ", 16)
Y_xor ya, ya
Y_mov yb, 200
Y_mov yc, 24
Y_sys [sys_read] ; read(stdin, &buf[200], 24)
Y_cmp yd, yc
Y_je +6
Y_mov ya, 1
Y_mov yb, 16
Y_mov yc, 16
Y_sys [sys_write] ; write(stdout, "Wrong password!\n", 16)
Y_xor ya, ya
Y_jmp -17
; start generate from python
Y_mov ya, 200
Y_mov yb, byte [ya]
Y_mov yc, 119
Y_sub yb, yc
Y_mov yc, 96
Y_mov byte[yc], yb
Y_xor yd, yd
Y_mov yb, 200
Y_mov ya, yb
Y_add ya, yd
Y_mov ya, byte [ya]
Y_mov yc, 1
Y_add yd, yc
Y_mov yc, yb
Y_add yc, yd
Y_mov yc, byte [yc]
Y_sub ya, yc
Y_mov yb, 96
Y_add yb, yd
Y_mov byte [yb], ya
Y_mov yb, 24
Y_cmp yd, yb
Y_jne -16
Y_xor yd, yd
Y_mov yb, 64
Y_mov ya, byte [yb]
Y_mov yb, 96
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 65
Y_mov ya, byte [yb]
Y_mov yb, 97
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 66
Y_mov ya, byte [yb]
Y_mov yb, 98
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 67
Y_mov ya, byte [yb]
Y_mov yb, 99
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 68
Y_mov ya, byte [yb]
Y_mov yb, 100
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 69
Y_mov ya, byte [yb]
Y_mov yb, 101
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 70
Y_mov ya, byte [yb]
Y_mov yb, 102
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 71
Y_mov ya, byte [yb]
Y_mov yb, 103
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 72
Y_mov ya, byte [yb]
Y_mov yb, 104
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 73
Y_mov ya, byte [yb]
Y_mov yb, 105
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 74
Y_mov ya, byte [yb]
Y_mov yb, 106
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 75
Y_mov ya, byte [yb]
Y_mov yb, 107
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 76
Y_mov ya, byte [yb]
Y_mov yb, 108
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 77
Y_mov ya, byte [yb]
Y_mov yb, 109
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 78
Y_mov ya, byte [yb]
Y_mov yb, 110
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 79
Y_mov ya, byte [yb]
Y_mov yb, 111
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 80
Y_mov ya, byte [yb]
Y_mov yb, 112
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 81
Y_mov ya, byte [yb]
Y_mov yb, 113
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 82
Y_mov ya, byte [yb]
Y_mov yb, 114
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 83
Y_mov ya, byte [yb]
Y_mov yb, 115
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 84
Y_mov ya, byte [yb]
Y_mov yb, 116
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 85
Y_mov ya, byte [yb]
Y_mov yb, 117
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 86
Y_mov ya, byte [yb]
Y_mov yb, 118
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_mov yb, 87
Y_mov ya, byte [yb]
Y_mov yb, 119
Y_mov yb, byte [yb]
Y_add ya, yb
Y_or yd, ya
Y_xor ya, ya
Y_cmp yd, ya
Y_je +6
Y_mov ya, 1
Y_mov yb, 16
Y_mov yc, 16
Y_sys [sys_write]
Y_xor ya, ya
Y_sys [sys_exit]
Y_mov ya, 1
Y_mov yb, 32
Y_mov yc, 16
Y_sys [sys_write]
Y_jmp -7
.MEMORY 456e7465722070617373776f72643a2057726f6e672070617373776f7264210a57656c636f6d652c206861636b65720a000000000000000000000000000000000001f5f611f215fee80dcafd2a0e0ce60303070307efff19000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
