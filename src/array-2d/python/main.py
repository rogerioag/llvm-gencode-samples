from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array bidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

/*
int B[2048][2048];

int main(){

	float D[2048][2048];

	B[0][1] = B[1][1] + 10;

	D[0][1] = D[1][1] + 10;
		
	return 0;
}
*/
'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Array global de 2048 x 2048 elementos.
typeB_0 = ir.ArrayType(ir.IntType(64), 2048)
typeB = ir.ArrayType(typeB_0, 2048)

arrayB = ir.GlobalVariable(module, typeB, "B")
# arrayB.initializer = ir.Constant.array(ir.IntType(64), 0)

# arrayA.initializer = ir.IntType(64)
arrayB.linkage = "common"
# arrayA.initializer = ir.Constant(ir.IntType(64), 0)
arrayB.align = 16

# Cria um valor zero para colocar no retorno.
Zero64 = ir.Constant(ir.IntType(64), 0)

# Declara o tipo do retorno da função main.
mainFnReturnType = ir.IntType(64)
# Cria a função main.
t_func_main = ir.FunctionType(mainFnReturnType, ())

# Declara a função main.
main = ir.Function(module, t_func_main, name='main')

# Declara o bloco de entrada.
entryBlock = main.append_basic_block('entry')
exitBasicBlock = main.append_basic_block('exit')

# Adiciona o bloco de entrada.
builder = ir.IRBuilder(entryBlock)

# Cria o valor de retorno e inicializa com zero.
returnVal = builder.alloca(ir.IntType(64), name='retorno')
builder.store(Zero64, returnVal)

# Array local de 2048 x 2048 elementos.
typeD_0 = ir.ArrayType(ir.IntType(64), 2048)
typeD = ir.ArrayType(typeD_0, 2048)

arrayD = builder.alloca(typeD, name='D')
arrayD.align = 16


# B[0][1] = B[1][1] + 10;
# D[0][1] = D[1][1] + 10
# Na documentação diz para usar um indice a mais, o primeiro em zero: http: // releases.llvm.org/2.3/docs/GetElementPtr.html  # extra_index
# The first index, i64 0 is required to step over the global variable % MyStruct. Since the first argument to the GEP instruction must always be a value of pointer type, the first index steps through that pointer. A value of 0 means 0 elements offset from that pointer.
int_ty = ir.IntType(64)

ptr_B_1_1 = builder.gep(arrayB, [int_ty(0), int_ty(1), int_ty(1)], name='ptr_B_1_1')

elem_B_1_1 = builder.load(ptr_B_1_1, name='', align=4)

add_temp = builder.add(elem_B_1_1, int_ty(10), name='', flags=())

# Armazena em B[0][1]
ptr_B_0_1 = builder.gep(
    arrayB, [int_ty(0), int_ty(0), int_ty(1)], name='ptr_B_0_1')

builder.store(add_temp, ptr_B_0_1)

# D[0][1] = D[1][1] + 10

ptr_D_1_1 = builder.gep(
    arrayD, [int_ty(0), int_ty(1), int_ty(1)], name='ptr_D_1_1')

elem_D_1_1 = builder.load(ptr_D_1_1, name='', align=4)

add_temp2 = builder.add(elem_D_1_1, int_ty(10), name='', flags=())

# Armazena em D[0][1]
ptr_D_0_1 = builder.gep(
    arrayD, [int_ty(0), int_ty(0), int_ty(1)], name='ptr_D_0_1')

builder.store(add_temp2, ptr_D_0_1)


# Cria um salto para o bloco de saída.
builder.branch(exitBasicBlock)

# Adiciona o bloco de saída.
builder = ir.IRBuilder(exitBasicBlock)

# Cria o return.
builder.ret(builder.load(returnVal, ""))

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
