#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

/*
repita
  corpo
até (n = 1024)
*/

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module =
      LLVMModuleCreateWithNameInContext("meu_modulo", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // Cria um valor zero para colocar no retorno.
  LLVMValueRef Zero64 = LLVMConstInt(LLVMInt64Type(), 0, false);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt64TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(
      module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "entry");

  LLVMBasicBlockRef predicateBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "predicate");
  LLVMBasicBlockRef bodyBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "body");
  LLVMBasicBlockRef incVar =
      LLVMAppendBasicBlockInContext(context, mainFn, "inc_var");
  LLVMBasicBlockRef endLoopBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "endloop");

  // Declara o bloco de saída.
  LLVMBasicBlockRef exitBasicBlock = LLVMAppendBasicBlock(mainFn, "exit");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMInt64Type(), "retorno");
  LLVMBuildStore(builder, Zero64, returnVal);

  // Declara uma variável i.
  LLVMValueRef i = LLVMBuildAlloca(builder, LLVMInt64Type(), "i");
  // Inicializa n.
  LLVMBuildStore(builder, LLVMConstInt(LLVMInt64Type(), 0, false), i);

  LLVMBuildBr(builder, bodyBlock);

  // Corpo do loop.
  LLVMPositionBuilderAtEnd(builder, bodyBlock);
  LLVMBuildStore(builder, LLVMConstInt(LLVMInt64TypeInContext(context), 11, 0), returnVal);
  LLVMBuildBr(builder, incVar);

  // Bloco do incremento da variavel de controle.
  LLVMPositionBuilderAtEnd(builder, incVar);
  LLVMValueRef i_inc = LLVMBuildAdd(builder,  LLVMBuildLoad(builder, i, ""), LLVMConstInt(LLVMInt64Type(), 1, false), "i_inc");
  LLVMBuildStore(builder, i_inc, i);

  // Salta para o teste do loop.
  LLVMBuildBr(builder, predicateBlock);

  // Bloco de predicado.
  LLVMPositionBuilderAtEnd(builder, predicateBlock);
  
  // Comparacao de n = 1024.
  LLVMValueRef i_cmp = LLVMBuildLoad(builder, i, "i");
  LLVMValueRef cmpVal = LLVMBuildICmp(builder, LLVMIntEQ, i_cmp, LLVMConstInt(LLVMInt64Type(), 1024, false), "repeat_test");

  // Teste do loop.
  LLVMBuildCondBr(builder, cmpVal, endLoopBlock, bodyBlock);

  // Fim do loop.
  LLVMPositionBuilderAtEnd(builder, endLoopBlock);

  // Cria um salto para o bloco de saída.
  LLVMBuildBr(builder, exitBasicBlock);

  // Adiciona o bloco de saída da função.
  LLVMPositionBuilderAtEnd(builder, exitBasicBlock);

  // Cria o return.
  LLVMBuildRet(builder, LLVMBuildLoad(builder, returnVal, ""));

  // Imprime o código do módulo.
  LLVMDumpModule(module);

  // Escreve para um arquivo no formato bitcode.
  if (LLVMWriteBitcodeToFile(module, "meu_modulo.bc") != 0) {
    fprintf(stderr, "error writing bitcode to file, skipping\n");
  }
}
