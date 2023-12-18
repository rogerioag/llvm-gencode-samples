from llvmlite import ir
from llvmlite import binding as llvm

# Esse código tem um exemplo de como passar vetores por parâmetro com o llvmlite
# Esse método só funciona se o tamanho dos vetores for explicitado no cabeçalho da função, como no exemplo em C:

# void exemplo(int a[100], int b[100], int c[100], int i)
# {
#     c[i] = b[i] + a[i];
#     return;
# }
#
#
# int main()
# {
#     int a[100], b[100], c[100], i;
#     i = 0
#
#     exemplo(a, b, c, i);
#
#     return(0);
# }

# inicialização
llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# cria o módulo
module = ir.Module('vetor_parametro.bc')
module.triple = llvm.get_process_triple()
target = llvm.Target.from_triple(module.triple)
target_machine = target.create_target_machine()
module.data_layout = target_machine.target_data

# tipos
INT = ir.IntType(32)
INT_ARRAY = ir.ArrayType(INT, 100)
ARRAY_POINTER = ir.PointerType(INT_ARRAY)

# cria a função exemplo
# void exemplo(int a[100], int b[100], int c[100], int i)
exemplo_type = ir.FunctionType(ir.VoidType(), [ARRAY_POINTER, ARRAY_POINTER, ARRAY_POINTER, INT])
exemplo_func = ir.Function(module, exemplo_type, "exemplo")
a, b, c, i = exemplo_func.args # ponteiros para os parâmetros

# dá nome aos argumentos no cabeçalho da função
exemplo_func.args[0].name = 'a'
exemplo_func.args[1].name = 'b'
exemplo_func.args[2].name = 'c'
exemplo_func.args[3].name = 'i'


# cria os blocos de entrada e saída
ex_entry = exemplo_func.append_basic_block("entry")
ex_exit = exemplo_func.append_basic_block("exit")

builder = ir.IRBuilder(ex_entry)

# só é preciso alocar variáveis que não são ponteiros localmente, nesse caso a i
# se você não alocar essas variáveis, não dá pra manipular elas no corpo da função
i_val = builder.alloca(INT, name="i")
# guarda o valor passado por parâmetro na variável local
builder.store(i, i_val)

# carrega o i
i_loaded = builder.load(i_val, name="i")

# soma
# c[i] = b[i] + a[i];
# calcula e carrega o endereço dos vetores com base no valor de i
bptr = builder.gep(b, [INT(0), i_loaded], name="b[i]")
b_val = builder.load(bptr, name="b[i]")
aptr = builder.gep(a, [INT(0), i_loaded], name="a[i]")
a_val = builder.load(aptr, name="a[i]")

add_temp = builder.add(b_val, a_val, name="add_tmp")

# guarda resultado da soma no endereço correto de c
cptr = builder.gep(c, [INT(0), i_loaded], name="c[i]")
builder.store(add_temp, cptr)

# dá branch, posiciona o builder no bloco de saída e retorna vazio
# return;
builder.branch(ex_exit)
builder.position_at_end(ex_exit)
builder.ret_void()

# declara função main
# int main()
main_type = ir.FunctionType(INT, [])
main_func = ir.Function(module, main_type, "main")

# declara blocos de entrada e saída da função main
main_entry = main_func.append_basic_block("entry")
main_exit = main_func.append_basic_block("exit")

main_builder = ir.IRBuilder(main_entry)

# aloca valor de retorno
return_value = main_builder.alloca(INT, name="return_value")

# aloca variáveis
# int a[100], b[100], c[100], i;
a_main = main_builder.alloca(INT_ARRAY, name="a") 
a_main.align = 4
b_main = main_builder.alloca(INT_ARRAY, name="b") 
b_main.align = 4
c_main = main_builder.alloca(INT_ARRAY, name="c") 
c_main.align = 4
i_main = main_builder.alloca(INT, name="i") 
i_main.align = 4

# armazena 0 no i 
# i = 0;
main_builder.store(INT(0), i_main)
i_main_loaded = main_builder.load(i_main, name="i")

# chama a função exemplo
# exemplo(a, b, c, i);
main_builder.call(exemplo_func, [a_main, b_main, c_main, i_main_loaded])

# armazena 0 no valor de retorno e dá branch
# posiciona o builder no bloco de saída, carrega o retorno e termina
# return(0);
main_builder.store(INT(0), return_value)
main_builder.branch(main_exit)
main_builder.position_at_end(main_exit)
return_val_loaded = main_builder.load(return_value, name="return_value")
main_builder.ret(return_val_loaded)

# salva o módulo
arquivo = open('vetor_parametro.ll', 'w')
arquivo.write(str(module))
