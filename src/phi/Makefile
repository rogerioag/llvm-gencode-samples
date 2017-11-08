CC = clang-3.5
CXX = clang++-3.5
LLVMCFG = llvm-config-3.5
OPT = opt-3.5
CFLAGS = -Wall `$(LLVMCFG) --cflags`
LDFLAGS = -Wall `$(LLVMCFG) --libs --system-libs` `$(LLVMCFG) --ldflags` 

all: main

main: main.o
	$(CXX) main.o -o main $(LDFLAGS)

main.o: main.c
	$(CC) -c main.c -o main.o $(CFLAGS)

out.ll: main
	./main >out.ll 2>&1

out-phi.ll: out.ll
	$(OPT) -S -mem2reg <out.ll >out-phi.ll

out-cfg.ll: out.ll
	$(OPT) -S -simplifycfg <out.ll >out-cfg.ll

out-o1.ll: out.ll
	$(OPT) -S -O1 <out.ll >out-o1.ll

exe-via-obj: main
	./main
	llc-3.5 -filetype=obj meu_modulo.bc -o meu_modulo.o
	llc-3.5 -filetype=obj io.bc -o io.o
	clang-3.5 meu_modulo.o io.o -o meu_modulo.exe
	./meu_modulo.exe

exe-via-link:
	llvm-link-3.5 meu_modulo.bc io.bc -o meu_modulo-linked.bc
	clang-3.5 meu_modulo-linked.bc -o meu_modulo-linked.exe
	./meu_modulo-linked.exe

clean:
	rm -rvf main.o main out*.ll

