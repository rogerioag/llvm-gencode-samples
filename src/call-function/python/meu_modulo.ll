; ModuleID = "meu_modulo.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"soma"(i32 %"a", i32 %"b")
{
entry:
  %".4" = add i32 %"a", %"b"
  br label %"exit"
exit:
  ret i32 %".4"
}

define void @"teste"()
{
entry:
  br label %"exit"
exit:
  ret void
}

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  %"b" = alloca i32
  store i32 2, i32* %"b"
  %"res" = alloca i32
  %".4" = load i32, i32* %"a"
  %".5" = load i32, i32* %"b"
  %".6" = call i32 @"soma"(i32 %".4", i32 %".5")
  store i32 %".6", i32* %"res"
  call void @"teste"()
  br label %"exit"
exit:
  %"ret_temp" = load i32, i32* %"res", align 4
  ret i32 %"ret_temp"
}
