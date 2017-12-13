# -*- coding: utf-8 -*-


from llvmlite import ir

from llvmlite import ir

'''
Este módulo apresenta um exemplo de como os parâmetros devem ser tratados.
São criadas variáveis locais e os parâmetros são compiados para elas.
Será gerado um código em LLVM como este em C:

<<Colocar o Código do Exemplo de Referência.>>

'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')



arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
