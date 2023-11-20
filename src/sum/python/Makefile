all:
	python3 main.py
	python3 sum.py
	llvm-link main.ll sum.ll -S -o main-sum.ll
	clang main-sum.ll
	./a.out && @echo $?
clean:
	rm *.ll *.out


