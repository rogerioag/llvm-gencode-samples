; ModuleID = "vetor_parametro.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

define void @"exemplo"([100 x i32]* %"a", [100 x i32]* %"b", [100 x i32]* %"c", i32 %"i")
{
entry:
  %"i.1" = alloca i32
  store i32 %"i", i32* %"i.1"
  %"i.2" = load i32, i32* %"i.1"
  %"b[i]" = getelementptr [100 x i32], [100 x i32]* %"b", i32 0, i32 %"i.2"
  %"b[i].1" = load i32, i32* %"b[i]"
  %"a[i]" = getelementptr [100 x i32], [100 x i32]* %"a", i32 0, i32 %"i.2"
  %"a[i].1" = load i32, i32* %"a[i]"
  %"add_tmp" = add i32 %"b[i].1", %"a[i].1"
  %"c[i]" = getelementptr [100 x i32], [100 x i32]* %"c", i32 0, i32 %"i.2"
  store i32 %"add_tmp", i32* %"c[i]"
  br label %"exit"
exit:
  ret void
}

define i32 @"main"()
{
entry:
  %"return_value" = alloca i32
  %"a" = alloca [100 x i32], align 4
  %"b" = alloca [100 x i32], align 4
  %"c" = alloca [100 x i32], align 4
  %"i" = alloca i32, align 4
  store i32 0, i32* %"i"
  %"i.1" = load i32, i32* %"i"
  call void @"exemplo"([100 x i32]* %"a", [100 x i32]* %"b", [100 x i32]* %"c", i32 %"i.1")
  store i32 0, i32* %"return_value"
  br label %"exit"
exit:
  %"return_value.1" = load i32, i32* %"return_value"
  ret i32 %"return_value.1"
}
