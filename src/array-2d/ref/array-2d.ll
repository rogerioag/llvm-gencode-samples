; ModuleID = 'array-2d.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@B = common global [2048 x [2048 x i32]] zeroinitializer, align 16

; Function Attrs: nounwind uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %D = alloca [2048 x [2048 x float]], align 16
  store i32 0, i32* %1
  %2 = load i32* getelementptr inbounds ([2048 x [2048 x i32]]* @B, i32 0, i64 1, i64 1), align 4
  %3 = add nsw i32 %2, 10
  store i32 %3, i32* getelementptr inbounds ([2048 x [2048 x i32]]* @B, i32 0, i64 0, i64 1), align 4
  %4 = getelementptr inbounds [2048 x [2048 x float]]* %D, i32 0, i64 1
  %5 = getelementptr inbounds [2048 x float]* %4, i32 0, i64 1
  %6 = load float* %5, align 4
  %7 = fadd float %6, 1.000000e+01
  %8 = getelementptr inbounds [2048 x [2048 x float]]* %D, i32 0, i64 0
  %9 = getelementptr inbounds [2048 x float]* %8, i32 0, i64 1
  store float %7, float* %9, align 4
  ret i32 0
}

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Debian clang version 3.5.0-10 (tags/RELEASE_350/final) (based on LLVM 3.5.0)"}
