; ModuleID = 'vars.c'
source_filename = "vars.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@g = common dso_local global i32 0, align 4
@h = common dso_local global float 0.000000e+00, align 4

; Function Attrs: noinline nounwind optnone sspstrong uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %a = alloca i32, align 4
  %b = alloca float, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* %a, align 4
  store float 1.000000e+00, float* %b, align 4
  store i32 10, i32* @g, align 4
  store float 1.000000e+01, float* @h, align 4
  %4 = load i32, i32* %a, align 4
  %5 = add nsw i32 %4, 10
  store i32 %5, i32* %a, align 4
  %6 = load float, float* %b, align 4
  %7 = load float, float* @h, align 4
  %8 = fadd float %6, %7
  store float %8, float* %b, align 4
  ret i32 0
}

attributes #0 = { noinline nounwind optnone sspstrong uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0, !1, !2}
!llvm.ident = !{!3}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{!"clang version 10.0.1 "}
