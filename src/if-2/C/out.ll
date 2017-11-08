; ModuleID = 'meu_modulo'

define i64 @main() {
entry:
  %retorno = alloca i64
  store i64 0, i64* %retorno
  %n = alloca i64
  store i64 10, i64* %n
  br label %predicate

predicate:                                        ; preds = %entry
  %n1 = load i64* %n
  %if_test = icmp slt i64 %n1, 1024
  br i1 %if_test, label %then, label %else

then:                                             ; preds = %predicate
  store i64 11, i64* %retorno
  br label %merge

else:                                             ; preds = %predicate
  store i64 22, i64* %retorno
  br label %merge

merge:                                            ; preds = %else, %then
  br label %end

end:                                              ; preds = %merge
  %0 = load i64* %retorno
  ret i64 %0
}
