; ModuleID = 'array-1d.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@A = common global [1024 x i64] zeroinitializer, align 16

; Function Attrs: nounwind uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %B = alloca [1024 x i64], align 16
  store i32 0, i32* %1
  %2 = load i64* getelementptr inbounds ([1024 x i64]* @A, i32 0, i64 49), align 8
  %3 = add nsw i64 %2, 5
  store i64 %3, i64* getelementptr inbounds ([1024 x i64]* @A, i32 0, i64 50), align 8
  %4 = getelementptr inbounds [1024 x i64]* %B, i32 0, i64 1
  %5 = load i64* %4, align 8
  %6 = add nsw i64 %5, 10
  %7 = getelementptr inbounds [1024 x i64]* %B, i32 0, i64 0
  store i64 %6, i64* %7, align 8
  ret i32 0
}

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Debian clang version 3.5.0-10 (tags/RELEASE_350/final) (based on LLVM 3.5.0)"}
