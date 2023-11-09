#!/usr/bin/python3
from llvmlite import ir

'''

Este módulo contém uma função main, duas variáveis e um blocos de condição.

Será gerado um código em LLVM (if3.ll) correspondente a este em C:

int main(){

    int a = 10;
    int b = 30;

    if (a >= 10) {
        a = b;
    }

    return b;
}

'''

# vars/functions types
TYPES = {
    "int": lambda size: ir.IntType(size),
    "constant": lambda typ, value: ir.Constant(typ=typ, constant=value)
}


# Cria o módulo.
module = ir.Module('if3.bc')

# Função main

# Tipo de retorno da função main
function_return_type = TYPES.get("int")(32)

# Tipos dos argumentos da função main
function_arguments_types = ()

# Tipo da função main
function_type = ir.FunctionType(
    function_return_type, function_arguments_types, var_arg=False)

# Nome da função main
function_name = "main"

# Referência da função main
function = ir.Function(module=module, ftype=function_type, name=function_name)


# Bloco : Main

# Bloco de entrada
entry_block_name = "entry"
# Ref do bloco de entrada
entry_block = function.append_basic_block(name=entry_block_name)



# IRBuilder
builder = ir.IRBuilder(block=entry_block)

# Variáveis

# Variável a
a_type = TYPES.get("int")(32)
a_name = "a"
a_ref = builder.alloca(a_type, name=a_name)
a_ref.align = 4
builder.store(TYPES.get("constant")(a_type, 30), a_ref)

# Variável b
b_type = TYPES.get("int")(32)
b_name = "b"
b_ref = builder.alloca(b_type, name=b_name)
b_ref.align = 4
builder.store(TYPES.get("constant")(b_type, 30), b_ref)


# Bloco de Condição

if_block = function.append_basic_block(name="if")
builder.branch(if_block)
builder.position_at_end(if_block)

# Condição
cmp_type = ">="
cmp_name = "a >= 10"
cmp_ref = builder.icmp_signed(cmp_type, builder.load(a_ref), TYPES.get("constant")(a_type, 10), cmp_name)

with builder.if_then(cmp_ref):
    builder.store(builder.load(b_ref), a_ref)


# Bloco de saída

exit_block_name = "exit"
exit_block = function.append_basic_block(name=exit_block_name)
builder.branch(exit_block)
builder.position_at_end(exit_block)

# Retorno da função main
builder.ret(builder.load(b_ref))


# Salva o módulo em um arquivo
with open("if3.ll", "w") as file:
    file.write(str(module))
