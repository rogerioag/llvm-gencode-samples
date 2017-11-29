; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"g" = common global i32 0, align 4
@"h" = common global float              0x0, align 4
define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"a" = alloca i32, align 4
  store i32 1, i32* %"a"
  %"b" = alloca float, align 4
  store float 0x3ff0000000000000, float* %"b"
  store i32 10, i32* @"g"
  store float 0x4024000000000000, float* @"h"
  %".7" = load i32, i32* %"a"
  %"temp" = add i32 %".7", 10
  store i32 %"temp", i32* %"a"
  %".9" = load float, float* %"b"
  %".10" = load float, float* @"h"
  %"temp2" = fadd float %".9", %".10"
  store float %"temp2", float* %"b"
  br label %"exit"
exit:
  %".13" = load i32, i32* %"retorno", align 4
  ret i32 %".13"
}
