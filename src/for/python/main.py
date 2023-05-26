from llvmlite import ir

'''
Este módulo contém uma função main no qual executa um "for".
Será gerado um código em LLVM como este em C:

int main(){

	int i = 0;
	int a = 1;

	for(i=0; i < 1024; i++) {
		a = i;
	}
		
	return 0;
}


'''

global bloco

def declara_e_atribui(name: str, _type: ir.Type, value) -> ir.AllocaInstr:
    global bloco

    temp = bloco.alloca(_type, name=name)

    # Alinhamento de 4 bytes
    temp.align = 4

    # Cria uma constante pra armazenar o valor passado
    constant = ir.Constant(_type, value)

    # Armazena a constante na variável criada
    bloco.store(constant, temp)

    return temp


def incrementa_var(var, value: int):
    global bloco

    # Carrega valor da variável
    _var = bloco.load(var)

    # Cria constante de decremento
    constant = ir.Constant(ir.IntType(32), value)

    # Efetua subtração
    result = bloco.add(_var, constant)

    # Salva o resultado da subtração na variável
    bloco.store(result, var)


def main():
    global bloco
    # Cria o módulo.
    modulo = ir.Module('meu_modulo.bc')

    # Declaração da função 'main'.
    main_type = ir.FunctionType(ir.IntType(32), [])
    main = ir.Function(modulo, main_type, "main")

    # Cria blocos de entrada e saída
    bloco_entrada = main.append_basic_block("bloco_entrada")
    bloco_saida = main.append_basic_block("bloco_saida")

    # Acessa o bloco de entrada
    bloco = ir.IRBuilder(bloco_entrada)

    # int i = 0
    i = declara_e_atribui("i", ir.IntType(32), 0)
    # int a = 1
    a = declara_e_atribui("a", ir.IntType(32), 0)

    # Cria blocos de condição, execução avaliando a expressão dada, e finalização
    bloco_condicao_for = main.append_basic_block("condicao_for")
    bloco_exec_for = main.append_basic_block("executa_for")
    bloco_final_for = main.append_basic_block("final_for")

    # Salta do bloco principal para o bloco de condição do for
    bloco.branch(bloco_condicao_for)

    # Entra no bloco de condição
    bloco = ir.IRBuilder(bloco_condicao_for)

    # Faz a comparação de i < 1024
    comparacao = bloco.icmp_signed("<", bloco.load(i), ir.Constant(ir.IntType(32), 1024))

    # Salto para o bloco de execução caso a condição for verdadeira, ou de saída se falso
    bloco.cbranch(comparacao, bloco_exec_for, bloco_final_for)

    # Entra no bloco de execução
    bloco = ir.IRBuilder(bloco_exec_for)
    #carrega i
    i_temp = bloco.load(i, "")
    # Armazena o i em a
    bloco.store(i_temp, a)
    # i++
    incrementa_var(i, 1)

    # Salta para o bloco de condição (loop)
    bloco.branch(bloco_condicao_for)

    # Salta para o bloco de saída do for
    bloco = ir.IRBuilder(bloco_final_for)

    # return 0;
    bloco.ret(ir.Constant(ir.IntType(32), 0))

    # Entra no bloco de saída 
    bloco = ir.IRBuilder(bloco_saida) 

    bloco.position_at_end(bloco_saida)

    arquivo = open('for.ll', 'w')
    arquivo.write(str(modulo))
    arquivo.close()
    print(modulo)

if __name__ == "__main__":
    main()