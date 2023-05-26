; ModuleID = "meu_modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"B" = common global [2048 x [2048 x i32]] zeroinitializer, align 4
define i32 @"main"() 
{
entry:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"D" = alloca [2048 x [2048 x i32]], align 4
  %"ptr_B_1_1" = getelementptr [2048 x [2048 x i32]], [2048 x [2048 x i32]]* @"B", i32 0, i32 1, i32 1
  %".3" = load i32, i32* %"ptr_B_1_1", align 4
  %".4" = add i32 %".3", 10
  %"ptr_B_0_1" = getelementptr [2048 x [2048 x i32]], [2048 x [2048 x i32]]* @"B", i32 0, i32 0, i32 1
  store i32 %".4", i32* %"ptr_B_0_1"
  %"ptr_D_1_1" = getelementptr [2048 x [2048 x i32]], [2048 x [2048 x i32]]* %"D", i32 0, i32 1, i32 1
  %".6" = load i32, i32* %"ptr_D_1_1", align 4
  %".7" = add i32 %".6", 10
  %"ptr_D_0_1" = getelementptr [2048 x [2048 x i32]], [2048 x [2048 x i32]]* %"D", i32 0, i32 0, i32 1
  store i32 %".7", i32* %"ptr_D_0_1"
  br label %"exit"
exit:
  %".10" = load i32, i32* %"retorno"
  ret i32 %".10"
}
