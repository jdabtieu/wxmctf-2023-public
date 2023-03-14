# Brainf - WxMCTF 2023
![](https://img.shields.io/badge/category-rev-blue) ![](https://img.shields.io/badge/author-BattleMage0231-orange)

## Description
My brain hurts after creating this challenge... but not as much as it would if I was a student at MGCI

[interpreter.py](dist/interpreter.py)

[program.bf](dist/program.bf)

## Solution

The files that we are provided appear to be a program written in some language and an interpreter for that language. Google "Brainf" reveals that this language is called [Brainf*ck](https://en.wikipedia.org/wiki/Brainfuck).

```python
if __name__ == '__main__':
    run(open(sys.argv[1]).read())
```

To run the interpreter, we need to pass in the name of the file as a command line argument.

```bash
$ python3 interpreter.py ./program.bf
Enter Password: password
Sorry, wrong password!
```

Running the program prompts you for a password. Unfortunately, we don't know it right now. However, we do know that in Brain*ck, the program operates on an array of memory called the tape. The first thing that we should do is examine the tape at different points in the program and see if we can find anything interesting.

```python
while iptr < len(code):
    print(tape[:50]) # print the tape
    instr = code[iptr]
```

We have edited the interpreter code to print the first 50 elements in the tape every instruction.

```bash
$ python3 interpreter.py ./program.bf
...
[0, 119, 120, 109, 99, 116, 102, 123, 98, 114, 52, 105, 110, 102, 95, 49, 115, 95, 84, 117, 114, 49, 110, 103, 95, 99, 48, 109, 112, 108, 51, 116, 101, 95, 51, 112, 80, 122, 89, 113, 125, 1, 1, 0, 1, 0, 0, 0, 0, 0]
[0, 119, 120, 109, 99, 116, 102, 123, 98, 114, 52, 105, 110, 102, 95, 49, 115, 95, 84, 117, 114, 49, 110, 103, 95, 99, 48, 109, 112, 108, 51, 116, 101, 95, 51, 112, 80, 122, 89, 113, 125, 1, 1, 0, 1, 0, 0, 0, 0, 0]
```

These values seem to correspond to ASCII characters. Let's try to convert them.

```python
>>> [119, 120, 109, 99, 116, 102, 123, 98, 114, 52, 105, 110, 102, 95, 49, 115, 95, 84, 117, 114, 49, 110, 103, 95, 99, 48, 109, 112, 108, 51, 116, 101, 95, 51, 112, 80, 122, 89, 113, 125]
[119, 120, 109, 99, 116, 102, 123, 98, 114, 52, 105, 110, 102, 95, 49, 115, 95, 84, 117, 114, 49, 110, 103, 95, 99, 48, 109, 112, 108, 51, 116, 101, 95, 51, 112, 80, 122, 89, 113, 125]
>>> ''.join(list(map(chr, _)))
'wxmctf{br4inf_1s_Tur1ng_c0mpl3te_3pPzYq}'
```

Flag: `wxmctf{br4inf_1s_Tur1ng_c0mpl3te_3pPzYq}`
