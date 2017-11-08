; ModuleID = 'if.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %c = alloca i32, align 4
  store i32 0, i32* %1
  store i32 1, i32* %a, align 4
  store i32 2, i32* %b, align 4
  store i32 0, i32* %c, align 4
  %2 = load i32* %a, align 4
  %3 = load i32* %b, align 4
  %4 = icmp slt i32 %2, %3
  br i1 %4, label %5, label %6

; <label>:5                                       ; preds = %0
  store i32 5, i32* %c, align 4
  br label %7

; <label>:6                                       ; preds = %0
  store i32 6, i32* %c, align 4
  br label %7

; <label>:7                                       ; preds = %6, %5
  %8 = load i32* %a, align 4
  %9 = icmp slt i32 %8, 1024
  br i1 %9, label %10, label %11

; <label>:10                                      ; preds = %7
  store i32 10, i32* %c, align 4
  br label %12

; <label>:11                                      ; preds = %7
  store i32 20, i32* %c, align 4
  br label %12

; <label>:12                                      ; preds = %11, %10
  ret i32 0
}

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Debian clang version 3.5.0-10 (tags/RELEASE_350/final) (based on LLVM 3.5.0)"}
