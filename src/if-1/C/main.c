#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

/*
int main(){

  int a = 1;
  int b = 2;
  int c = 0;

  if(a < b) {
    c = 5; 
  }
  else {
    c = 6;
  }

  if(a < 1024){
    c = 10;
  }
  else {
    c = 20;
  }
  
  return 0;
}
*/

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // Cria um valor zero para colocar no retorno.
  LLVMValueRef Zero = LLVMConstInt(LLVMIntType(32), 0, false);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt32TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock = LLVMAppendBasicBlockInContext(context, mainFn, "entry");
  // Declara o bloco de saída.
  LLVMBasicBlockRef exitBasicBlock = LLVMAppendBasicBlock(mainFn, "exit");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMIntType(32), "retorno");
	LLVMBuildStore(builder, Zero, returnVal);

  // Declara as variáveis a, b, e c.
  LLVMValueRef a = LLVMBuildAlloca(builder, LLVMIntType(32), "a");
  LLVMValueRef b = LLVMBuildAlloca(builder, LLVMIntType(32), "b");
  LLVMValueRef c = LLVMBuildAlloca(builder, LLVMIntType(32), "c");
  
  // Inicializa as variáveis.
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 1, false), a);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 2, false), b);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 0, false), c);

  // Declara os blocos básicos para o primeiro if.
  // if(a < b) {
  //  c = 5; 
  // }
  // else {
  //   c = 6;
  // }
  LLVMBasicBlockRef iftrue_1 = LLVMAppendBasicBlock(mainFn, "iftrue_1");
  LLVMBasicBlockRef iffalse_1 = LLVMAppendBasicBlock(mainFn, "iffalse_1");
  LLVMBasicBlockRef ifend_1 = LLVMAppendBasicBlock(mainFn, "ifend_1");

  // Carrega as variáveis a e b para comparação.
  LLVMValueRef a_cmp = LLVMBuildLoad(builder, a, "a_cmp");
  LLVMValueRef b_cmp = LLVMBuildLoad(builder, b, "b_cmp");

  LLVMValueRef If_1 = LLVMBuildICmp(builder, LLVMIntSLT, a_cmp, b_cmp, "if_test_1");
  LLVMBuildCondBr(builder, If_1, iftrue_1, iffalse_1);

  LLVMPositionBuilderAtEnd(builder, iftrue_1);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 5, 0), c);
  LLVMBuildBr(builder, ifend_1);

  LLVMPositionBuilderAtEnd(builder, iffalse_1);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 6, 0), c);
  LLVMBuildBr(builder, ifend_1);

  LLVMPositionBuilderAtEnd(builder, ifend_1);

  // Segundo If.
  // if(a < 1024){
  //   c = 10;
  // }
  // else {
  //   c = 20;
  // }
  // Declara os blocos básicos para o if.
	LLVMBasicBlockRef iftrue_2 = LLVMAppendBasicBlock(mainFn, "iftrue_2");
  LLVMBasicBlockRef iffalse_2 = LLVMAppendBasicBlock(mainFn, "iffalse_2");
  LLVMBasicBlockRef ifend_2 = LLVMAppendBasicBlock(mainFn, "ifend_2");
  
  // Carrega o valor que será comparado: a < 1024.
  LLVMValueRef a_cmp_2 = LLVMBuildLoad(builder, a, "a");

  LLVMValueRef If_2 = LLVMBuildICmp(builder, LLVMIntSLT, a_cmp_2, LLVMConstInt(LLVMIntType(32), 1024, false), "if_test_2");
  LLVMBuildCondBr(builder, If_2, iftrue_2, iffalse_2);

  LLVMPositionBuilderAtEnd(builder, iftrue_2);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 10, 0), c);
  LLVMBuildBr(builder, ifend_2);

  LLVMPositionBuilderAtEnd(builder, iffalse_2);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 20, 0), c);
  LLVMBuildBr(builder, ifend_2);

  LLVMPositionBuilderAtEnd(builder, ifend_2);

  // Cria um salto para o bloco de saída.
	LLVMBuildBr(builder, exitBasicBlock);
	
	// Adiciona o bloco de saída.
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
