; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaChar"(i8* %".1", ...) 

define i32 @"main"() 
{
entry:
  %"string" = alloca [15 x i8]
  store [15 x i8] c"Hello world!!\0a\00", [15 x i8]* %"string"
  %".3" = bitcast [15 x i8]* %"string" to i8*
  call void (i8*, ...) @"escrevaChar"(i8* %".3", [15 x i8]* %"string")
  call void @"escrevaInteiro"(i32 23)
  br label %"exit"
exit:
  %"variavel_retorno" = alloca i32, align 4
  store i32 0, i32* %"variavel_retorno"
  %"retorno" = load i32, i32* %"variavel_retorno", align 4
  ret i32 %"retorno"
}
