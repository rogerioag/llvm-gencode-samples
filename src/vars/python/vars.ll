; ModuleID = "meu_modulo.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

@"a" = common global i32 0, align 4
@"b" = common global float              0x0, align 4
define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
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

