from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

<<Colocar o Código do Exemplo de Referência.>>

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


# Salva o Módulo.
arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
