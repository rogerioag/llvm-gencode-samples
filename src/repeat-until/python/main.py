from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

<<Colocar o Código do Exemplo de Referência.>>

int main(){

	int i = 0;
	int a = 1;

	do {
		a = 5;
		i =  i + 1;
	} while(i = 1024);
		
	return 0;
}

'''

# Variável auxiliar
intType = ir.IntType(32)

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Declara função
func = ir.FunctionType(intType, ())

# Cria o cabeçalho da função main
main = ir.Function(module, func, name='main')

# Cria o corpo da função main
entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')
builder = ir.IRBuilder(entryBlock)

# Aloca variável do tipo inteiro
iVar = builder.alloca(intType, name='i')
iVar.align = 4

# Insere o valor 0 para a variável 'i'
zeroValue = ir.Constant(intType, 0) 
builder.store(zeroValue, iVar)

# Aloca variável do tipo inteiro
aVar = builder.alloca(intType, name='a')
aVar.align = 4

# Insere o valor 1 para a variável 'a'
oneValue = ir.Constant(intType, 1) 
builder.store(oneValue, aVar)

# Cria os blocos de repetição
loop = builder.append_basic_block('loop')
loop_val = builder.append_basic_block('loop_val')
loop_end = builder.append_basic_block('loop_end')

# Pula para o laço do loop
builder.branch(loop)

# Posiciona no inicio do bloco do loop
builder.position_at_end(loop)

# Insere o valor 5 para a variável 'a'
fiveValue = ir.Constant(intType, 5) 
builder.store(fiveValue, aVar)

# Carrega a variável 'i'
iVarLoad = builder.load(i)

# i + 1
sumExpression = builder.add(iVarLoad, oneValue)

# i = i + 1
builder.store(i, soma)

# Pula para o laço de validação
builder.branch(lopp_val)

# Posiciona no inicio do bloco de validação
builder.position_at_end(loop_val)

# Valor de comparação
comperValue = ir.Constant(intType, 1024) 

# Gera a expressão de comparação
sumExpression = builder.icmp_signed('==', iVarLoad, comperValue, name='expressao_soma')

# Compara se a expressão é verdadeira ou não, caso for pula para o bloco do loop end, caso contrário pula para o bloco do loop
builder.cbranch(sumExpression, loop_end, loop)

# Posiciona no inicio do bloco do fim do loop (saída do laço) e define o que o será executado após o fim (o resto do programa)  
builder.position_at_end(loop_end)

# Cria um salto para o bloco de saída
builder.branch(endBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(endBasicBlock)

# Cria a variável de retorno
returnValue = builder.alloca(intType, name='variavel_retorno')
returnValue.align = 4

# Adiciono o valor 0 na variável
builder.store(zeroValue, returnValue)

# Carrega a variável
returnVarLoad = builder.load(returnValue, name='retorno', align=4)

# Retorna ela
builder.ret(returnVarLoad)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)