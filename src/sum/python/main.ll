; ModuleID = "main.bc"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"sum"(i32 %"x", i32 %"y")

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 12, i32* %"a"
  %"b" = alloca i32
  store i32 30, i32* %"b"
  %"res" = alloca i32
  %".4" = load i32, i32* %"a"
  %".5" = load i32, i32* %"b"
  %".6" = call i32 @"sum"(i32 %".4", i32 %".5")
  store i32 %".6", i32* %"res"
  br label %"exit"
exit:
  %"ret" = load i32, i32* %"res", align 4
  ret i32 %"ret"
}
