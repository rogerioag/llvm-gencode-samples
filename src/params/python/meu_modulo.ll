; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"func"(i32 %"p1", float %"p2") 
{
entry:
  %"r" = alloca i32, align 4
  %".4" = load i32, i32* %"r"
  ret i32 %".4"
}

define i32 @"main"(i32 %"argv") 
{
entry:
  %"x" = alloca i32
  %"temp1" = alloca i32
  store i32 1, i32* %"temp1"
  %"temp2" = alloca float
  store float 0x4000000000000000, float* %"temp2"
  %".5" = load i32, i32* %"temp1"
  %".6" = load float, float* %"temp2"
  %".7" = call i32 @"func"(i32 %".5", float %".6")
  store i32 %".7", i32* %"x"
  %"retorno" = alloca i32, align 4
  store i32 0, i32* %"retorno"
  %".10" = load i32, i32* %"retorno"
  ret i32 %".10"
}
