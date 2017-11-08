#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo.bc", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  // extern int leiaInteiro(void)
  // LLVMTypeRef leiaInteiroParams[] = {LLVMVoidType()};
  LLVMTypeRef leiaInteiroFuncType = LLVMFunctionType(LLVMInt32Type(), NULL, 0, 0);
  LLVMValueRef leiaInteiro = LLVMAddFunction(module, "leiaInteiro", leiaInteiroFuncType);

  // extern float leiaFlutuante(void)
  // LLVMTypeRef leiaFlutuanteParams[] = {LLVMVoidType()};
  LLVMTypeRef leiaFlutuanteFuncType = LLVMFunctionType(LLVMFloatType(), NULL, 0, 0);
  LLVMValueRef leiaFlutuante = LLVMAddFunction(module, "leiaFlutuante", leiaFlutuanteFuncType);

  // extern void escrevaInteiro(int ni)
  LLVMTypeRef escrevaInteiroParams[] = {LLVMInt32Type()};
  LLVMTypeRef escrevaInteiroFuncType = LLVMFunctionType(LLVMVoidType(), escrevaInteiroParams, 1, 0);
  LLVMValueRef escrevaInteiro = LLVMAddFunction(module, "escrevaInteiro", escrevaInteiroFuncType);

  // extern void escrevaFlutuante(float nf)
  LLVMTypeRef escrevaFlutuanteParams[] = {LLVMFloatType()};
  LLVMTypeRef escrevaFlutuanteFuncType = LLVMFunctionType(LLVMVoidType(), escrevaFlutuanteParams, 1, 0);
  LLVMValueRef escrevaFlutuante = LLVMAddFunction(module, "escrevaFlutuante", escrevaFlutuanteFuncType);
 
  // Cria um valor zero para colocar no retorno para o main.
  LLVMValueRef Zero64 = LLVMConstInt(LLVMInt64Type(), 0, false);

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
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMInt64Type(), "retorno");
	LLVMBuildStore(builder, Zero64, returnVal);

  // Declara a variável a (int).
  LLVMValueRef a = LLVMBuildAlloca(builder, LLVMInt32Type(), "a");

  // Declara a variável f (float)
  LLVMValueRef f = LLVMBuildAlloca(builder, LLVMFloatType(), "f");
    
  // a = leiaInteiro()
  // LLVMValueRef leia_a = LLVMBuildCall(builder, leiaInteiro, NULL, 0, "leia_a");

  LLVMValueRef temp = LLVMBuildCall(
    builder,
    leiaInteiro,
    NULL,
    0,
    "leia_a"
  );

  LLVMBuildStore(builder, temp, a);

  LLVMValueRef temp2 = LLVMBuildCall(
    builder,
    leiaFlutuante,
    NULL,
    0,
    "leia_f"
  );

  LLVMBuildStore(builder, temp2, f);

  LLVMValueRef print_a = LLVMBuildLoad(builder, a, "print_a");

  LLVMValueRef escrevaInteiroArgs[] = { print_a };

  LLVMBuildCall(
        builder,
        escrevaInteiro,
        escrevaInteiroArgs,
        1,
        ""
  );

  LLVMValueRef print_f = LLVMBuildLoad(builder, f, "print_f");

  LLVMValueRef escrevaFlutuanteArgs[] = { print_f };

  LLVMBuildCall(
        builder,
        escrevaFlutuante,
        escrevaFlutuanteArgs,
        1,
        ""
  );
  
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
