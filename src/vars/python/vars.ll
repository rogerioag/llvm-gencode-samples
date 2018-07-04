; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"g" = global i32 0, align 4
@"h" = global float              0x0, align 4
define i32 @"main"() 
{
bloco_entrada:
  %"a" = alloca i32, align 4
  store i32 1, i32* %"a"
  %"a.1" = alloca float, align 4
  store float 0x3ff0000000000000, float* %"a.1"
  store i32 10, i32* @"g"
  store float 0x4024000000000000, float* @"h"
  %".6" = load i32, i32* %"a", align 4
  %"temp" = add i32 %".6", 10
  store i32 %"temp", i32* %"a"
  %".8" = load float, float* %"a.1", align 4
  %".9" = load float, float* @"h", align 4
  %"temp2" = fadd float %".8", %".9"
  store float %"temp2", float* %"a.1"
  br label %"bloco_saida"
bloco_saida:
  ret i32 0
}
