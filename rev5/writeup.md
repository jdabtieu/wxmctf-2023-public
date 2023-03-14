# x130 - WxMCTF 2023
![](https://img.shields.io/badge/category-rev-blue) ![](https://img.shields.io/badge/author-jdabtieu-orange)

## Description
64-bit programs and modern x86 CPUs are way too complicated.

If 64-bit is x64 and 32-bit is x86, then 8-bit is x130!

My new x130 architecture is so novel that I'm sure the WLMAC losers can't reverse engineer it.

Hint: the custom architecture is based on/inspired by <https://github.com/jdabtieu/yan85-disassembler> including the optional `.MEMORY` directive, with some key differences

[main](dist/main)

[prog](dist/prog)

## Solution
If you try to run `file` on prog, it will report a zip file, but trying to extract it as a zip will fail. Instead, we can try running main, which tells us to pass prog as an argument. We're told to enter a password (the flag), and after entering some random input, we're told that it's wrong.

To figure out what's going on, we need to reverse engineer `main` using a tool like Ghidra. The binary is stripped for extra pain, but combing through the `main` function and then the other functions, you can slowly piece together the puzzle.
1. The `prog` file has a 6 byte header, after that is $256\*3=768$ bytes of bytecode and 256 bytes of memory.
2. Each instruction is a struct with three bytes: byte 1 is the first argument, byte 2 is the opcode, and byte 3 is the second argument.
3. The register values are stored in an array
  - instruction pointer is index 5
  - stack pointer is index 2
  - eflags register is index 4
  - syscall arg1 is index 0
  - syscall arg2 is index 3
  - syscall arg3 is index 1
  - syscall return value is index 6
  - indices 0, 1, 3, 6 are general purpose registers
4. Syscalls have only one argument equal to the syscall number (1 is read, 2 is write, 3 is exit)
5. For jumps, if the jump mask has the `0x20` bit set, it's a relative jump, otherwise it's an absolute jump.
6. Each register goes up to 256, so the program has at most 256 instructions and 256 memory slots.
7. Unlike x86, registers are preserved after syscalls (except register 6)

After thoroughly debugging the program, you should get something resembling [main.c](admin/main.c). At this point, with the knowledge of the x130 ABI, you'll need to write a disassembler to convert the `prog` file into instructions (and grab the memory while you're at it). You can disassemble into a C-like language and debug by hand or using gdb, or perhaps Python, or anything you want. I chose to disassemble into the yan85 architecture mentioned in the hint because it was similar and came with a gdb-like debugger. Since it is a bit different than x130, I had to change [a bit of code](admin/ctf.patch) to make it work. [This](admin/prog.asm) is the disassembled yan85 assembly. Once again, disassembling into a more familiar syntax like C would have also been fine. The goal of disassembly is to convert the bytecode into *any* readable format.

Because not everyone would have created a working debugger during the contest, I'll stick to debugging by hand. However, GDB (or the patched yan85 debugger) would help a lot in dynamic analysis.

The first few instructions just call a few syscalls. Wrong password is printed if the password length is not 24.
```as
Y_jmp +1
Y_sys [sys_exit]
Y_mov ya, 1
Y_xor yb, yb
Y_mov yc, 16
Y_sys [sys_write] ; write(stdout, "Enter password: ", 16)
Y_xor ya, ya
Y_mov yb, 200
Y_mov yc, 24
Y_sys [sys_read] ; read(stdin, &mem[200], 24)
Y_cmp yd, yc
Y_je +6
Y_mov ya, 1
Y_mov yb, 16
Y_mov yc, 16
Y_sys [sys_write] ; write(stdout, "Wrong password!\n", 16)
Y_xor ya, ya
Y_jmp -17
```
After that is a loop. This loop structure is somewhat similar to gcc loops, but having only 4 registers means there is a lot of register overlap.
```as
Y_mov ya, 200
Y_mov yb, byte [ya] ; move mem[200] into yb (first char of password)
Y_mov yc, 119
Y_sub yb, yc        ; yb -= 119
Y_mov yc, 96
Y_mov byte[yc], yb  ; move yb into mem[96]
Y_xor yd, yd        ; clear yd --> after reading through the loop you'll find that yd is the loop counter, i
Y_mov yb, 200       ; loop start
Y_mov ya, yb
Y_add ya, yd        ; ya = 200 + i
Y_mov ya, byte [ya] ; ya = mem[200+i] or if we consider mem[200] to be the start of input array, input[i]
Y_mov yc, 1
Y_add yd, yc        ; i++ (yes, i is incremented mid loop)
Y_mov yc, yb        ; yc = 201
Y_add yc, yd        ; yc += i
Y_mov yc, byte [yc] ; yc = mem[201+i] (i is old i at the start of the loop) or perhaps better, input[i+1]
Y_sub ya, yc        ; ya = input[i] - input[i+1] (still using old i)
Y_mov yb, 96
Y_add yb, yd
Y_mov byte [yb], ya ; mem[96+i+1] = input[i] - input[i+1] (still old i)
Y_mov yb, 24
Y_cmp yd, yb        ; continue looping if i != 24
Y_jne -16
```
The incrementing of i mid-loop is pretty non-standard, but fiddling with the indexes a bit can help us create a more standard loop. We also figure out at this point that at memory address 96, there is a 24-byte array in addition to the input array at address 200. The above assembly is then identical to:
```c
unsigned char arr[24];
unsigned char input[24];
arr[0] = input[0] - 119;
for (int i = 0; i < 23; i++) {
  arr[i+1] = input[i] - input[i+1];
}
```
Every item after the 0th is set to the difference between adjacent characters in the input. As an aside, even for this one line loop, [gcc requires many instructions too](https://gcc.godbolt.org/z/37bd3PYd8) and uses less instructions than x130 mainly because of `byte [reg+offset]` which saves instructions and registers.

After this loop, the `yd` register is cleared and a lot of very repetitive instructions are executed. (It's an unrolled loop because I really did not want to handwrite another x130 loop.) We'll look at just the first one.
```as
Y_mov yb, 64
Y_mov ya, byte [yb]  ; ya = byte[yb] and if we interpret mem@64 to be an array by looking at the rest of the instructions, ya = arr2[i]
Y_mov yb, 96
Y_mov yb, byte [yb]  ; yb = byte[yb] but since we said earlier that mem@96 is an arr, yb = arr[i]
Y_add ya, yb
Y_or yd, ya          ; yd |= ya + yb
```
The function of this is a bit less clear: why the bitwise or? And where does `arr2` come from? `arr2`, as it turns out, comes from the predefined memory in `prog` (remember all the way at the start, how the last 256 bytes were predefined memory?). The function of the bitwise or will become obvious later, but one might make an educated guess that we need want `yd = 0` by the end, hence `ya + yb = 0`. This can be done by making `ya + yb = 256` because of the integer overflow.

Our suspicions are confirmed by reading the assembly after the unrolled loop:
```as
Y_xor ya, ya
Y_cmp yd, ya      ; check if yd = 0 !!!!
Y_je +6
Y_mov ya, 1       ; branch if yd != 0
Y_mov yb, 16
Y_mov yc, 16
Y_sys [sys_write] ; print wrong password
Y_xor ya, ya
Y_sys [sys_exit]  ; exit
Y_mov ya, 1       ; branch if yd = 0
Y_mov yb, 32
Y_mov yc, 16
Y_sys [sys_write] ; print welcome hacker
Y_jmp -7          ; jump to exit
```
Now that we know what the program does, we have to reverse engineer the correct input. The array at index 96 can be lazily constructed with `arr[i] = 256 - arr2[i]` which fails for `arr[0]` because `arr2[0]` is 0, but that's fine because we know from earlier that `arr[0]` should be 119. Then, `input[0] = 119` and `input[i+1] = input[i] - arr[i+1]`.

`solve.py`:
```py
mem = "456e7465722070617373776f72643a2057726f6e672070617373776f7264210a57656c636f6d652c206861636b65720a000000000000000000000000000000000001f5f611f215fee80dcafd2a0e0ce60303070307efff19000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
mem = [int(mem[x*2:x*2+2], 16) for x in range(128)]

input = [0]*24
arr = [0]*24
arr2 = mem[64:64+24]

for i in range(1, 24):
  arr[i] = 256 - arr2[i]

input[0] = 119
for i in range(0, 23):
  input[i+1] = (input[i] - arr[i+1] + 256) % 256

input = [chr(x) for x in input]
print(*input, sep='')
```

Flag: `wxmctf{yan85_my_beloved}`
