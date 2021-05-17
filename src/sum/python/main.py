from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

int sum(int x, int y) {
    return (x + y)
}

int main(){
	int a = 12;
	int b = 30;
	int res = sum(a,b);
	printf("res: %d\n", res);
	return 0;
}

'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Cria o cabeçalho da função soma
t_soma = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
soma = ir.Function(module, t_soma, 'soma')
soma.args[0].name = 'a'
soma.args[1].name = 'b'

# Cria o corpo da função soma
entryBlock = soma.append_basic_block('entry')
builder = ir.IRBuilder(entryBlock)

res = builder.add(soma.args[0], soma.args[1])
builder.ret(res)

# Cria o cabeçalho da função main
t_main = ir.FunctionType(ir.IntType(32), [])
main = ir.Function(module, t_main, 'main')

# Cria o corpo da função main
entryBlock = main.append_basic_block('entry')
builder = ir.IRBuilder(entryBlock)

# int a = 12;
a = builder.alloca(ir.IntType(32), name='a')
builder.store(ir.Constant(ir.IntType(32), 12), a)

# int b = 30;
b = builder.alloca(ir.IntType(32), name='b')
builder.store(ir.Constant(ir.IntType(32), 30), b)

# int res = soma(a,b);
res = builder.alloca(ir.IntType(32), name='res')
call = builder.call(soma, [builder.load(a), builder.load(b)])
builder.store(call, res)

# return res;
builder.ret(res)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)