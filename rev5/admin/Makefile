all:
	gcc -O2 -s main.c -o main
debug:
	gcc -ggdb main.c -o main
asm:
	python yan85-disassembler/yanas.py -o prog prog.asm
zip:
	zip dist.zip main prog
