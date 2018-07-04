#!/usr/bin/env python
# -*- coding: utf-8 -*

from llvmlite import ir

'''
Este módulo contém declarações de variáveis, operações e atribuições
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

    # Inicializa a variavel g
    g = declara_global('g', ir.IntType(32), 0)

    # Variável float global h
    h = declara_global('h', ir.FloatType(), 0.0)

    # Declaração da função 'principal', que DEVE ser usada com o nome 'main'.
    main_type = ir.FunctionType(ir.IntType(32), [])
    main = ir.Function(modulo, main_type, 'main')

    # Cria blocos de entrada e saída
    bloco_entrada = main.append_basic_block('bloco_entrada')
    bloco_saida = main.append_basic_block('bloco_saida')

    # Entra no bloco de entrada
    bloco = ir.IRBuilder(bloco_entrada)

    # int a = 1;
    a = declara_e_atribui('a', ir.IntType(32), 1)

    # float b = 1.0
    b = declara_e_atribui('a', ir.FloatType(), 1.0)

    # g = 10
    # Outra maneira de fazer o store (sem precisar criar constante previamente)
    bloco.store(ir.Constant(ir.IntType(32), 10), g)

    # h = 10.0
    bloco.store(ir.Constant(ir.FloatType(), 10.0), h)

    # a = a + 10
    a_temp = bloco.load(a, align=4)
    num10 = ir.Constant(ir.IntType(32), 10)
    temp = bloco.add(a_temp, num10, name='temp')

    # Armazena o temp (a + 10) no a
    bloco.store(temp, a)

    # b = b + h
    b_temp = bloco.load(b, align=4)
    h_temp = bloco.load(h, align=4)
    temp2 = bloco.fadd(b_temp, h_temp, name='temp2')

    # Armazena temp2 em b
    bloco.store(temp2, b)

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
