CC = clang-3.5

all: compile bc ll

compile:
	$(CC) hello.c -o hello.exe
	./hello.exe

bc: hello.c
	$(CC) -emit-llvm -S -c hello.c -o hello.bc
	lli-3.5 hello.bc
	$(CC) hello.bc -o hello.exe
	./hello.exe

ll: hello.c
	$(CC) -c hello.c -S -emit-llvm -o hello.ll
	llc-3.5 hello.ll -o hello.s
	gcc hello.s -o hello-gcc.exe
	$(CC) hello.s -o hello-clang.exe

clean:
	rm -rvf *.ll
