#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module =
      LLVMModuleCreateWithNameInContext("meu_modulo", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // Cria um valor zero para colocar no retorno.
  LLVMValueRef Zero = LLVMConstInt(LLVMIntType(32), 0, false);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt32TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(
      module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "entry");

  LLVMBasicBlockRef predicateBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "predicate");
  LLVMBasicBlockRef thenBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "then");
  LLVMBasicBlockRef elseBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "else");
  LLVMBasicBlockRef mergeBlock =
      LLVMAppendBasicBlockInContext(context, mainFn, "merge");

  // Declara o bloco de saída.
  LLVMBasicBlockRef endBasicBlock = LLVMAppendBasicBlock(mainFn, "end");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMIntType(32), "retorno");
  LLVMBuildStore(builder, Zero, returnVal);

  // Declara uma variável n.
  LLVMValueRef n = LLVMBuildAlloca(builder, LLVMIntType(32), "n");

  // Inicializa n.
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 10, false), n);
  LLVMBuildBr(builder, predicateBlock);

  // Bloco de predicado.
  LLVMPositionBuilderAtEnd(builder, predicateBlock);
  
  // Comparacao de n < 1024.
  LLVMValueRef n_cmp = LLVMBuildLoad(builder, n, "n");
  LLVMValueRef cmpVal = LLVMBuildICmp(builder, LLVMIntSLT, n_cmp, LLVMConstInt(LLVMIntType(32), 1024, false), "if_test");

  // Teste di if.
  LLVMBuildCondBr(builder, cmpVal, thenBlock, elseBlock);

  // Bloco then.
  LLVMPositionBuilderAtEnd(builder, thenBlock);
  LLVMBuildStore(builder, LLVMConstInt(LLVMInt64TypeInContext(context), 11, 0), returnVal);
  LLVMBuildBr(builder, mergeBlock);

  // Bloco else.
  LLVMPositionBuilderAtEnd(builder, elseBlock);
  LLVMBuildStore(builder, LLVMConstInt(LLVMInt64TypeInContext(context), 22, 0), returnVal);
  LLVMBuildBr(builder, mergeBlock);

  // Fim do if.
  LLVMPositionBuilderAtEnd(builder, mergeBlock);

  // Cria um salto para o bloco de saída.
  LLVMBuildBr(builder, endBasicBlock);

  // Adiciona o bloco de saída da função.
  LLVMPositionBuilderAtEnd(builder, endBasicBlock);

  // Cria o return.
  LLVMBuildRet(builder, LLVMBuildLoad(builder, returnVal, ""));

  // Imprime o código do módulo.
  LLVMDumpModule(module);

  // Escreve para um arquivo no formato bitcode.
  if (LLVMWriteBitcodeToFile(module, "meu_modulo.bc") != 0) {
    fprintf(stderr, "error writing bitcode to file, skipping\n");
  }
}
