; ModuleID = 'vars.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@g = common global i32 0, align 4
@h = common global float 0.000000e+00, align 4

; Function Attrs: nounwind uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %a = alloca i32, align 4
  %b = alloca float, align 4
  store i32 0, i32* %1
  store i32 1, i32* %a, align 4
  store float 1.000000e+00, float* %b, align 4
  store i32 10, i32* @g, align 4
  store float 1.000000e+01, float* @h, align 4
  %2 = load i32* %a, align 4
  %3 = add nsw i32 %2, 10
  store i32 %3, i32* %a, align 4
  %4 = load float* %b, align 4
  %5 = load float* @h, align 4
  %6 = fadd float %4, %5
  store float %6, float* %b, align 4
  ret i32 0
}

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Debian clang version 3.5.0-10 (tags/RELEASE_350/final) (based on LLVM 3.5.0)"}
