; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
bloco_entrada:
  %"a" = alloca i32, align 4
  store i32 1, i32* %"a"
  %"b" = alloca float, align 4
  store float 0x3ff0000000000000, float* %"b"
  %"c" = alloca float, align 4
  store float 0x4000000000000000, float* %"c"
  %".5" = load i32, i32* %"a"
  %".6" = add i32 %".5", %".5"
  store i32 %".6", i32* %"a", align 4
  %".8" = load float, float* %"b"
  %".9" = load float, float* %"c"
  %".10" = add float %".8", %".9"
  store float %".10", float* %"b", align 4
bloco_saida:
  ret i32 0
}
