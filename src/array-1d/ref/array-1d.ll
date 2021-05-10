; ModuleID = 'array-1d.c'
source_filename = "array-1d.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@A = dso_local global [1024 x i64] zeroinitializer, align 16

; Function Attrs: noinline nounwind optnone sspstrong uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [1024 x i64], align 16
  store i32 0, i32* %1, align 4
  %3 = load i64, i64* getelementptr inbounds ([1024 x i64], [1024 x i64]* @A, i64 0, i64 49), align 8
  %4 = add nsw i64 %3, 5
  store i64 %4, i64* getelementptr inbounds ([1024 x i64], [1024 x i64]* @A, i64 0, i64 50), align 16
  %5 = getelementptr inbounds [1024 x i64], [1024 x i64]* %2, i64 0, i64 1
  %6 = load i64, i64* %5, align 8
  %7 = add nsw i64 %6, 10
  %8 = getelementptr inbounds [1024 x i64], [1024 x i64]* %2, i64 0, i64 0
  store i64 %7, i64* %8, align 16
  ret i32 0
}

attributes #0 = { noinline nounwind optnone sspstrong uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0, !1, !2}
!llvm.ident = !{!3}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{!"clang version 11.1.0"}
