from llvmlite import ir

'''
Este módulo contém um exemplo de instruções aritméticas/lógicas.
Será gerado um código em LLVM como este em C:

int main(){
    int a = 1;
    float b = 1.0;
    float c = 2.0;
    a = a + a;
    b = b + c;
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


if __name__ == "__main__":
    # Cria o módulo.
    modulo = ir.Module('meu_modulo.bc')

    # Declaração da função 'principal', que DEVE ser usada com o nome 'main'.
    main_type = ir.FunctionType(ir.IntType(32), [])
    main = ir.Function(modulo, main_type, "main")

    # Cria blocos de entrada e saída
    bloco_entrada = main.append_basic_block("bloco_entrada")
    bloco_saida = main.append_basic_block("bloco_saida")

    # Entra no bloco de entrada
    bloco = ir.IRBuilder(bloco_entrada)

    # int a = 1;
    a = declara_e_atribui("a", ir.IntType(32), 1)

    # float b = 1.0;
    b = declara_e_atribui("b", ir.FloatType(), 1.0)

    # float c = 2.0;
    c = declara_e_atribui("c", ir.FloatType(), 2.0)

    # a = a + a;
    # Carrega 'a'
    a_load = bloco.load(a)

    # Efetua adição
    res = bloco.add(a_load, a_load)

    # Armazena em 'a' o resultado
    bloco.store(res, a, 4)

    # b = b + c;
    # Carrega variáveis 'b' e 'c'
    b_load = bloco.load(b)
    c_load = bloco.load(c)

    # Efetua adição
    res = bloco.add(b_load, c_load)

    # Armazena em 'b' o resultado
    bloco.store(res, b, 4)

    # Entra no bloco de saída
    bloco = ir.IRBuilder(bloco_saida)

    # Cria constante de retorno
    retorno = ir.Constant(ir.IntType(32), 0)

    # Efetua o retorno
    bloco.ret(retorno)

    with open('meu_modulo.ll', 'w') as arquivo:
        arquivo.write(str(modulo))
