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

def declara_e_atribui(name: str, _type: ir.Type, value) -> ir.AllocaInstr:
    global bloco

    temp = bloco.alloca(_type, name=name)

    # Define o alinhamento de 4 bytes
    temp.align = 4

    # Cria uma constante pra armazenar o valor passado
    constant = ir.Constant(_type, value)

    # Armazena a constante na variável criada
    bloco.store(constant, temp)

    return temp


def declara_global(name: str, _type: ir.Type, value) -> ir.GlobalValue:
    global modulo

    # Declara variável global do tipo especificado
    temp = ir.GlobalVariable(modulo, _type, name)

    # Inicializa variável
    temp.initializer = ir.Constant(_type, value)

    # Define alinhamento de 4 bytes
    temp.align = 4

    return temp


if __name__ == '__main__':
    # Cria o módulo.
    modulo = ir.Module('meu_modulo.bc')

    # Inicializa a variavel a
    a = declara_global('a', ir.IntType(32), 0)

    # Variável float global b
    b = declara_global('b', ir.FloatType(), 0.0)

    # Declaração da função 'principal', que DEVE ser usada com o nome 'main'.
    main_type = ir.FunctionType(ir.IntType(32), [])
    main = ir.Function(modulo, main_type, 'main')

    # Cria blocos de entrada e saída
    bloco_entrada = main.append_basic_block('entry')
    bloco_saida = main.append_basic_block('exit')

    # Entra no bloco de entrada
    bloco = ir.IRBuilder(bloco_entrada)

    # Cria o valor de retorno e inicializa com zero
    retorno = declara_e_atribui('retorno', ir.IntType(32), 0)

    # int c = 1;
    c = declara_e_atribui('c', ir.IntType(32), 1)

    # float d = 1.0
    d = declara_e_atribui('d', ir.FloatType(), 1.0)

    # a = 10
    # Outra maneira de fazer o store (sem precisar criar constante previamente)
    bloco.store(ir.Constant(ir.IntType(32), 10), a)

    # b = 10.0
    bloco.store(ir.Constant(ir.FloatType(), 10.0), b)

    # Salto para bloco de saída
    bloco.branch(bloco_saida)

    # Entra no bloco de saída
    bloco = ir.IRBuilder(bloco_saida)

    # Cria constante de retorno
    retorno = ir.Constant(ir.IntType(32), 0)

    # Efetua o retorno
    bloco.ret(retorno)

    with open('vars.ll', 'w') as arquivo:
        arquivo.write(str(modulo))

    arquivo.close()
    print(modulo)
    
    # Shutdown.
    llvm.shutdown()
