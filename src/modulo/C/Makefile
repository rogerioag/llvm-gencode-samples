CC = clang
CXX = clang++
LLVMCFG = llvm-config
OPT = opt
CFLAGS = -Wall `$(LLVMCFG) --cflags`
LDFLAGS = -Wall `$(LLVMCFG) --ldflags --libs core`

all: modulo

modulo: modulo.o
	$(CXX) modulo.o -o modulo $(LDFLAGS)

modulo.o: modulo.c
	$(CC) -c modulo.c -o modulo.o $(CFLAGS)

out.ll: modulo
	./modulo >out.ll 2>&1

out-phi.ll: out.ll
	$(OPT) -S -mem2reg <out.ll >out-phi.ll

out-cfg.ll: out.ll
	$(OPT) -S -simplifycfg <out.ll >out-cfg.ll

out-o1.ll: out.ll
	$(OPT) -S -O1 <out.ll >out-o1.ll

clean:
	rm -rvf modulo.o modulo out*.ll

