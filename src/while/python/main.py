from llvmlite import ir

'''
Este módulo contém um exemplo com o laço while, printf e operações aritméticas.
Será gerado um código em LLVM como este em C:

int main() {
    int a = 10;

    while(a > 0) {
        printf("%d\n", a);
        a = a - 1;
    }

    return 0;
}

'''


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


def decrementa_var(var, value: int):
    global bloco

    # Carrega valor da variável
    _var = bloco.load(var)

    # Cria constante de decremento
    constant = ir.Constant(ir.IntType(32), value)

    # Efetua subtração
    result = bloco.sub(_var, constant)

    # Salva o resultado da subtração na variável
    bloco.store(result, var)


if __name__ == "__main__":
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

    # Entra no bloco de entrada
    bloco = ir.IRBuilder(bloco_entrada)
    a = declara_e_atribui("a", ir.IntType(32), 10)

    # Cria blocos para validar a condição e de execução, caso seja válida a expressão
    bloco_valida_while = main.append_basic_block("valida_while")
    bloco_exec_while = main.append_basic_block("executa_while")

    # Salta do bloco principal para o bloco de validação da expressão
    bloco.branch(bloco_valida_while)

    # Entra no bloco de validação
    bloco = ir.IRBuilder(bloco_valida_while)

    # Faz a comparação
    comparacao = bloco.icmp_signed(">", bloco.load(a),
                                   ir.Constant(ir.IntType(32), 0))

    # Salto condicional, se verdade salta para o bloco de execução, salta para o bloco de saída
    bloco.cbranch(comparacao, bloco_exec_while, bloco_saida)

    # Entra no bloco de execução
    bloco = ir.IRBuilder(bloco_exec_while)

    # Escreve o valor de 'a'
    bloco.call(escrevaI, args=[bloco.load(a)])

    # Decrementa o valor de 'a'
    decrementa_var(a, 1)

    # Salta para o bloco de validação (loop)
    bloco.branch(bloco_valida_while)

    # Entra no bloco de saída
    bloco = ir.IRBuilder(bloco_saida)

    # Cria constante de retorno
    retorno = ir.Constant(ir.IntType(32), 0)

    # Efetua o retorno
    bloco.ret(retorno)

    with open('meu_modulo.ll', 'w') as arquivo:
        arquivo.write(str(modulo))
