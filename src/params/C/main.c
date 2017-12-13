#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

/*
int func(int p1, float p2) {
  int r;
  return r;
}

int main(int argc, char **argv) {
  int x;
  
  x = func(1,2);

  return 0;
}
*/

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo.bc", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // criação da função para adicionar ao módulo.
  LLVMTypeRef funcParams[] = {LLVMInt32Type(), LLVMFloatType()};
  LLVMTypeRef funcType = LLVMFunctionType(LLVMInt32Type(), funcParams, 2, 0);
  LLVMValueRef func = LLVMAddFunction(module, "func", funcType); 

  // criação de um bloco básico para adicionar o código principal da função "soma"
  LLVMBasicBlockRef entryFunc = LLVMAppendBasicBlock(func, "entry");

  // Declara o bloco de saída.
  LLVMBasicBlockRef exitFunc = LLVMAppendBasicBlock(func, "exit");
  
  LLVMPositionBuilderAtEnd(builder, entryFunc);

  // LLVMValueRef LLVMGetParam(LLVMValueRef Fn, unsigned Index);
  LLVMValueRef tmp = LLVMGetParam(func, 0);
  // LLVMBuildAdd(builder, LLVMGetParam(soma, 0), LLVMGetParam(soma, 1), "tmp");

  // Cria um salto para o bloco de saída.
  LLVMBuildBr(builder, exitFunc);

  // Adiciona o bloco de saída.
  LLVMPositionBuilderAtEnd(builder, exitFunc); 
  // LLVMValueRef tmp1 = LLVMBuildLoad(builder, tmp, "ret");

  LLVMBuildRet(builder, tmp);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt64TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock = LLVMAppendBasicBlockInContext(context, mainFn, "entry");
  // Declara o bloco de saída.
  LLVMBasicBlockRef exitBasicBlock = LLVMAppendBasicBlock(mainFn, "exit");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef x = LLVMBuildAlloca(builder, LLVMInt64Type(), "x");
  
  // Declara as variáveis a,b e c.
  LLVMValueRef a = LLVMBuildAlloca(builder, LLVMInt64Type(), "a");
  LLVMValueRef b = LLVMBuildAlloca(builder, LLVMInt64Type(), "b");
  
  // Parâmetros.
  LLVMValueRef args[2] = {
       LLVMConstInt(LLVMInt32Type(), 1, false),
       LLVMConstInt(LLVMFloatType(), 2, false)
  };

  LLVMValueRef callf = LLVMBuildCall(
        builder,
        func,
        args,
        2,
        "x"
  );

  // Cria um salto para o bloco de saída.
  LLVMBuildBr(builder, exitBasicBlock);
  
  // Adiciona o bloco de saída.
  LLVMPositionBuilderAtEnd(builder, exitBasicBlock);
  
  // Cria o return.
  LLVMBuildRet(builder, LLVMBuildLoad(builder, LLVMConstInt(LLVMInt32Type(), 0, false), ""));

  // Imprime o código do módulo.
  LLVMDumpModule(module);

  // Escreve para um arquivo no formato bitcode.
  if (LLVMWriteBitcodeToFile(module, "meu_modulo.bc") != 0) {
    fprintf(stderr, "error writing bitcode to file, skipping\n");
  }
}
