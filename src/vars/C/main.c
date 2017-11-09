#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

/*
int g;
float h;

int main(){
  int a = 1;
  float b = 1.0;
  
  g = 10;
  h = 10.0;
  a = a + 10;
  b = b + h;
  
  return 0;
}
*/

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo.bc", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // int g;
  // Declaração da variável global g.
  // LLVMValueRef LLVMAddGlobal(LLVMModuleRef M, LLVMTypeRef Ty, const char *Name);
  LLVMValueRef g = LLVMAddGlobal (module, LLVMIntType(32), "g");

  // void LLVMSetInitializer(LLVMValueRef GlobalVar, LLVMValueRef ConstantVal);
  LLVMSetInitializer(g, LLVMConstInt(LLVMIntType(32), 0, false));

  // common.
  LLVMSetLinkage(g, LLVMCommonLinkage);
  // Alignment.
  LLVMSetAlignment(g, 4);

  // float h;
  // Declaração da variável global h.
  // LLVMValueRef LLVMAddGlobal(LLVMModuleRef M, LLVMTypeRef Ty, const char *Name);
  LLVMValueRef h = LLVMAddGlobal (module, LLVMFloatType(), "h");

  // void LLVMSetInitializer(LLVMValueRef GlobalVar, LLVMValueRef ConstantVal);
  LLVMSetInitializer(h, LLVMConstInt(LLVMFloatType(), 0.0, false));

  // common.
  LLVMSetLinkage(h, LLVMCommonLinkage);
  // Alignment.
  LLVMSetAlignment(h, 4);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt32TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Cria um valor zero para colocar no retorno.
  LLVMValueRef Zero32 = LLVMConstInt(LLVMIntType(32), 0, false);

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock = LLVMAppendBasicBlockInContext(context, mainFn, "entry");
  // Declara o bloco de saída.
  LLVMBasicBlockRef endBasicBlock = LLVMAppendBasicBlock(mainFn, "end");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMIntType(32), "retorno");
	

  // int a = 1;
  // float b = 1.0;

  // Declaracao da variavel a. 
  LLVMValueRef a = LLVMBuildAlloca(builder, LLVMIntType(32), "a");
  LLVMSetAlignment(a, 4);
  
  LLVMValueRef b = LLVMBuildAlloca(builder, LLVMFloatType(), "b");
  LLVMSetAlignment(b, 4);

  // Inicializa as variáveis.
  LLVMBuildStore(builder, Zero32, returnVal);
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 1, false), a);
  LLVMBuildStore(builder, LLVMConstReal(LLVMFloatType(), 1.0), b);


  // g = 10;
  // h = 10.0;
  LLVMBuildStore(builder, LLVMConstInt(LLVMIntType(32), 10, false), g);

  LLVMBuildStore(builder, LLVMConstReal(LLVMFloatType(), 10.0), h);

  // a = a + 10;

  LLVMValueRef temp = LLVMBuildAdd(builder, LLVMBuildLoad(builder, a, ""), LLVMConstInt(LLVMIntType(32), 10, false), "temp");
  LLVMBuildStore(builder, temp, a);


  //b = b + h;

  LLVMValueRef temp2 = LLVMBuildFAdd(builder, LLVMBuildLoad(builder, b, ""), LLVMBuildLoad(builder, h, ""), "temp");
  LLVMBuildStore(builder, temp2, b);
  
    // Cria um salto para o bloco de saída.
	LLVMBuildBr(builder, endBasicBlock);
	
	// Adiciona o bloco de saída.
	LLVMPositionBuilderAtEnd(builder, endBasicBlock);
  
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
