; ModuleID = 'instrucoeslogicas.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %x = alloca i32, align 4
  %y = alloca i32, align 4
  %maior = alloca i32, align 4
  %menor = alloca i32, align 4
  %maiorIgual = alloca i32, align 4
  %menorIgual = alloca i32, align 4
  %igual = alloca i32, align 4
  %diferente = alloca i32, align 4
  %and = alloca i32, align 4
  %or = alloca i32, align 4
  %not = alloca i32, align 4
  %xor = alloca i32, align 4
  %soma = alloca i32, align 4
  %subtracao = alloca i32, align 4
  %multiplicacao = alloca i32, align 4
  %divisao = alloca i32, align 4
  %modulo = alloca i32, align 4
  %shiftDireita = alloca i32, align 4
  %shiftEsquerda = alloca i32, align 4
  store i32 0, i32* %1
  store i32 2, i32* %x, align 4
  store i32 1, i32* %y, align 4
  %2 = load i32* %x, align 4
  %3 = load i32* %y, align 4
  %4 = icmp sgt i32 %2, %3
  %5 = zext i1 %4 to i32
  store i32 %5, i32* %maior, align 4
  %6 = load i32* %x, align 4
  %7 = load i32* %y, align 4
  %8 = icmp slt i32 %6, %7
  %9 = zext i1 %8 to i32
  store i32 %9, i32* %menor, align 4
  %10 = load i32* %x, align 4
  %11 = load i32* %y, align 4
  %12 = icmp sge i32 %10, %11
  %13 = zext i1 %12 to i32
  store i32 %13, i32* %maiorIgual, align 4
  %14 = load i32* %x, align 4
  %15 = load i32* %y, align 4
  %16 = icmp sle i32 %14, %15
  %17 = zext i1 %16 to i32
  store i32 %17, i32* %menorIgual, align 4
  %18 = load i32* %x, align 4
  %19 = load i32* %y, align 4
  %20 = icmp eq i32 %18, %19
  %21 = zext i1 %20 to i32
  store i32 %21, i32* %igual, align 4
  %22 = load i32* %x, align 4
  %23 = load i32* %y, align 4
  %24 = icmp ne i32 %22, %23
  %25 = zext i1 %24 to i32
  store i32 %25, i32* %diferente, align 4
  %26 = load i32* %x, align 4
  %27 = load i32* %y, align 4
  %28 = and i32 %26, %27
  store i32 %28, i32* %and, align 4
  %29 = load i32* %x, align 4
  %30 = load i32* %y, align 4
  %31 = or i32 %29, %30
  store i32 %31, i32* %or, align 4
  %32 = load i32* %x, align 4
  %33 = icmp ne i32 %32, 0
  %34 = xor i1 %33, true
  %35 = zext i1 %34 to i32
  store i32 %35, i32* %not, align 4
  %36 = load i32* %x, align 4
  %37 = load i32* %y, align 4
  %38 = xor i32 %36, %37
  store i32 %38, i32* %xor, align 4
  %39 = load i32* %x, align 4
  %40 = load i32* %y, align 4
  %41 = add nsw i32 %39, %40
  store i32 %41, i32* %soma, align 4
  %42 = load i32* %x, align 4
  %43 = load i32* %y, align 4
  %44 = sub nsw i32 %42, %43
  store i32 %44, i32* %subtracao, align 4
  %45 = load i32* %x, align 4
  %46 = load i32* %y, align 4
  %47 = mul nsw i32 %45, %46
  store i32 %47, i32* %multiplicacao, align 4
  %48 = load i32* %x, align 4
  %49 = load i32* %y, align 4
  %50 = sdiv i32 %48, %49
  store i32 %50, i32* %divisao, align 4
  %51 = load i32* %x, align 4
  %52 = load i32* %y, align 4
  %53 = srem i32 %51, %52
  store i32 %53, i32* %modulo, align 4
  %54 = load i32* %x, align 4
  %55 = ashr i32 %54, 1
  store i32 %55, i32* %shiftDireita, align 4
  %56 = load i32* %x, align 4
  %57 = shl i32 %56, 1
  store i32 %57, i32* %shiftEsquerda, align 4
  ret i32 0
}

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Ubuntu clang version 3.5.2-3ubuntu1 (tags/RELEASE_352/final) (based on LLVM 3.5.2)"}
