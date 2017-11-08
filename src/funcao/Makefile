CC = clang
CXX = clang++
LLVMCFG = llvm-config
OPT = opt
CFLAGS = -Wall `$(LLVMCFG) --cflags`
LDFLAGS = -Wall `$(LLVMCFG) --ldflags --libs core`



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


clean:
	rm -rvf main.o main out*.ll

