; ModuleID = "meu_modulo.bc"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"ret_val" = alloca i32
  store i32 0, i32* %"ret_val", align 4
  %"x" = alloca i32
  store i32 2, i32* %"x", align 4
  %"y" = alloca i32
  store i32 1, i32* %"y", align 4
  %"x_temp" = load i32, i32* %"x"
  %"y_temp" = load i32, i32* %"y"
  %"maior" = icmp sgt i32 %"x_temp", %"y_temp"
  %"menor" = icmp slt i32 %"x_temp", %"y_temp"
  %"maiorIgual" = icmp sge i32 %"x_temp", %"y_temp"
  %"menorIgual" = icmp sle i32 %"x_temp", %"y_temp"
  %"igual" = icmp eq i32 %"x_temp", %"y_temp"
  %"diferente" = icmp ne i32 %"x_temp", %"y_temp"
  %"and" = and i32 %"x_temp", %"y_temp"
  %"or" = or i32 %"x_temp", %"y_temp"
  %"xor" = xor i32 %"x_temp", %"y_temp"
  %"not" = xor i32 %"x_temp", -1
  %"soma" = add i32 %"x_temp", %"y_temp"
  %"subtracao" = sub i32 %"x_temp", %"y_temp"
  %"multiplicacao" = mul i32 %"x_temp", %"y_temp"
  %"divisao" = sdiv i32 %"x_temp", %"y_temp"
  %"modulo" = srem i32 %"x_temp", %"y_temp"
  %"shiftDireita" = ashr i32 %"x_temp", 1
  %"shiftEsquerda" = shl i32 %"x_temp", 1
  br label %"exit"
exit:
  %".6" = load i32, i32* %"ret_val"
  ret i32 %".6"
}
