; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"x" = alloca i32
  store i32 19, i32* %"x"
  %"y" = alloca i32
  store i32 23, i32* %"y"
  %"resultado" = alloca i32
  %".4" = load i32, i32* %"x"
  %".5" = load i32, i32* %"y"
  %".6" = add i32 %".4", %".5"
  store i32 %".6", i32* %"resultado"
  ret i32* %"resultado"
}
