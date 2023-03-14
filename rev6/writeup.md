# TEJ5M - WxMCTF 2023
![](https://img.shields.io/badge/category-rev-blue) ![](https://img.shields.io/badge/author-BattleMage0231-orange)

## Description
While we're at it, here's my TEJ5M ISP too. Unfortunately, I forgot to comment my code so I don't remember what it does. I think it had something to do with IEEE 754 floating-point numbers?

[TEJ5M.zip](files/TEJ5M.zip)

## Solution

The description mentions IEEE 754, which is a standard for representing real numbers in binary. To solve the challenge in the intended way, we will need to know how IEEE 754 represents numbers and how it supports arithmetic operations between those numbers. 

First we will try running the program.

```
Welcome to my ISP!
Enter a 39-bit number in binary: 000000000000000000000000000000000000000
100110011101000011101101110110000000001
```

```nasm
_start:
    call get_input
    mov rax, 001101011101010001100001000101111011111b
    call f
    mov rax, 101000000011010111111010100110101011010b
    call g
    mov rax, 010110001000001011010111000000100011110b
    ...
```

Looking at the NASM code (we can also use a decompiler to make our lives easier), we can see that the program first calls get_input and then calls the functions f and g many times with different inputs. Examining get_input, we find that it simply stores the inputted binary number in the "num" variable.

Now let's look at the end of _start.

```nasm
    ...
    mov rax, 100011100000111111000001101000000011101b
    call f
    mov rax, [num]
    call print_number
    mov rax, [num]
    mov rbx, 100110011101000011101101111110011101011b
    cmp rax, rbx
    jne l0
    call print_flag
l0:
    call exit
```

First, it calls the print_number function on num. True to its name, this function prints out num in binary. Then, num is compared with a binary value and the flag is printed only if they are equal. So, our task is find an input that produces the desired output after the function calls.

Now comes the painful part. Examining f and g, we see that they transform num based on the input value of rax.

Based on the hint about IEEE 754, we might guess that each binary number represents a real number and f and g support arithmetic operations on those numbers. One way that we can come to this conclusion is by examining the first part of f and g, which appears to extract mantissas and exponents from the two inputs.

```nasm
    mov r14, 127
    mov r15, rax
    ; r8 is the exponent of num, stored with a bias of 127
    mov r8, [num]
    shr r8, 31
    sub r8, r14
    ; similarly r10 is the exponent of r15
    mov r10, r15
    shr r10, 31
    sub r10, r14
    ; r9 is the mantissa of num, stored with an implicit 1 bit
    mov r9, 1
    shl r9, 31
    mov rbx, [num]
    mov eax, ebx
    btr rax, 31
    or r9, rax
    ; similarly r11 is the mantissa of r15s
    mov r11, 1
    shl r11, 31
    mov rbx, r15
    mov eax, ebx
    btr rax, 31
    or r11, rax
```

In fact, this is enough to tell us the format of the "modified" IEEE 754 representation. The top 8 bits of the 39-bit integer store the exponent and the bottom 31 bits store the mantissa. Now, we will identify what operations f and g support respectively.

```nasm
    mov r12, r8
    mov r13, r9
    add r13, r11
```

For f, this snippet assigns to r12 the exponent of num (after some tranformations) and to r13 the sum of the mantissas (also after some transformations). This leads us to believe that f implements addition. If we are skeptical, we can also look for additional clues in f, such as shifting the numbers so that they have equal exponents.

```nasm
    mov r12, r8
    add r12, r10
    mov rax, r9
    mul r11d
    shl rdx, 32
    mov r13, rdx
```

For g, this snippet assigns to r12 the sum of the two exponents and to r13 the product of the mantissas. This leads us to believe that g implements multiplication.

Now that we know what the program does, we can find a valid input. We will do this by converting all of the binary literals to real numbers and then simply doing subtraction and division to find the original number. Writing a program to do this is left as an exercise :) 

Note that the number we end up with may not actually work. This is because f and g use truncation when rounding, possibly leading to floating point errors. In this case, we should try numbers close to what we have and observe how the output changes, eventually finding an input that works.

One input that works is 001101001110010011110011100011010101011.

```
Welcome to my ISP!
Enter a 39-bit number in binary: 001101001110010011110011100011010101011
100110011101000011101101111110011101011
wxmctf{4r3nt_fl10at1ng_p0int5_5o_fun_yM9EuI}
```

Flag: `wxmctf{4r3nt_fl10at1ng_p0int5_5o_fun_yM9EuI}`
