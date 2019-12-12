import llvmlite
from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

<<Exemplo de Referência.>>

int main() {
  int retorno;
  retorno = 0;
  return retorno;
}

'''

# Cria o módulo.

module = ir.Module('meu_modulo.bc')

# Declara função
func = ir.FunctionType(ir.IntType(32), ())

# Cria o cabeçalho da função main
main = ir.Function(module, func, name='main')


# Cria o corpo da função main

entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')
builder = ir.IRBuilder(entryBlock)

# Aloca variável do tipo inteiro
retorno = builder.alloca(ir.IntType(32), name='retorno')

# Define o alinhamento
retorno.align = 4

# Define variável com valor 0
##aux = builder.alloca(ir.IntType(32), name='aux')
aux = ir.Constant(ir.IntType(32), 0) 
##builder.store(ir.Constant(ir.IntType(32), 0), aux)
builder.store(aux, retorno)

# Atribuição  retorno = 0 
builder.store(aux, retorno)

# Cria um salto para o bloco de saída
builder.branch(endBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(endBasicBlock)

# Retorna res
res = builder.load(retorno, name='res', align=4)
builder.ret(res)

# Open e print módulo
arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)