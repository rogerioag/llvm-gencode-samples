; ModuleID = "sum.bc"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"sum"(i32 %"x", i32 %"y")
{
entry:
  %".4" = add i32 %"x", %"y"
  br label %"exit"
exit:
  ret i32 %".4"
}
