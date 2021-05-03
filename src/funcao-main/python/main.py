# -*- coding: utf-8 -*-


from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:


int main() {
  int retorno = 0;
  return retorno;
}

'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# É possível criar algumas variaveis de apoio 
inteiro = ir.IntType(32) #nesse caso inteiro recebe um i32
functy = ir.FunctionType(inteiro, ()) # nessa linha é declrado o tipo de retorno e os argumentos da função FunctionType(type, (list of type))

# Declarar a função main
main = ir.Function(module, functy, name='main')

# Declara o bloco de entrada
entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')

#Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlock)

# Declarando e alocando a variavel 'retorno' com o tipo inteiro
retorno = builder.alloca(ir.IntType(32), name='retorno')

# Define o alinhamento
retorno.align = 4

# define uma constande 0 do tipo i32
Zero32 = ir.Constant(ir.IntType(32), 0) 

#armazena o 0 na váriavel retorno
builder.store(Zero32, retorno)

# Cria um salto para o bloco de saída
builder.branch(endBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(endBasicBlock)

# Cria o return
returnVal_temp = builder.load(retorno, name='ret_temp', align=4)
builder.ret(returnVal_temp)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)