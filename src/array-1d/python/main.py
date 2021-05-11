from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

int A[1024];

int main(){

  int B[1024];

  A[50] = A[49] + 5;

  B[0] = B[1] + 10;
    
  return 0;
}
'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Array global de 1024 elementos.
typeA = ir.ArrayType(ir.IntType(32), 1024)

arrayA = ir.GlobalVariable(module, typeA, "A")
# arrayA.initializer = ir.Constant(ir.ArrayType(ir.IntType(64), 1024), 0)

arrayA.linkage = "common"

arrayA.initializer = ir.Constant(typeA, None)
arrayA.align = 4

# Cria um valor zero para colocar no retorno.
Zero64 = ir.Constant(ir.IntType(32), 0)

# Declara o tipo do retorno da função main.
mainFnReturnType = ir.IntType(32)
# Cria a função main.
t_func_main = ir.FunctionType(mainFnReturnType, ())

# Declara a função main.
main = ir.Function(module, t_func_main, name='main')

# Declara o bloco de entrada.
entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')

# Adiciona o bloco de entrada.
builder = ir.IRBuilder(entryBlock)

# Cria o valor de retorno e inicializa com zero.
returnVal = builder.alloca(ir.IntType(32), name='retorno')
builder.store(Zero64, returnVal)

# Array local de 1024 elementos.
typeB = ir.ArrayType(ir.IntType(32), 1024)

arrayB = builder.alloca(typeB, name='B')
arrayB.align = 4


# A[50] = A[49] + 5;
# Na documentação diz para usar dois indices, o primeiro em zero: http://releases.llvm.org/2.3/docs/GetElementPtr.html#extra_index
# The first index, i64 0 is required to step over the global variable %MyStruct. Since the first argument to the GEP instruction must always be a value of pointer type, the first index steps through that pointer. A value of 0 means 0 elements offset from that pointer.

#indices = [ir.Constant(ir.IntType(64), 0), ir.Constant(ir.IntType(64), 49)]

int_ty = ir.IntType(32)

ptr_A_49 = builder.gep(arrayA, [int_ty(0), int_ty(49)], name='ptr_A_49')

# ptr_A_49 = builder.gep(arrayA, [indices], name='ptr_A_49')

elem_A_49 = builder.load(ptr_A_49, name='', align=4)

temp_add = builder.add(elem_A_49, int_ty(5), name='', flags=())

# Armazena no A[50].
ptr_A_50 = builder.gep(arrayA, [int_ty(0), int_ty(50)], name='ptr_A_50')

builder.store(temp_add, ptr_A_50)

# Cria um salto para o bloco de saída.
builder.branch(endBasicBlock);

# Adiciona o bloco de saída.
builder = ir.IRBuilder(endBasicBlock)
  
# Cria o return.
builder.ret(builder.load(returnVal, ""))

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
