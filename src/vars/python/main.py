#!/usr/bin/env python
# -*- coding: utf-8 -*

from llvmlite import ir
from llvmlite import binding as llvm

'''
Este módulo contém declarações de variáveis, operações e atribuições
Será gerado um código em LLVM como este em C:

int a;
float b;

int main(){
  int c = 1;
  float d = 1.0;

  a = 10;
  b = 10.0;
  
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

# Variável float global b
b = ir.GlobalVariable(module, ir.FloatType(),"b")
# Inicializa a variavel h
b.initializer =  ir.Constant(ir.FloatType(), 0.0)
# Linkage = common
b.linkage = "common"
# Define o alinhamento em 4
b.align = 4

# Define o retorno da função main
Zero32 = ir.Constant(ir.IntType(32), 0)
# Cria função main
t_func_main = ir.FunctionType(ir.IntType(32), ())
# Declara função main
main = ir.Function(module, t_func_main, name='main')

# Declara os blocos de entrada e saída da função.
entryBlock = main.append_basic_block('entry')
exitBasicBlock = main.append_basic_block('exit')

# Adiciona o bloco de entrada.
builder = ir.IRBuilder(entryBlock)

# Cria o valor de retorno e inicializa com zero
returnVal = builder.alloca(ir.IntType(32), name='retorno')
builder.store(Zero32, returnVal)

# int c = 1;
# float d = 1.0

# Variável inteira 'c'
# Aloca na memória variável a do tipo inteiro com nome 'c'
c = builder.alloca(ir.IntType(32), name="c")
# Define o alinhamento
c.align = 4
# Cria uma constante pra armazenar o numero 1
num1 = ir.Constant(ir.IntType(32),1)
# Armazena o 1 na variavel 'c'
builder.store(num1, c)

# Variavel float d
# Aloca na memoria 
d = builder.alloca(ir.FloatType(), name="d")
# Define o alinhamento
d.align = 4
# Cria uma constante pra armazenar o numero 1
num1Float = ir.Constant(ir.FloatType(), 1.0)
# Armazena o 1.0 na variavel 'd'
builder.store(num1Float, d)

# a = 10
# Outra maneira de fazer o store (sem precisar criar constante pra armazenar numero)
builder.store(ir.Constant(ir.IntType(32), 10), a)

# b = 10.0
builder.store(ir.Constant(ir.FloatType(), 10.0), b)

# Cria um salto para o bloco de saída
builder.branch(exitBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(exitBasicBlock)

# return 0
# Cria o return
# returnVal_temp = builder.load(returnVal, name='', align=4)
# builder.ret(returnVal_temp)
builder.ret(ir.Constant(ir.IntType(32), 0))

arquivo = open('vars.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)

# Shutdown.
llvm.shutdown()
