#!/usr/bin/env python
# -*- coding: utf-8 -*

from llvmlite import ir
from llvmlite import binding as llvm

'''
Este módulo contém uma função main, declarações de variáveis, operações e atribuições
Será gerado um código em LLVM como este em C:

int a,b,c;

int main(){
  a = 1;
  b = 2;
  c = a + b;
  
  return 0;
}

'''

# Código de Inicialização.
llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Cria o módulo.
module = ir.Module('meu_modulo.bc')
module.triple = llvm.get_process_triple()
target = llvm.Target.from_triple(module.triple)
target_machine = target.create_target_machine()
module.data_layout = target_machine.target_data


# Variável inteira global a
a = ir.GlobalVariable(module, ir.IntType(32),"a")
# Inicializa a variavel a
a.initializer = ir.Constant(ir.IntType(32), 0)
# Linkage = common
a.linkage = "common"
# Define o alinhamento em 4
a.align = 4

# Variável inteira global b
b = ir.GlobalVariable(module, ir.IntType(32), "b")
# Inicializa a variavel b
b.initializer = ir.Constant(ir.IntType(32), 0)
# Linkage = common
b.linkage = "common"
# Define o alinhamento em 4
b.align = 4

# Variável inteira global c
c = ir.GlobalVariable(module, ir.IntType(32), "c")
# Inicializa a variavel c
c.initializer = ir.Constant(ir.IntType(32), 0)
# Linkage = common
c.linkage = "common"
# Define o alinhamento em 4
c.align = 4

# Define o retorno da função main
Zero32 = ir.Constant(ir.IntType(32), 0)
# Cria função main
t_func_main = ir.FunctionType(ir.IntType(32), ())
# Declara função main
main = ir.Function(module, t_func_main, name='main')

# Declara o bloco de entrada
entryBlock = main.append_basic_block('entry')
exitBasicBlock = main.append_basic_block('exit')

# Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlock)

# Cria o valor de retorno e inicializa com zero
returnVal = builder.alloca(ir.IntType(32), name='retorno')
builder.store(Zero32, returnVal)

# a = 1;

# Variável inteira 'a'
# Cria uma constante pra armazenar o numero 1
num1 = ir.Constant(ir.IntType(32),1)
# Armazena o 1 na variavel 'a'
builder.store(num1, a)

# b = 2;
# Outra maneira de fazer o store (sem precisar criar constante pra armazenar numero)
builder.store(ir.Constant(ir.IntType(32), 2), b)

# c = a + b
a_temp = builder.load(a, "")
b_temp = builder.load(b, "")
add_temp = builder.add(a_temp, b_temp, name='temp', flags=())
# Armazena o temp (a + b) no c
builder.store(add_temp, c)

# Cria um salto para o bloco de saída
builder.branch(exitBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(exitBasicBlock)

# return o valor de retorno alocado e inicializado como zero.
# Cria o return
# returnVal_temp = builder.load(returnVal, name='', align=4)
# builder.ret(returnVal_temp)

# return 0.
builder.ret(ir.Constant(ir.IntType(32), 0))

# Se quisessemos retornar o valor de 'c'.
# returnVal_temp = builder.load(c, name='', align=4)
# builder.ret(returnVal_temp)

arquivo = open('atribuicao.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)

# Shutdown.
llvm.shutdown()
