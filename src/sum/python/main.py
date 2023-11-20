from llvmlite import ir
from llvmlite import binding as llvm

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

int main(){
	int a = 12;
	int b = 30;
	int res = sum(a,b);
	return res;
}

'''

# Cria o módulo e faz inicialização do llvm.
llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()
module = ir.Module('main.bc')
module.triple = llvm.get_process_triple()
target = llvm.Target.from_triple(module.triple)
target_machine = target.create_target_machine()
module.data_layout = target_machine.target_data

# Cria o cabeçalho da função sum. Será definida como externa.
t_sum = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
sum = ir.Function(module, t_sum, 'sum')
sum.args[0].name = 'x'
sum.args[1].name = 'y'


# Cria o cabeçalho da função main
t_main = ir.FunctionType(ir.IntType(32), [])
main = ir.Function(module, t_main, 'main')

# Cria o bloco de entrada e saida da main
entryBlockMain = main.append_basic_block('entry')
endBasicBlockMain = main.append_basic_block('exit')

#Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlockMain)

# int a = 12;
a = builder.alloca(ir.IntType(32), name='a')
builder.store(ir.Constant(ir.IntType(32), 12), a)

# int b = 30;
b = builder.alloca(ir.IntType(32), name='b')
builder.store(ir.Constant(ir.IntType(32), 30), b)

# int res = sum(a,b);
res = builder.alloca(ir.IntType(32), name='res')
call = builder.call(sum, [builder.load(a), builder.load(b)])
builder.store(call, res)

# Salta para o bloco de saida.
builder.branch(endBasicBlockMain)

#Adiciona o bloco de saida
builder.position_at_start(endBasicBlockMain)

# return res;
returnVal_temp = builder.load(res, name='ret', align=4)
builder.ret(returnVal_temp)

arquivo = open('main.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
