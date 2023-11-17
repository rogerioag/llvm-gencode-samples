from llvmlite import ir
from llvmlite import binding as llvm

#Código de exemplo para criação do módulo para os códigos.

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

#Esse código não será executado pois não possui função main, mas 
#Esse código é necessário para a inicialização de todo código feito com o llvmlite.
