#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

/*int A[1024];

int main(){

  int B[1024];

  A[50] = A[49] + 5;

  B[0] = B[1] + 10;
    
  return 0;
}
*/

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo.bc", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);
  
  // Array global de 1024 elementos.
  LLVMTypeRef typeA = LLVMArrayType(LLVMInt64Type(), 1024);
  // LLVMValueRef LLVMAddGlobal(LLVMModuleRef M, LLVMTypeRef Ty, const char *Name);
  LLVMValueRef arrayA = LLVMAddGlobal (module, typeA, "A");

  // void LLVMSetInitializer(LLVMValueRef GlobalVar, LLVMValueRef ConstantVal);
  // LLVMSetInitializer(arrayA, LLVMConstInt(LLVMIntType(64), 0, false));

  LLVMSetInitializer(arrayA, LLVMConstInt(LLVMIntType(64), 0, false));

  globalData.getInitializer()->getType()

  // common.
  LLVMSetLinkage(arrayA, LLVMCommonLinkage);
  // Alignment.
  LLVMSetAlignment(arrayA, 16);

  // Cria um valor zero para colocar no retorno.
  LLVMValueRef Zero64 = LLVMConstInt(LLVMInt64Type(), 0, false);

  // Declara o tipo do retorno da função main.
  LLVMTypeRef mainFnReturnType = LLVMInt64TypeInContext(context);
  // Cria a função main.
  LLVMValueRef mainFn = LLVMAddFunction(module, "main", LLVMFunctionType(mainFnReturnType, NULL, 0, 0));

  // Declara o bloco de entrada.
  LLVMBasicBlockRef entryBlock = LLVMAppendBasicBlockInContext(context, mainFn, "entry");
  // Declara o bloco de saída.
  LLVMBasicBlockRef endBasicBlock = LLVMAppendBasicBlock(mainFn, "end");

  // Adiciona o bloco de entrada.
  LLVMPositionBuilderAtEnd(builder, entryBlock);

  // Cria o valor de retorno e inicializa com zero.
  LLVMValueRef returnVal = LLVMBuildAlloca(builder, LLVMInt64Type(), "retorno");
	LLVMBuildStore(builder, Zero64, returnVal);

  // Array local de 1024 elementos. 
  LLVMTypeRef typeB = LLVMArrayType(LLVMInt64Type(), 1024);
  LLVMValueRef arrayB = LLVMBuildArrayAlloca(builder, typeB, LLVMConstInt(LLVMInt64Type(), 0, false), "B");
  LLVMSetAlignment(arrayB, 16);

  // A[50] = A[49] + 5;

  // Na documentação diz para usar dois indices, o primeiro em zero: http://releases.llvm.org/2.3/docs/GetElementPtr.html#extra_index
  // The first index, i64 0 is required to step over the global variable %MyStruct. Since the first argument to the GEP instruction must always be a value of pointer type, the first index steps through that pointer. A value of 0 means 0 elements offset from that pointer.
  LLVMValueRef indices[2];
  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 49, false);

  LLVMValueRef ptr_A_49 = LLVMBuildInBoundsGEP(builder, arrayA, indices, 2, "ptr_A_49");

  // LLVMValueRef LLVMBuildLoad(LLVMBuilderRef, LLVMValueRef PointerVal, const char *Name);
  LLVMValueRef elem_A_49 = LLVMBuildLoad(builder, ptr_A_49, "elem_of_A");

  LLVMValueRef temp = LLVMBuildAdd(builder,  elem_A_49, LLVMConstInt(LLVMInt64Type(), 5, false), "temp");

  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 50, false);
  LLVMValueRef ptr_A_50 = LLVMBuildInBoundsGEP(builder, arrayA, indices, 2, "ptr_A_50");

  LLVMBuildStore(builder, temp, ptr_A_50);

  // B[0] = B[1] + 10;
  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 1, false);

  LLVMValueRef ptr_B_1 = LLVMBuildInBoundsGEP(builder, arrayB, indices, 2, "ptr_B_1");

  // LLVMValueRef LLVMBuildLoad(LLVMBuilderRef, LLVMValueRef PointerVal, const char *Name);
  LLVMValueRef elem_B_1 = LLVMBuildLoad(builder, ptr_B_1, "elem_of_B");

  LLVMValueRef temp2 = LLVMBuildAdd(builder,  elem_B_1, LLVMConstInt(LLVMInt64Type(), 10, false), "temp2");

  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 0, false);
  LLVMValueRef ptr_B_0 = LLVMBuildInBoundsGEP(builder, arrayB, indices, 2, "ptr_B_0");

  LLVMBuildStore(builder, temp2, ptr_B_0);
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
