from llvmlite import ir

'''
Este módulo contém uma função main.
Será gerado um código em LLVM como este em C:

int main() {
  return 0;
}

'''

# Cria o módulo.
modulo = ir.Module('meu_modulo.bc')

# Declaração da função 'main'.
main_type = ir.FunctionType(ir.IntType(32), [])
main = ir.Function(modulo, main_type, "main")

# Cria blocos de entrada e saída
bloco_entrada = main.append_basic_block("bloco_entrada")
bloco_saida = main.append_basic_block("bloco_saida")

# Acessa o bloco de entrada
bloco = ir.IRBuilder(bloco_entrada)

# return 0;
bloco.ret(ir.Constant(ir.IntType(32), 0))

bloco = ir.IRBuilder(bloco_saida)

# Adiciona o bloco de saida
bloco.position_at_end(bloco_saida)

arquivo = open('funcao_main.ll', 'w')
arquivo.write(str(modulo))
arquivo.close()
print(modulo)