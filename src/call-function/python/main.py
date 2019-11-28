from llvmlite import ir

'''
Este módulo contém uma função main, uma função inteira "soma" que aceita 2 parâmetros inteiros e uma função "teste" que não retorna nada.
Será gerado um código em LLVM como este em C:


int soma (int a, int b){
	return a + b;
}

void teste (){

}

int main(){

	int a = 1;
	int b = 2;

	int res = soma(a,b);

	teste();
	
	return res;
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

# Cria o cabeçalho da função teste
t_teste = ir.FunctionType(ir.VoidType(), [])
teste = ir.Function(module, t_teste, 'teste')

# Cria o corpo da função teste
entryBlock = teste.append_basic_block('entry')
builder = ir.IRBuilder(entryBlock)

builder.ret_void()

# Cria o cabeçalho da função main
t_main = ir.FunctionType(ir.IntType(32), [])
main = ir.Function(module, t_main, 'main')

# Cria o corpo da função main
entryBlock = main.append_basic_block('entry')
builder = ir.IRBuilder(entryBlock)

# int a = 1;
a = builder.alloca(ir.IntType(32), name='a')
builder.store(ir.Constant(ir.IntType(32), 1), a)

# int b = 2;
b = builder.alloca(ir.IntType(32), name='b')
builder.store(ir.Constant(ir.IntType(32), 2), b)

# int res = soma(a,b);
res = builder.alloca(ir.IntType(32), name='res')
call = builder.call(soma, [builder.load(a), builder.load(b)])
builder.store(call, res)

# teste();
builder.call(teste, [])

# return res;
builder.ret(res)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
