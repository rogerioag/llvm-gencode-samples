from llvmlite import ir
from llvmlite import binding

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

int main(){

	int a = 1;
	int b = 2;
	int c = 0;

	if(a < b) {
		c = 5; 
	}
	else {
		c = 6;
	}

	if(a < 1024){
		c = 10;
	}
	else {
		c = 20;
	}
	
	return 0;
}
'''
binding.initialize()
binding.initialize_native_target()
binding.initialize_native_asmprinter()  # yes, even this one

# Define o target.
target = binding.Target.from_triple("x86_64-pc-linux-gnu")
target_machine = target.create_target_machine()


# Cria o módulo.
module = ir.Module(name='meu_modulo.bc')

# Cria um valor zero para colocar no retorno.
Zero = ir.Constant(ir.IntType(32), 0)

# Declara o tipo do retorno da função main.
mainFnReturnType = ir.IntType(32)
# Cria a função main.
t_func_main = ir.FunctionType(mainFnReturnType, ())

# Declara a função main.
main = ir.Function(module, t_func_main, name='main')

# Declara o bloco de entrada.
entryBlock = main.append_basic_block('entry')
exitBasicBlock = main.append_basic_block('exit')

# Adiciona o bloco de entrada.
builder = ir.IRBuilder(entryBlock)

# Cria o valor de retorno e inicializa com zero.
returnVal = builder.alloca(ir.IntType(32), name='retorno')
builder.store(Zero, returnVal)

#	int a = 1;
a = builder.alloca(ir.IntType(32), name='a')
a.align = 4
#	int b = 2;
b = builder.alloca(ir.IntType(32), name='b')
b.align = 4
#	int c = 0;
c = builder.alloca(ir.IntType(32), name='c')
c.align = 4

# Inicializa as variáveis.
builder.store(ir.Constant(ir.IntType(32), 1), a)
builder.store(ir.Constant(ir.IntType(32), 2), b)
builder.store(ir.Constant(ir.IntType(32), 0), c)

# Declara os blocos básicos para o primeiro if.
#	if(a < b) {
#		c = 5; 
#	}
#	else {
#		c = 6;
#	}
iftrue_1 = main.append_basic_block('iftrue_1')
iffalse_1 = main.append_basic_block('iffalse_1')
ifend_1 = main.append_basic_block('ifend_1')

# Carrega as variáveis a e b para comparação.
# IRBuilder.load(ptr, name='', align=None)
a_cmp = builder.load(a, 'a_cmp', align=4)
b_cmp = builder.load(a, 'b_cmp', align=4)


#  IRBuilder.icmp_signed(cmpop, lhs, rhs, name='')
If_1 = builder.icmp_signed('<', a_cmp, b_cmp, name='if_test_1')
builder.cbranch(If_1, iftrue_1, iffalse_1)

builder.position_at_end(iftrue_1)
builder.store(ir.Constant(ir.IntType(32), 5), c)
builder.branch(ifend_1)

builder.position_at_end(iffalse_1)
builder.store(ir.Constant(ir.IntType(32), 6), c)
builder.branch(ifend_1)

builder.position_at_end(ifend_1)

# Declara os blocos básicos para o if.
#	if(a < 1024){
#		c = 10;
#	}
#	else {
#		c = 20;
#	}
	
#	return 0;
iftrue_2 = main.append_basic_block('iftrue_2')
iffalse_2 = main.append_basic_block('iffalse_2')
ifend_2 = main.append_basic_block('ifend_2')

a_cmp_2 = builder.load(a, 'a_cmp_2', align=4)
If_2 = builder.icmp_signed('<', a_cmp, ir.Constant(ir.IntType(32), 1024), name='if_test_1')
builder.cbranch(If_2, iftrue_2, iffalse_2)

builder.position_at_end(iftrue_2)
builder.store(ir.Constant(ir.IntType(32), 10), c)
builder.branch(ifend_2)

builder.position_at_end(iffalse_2)
builder.store(ir.Constant(ir.IntType(32), 20), c)
builder.branch(ifend_2)

builder.position_at_end(ifend_2)

# Cria um salto para o bloco de saída.
builder.branch(exitBasicBlock);

# Adiciona o bloco de saída.
builder = ir.IRBuilder(exitBasicBlock)
  
# Cria o return.
builder.ret(builder.load(returnVal, ""))

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)