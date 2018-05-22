#!/usr/bin/env python
# -*- coding: utf-8 -*

from llvmlite import ir

'''
Este módulo contém uma função main, declarações de variáveis, operações e atribuições
Será gerado um código em LLVM como este em C:

int g;
float h;

int main(){
  int a = 1;
  float b = 1.0;
  
  g = 10;
  h = 10.0;
  a = a + 10;
  b = b + h;
  
  return 0;
}

'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Variável inteira global g
g = ir.GlobalVariable(module, ir.IntType(32),"g")
# Inicializa a variavel g
g.initializer = ir.Constant(ir.IntType(32), 0)
# Linkage = common
g.linkage = "common"
# Define o alinhamento em 4
g.align = 4

# Variável float global h
h = ir.GlobalVariable(module, ir.FloatType(),"h")
# Inicializa a variavel h
h.initializer =  ir.Constant(ir.FloatType(), 0.0)
# Linkage = common
h.linkage = "common"
# Define o alinhamento em 4
h.align = 4

# Define o retorno da função main
Zero32 = ir.Constant(ir.IntType(32), 0)
# Cria função main
t_func_main = ir.FunctionType(ir.IntType(32), ())
# Declara função main
main = ir.Function(module, t_func_main, name='main')

# Declara o bloco de entrada
entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')

# Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlock)

# Cria o valor de retorno e inicializa com zero
returnVal = builder.alloca(ir.IntType(32), name='retorno')
builder.store(Zero32, returnVal)

# int a = 1;
# float b = 1.0

# Variável inteira 'a'
# Aloca na memória variável a do tipo inteiro com nome 'a'
a = builder.alloca(ir.IntType(32), name="a")
# Define o alinhamento
a.align = 4
# Cria uma constante pra armazenar o numero 1
num1 = ir.Constant(ir.IntType(32),1)
# Armazena o 1 na variave 'a'
builder.store(num1, a)

# Variavel float b
# Aloca na memoria 
b = builder.alloca(ir.FloatType(), name="b")
# Define o alinhamento
b.align = 4
# Cria uma constante pra armazenar o numero 1
num1Float = ir.Constant(ir.FloatType(), 1.0)
# Armazena o 1.0 na variavel 'b'
builder.store(num1Float, b)

# g = 10
# Outra maneira de fazer o store (sem precisar criar constante pra armazenar numero)
builder.store( ir.Constant(ir.IntType(32), 10) , g )

# h = 10.0
builder.store( ir.Constant(ir.FloatType(), 10.0) , h )

# a = a + 10
a_temp = builder.load(a, "")
num10 = ir.Constant(ir.IntType(32), 10)
temp = builder.add(a_temp, num10, name='temp', flags=())
# Armazena o temp (a + 10) no a
builder.store(temp, a)

# b = b + h
b_temp = builder.load(b, "")
h_temp = builder.load(h,"")
temp2 = builder.fadd( b_temp , h_temp , name='temp2', flags=())
# Armazena temp2 em b
builder.store(temp2, b)

# Cria um salto para o bloco de saída
builder.branch(endBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(endBasicBlock)

# return 0
# Cria o return
returnVal_temp = builder.load(returnVal, name='', align=4)
builder.ret(returnVal_temp)

arquivo = open('vars.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)