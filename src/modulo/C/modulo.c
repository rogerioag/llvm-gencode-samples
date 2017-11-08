/*
clang-3.5 -g `llvm-config-3.5 --cflags` soma_llvm.cpp -c -o soma_llvm.o
clang++-3.5 soma_llvm.o `llvm-config-3.5 --cxxflags --ldflags --libs core
executionengine jit interpreter analysis native bitwriter --system-libs` -o
soma.exe

*/

#include <stdio.h>
#include <llvm-c/Core.h>
#include <llvm-c/BitWriter.h>

int main(int argc, char *argv[]) {
  LLVMContextRef context = LLVMGetGlobalContext();
  LLVMModuleRef module = LLVMModuleCreateWithNameInContext("meu_modulo", context);
  
  // Imprime o código do módulo.
  LLVMDumpModule(module);

  // Escreve para um arquivo no formato bitcode.
  if (LLVMWriteBitcodeToFile(module, "meu_modulo.bc") != 0) {
    fprintf(stderr, "error writing bitcode to file, skipping\n");
  }
}
