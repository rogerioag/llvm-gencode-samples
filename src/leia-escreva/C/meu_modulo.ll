; ModuleID = 'meu_modulo.bc'

declare i32 @leiaInteiro()

declare float @leiaFlutuante()

declare void @escrevaInteiro(i32)

declare void @escrevaFlutuante(float)

define i64 @main() {
entry:
  %retorno = alloca i64
  store i64 0, i64* %retorno
  %a = alloca i32
  %f = alloca float
  %leia_a = call i32 @leiaInteiro()
  store i32 %leia_a, i32* %a
  %leia_f = call float @leiaFlutuante()
  store float %leia_f, float* %f
  %print_a = load i32* %a
  call void @escrevaInteiro(i32 %print_a)
  %print_f = load float* %f
  call void @escrevaFlutuante(float %print_f)
  br label %exit

exit:                                             ; preds = %entry
  %0 = load i64* %retorno
  ret i64 %0
}
