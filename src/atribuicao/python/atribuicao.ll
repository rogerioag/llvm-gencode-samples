; ModuleID = "meu_modulo.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

@"a" = common global i32 0, align 4
@"b" = common global i32 0, align 4
@"c" = common global i32 0, align 4
define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  store i32 1, i32* @"a"
  store i32 2, i32* @"b"
  %".5" = load i32, i32* @"a"
  %".6" = load i32, i32* @"b"
  %"temp" = add i32 %".5", %".6"
  store i32 %"temp", i32* @"c"
  br label %"exit"
exit:
  ret i32 0
}

