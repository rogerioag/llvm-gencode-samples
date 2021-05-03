from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

<<Colocar o Código do Exemplo de Referência.>>

'''





# Cria o módulo.
module = ir.Module('meu_modulo.bc')


# Salva o Módulo.
arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)