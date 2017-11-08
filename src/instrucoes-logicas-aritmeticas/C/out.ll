; ModuleID = 'meu_modulo'
source_filename = "meu_modulo"

define i64 @main() {
entry:
  %retorno = alloca i64
  store i64 0, i64* %retorno
  %a = alloca i64
  %b = alloca float
  %c = alloca float
  store i64 1, i64* %a
  store i0 1, float* %b
  store i0 2, float* %c
  %0 = load i64, i64* %a
  %1 = load i64, i64* %a
  %temp = add i64 %0, %1
  store i64 %temp, i64* %a
  %2 = load float, float* %b
  %3 = load float, float* %c
  %temp2 = fadd float %2, %3
  store float %temp2, float* %b
  br label %end

end:                                              ; preds = %entry
  %4 = load i64, i64* %retorno
  ret i64 %4
}
