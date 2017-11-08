; ModuleID = 'meu_modulo.bc'

define i64 @soma(i64, i64) {
entry:
  %tmp = add i64 %0, %1
  br label %exit

exit:                                             ; preds = %entry
  ret i64 %tmp
}

define i64 @main() {
entry:
  %retorno = alloca i64
  store i64 0, i64* %retorno
  %a = alloca i64
  %b = alloca i64
  store i64 1, i64* %a
  store i64 2, i64* %b
  %0 = load i64* %a
  %1 = load i64* %b
  %res = call i64 @soma(i64 %0, i64 %1)
  store i64 %res, i64* %retorno
  br label %exit

exit:                                             ; preds = %entry
  %2 = load i64* %retorno
  ret i64 %2
}
