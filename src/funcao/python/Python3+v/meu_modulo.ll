; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32, align 4
  store i32 0, i32* %"retorno"
  store i32 0, i32* %"retorno"
  br label %"exit"
exit:
  %"res" = load i32, i32* %"retorno", align 4
  ret i32 %"res"
}
