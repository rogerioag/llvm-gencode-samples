; ModuleID = 'meu_modulo'
source_filename = "meu_modulo"

define i64 @main() {
entry:
  %retorno = alloca i64
  store i64 0, i64* %retorno
  %a = alloca i64
  %b = alloca i64
  %c = alloca i64
  store i64 1, i64* %a
  store i64 2, i64* %b
  store i64 0, i64* %c
  %0 = load i64, i64* %a
  %1 = load i64, i64* %b
  %temp = add i64 %0, %1
  store i64 %temp, i64* %c
  br label %end

end:                                              ; preds = %entry
  %2 = load i64, i64* %retorno
  ret i64 %2
}
