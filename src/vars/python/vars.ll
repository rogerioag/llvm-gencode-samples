; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"a" = global i32 0, align 4
@"b" = global float              0x0, align 4
define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32, align 4
  store i32 0, i32* %"retorno"
  %"c" = alloca i32, align 4
  store i32 1, i32* %"c"
  %"d" = alloca float, align 4
  store float 0x3ff0000000000000, float* %"d"
  store i32 10, i32* @"a"
  store float 0x4024000000000000, float* @"b"
  br label %"exit"
exit:
  ret i32 0
}
