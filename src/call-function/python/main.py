from llvmlite import ir
from llvmlite import binding as llvm
'''
Este módulo contém uma função main, uma função inteira "soma" que aceita 2 parâmetros inteiros e uma função "teste" que não retorna nada.
Será gerado um código em LLVM como este em C:


int soma (int a, int b){
	return a + b;
}

void teste (){

}

int main(){

	int a = 1;
	int b = 2;

	int res = soma(a,b);

	teste();
	
	return res;
}
'''

# Cria o módulo e faz inifialização do llvm.
llvm.initialize()
llvm.initialize_all_targets()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()
module = ir.Module('meu_modulo.bc')
module.triple = llvm.get_process_triple()
target = llvm.Target.from_triple(module.triple)
target_machine = target.create_target_machine()
module.data_layout = target_machine.target_data

# Cria o cabeçalho da função soma
t_soma = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
soma = ir.Function(module, t_soma, 'soma')
soma.args[0].name = 'a' #Esses nomes atribuidos são os mesmos nomes usados na declaração das variaveis usadas, ver linhas 96 e 100
soma.args[1].name = 'b'

# Cria os blocos de entrada e saidaa da função soma
entryBlock = soma.append_basic_block('entry')
endBasicBlock = soma.append_basic_block('exit')

#Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlock)

#Realiza a operação de soma
res = builder.add(soma.args[0], soma.args[1])

#Pula para o bloco de saida
builder.branch(endBasicBlock)

#Posiciona na saida da funçao
builder.position_at_start(endBasicBlock)
#Retorna res
builder.ret(res)

# Cria o cabeçalho da função teste
t_teste = ir.FunctionType(ir.VoidType(), [])
teste = ir.Function(module, t_teste, 'teste')

# Cria o bloco de entrada e saida
entryBlock = teste.append_basic_block('entry')
endBasicBlock = teste.append_basic_block('exit')

#Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlock)
builder.position_at_start(entryBlock)

#Pula para o bloco de saida
builder.branch(endBasicBlock)

#Adiciona o bloco de saida
builder.position_at_start(endBasicBlock)
#Retorna vazio pois a função teste retorna void
builder.ret_void()

# Cria o cabeçalho da função main
t_main = ir.FunctionType(ir.IntType(32), [])
main = ir.Function(module, t_main, 'main')

# Cria o bloco de entrada e saida da main
entryBlockMain = main.append_basic_block('entry')
endBasicBlockMain = main.append_basic_block('exit')

#Adiciona o bloco de entrada
builder = ir.IRBuilder(entryBlockMain)

# int a = 1;
a = builder.alloca(ir.IntType(32), name='a')
builder.store(ir.Constant(ir.IntType(32), 1), a)

# int b = 2;
b = builder.alloca(ir.IntType(32), name='b')
builder.store(ir.Constant(ir.IntType(32), 2), b)

# int res = soma(a,b);
res = builder.alloca(ir.IntType(32), name='res')
call = builder.call(soma, [builder.load(a), builder.load(b)])
builder.store(call, res)

# teste();
builder.call(teste, [])

#Pula para o bloco de saida
builder.branch(endBasicBlock)

#Adiciona o bloco de saida
builder.position_at_start(endBasicBlockMain)

# return res;
returnVal_temp = builder.load(res, name='ret_temp', align=4)
builder.ret(returnVal_temp)

arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)
