#include <stdio.h>
#include <llvm-c/Core.h>

int main( int argc, char* argv[] )
{
	LLVMContextRef context = LLVMGetGlobalContext();
	LLVMModuleRef module = LLVMModuleCreateWithNameInContext( "mytop", context );
	LLVMBuilderRef builder = LLVMCreateBuilderInContext( context );

	LLVMTypeRef mainFnParamTypes[] = { LLVMInt64TypeInContext( context ) };
	LLVMTypeRef mainFnReturnType = LLVMInt64TypeInContext( context );
	LLVMValueRef mainFn = LLVMAddFunction( module, "main", LLVMFunctionType( mainFnReturnType, mainFnParamTypes, 1, 0 ) );

	LLVMBasicBlockRef entryblock = LLVMAppendBasicBlockInContext( context, mainFn, "entry" );
	LLVMBasicBlockRef predicateblock = LLVMAppendBasicBlockInContext( context, mainFn, "predicate" );
	LLVMBasicBlockRef thenblock = LLVMAppendBasicBlockInContext( context, mainFn, "then" );
	LLVMBasicBlockRef elseblock = LLVMAppendBasicBlockInContext( context, mainFn, "else" );
	LLVMBasicBlockRef mergeblock = LLVMAppendBasicBlockInContext( context, mainFn, "merge" );

	LLVMPositionBuilderAtEnd( builder, entryblock );
	LLVMValueRef xpVar = LLVMBuildAlloca( builder, LLVMInt64TypeInContext( context ), "xp" );
	LLVMBuildBr( builder, predicateblock );

	LLVMPositionBuilderAtEnd( builder, predicateblock );
	LLVMValueRef cmpVal = LLVMBuildICmp( builder, LLVMIntEQ, LLVMGetParam( mainFn, 0 ), LLVMConstInt( LLVMInt64TypeInContext( context ), 10, 0 ), "eq10" );
	LLVMBuildCondBr( builder, cmpVal, thenblock, elseblock );

	LLVMPositionBuilderAtEnd( builder, thenblock );
	LLVMBuildStore( builder, LLVMConstInt( LLVMInt64TypeInContext( context ), 11, 0  ), xpVar );
	LLVMBuildBr( builder, mergeblock );

	LLVMPositionBuilderAtEnd( builder, elseblock );
	LLVMBuildStore( builder, LLVMConstInt( LLVMInt64TypeInContext( context ), 22, 0  ), xpVar );
	LLVMBuildBr( builder, mergeblock );

	LLVMPositionBuilderAtEnd( builder, mergeblock );
	LLVMValueRef xVar = LLVMBuildLoad( builder, xpVar, "x");
	LLVMBuildRet( builder, xVar );

	LLVMDumpModule(module);
}

