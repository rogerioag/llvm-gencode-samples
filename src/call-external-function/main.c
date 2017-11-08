#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo.bc", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);

  /// extern int printf(char*, ...)
  LLVMTypeRef printfArgsTyList[] = { LLVMPointerType(LLVMInt8Type(), 0) };
  LLVMTypeRef printfTy = LLVMFunctionType(
        LLVMInt32Type(),
        printfArgsTyList,
        0,
        true // IsVarArg
  );

  LLVMValueRef printfFunction = LLVMAddFunction(module, "printf", printfTy); 

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

  // Declara as variáveis a e b.
  LLVMValueRef a = LLVMBuildAlloca(builder, LLVMInt64Type(), "a");
    
  // Inicializa as variáveis.
  LLVMBuildStore(builder, LLVMConstInt(LLVMInt64Type(), 10, false), a);
  
  LLVMValueRef format = LLVMBuildGlobalStringPtr(
        builder,
        "%s\n",
        "format"
  );

  LLVMValueRef helloworld = LLVMBuildGlobalStringPtr(
        builder,
        "Hello World!!",
        "hello_world"
  );

  // printf("%s\n", helloworld);
  LLVMValueRef printfArgs[] = { format, helloworld };

  LLVMBuildCall(
        builder,
        printfFunction,
        printfArgs,
        2,
        "printf"
  );

  LLVMValueRef formatint = LLVMBuildGlobalStringPtr(
        builder,
        "%d\n",
        "formatint"
  );

  // printf("%d\n", 23);
  printfArgs[0] = formatint;
  printfArgs[1] = LLVMConstInt(LLVMInt32Type(), 23, false);

  LLVMBuildCall(
        builder,
        printfFunction,
        printfArgs,
        2,
        "printfint"
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
