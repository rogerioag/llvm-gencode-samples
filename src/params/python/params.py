# -*- coding: utf-8 -*-


from llvmlite import ir

from llvmlite import ir

'''
Este módulo apresenta um exemplo de como os parâmetros devem ser tratados.
São criadas variáveis locais e os parâmetros são compiados para elas.
Será gerado um código em LLVM como este em C:

/*
int func(int p1, float p2) {
  int r;
  return r;
}
int main(int argv) {
  int x;
  
  x = func(1,2);
  return 0;
}
*/

'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Cria o cabeçalho da função func
t_func = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.FloatType()])
func = ir.Function(module, t_func, 'func')
func.args[0].name = 'p1'
func.args[1].name = 'p2'

# Cria o corpo da função func
entryBlock = func.append_basic_block('entry')
builder = ir.IRBuilder(entryBlock)

#cria int r
r = builder.alloca(ir.IntType(32), name='r')
#builder.store(ir.Constant(ir.IntType(32), 0), r)
r.align = 4
#retorna r
builder.ret(builder.load(r))

# Cria o cabeçalho da função main
t_main = ir.FunctionType(ir.IntType(32), [ir.IntType(32)])
main = ir.Function(module, t_main, 'main')
main.args[0].name = 'argv'

# Cria o corpo da função main
entryBlock = main.append_basic_block('entry')
builder = ir.IRBuilder(entryBlock)

#cria int x
x = builder.alloca(ir.IntType(32), name='x')

#cria variavel temporaria inteira e adiciona 1 no valor
temp1= builder.alloca(ir.IntType(32), name='temp1')
builder.store(ir.Constant(ir.IntType(32), 1), temp1)

#cria variavel temporaria flutuante e adiciona 2 no valor
temp2= builder.alloca(ir.FloatType(), name='temp2')
builder.store(ir.Constant(ir.FloatType(), 2), temp2)

#chama func e armazena em x
call = builder.call(func, [builder.load(temp1), builder.load(temp2)])
builder.store(call, x)

#cria variavel retorno como 0
retorno = builder.alloca(ir.IntType(32), name='retorno')
retorno.align = 4
aux = ir.Constant(ir.IntType(32), 0) 
builder.store(aux, retorno)

#retorna variavel retorno com valor 0
builder.ret(builder.load(retorno))


arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
