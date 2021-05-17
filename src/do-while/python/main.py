from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

<<Colocar o Código do Exemplo de Referência.>>

int main(){

	int i = 0;
	int a = 1;

	do{
		a = 5;
		i =  i + 1;
	} while(i < 1024);
		
	return 0;
}

'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Declara função
func = ir.FunctionType(ir.IntType(32), ())

# Cria o cabeçalho da função main
main = ir.Function(module, func, name='main')

# Cria o corpo da função main
entryBlock = main.append_basic_block('entry')
endBasicBlock = main.append_basic_block('exit')
builder = ir.IRBuilder(entryBlock)

# Aloca variável do tipo inteiro
i = builder.alloca(ir.IntType(32), name='i')
a = builder.alloca(ir.IntType(32), name='a')

# Define o alinhamento
i.align = 4
a.align = 4

# Define variável com valor 1z
auxi = ir.Constant(ir.IntType(32), 1)
auxa = ir.Constant(ir.IntType(32), 1)
builder.store(auxi, i)
builder.store(auxa, a)

loop = builder.append_basic_block('loop')
lopp_val = builder.append_basic_block('loop_val')
loop_end = builder.append_basic_block('loop_end')

# Pula para o laço do loop
builder.branch(loop)

# Posiciona no inicio do bloco do loop e define o que o loop irá executar
builder.position_at_end(loop)
builder.store(ir.Constant(ir.IntType(32), 5), a)
soma = builder.add(builder.load(i), ir.Constant(ir.IntType(32), 1))
builder.store(i, soma)

# Pula para o laço de validação
builder.branch(lopp_val)

# Posiciona no inicio do bloco de validação e define o que o loop de validação irá executar
builder.position_at_end(lopp_val)

i_loaded = builder.load(i, 'i', align=4)
aux_number = ir.Constant(ir.IntType(32), 1024)

# Gera a expressão de comparação
expression = builder.icmp_signed('<', i_loaded, aux_number, name='expression')

# Compara se a expressão é verdadeira ou não, caso for pula para o bloco do loop, caso contrário pula para o bloco do loop end
builder.cbranch(expression, loop, loop_end)

# Posiciona no inicio do bloco do fim do loop (saída do laço) e define o que o será executado após o fim (o resto do programa)  
builder.position_at_end(loop_end)

# Cria um salto para o bloco de saída
builder.branch(endBasicBlock)

# Adiciona o bloco de saida
builder.position_at_end(endBasicBlock)

retorno = builder.alloca(ir.IntType(32), name='retorno')
retorno.align = 4
aux = ir.Constant(ir.IntType(32), 0) 
builder.store(aux, retorno)

# Retorna res
res = builder.load(retorno, name='res', align=4)
builder.ret(res)

# Open e print módulo
arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
