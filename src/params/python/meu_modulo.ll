; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"retorna" = alloca i32, align 4
  store i32 0, i32* %"retorna"
  br label %"exit"
exit:
  %"ret_temp" = load i32, i32* %"retorna", align 4
  ret i32 %"ret_temp"
}
