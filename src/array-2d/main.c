#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

/*
int B[2048][2048];

int main(){

	float D[2048][2048];

	B[0][1] = B[1][1] + 10;

	D[0][1] = D[1][1] + 10;
		
	return 0;
}
*/

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo", context);
  LLVMBuilderRef builder = LLVMCreateBuilderInContext(context);
  
  // Array global de 2048 x 2048 elementos.
  LLVMTypeRef typeB_0 = LLVMArrayType(LLVMInt64Type(), 2048);
  LLVMTypeRef typeB = LLVMArrayType(typeB_0, 2048);
  // LLVMValueRef LLVMAddGlobal(LLVMModuleRef M, LLVMTypeRef Ty, const char *Name);
  LLVMValueRef arrayB = LLVMAddGlobal(module, typeB, "B");

  // void LLVMSetInitializer(LLVMValueRef GlobalVar, LLVMValueRef ConstantVal);
  LLVMSetInitializer(arrayB, LLVMConstInt(LLVMInt64Type(), 0, false));
  // common.
  LLVMSetLinkage(arrayB, LLVMCommonLinkage);
  // Alignment.
  LLVMSetAlignment(arrayB, 16);

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

  // Array local de 2048 x 2048 elementos. 
  LLVMTypeRef typeD_0 = LLVMArrayType(LLVMFloatType(), 2048);
  LLVMTypeRef typeD = LLVMArrayType(typeD_0, 2048);
  LLVMValueRef arrayD = LLVMBuildArrayAlloca (builder, typeD, LLVMConstInt(LLVMInt64Type(), 0, false), "D");
  LLVMSetAlignment(arrayD, 16);

  // B[0][1] = B[1][1] + 10;

  // Na documentação diz para usar um indice a mais, o primeiro em zero: http://releases.llvm.org/2.3/docs/GetElementPtr.html#extra_index
  // The first index, i64 0 is required to step over the global variable %MyStruct. Since the first argument to the GEP instruction must always be a value of pointer type, the first index steps through that pointer. A value of 0 means 0 elements offset from that pointer.
  LLVMValueRef indices[3];
  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 1, false);
  indices[2] = LLVMConstInt(LLVMInt32Type(), 1, false);

  LLVMValueRef ptr_B_1_1 = LLVMBuildInBoundsGEP(builder, arrayB, indices, 3, "ptr_B_1_1");

  // LLVMValueRef LLVMBuildLoad(LLVMBuilderRef, LLVMValueRef PointerVal, const char *Name);
  LLVMValueRef elem_B_1_1 = LLVMBuildLoad(builder, ptr_B_1_1, "elem_of_B");

  LLVMValueRef temp = LLVMBuildAdd(builder,  elem_B_1_1, LLVMConstInt(LLVMInt64Type(), 10, false), "temp");

  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[2] = LLVMConstInt(LLVMInt32Type(), 1, false);
  LLVMValueRef ptr_B_0_1 = LLVMBuildInBoundsGEP(builder, arrayB, indices, 3, "ptr_B_0_1");

  LLVMBuildStore(builder, temp, ptr_B_0_1);

  // D[0][1] = D[1][1] + 10;
  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 1, false);
  indices[2] = LLVMConstInt(LLVMInt32Type(), 1, false);

  LLVMValueRef ptr_D_1_1 = LLVMBuildInBoundsGEP(builder, arrayD, indices, 3, "ptr_D_1_1");

  // LLVMValueRef LLVMBuildLoad(LLVMBuilderRef, LLVMValueRef PointerVal, const char *Name);
  LLVMValueRef elem_D_1_1 = LLVMBuildLoad(builder, ptr_D_1_1, "elem_of_D");

  LLVMValueRef temp2 = LLVMBuildAdd(builder, elem_D_1_1, LLVMConstInt(LLVMInt64Type(), 10, false), "temp2");

  indices[0] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[1] = LLVMConstInt(LLVMInt32Type(), 0, false);
  indices[2] = LLVMConstInt(LLVMInt32Type(), 1, false);
  LLVMValueRef ptr_D_0_1 = LLVMBuildInBoundsGEP(builder, arrayD, indices, 3, "ptr_D_0_1");

  LLVMBuildStore(builder, temp2, ptr_D_0_1);
  // Cria um salto para o bloco de saída.
  LLVMBuildBr(builder, endBasicBlock);
	
  // Adiciona o bloco de saída.
  LLVMPositionBuilderAtEnd(builder, endBasicBlock);
  
  // Cria o return.
  LLVMBuildRet(builder, LLVMBuildLoad(builder, returnVal, ""));

  // Imprime o código do módulo.
  LLVMDumpModule(module);

  // Escreve para um arquivo no formato bitcode.
  // if (LLVMWriteBitcodeToFile(module, "meu_modulo.bc") != 0) {
  //  fprintf(stderr, "error writing bitcode to file, skipping\n");
  // }
}
