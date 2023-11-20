from llvmlite import ir
from llvmlite import binding as llvm

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

int sum(int x, int y) {
    return (x + y)
}

'''

# Cria o módulo e faz inicialização do llvm.
llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()
module = ir.Module('sum.bc')
module.triple = llvm.get_process_triple()
target = llvm.Target.from_triple(module.triple)
target_machine = target.create_target_machine()
module.data_layout = target_machine.target_data

# Cria o cabeçalho da função sum
t_sum = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
sum = ir.Function(module, t_sum, 'sum')
sum.args[0].name = 'x'
sum.args[1].name = 'y'

# Cria os blocos de entrada e saida da função sum
entryBlock = sum.append_basic_block('entry')
endBasicBlock = sum.append_basic_block('exit')
builder = ir.IRBuilder(entryBlock)

#Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlock)

#Realiza a operação de sum
res = builder.add(sum.args[0], sum.args[1])

#Pula para o bloco de saida
builder.branch(endBasicBlock)

#Posiciona na saida da funçao
builder.position_at_start(endBasicBlock)
# return res;
builder.ret(res)

arquivo = open('sum.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
