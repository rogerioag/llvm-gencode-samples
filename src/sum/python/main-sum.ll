; ModuleID = 'llvm-link'
source_filename = "llvm-link"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

define i32 @main() {
entry:
  %a = alloca i32, align 4
  store i32 12, ptr %a, align 4
  %b = alloca i32, align 4
  store i32 30, ptr %b, align 4
  %res = alloca i32, align 4
  %.4 = load i32, ptr %a, align 4
  %.5 = load i32, ptr %b, align 4
  %.6 = call i32 @sum(i32 %.4, i32 %.5)
  store i32 %.6, ptr %res, align 4
  br label %exit

exit:                                             ; preds = %entry
  %ret = load i32, ptr %res, align 4
  ret i32 %ret
}

define i32 @sum(i32 %x, i32 %y) {
entry:
  %.4 = add i32 %x, %y
  br label %exit

exit:                                             ; preds = %entry
  ret i32 %.4
}
