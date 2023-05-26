; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"A" = common global [1024 x i32] zeroinitializer, align 4
define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"B" = alloca [1024 x i32], align 4
  %"ptr_A_49" = getelementptr [1024 x i32], [1024 x i32]* @"A", i32 0, i32 49
  %".3" = load i32, i32* %"ptr_A_49", align 4
  %".4" = add i32 %".3", 5
  %"ptr_A_50" = getelementptr [1024 x i32], [1024 x i32]* @"A", i32 0, i32 50
  store i32 %".4", i32* %"ptr_A_50"
  br label %"exit"
exit:
  %".7" = load i32, i32* %"retorno"
  ret i32 %".7"
}
