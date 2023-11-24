# Exemplos de Geração de Código LLVM [[llvm-gencode-samples](https://github.com/rogerioag/llvm-gencode-samples)]

Repositório de exemplos de geração de código intermediário do [`LLVM`](https://llvm.org/), o [`LLVM-IR`](https://llvm.org/docs/LangRef.htm) utilizando as  `LLVM C API` e [`llvmlite`](https://github.com/numba/llvmlite) (Python).

São apresentadas implementações seguindo a nomenclatura:

+ **Ref**: De referência exemplo escrito em `C` compilado com o `clang`.

+ **C**: Implementação utilizando `LLVM C API`.
+ **Python**: Implementação utilizando `llvmlite`

Os exemplos estão organizados em ordem crescente de dificuldade:

## Exemplos:

+ [Criação de Módulo](src/modulo)
    - [Ref](src/modulo/ref)
    - [C](src/modulo/C)
    - [Python](src/modulo/python)

+ [Declaração de Variáveis](src/vars)
    - [Ref](src/vars/ref)
    - [C](src/vars/C)
    - [Python](src/vars/python)

+ [Atribuição e Expressões](src/atribuicao)
    - [Ref](src/atribuicao/ref)
    - [C](src/atribuicao/C)
    - [Python](src/atribuicao/python)

+ [Instruções Lógicas e Aritméticas](src/instrucoes-logicas-aritmeticas)
    - [Ref](src/instrucoes-logicas-aritmeticas/ref)
    - [C](src/instrucoes-logicas-aritmeticas/C)
    - [Python](src/instrucoes-logicas-aritmeticas/python)

+ [Coerção](src/coercao)
    - [Ref](src/coercao/ref)
    - [C](src/coercao/C)
    - [Python](src/coercao/python)

+ [Declaração de Array 1d](src/array-1d)
    - [Ref](src/array-1d/ref)
    - [C](src/array-1d/C)
    - [Python](src/array-1d/python)

+ [Declaração de Array 2d](src/array-2d)
    - [Ref](src/array-2d/ref)
    - [C](src/array-2d/C)
    - [Python](src/array-2d/python)

+ [Declaração da Função `main`](src/funcao-main)
    - [Ref](src/funcao-main/ref)
    - [C](src/funcao-main/C)
    - [Python](src/funcao-main/python)

+ [Comando de Seleção: If 1](src/if-1)
    - [Ref](src/if-1/ref)
    - [C](src/if-1/C)
    - [Python](src/if-1/python)

+ [Comando de Seleção: If 2](src/if-2)
    - [Ref](src/if-2/ref)
    - [C](src/if-2/C)
    - [Python](src/if-2/python)

+ [Comando de Seleção: If 3](src/if-3)
    - [Ref](scr/if-3/ref)
    - [C](src/if-3/C)
    - [Python](src/if-3/python)

+ [Comando de Seleção: Phi](src/phi)
    - [Ref](src/phi/ref)
    - [C](src/phi/C)
    - [Python](src/phi/python)

+ [Repetição: Repeat..until](src/repeat-until)
    - [Ref](src/repeat-until/ref)
    - [C](src/repeat-until/C)
    - [Python](src/repeat-until/python)

+ [Repetição: Do...while](src/do-while)
    - [Ref](src/do-while/ref)
    - [C](src/do-while/C)
    - [Python](src/do-while/python)

+ [Repetição: While](src/while)
    - [Ref](src/while/ref)
    - [C](src/while/C)
    - [Python](src/while/python)

+ [Repetição: For loop](src/for)
    - [Ref](src/for/ref)
    - [C](src/for/C)
    - [Python](src/for/python)

+ [Function Parameters](src/params)
    - [Ref](src/params/ref)
    - [C](src/params/C)
    - [Python](src/params/python)

+ [Chamada de Função: Call Function](src/call-function)
    - [Ref](src/call-function/ref)
    - [C](src/call-function/C)
    - [Python](src/call-function/python)

+ [Chamada de Funções Aninhadas: Nested Call Functions](src/nested-call-function)
    - [Ref](src/nested-call-function/ref)
    - [C](src/nested-call-function/C)
    - [Python](src/nested-call-function/python)

+ [Chamada de Função Externa: Call External Function](src/call-external-function)
    - [Ref](src/call-external-function/ref)
    - [C](src/call-external-function/C)
    - [Python](src/call-external-function/python)

+ [Funções Leia e escreva](src/leia-escreva)
    - [Ref](src/leia-escreva/ref)
    - [C](src/leia-escreva/C)
    - [Python](src/leia-escreva/python)

+ [Scanf](src/scanf)
    - [Ref](src/scanf/ref)
    - [C](src/scanf/C)
    - [Python](src/scanf/python)

+ [Exemplo: Hello World](src/hello)
    - [Ref](src/hello/ref)
    - [C](src/hello/C)
    - [Python](src/hello/python)

+ [Exemplo: Sum](src/sum)
    - [Ref](src/sum/ref)
    - [C](src/sum/C)
    - [Python](src/sum/python)
