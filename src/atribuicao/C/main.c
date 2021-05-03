#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

/*
int a,b,c;

int main(){
  a = 1;
  b = 2;
  c = a + b;
  
  return 0;
}
*/

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo.bc", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // int a;
  // Declaração da variável global a.
  LLVMValueRef a = LLVMAddGlobal (module, LLVMIntType(32), "a");
  
  // void LLVMSetInitializer(LLVMValueRef GlobalVar, LLVMValueRef ConstantVal);
  LLVMSetInitializer(a, LLVMConstInt(LLVMIntType(32), 0, false));

  // common.
  LLVMSetLinkage(a, LLVMCommonLinkage);
  // Alignment.
  LLVMSetAlignment(a, 4);

  // Declaração da variável global b.
  LLVMValueRef b = LLVMAddGlobal (module, LLVMIntType(32), "b");
  
  // void LLVMSetInitializer(LLVMValueRef GlobalVar, LLVMValueRef ConstantVal);
  LLVMSetInitializer(b, LLVMConstInt(LLVMIntType(32), 0, false));

  // common.
  LLVMSetLinkage(b, LLVMCommonLinkage);
  // Alignment.
  LLVMSetAlignment(b, 4);

  // Declaração da variável global c.
  LLVMValueRef c = LLVMAddGlobal (module, LLVMIntType(32), "c");
  
  // void LLVMSetInitializer(LLVMValueRef GlobalVar, LLVMValueRef ConstantVal);
  LLVMSetInitializer(c, LLVMConstInt(LLVMIntType(32), 0, false));

  // common.
  LLVMSetLinkage(c, LLVMCommonLinkage);
  // Alignment.
  LLVMSetAlignment(c, 4);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt32TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Cria um valor zero para colocar no retorno.
  LLVMValueRef Zero32 = LLVMConstInt(LLVMIntType(32), 0, false);

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock = LLVMAppendBasicBlockInContext(context, mainFn, "entry");
  // Declara o bloco de saída.
  LLVMBasicBlockRef exitBasicBlock = LLVMAppendBasicBlock(mainFn, "exit");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMIntType(32), "retorno");
	
  // a = 1;
  // b = 2;
  // Inicializa as variáveis.
  LLVMBuildStore(builder, Zero32, returnVal);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 1, false), a);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 2, false), b);
   
  // c = a + b;

  LLVMValueRef temp_a = LLVMBuildLoad(builder, a, "");
  LLVMValueRef temp_b = LLVMBuildLoad(builder, b, "");

  LLVMValueRef add_temp = LLVMBuildAdd(builder, temp_a, temp_b, "temp");
  LLVMBuildStore(builder, add_temp, c);

  // Cria um salto para o bloco de saída.
	LLVMBuildBr(builder, exitBasicBlock);
	
	// Adiciona o bloco de saída.
	LLVMPositionBuilderAtEnd(builder, exitBasicBlock);
  
  // return 0;
  // Cria o return.
	LLVMBuildRet(builder, LLVMBuildLoad(builder, returnVal, ""));

	// Imprime o código do módulo.
  LLVMDumpModule(module);

  // Escreve para um arquivo no formato bitcode.
  if (LLVMWriteBitcodeToFile(module, "meu_modulo.bc") != 0) {
    fprintf(stderr, "error writing bitcode to file, skipping\n");
  }
}
