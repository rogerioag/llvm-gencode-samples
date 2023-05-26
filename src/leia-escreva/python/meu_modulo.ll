; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1")

declare void @"escrevaFlutuante"(float %".1")

declare i32 @"leiaInteiro"()

declare float @"leiaFlutuante"()

define i32 @"main"()
{
bloco_entrada:
  %"a" = alloca i32, i32 4
  %".2" = call i32 @"leiaInteiro"()
  store i32 %".2", i32* %"a", align 4
  %".4" = load i32, i32* %"a"
  call void @"escrevaInteiro"(i32 %".4")
  br label %"bloco_saida"
bloco_saida:
  ret i32 0
}
