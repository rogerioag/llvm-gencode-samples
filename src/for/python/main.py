from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
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

    # Define o alinhamento de 4 bytes
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
    # Cria o módulo.
    modulo = ir.Module('meu_modulo.bc')

    # Declaração das funções que serão 'adicionadas' em tempo de vinculação.
    _escrevaI = ir.FunctionType(ir.VoidType(), [ir.IntType(32)])
    escrevaI = ir.Function(modulo, _escrevaI, "escrevaInteiro")

    # Declaração da função 'principal', que DEVE ser usada com o nome 'main'.
    main_type = ir.FunctionType(ir.IntType(32), [])
    main = ir.Function(modulo, main_type, "main")

    # Cria blocos de entrada e saída
    bloco_entrada = main.append_basic_block("bloco_entrada")
    bloco_saida = main.append_basic_block("bloco_saida")

    global bloco
    # Entra no bloco de entrada
    bloco = ir.IRBuilder(bloco_entrada)

    # int i = 1
    i = declara_e_atribui("i", ir.IntType(32), 1)

    # Cria blocos para validar a condição e de execução, caso seja válida a expressão
    bloco_valida_for = main.append_basic_block("valida_for")
    bloco_exec_for = main.append_basic_block("executa_for")

    # Salta do bloco principal para o bloco de validação da expressão
    bloco.branch(bloco_valida_for)

    # Entra no bloco de validação
    bloco = ir.IRBuilder(bloco_valida_for)

    # Faz a comparação de i < 11
    comparacao = bloco.icmp_signed("<", bloco.load(i),
                                   ir.Constant(ir.IntType(32), 11))

    # Salto condicional, se verdade salta para o bloco de execução, salta para o bloco de saída
    bloco.cbranch(comparacao, bloco_exec_for, bloco_saida)

    # Entra no bloco de execução
    bloco = ir.IRBuilder(bloco_exec_for)

    # printf("%d", i);
    bloco.call(escrevaI, args=[bloco.load(i)])

    # i++
    incrementa_var(i, 1)

    # Salta para o bloco de validação (loop)
    bloco.branch(bloco_valida_for)

    # Entra no bloco de saída
    bloco = ir.IRBuilder(bloco_saida)

    # return 0;
    bloco.ret(ir.Constant(ir.IntType(32), 0))

    with open('for.ll', 'w') as arquivo:
        arquivo.write(str(modulo))

if __name__ == "__main__":
    main()