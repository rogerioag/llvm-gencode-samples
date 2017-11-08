; ModuleID = 'main-c.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %c = alloca float, align 4
  %d = alloca float, align 4
  store i32 0, i32* %1
  %2 = call i32 @leiaInteiro()
  store i32 %2, i32* %a, align 4
  %3 = call i32 @leiaInteiro()
  store i32 %3, i32* %b, align 4
  %4 = load i32* %a, align 4
  %5 = load i32* %b, align 4
  %6 = add nsw i32 %4, %5
  call void @escrevaInteiro(i32 %6)
  %7 = call float @leiaFlutuante()
  store float %7, float* %c, align 4
  %8 = call float @leiaFlutuante()
  store float %8, float* %d, align 4
  %9 = load float* %c, align 4
  %10 = load float* %d, align 4
  %11 = fadd float %9, %10
  call void @escrevaFlutuante(float %11)
  ret i32 0
}

declare i32 @leiaInteiro() #1

declare void @escrevaInteiro(i32) #1

declare float @leiaFlutuante() #1

declare void @escrevaFlutuante(float) #1

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Debian clang version 3.5.0-10 (tags/RELEASE_350/final) (based on LLVM 3.5.0)"}
