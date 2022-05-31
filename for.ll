; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1") 

define i32 @"main"() 
{
bloco_entrada:
  %"i" = alloca i32, align 4
  store i32 1, i32* %"i"
  br label %"valida_for"
bloco_saida:
  ret i32 0
valida_for:
  %".4" = load i32, i32* %"i"
  %".5" = icmp slt i32 %".4", 11
  br i1 %".5", label %"executa_for", label %"bloco_saida"
executa_for:
  %".7" = load i32, i32* %"i"
  call void @"escrevaInteiro"(i32 %".7")
  %".9" = load i32, i32* %"i"
  %".10" = add i32 %".9", 1
  store i32 %".10", i32* %"i"
  br label %"valida_for"
}
