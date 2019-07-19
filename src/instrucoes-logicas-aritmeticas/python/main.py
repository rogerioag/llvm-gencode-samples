from llvmlite import ir, binding

'''
Este módulo contém uma função main com exemplos de várias operações lógicas e aritméticas.
Será gerado um código em LLVM como este em C:

int main(){
	int x = 2;
	int y = 1;

	// Operações lógicas
	int maior = (x > y);
	int menor = (x < y);
	int maiorIgual = (x >= y);
	int menorIgual = (x <= y);
	int igual = (x == y);
	int diferente = (x != y);
	int and = (x & y);
	int or = (x | y);
	int not = !x;
	int xor = (x ^ y);

	// Operações aritméticas
	int soma = (x + y);
	int subtracao = (x - y);
	int multiplicacao = (x * y);
	int divisao = (x / y);
	int modulo = (x % y);
	int shiftDireita = (x >> 1);
	int shiftEsquerda = (x << 1);

    return 0;
}


'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')
module.triple = binding.get_default_triple()

main_ftype = ir.FunctionType(ir.IntType(32), ())
main_func = ir.Function(module, main_ftype, 'main')

entry_block = main_func.append_basic_block('entry');
exit_block = main_func.append_basic_block('exit');

builder = ir.IRBuilder(entry_block)

return_val = builder.alloca(ir.IntType(32), name='ret_val')
builder.store(
    value=ir.Constant(ir.IntType(32), 0),
    ptr=return_val,
    align=4
)

x = builder.alloca(ir.IntType(32), name='x')
builder.store(
    value=ir.Constant(ir.IntType(32), 2),
    ptr=x,
    align=4
)
y = builder.alloca(ir.IntType(32), name='y')
builder.store(
    value=ir.Constant(ir.IntType(32), 1),
    ptr=y,
    align=4
)

x_temp = builder.load(x, name='x_temp')
y_temp = builder.load(y, name='y_temp')

# Operações lógicas
builder.icmp_signed('>', x_temp, y_temp, name='maior')
builder.icmp_signed('<', x_temp, y_temp, name='menor')
builder.icmp_signed('>=', x_temp, y_temp, name='maiorIgual')
builder.icmp_signed('<=', x_temp, y_temp, name='menorIgual')
builder.icmp_signed('==', x_temp, y_temp, name='igual')
builder.icmp_signed('!=', x_temp, y_temp, name='diferente')
builder.and_(x_temp, y_temp, name='and')
builder.or_(x_temp, y_temp, name='or')
builder.xor(x_temp, y_temp, name='xor')
builder.not_(x_temp, name='not')

# Operações aritméticas
builder.add(x_temp, y_temp, name='soma')
builder.sub(x_temp, y_temp, name='subtracao')
builder.mul(x_temp, y_temp, name='multiplicacao')
builder.sdiv(x_temp, y_temp, name='divisao')
builder.srem(x_temp, y_temp, name='modulo')
um = ir.Constant(ir.IntType(32), 1)
builder.ashr(x_temp, um, name='shiftDireita')
builder.shl(x_temp, um, name='shiftEsquerda')

builder.branch(exit_block)
builder.position_at_end(exit_block)

builder.ret(builder.load(return_val))

arquivo = open('main.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)