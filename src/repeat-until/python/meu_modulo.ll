; ModuleID = "meu_modulo.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"i" = alloca i32, align 4
  store i32 0, i32* %"i"
  %"a" = alloca i32, align 4
  store i32 1, i32* %"a"
  br label %"loop"
exit:
  %"variavel_retorno" = alloca i32, align 4
  %".13" = load i32, i32* %"i"
  store i32 %".13", i32* %"variavel_retorno"
  %"retorno" = load i32, i32* %"variavel_retorno", align 4
  ret i32 %"retorno"
loop:
  store i32 5, i32* %"a"
  %".6" = load i32, i32* %"i"
  %".7" = add i32 %".6", 1
  store i32 %".7", i32* %"i"
  br label %"loop_val"
loop_val:
  %".10" = load i32, i32* %"i"
  %"expressao_soma" = icmp eq i32 %".10", 10
  br i1 %"expressao_soma", label %"loop_end", label %"loop"
loop_end:
  br label %"exit"
}
