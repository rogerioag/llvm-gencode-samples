; ModuleID = 'meu_modulo.bc'

@g = common global i32 0, align 4
@h = common global float 0, align 4

define i32 @main() {
entry:
  %retorno = alloca i32
  %a = alloca i32, align 4
  %b = alloca float, align 4
  store i32 0, i32* %retorno
  store i32 1, i32* %a
  store float 1.000000e+00, float* %b
  store i32 10, i32* @g
  store float 1.000000e+01, float* @h
  %0 = load i32* %a
  %temp = add i32 %0, 10
  store i32 %temp, i32* %a
  %1 = load float* %b
  %2 = load float* @h
  %temp1 = fadd float %1, %2
  store float %temp1, float* %b
  br label %end

end:                                              ; preds = %entry
  %3 = load i32* %retorno
  ret i32 %3
}
