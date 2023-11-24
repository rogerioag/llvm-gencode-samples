'''
Este módulo contém uma função main, e funções para operações aritméticas que aceitam 2 parâmetros inteiros retornando o resultado da operação.
Será gerado um código em LLVM como este em C:

int leiaInteiro();
void escrevaInteiro(int pi);

int add(int s, int t){
	return s + t;
}

int sub(int u, int v){
	return u - v;
}

int mul(int x, int w){
	return x * w;
}

int div(int y, int z){
	return y / z;
}

int main(){
	int a = 0;
	int b = 0;
	int c = 0;
	int d = 0;
	int res = 0;
	int i;

	i = 0;

    do {
        a = leiaInteiro();
        b = leiaInteiro();
        c = leiaInteiro();
        d = leiaInteiro();
        res = add(add(mul(a,b),div(a,b)), sub(d,c));
        escrevaInteiro(res);
        i = i + 1;
	} while (i < 5);

    return(0);
}
'''

from llvmlite import ir
from llvmlite import binding as llvm

int32 = ir.IntType(32)

# Cria o módulo e faz inicialização do llvm.
llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()
module = ir.Module('nested-call-function.bc')
module.triple = llvm.get_process_triple()
target = llvm.Target.from_triple(module.triple)
target_machine = target.create_target_machine()
module.data_layout = target_machine.target_data

def create_function(module, pfunc, fargs, targs):
	# Cria a função.
	type_func = ir.FunctionType(targs[0], targs[1])
	func = ir.Function(module, type_func, pfunc.__name__)

	for i in range(len(fargs)):
		func.args[i].name = fargs[i]
	
	# Cria os blocos de entrada e saidaa da função func
	entryBlock = func.append_basic_block('entry')
	endBasicBlock = func.append_basic_block('exit')

	# Adiciona o bloco de entrada
	builder = ir.IRBuilder(entryBlock)
    
    # Realiza a operação de func
	res = pfunc(builder, func.args[0], func.args[1])
    
    # Pula para o bloco de saida
	builder.branch(endBasicBlock)
    
    # Posiciona na saida da funçao
	builder.position_at_start(endBasicBlock)
    
	# Retorna res
	builder.ret(res)

	return func


# Declaração das funções que serão 'adicionadas' em tempo de vinculação.
escrevaI = ir.Function(module, ir.FunctionType(ir.VoidType(), [ir.IntType(32)]), "escrevaInteiro")
leiaI = ir.Function(module, ir.FunctionType(ir.IntType(32), []), "leiaInteiro")

# Declara as funções de operações.
func_add = create_function(module, ir.IRBuilder.add, ['s','t'], [int32, [int32, int32]])
func_sub = create_function(module, ir.IRBuilder.sub, ['u','v'], [int32, [int32, int32]])
func_mul = create_function(module, ir.IRBuilder.mul, ['x','w'], [int32, [int32, int32]])
func_div = create_function(module, ir.IRBuilder.sdiv, ['y','z'], [int32, [int32, int32]])


# Cria o cabeçalho da função main
t_main = ir.FunctionType(ir.IntType(32), [])
main = ir.Function(module, t_main, 'main')

# Cria o bloco de entrada e saida da main
entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')

#Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlock)

# int a = 0;
a = builder.alloca(ir.IntType(32), name='a')
builder.store(ir.Constant(ir.IntType(32), 0), a)
# int b = 0;
b = builder.alloca(ir.IntType(32), name='b')
builder.store(ir.Constant(ir.IntType(32), 0), b)
# int c = 0;
c = builder.alloca(ir.IntType(32), name='c')
builder.store(ir.Constant(ir.IntType(32), 0), c)
# int d = 0;
d = builder.alloca(ir.IntType(32), name='d')
builder.store(ir.Constant(ir.IntType(32), 0), d)
#int res = 0;
res = builder.alloca(ir.IntType(32), name='res')
builder.store(ir.Constant(ir.IntType(32), 0), res)
#int i;
i = builder.alloca(ir.IntType(32), name='i')
# i = 0;
builder.store(ir.Constant(ir.IntType(32), 0), i)

# Cria os blocos de repetição
loop = builder.append_basic_block('loop')
loop_val = builder.append_basic_block('loop_val')
loop_end = builder.append_basic_block('loop_end')

# Pula para o laço do loop
builder.branch(loop)

# Posiciona no inicio do bloco do loop
builder.position_at_end(loop)

# Insere o valor 5 para a variável 'a'
# Corpo do laço.
#Adiciona o bloco de saida

# a = leiaInteiro();
res_leia = builder.call(leiaI, args=[])
builder.store(res_leia, a, align=4)

# b = leiaInteiro();
res_leia = builder.call(leiaI, args=[])
builder.store(res_leia, b, align=4)

# c = leiaInteiro();
res_leia = builder.call(leiaI, args=[])
builder.store(res_leia, c, align=4)

# d = leiaInteiro();
res_leia = builder.call(leiaI, args=[])
builder.store(res_leia, d, align=4)

# res = add(add(mul(a,b),div(a,b)), sub(d,c));
res_mul = builder.call(func_mul, [builder.load(a), builder.load(b)])
res_div = builder.call(func_div, [builder.load(a), builder.load(b)])
res_sub = builder.call(func_sub, [builder.load(d), builder.load(c)])
res_add = builder.call(func_add, [res_mul,res_div])
call = builder.call(func_add, [res_add,res_sub])
builder.store(call, res)

# escrevaInteiro(res);
builder.call(escrevaI, args=[builder.load(res)])

# Carrega a variável 'i'
iVarLoad = builder.load(i)
# i + 1
inc = builder.add(iVarLoad, ir.Constant(int32, 1))
# i = i + 1
builder.store(inc, i)

# Pula para o laço de validação
builder.branch(loop_val)

# Posiciona no inicio do bloco de validação
builder.position_at_end(loop_val)

#Carrega iVar novamente antes da comparação para garantir o valor atualizado
iVarLoad = builder.load(i)

# Gera a expressão de comparação
comp_expr = builder.icmp_signed('==', iVarLoad, ir.Constant(int32, 5), name='expr_comp')

# Compara se a expressão é verdadeira ou não, caso for pula para o bloco do loop end, caso contrário pula para o bloco do loop
builder.cbranch(comp_expr, loop_end, loop)

# Posiciona no inicio do bloco do fim do loop (saída do laço) e define o que o será executado após o fim (o resto do programa)  
builder.position_at_end(loop_end)

# Cria um salto para o bloco de saída
builder.branch(endBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(endBasicBlock)

# return (0);
builder.ret(ir.Constant(int32, 0))

arquivo = open('nested-call-function.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
