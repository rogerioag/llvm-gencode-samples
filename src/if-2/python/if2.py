#!/usr/bin/python3
from llvmlite import ir

'''

Este módule contém uma função main, três variáveis e dois blocos de condição.

Será gerado um código em LLVM (if2.ll) correspondente a este em C:

int main(){

	int a = 1;
	int b = 2;
	int c = 0;


	if(a < b) {
		c = 5; 
	}
	else {
		c = 6;
	}

	if(a < 1024){
		c = 10;
	}
	else {
		c = 20;
	}
	
	return 0;
}

'''

# vars/functions types
TYPES = {
    "int": lambda size: ir.IntType(size),
    "constant": lambda typ, value: ir.Constant(typ=typ, constant=value)
}


# Cria o módulo.
module = ir.Module('if2.bc')

# main function

# main function return type
function_return_type = TYPES.get("int")(32)

# main function arguments type
function_arguments_types = ()

# main function type
function_type = ir.FunctionType(
    function_return_type, function_arguments_types, var_arg=False)

# main function name
function_name = "main"

# main function ref
function = ir.Function(module=module, ftype=function_type, name=function_name)


# main function block

# entry block name
entry_block_name = "entry"
# entry block ref
entry_block = function.append_basic_block(name=entry_block_name)



# IRBuilder
builder = ir.IRBuilder(block=entry_block)


# variables

# int a = 1;
a_type = TYPES.get("int")(32)
a_name = "a"
a_ref = builder.alloca(a_type, name=a_name)
a_ref.align = 4
builder.store(TYPES.get("constant")(a_type, 1), a_ref)

# int b = 2;
b_type = TYPES.get("int")(32)
b_name = "b"
b_ref = builder.alloca(b_type, name=b_name)
b_ref.align = 4
builder.store(TYPES.get("constant")(b_type, 2), b_ref)

# int c = 0;
c_type = TYPES.get("int")(32)
c_name = "c"
c_ref = builder.alloca(c_type, name=c_name)
c_ref.align = 4
c_ref.initializer = TYPES.get("constant")(c_type, 0)


if_block = function.append_basic_block(name="if")
builder.branch(if_block)
builder.position_at_end(if_block)

# first condition (a < b)
cmp_type = "<"
cmp_name = "a < b"
first_condition = builder.icmp_signed(cmp_type, builder.load(a_ref), builder.load(b_ref), cmp_name)

with builder.if_else(first_condition) as (then, otherwise):

    with then:
        ## c = 5
        # constant 5
        constant_5 = TYPES.get("constant")(c_type, 5)
        builder.store(constant_5, c_ref)
        pass

    with otherwise:
        ## c = 6
        # constant 6
        constant_6 = TYPES.get("constant")(c_type, 6)
        builder.store(constant_6, c_ref)
        pass

    pass



if_block = function.append_basic_block(name="if")
builder.branch(if_block)
builder.position_at_end(if_block)

# second condition (a < 1024)
cmp_type = "<"
cmp_name = "a < 1024"


# constant 1024
constant_1024 = TYPES.get("constant")(a_type, 1024)

second_condition = builder.icmp_signed(
    cmp_type, builder.load(a_ref), constant_1024, cmp_name)


with builder.if_else(second_condition) as (then, otherwise):

    with then:
        ## c = 10
        # constant 10
        constant_10 = TYPES.get("constant")(c_type, 10)
        builder.store(constant_10, c_ref)
        pass

    with otherwise:
        ## c = 20
        # constant 20
        constant_20 = TYPES.get("constant")(c_type, 20)
        builder.store(constant_20, c_ref)
        pass

    pass



# exit block name
exit_block_name = "exit"
# exit block ref
exit_block = function.append_basic_block(name=exit_block_name)

# jump to exit block
builder.branch(exit_block)
builder.position_at_end(exit_block)

# constant int 0
return_value = 0
return_constant = TYPES.get("constant")(function_return_type, return_value)

# return 0
builder.ret(return_constant)

## save in file (if2.ll)
with open("if2.ll", "w") as file:
    file.write(str(module))

print(module)
