
'''
Este módulo contém uma função main, adeclaração de três variáveis do tipo inteiro auxA, auxB, resultado. Após feita a soma das variáveis é armazenada na variável resultado.
Será gerado um código em LLVM como este em C:

int main(){
	int a = 19;
	int b = 23;

	int resultado = a+b
	
	return resultado;
}
'''
from llvmlite import ir

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

#cabecalho main
t_main = ir.FunctionType(ir.IntType(32), [])
main = ir.Function(module, t_main, 'main')

#corpo main 
entryBlock = main.append_basic_block('entry')
builder = ir.IRBuilder(entryBlock)

# aloca int x = 19
x = builder.alloca(ir.IntType(32), name='x')
builder.store(ir.Constant(ir.IntType(32), 19), x)

# aloca int y = 23;
y = builder.alloca(ir.IntType(32), name='y')
builder.store(ir.Constant(ir.IntType(32), 23), y)

# alloca int resultado;
resultado = builder.alloca(ir.IntType(32), name='resultado')

#carrega x e y. Depois soma, salva na variavel temporaria "res" e salva "res" dentro de resultado
res = builder.add(builder.load(x), builder.load(y))
builder.store(res, resultado)

# return res;
builder.ret(resultado)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
