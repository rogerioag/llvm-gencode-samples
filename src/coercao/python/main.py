from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:


int main(){
	int a = 1;
	float b = 1.0;
	a = a + b;
	b = b + a;
	return 0;
}


'''

# Cria o módulo.
modulo = ir.Module('meu_modulo.bc')

FLOAT = ir.FloatType()
INT = ir.IntType(32)

# int main()
tipo_funcao = ir.FunctionType(INT, [])
main = ir.Function(modulo, tipo_funcao, name="main")

bloco_entrada = main.append_basic_block("entry")
bloco_saida = main.append_basic_block("exit")

# ====================================================================

# Trabalhando sobre o corpo da funcao
builder = ir.IRBuilder(bloco_entrada)

# int retorno
retorno = builder.alloca(INT, name='retorno')
retorno.align = 4
# retorno = 0
builder.store(ir.Constant(INT, 0), retorno)

# int a
variavel_a = builder.alloca(INT, name='a')
variavel_a.align = 4
# a = 1
builder.store(ir.Constant(INT, 1), variavel_a)

# float b
variavel_b = builder.alloca(FLOAT, name='b')
variavel_b.align = 4
# b = 1.0
builder.store(ir.Constant(FLOAT, 1.0), variavel_b)

# ====================================================================

# a = a + b

# Para resolver a atribuição "a = a + b", o compilador C
# faz um cast de "a" para "float" e então faz soma.
# Por fim é feito um cast do resultado para "int" para ser
# armazenado em "a" novamente.

# temp1 = a
temp1 = builder.load(variavel_a, name="temp1")
# temp2 = (float) temp1
temp2 = builder.sitofp(temp1, FLOAT, name="temp2")

# temp3 = b 
temp3 = builder.load(variavel_b, name="temp3")

# temp4 = temp2 + temp3
temp4 = builder.fadd(temp2, temp3, name="temp4")

# temp5 = (int) temp4
temp5 = builder.fptosi(temp4, INT, name="temp5")

# a = temp5
builder.store(temp5, variavel_a)

# ====================================================================

# b = b + a

# Para resolver a atribuição "b = b + a", a operação é parecida
# com a realizada anteriormente. Contudo, no final não é necessário
# fazer um cast reverso.


# temp6 = b
temp6 = builder.load(variavel_b, name="temp6")

# temp7 = a
temp7 = builder.load(variavel_a, name="temp7")
# temp8 = (float) a
temp8 = builder.sitofp(temp7, FLOAT, name="temp8")

# temp9 = temp6 + temp8
temp9 = builder.fadd(temp6, temp8, name="temp9")

# b = temp9
builder.store(temp9, variavel_b)

# Jump (obrigatório)
builder.branch(bloco_saida)

# ====================================================================

# Trabalhando sobre o bloco de retorno
builder.position_at_end(bloco_saida)

# return 0;
temp_retorno = builder.load(retorno, name="temp_retorno")
builder.ret(temp_retorno)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(modulo))
arquivo.close()
print(modulo)
