#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo.bc", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // Cria um valor zero para colocar no retorno.
  LLVMValueRef Zero64 = LLVMConstInt(LLVMInt64Type(), 0, false);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt64TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock = LLVMAppendBasicBlockInContext(context, mainFn, "entry");
  // Declara o bloco de saída.
  LLVMBasicBlockRef endBasicBlock = LLVMAppendBasicBlock(mainFn, "exit");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMInt64Type(), "retorno");
	LLVMBuildStore(builder, Zero64, returnVal);

	// Declara as variáveis a,b e c.
	LLVMValueRef a = LLVMBuildAlloca(builder, LLVMInt64Type(), "a");
	LLVMValueRef b = LLVMBuildAlloca(builder, LLVMFloatType(), "b");
	LLVMValueRef c = LLVMBuildAlloca(builder, LLVMFloatType(), "c");

	// Inicializa as variáveis.
	LLVMBuildStore(builder, LLVMConstInt(LLVMInt64Type(), 1, false), a);
	LLVMBuildStore(builder, LLVMConstReal(LLVMFloatType(), 1.0), b);
	LLVMBuildStore(builder, LLVMConstReal(LLVMFloatType(), 2.0), c);

	LLVMValueRef temp = LLVMBuildAdd(builder, LLVMBuildLoad(builder, a, ""), LLVMBuildLoad(builder, a, ""), "temp");
	LLVMBuildStore(builder, temp, a);

	// Cria a instrução add. Outras funções podem ser criadas com: LLVMBuildSub, LLVMBuildAnd, LLVMBuildOr...
	LLVMValueRef temp2 = LLVMBuildFAdd(builder, LLVMBuildLoad(builder, b, ""), LLVMBuildLoad(builder, c, ""), "temp2");
	LLVMBuildStore(builder, temp2, b);

	// Cria um salto para o bloco de saída.
	LLVMBuildBr(builder, endBasicBlock);
	
	// Adiciona o bloco de saída.
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
