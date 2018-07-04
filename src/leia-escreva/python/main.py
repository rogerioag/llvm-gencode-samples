from llvmlite import ir

'''
Este módulo contém uma função main e exemplo de uso das funções printf e scanf.
Será gerado um código em LLVM como este em C:

int main() {
    int a;

    a = scanf("%d", &a);
    printf("%d", a);
    
    return 0;
}

'''

if __name__ == '__main__':
    modulo = ir.Module('meu_modulo.bc')

    # Declaração das funções que serão 'adicionadas' em tempo de vinculação.
    _escrevaI = ir.FunctionType(ir.VoidType(), [ir.IntType(32)])
    escrevaI = ir.Function(modulo, _escrevaI, "escrevaInteiro")

    _escrevaF = ir.FunctionType(ir.VoidType(), [ir.FloatType()])
    escrevaF = ir.Function(modulo, _escrevaF, "escrevaFlutuante")

    _leiaI = ir.FunctionType(ir.IntType(32), [])
    leiaI = ir.Function(modulo, _leiaI, "leiaInteiro")

    _leiaF = ir.FunctionType(ir.FloatType(), [])
    leiaF = ir.Function(modulo, _leiaF, "leiaFlutuante")

    # Declaração da função 'principal', que DEVE ser usada com o nome 'main'.
    main_type = ir.FunctionType(ir.IntType(32), [])
    main = ir.Function(modulo, main_type, "main")

    # Cria blocos de entrada e saída
    bloco_entrada = main.append_basic_block("bloco_entrada")
    bloco_saida = main.append_basic_block("bloco_saida")

    # Entra no bloco de entrada
    bloco = ir.IRBuilder(bloco_entrada)

    # Aloca variável 'a'
    a = bloco.alloca(ir.IntType(32), 4, "a")

    # Invoca a função 'leiaI' e salva o resultado no ponteiro
    # que representa a variável 'a'
    resultado_leia = bloco.call(leiaI, args=[])
    bloco.store(resultado_leia, a, align=4)

    # Invoca a função 'escrevaI', carregando o valor da variável 'a'
    # e o passando como argumento
    bloco.call(escrevaI, args=[bloco.load(a)])

    # Salto para bloco de saída
    bloco.branch(bloco_saida)

    # Entra no bloco de saída
    bloco = ir.IRBuilder(bloco_saida)

    # Cria constante de retorno
    retorno = ir.Constant(ir.IntType(32), 0)

    # Efetua o retorno
    bloco.ret(retorno)

    with open('meu_modulo.ll', 'w') as arquivo:
        arquivo.write(str(modulo))
