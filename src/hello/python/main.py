from llvmlite import ir

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

<<Colocar o Código do Exemplo de Referência.>>

'''

# Cria o módulo.
module = ir.Module('meu_modulo.bc')

# Cria um valor zero para colocar no retorno.
Zero32 = ir.Constant(ir.IntType(32), 0)

# Declara o tipo do retorno da função main.
mainFnReturnType = ir.IntType(32)
# Cria a função main.
t_func_main = ir.FunctionType(mainFnReturnType, ())

# Declara a função printf.
printfFunction = ir.Function(module, "printf", printfTy);


# Declara a função main.
main = ir.Function(module, t_func_main, name='main')

cstring = voidptr_t
    fmt_bytes = make_bytearray((format + '\00').encode('ascii'))
    global_fmt = global_constant(mod, "printf_format", fmt_bytes)
    fnty = ir.FunctionType(int32_t, [cstring], var_arg=True)
    # Insert printf()
    fn = mod.get_global('printf')
    if fn is None:
        fn = ir.Function(mod, fnty, name="printf")
    # Call
    ptr_fmt = builder.bitcast(global_fmt, cstring)
    return builder.call(fn, [ptr_fmt] + list(args))



# Declara o bloco de entrada.
entryBlock = main.append_basic_block('entry')

endBasicBlock = main.append_basic_block('exit')

# Adiciona o bloco de entrada.
builder = ir.IRBuilder(entryBlock)

# Cria o valor de retorno e inicializa com zero.
returnVal = builder.alloca(ir.IntType(32), name='retorno')
builder.store(Zero32, returnVal)









arquivo = open('meu_modulo.ll', 'w')
arquivo.write(str(module))
arquivo.close()
print(module)