from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:
<<Colocar o Código do Exemplo de Referência.>>
int main(){

	char * helloworld = "Hello World!!";

	printf("%s\n", helloworld);

	printf("%d\n", 23);

	return 0;
}
'''

# Variável auxiliar
intType = ir.IntType(32)
voidType = ir.IntType(8).as_pointer()

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Funções para a escrita de inteiro e de string
escrevaInteiro = ir.Function(module, ir.FunctionType(ir.VoidType(), [ir.IntType(32)]), name="escrevaInteiro")
escrevaChar = ir.Function(module, ir.FunctionType(ir.VoidType(), [voidType], var_arg=True), name="escrevaChar")

# Declara função
func = ir.FunctionType(intType, ())

# Cria o cabeçalho da função main
main = ir.Function(module, func, name='main')

# Cria o corpo da função main
entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')
builder = ir.IRBuilder(entryBlock)

# Cria a string com o valor padrão
string = "Hello world!!\n\0"

# Cria o tipo da string
stringType = ir.ArrayType(ir.IntType(8), len(string))

# Cria o valor da constante
stringVal = ir.Constant(stringType, bytearray(string.encode("utf8")))

# Cria a variável
stringVar = builder.alloca(stringVal.type, name='string')

# Guarda a variável
builder.store(stringVal, stringVar)

# Faz a chamada para a função: escrevaChar
funcArg = builder.bitcast(stringVar, voidType)
builder.call(escrevaChar, [funcArg, stringVar])

# Faz a chamada para a função: escrevaInteiro
builder.call(escrevaInteiro, [ir.Constant(intType, 23)])

# Cria um salto para o bloco de saída
builder.branch(endBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(endBasicBlock)

# Cria a variável de retorno
returnValue = builder.alloca(intType, name='variavel_retorno')
returnValue.align = 4

# Adiciono o valor 0 na variável
builder.store(ir.Constant(intType, 0), returnValue)

# Carrega a variável
returnVarLoad = builder.load(returnValue, name='retorno', align=4)

# Retorna ela
builder.ret(returnVarLoad)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)