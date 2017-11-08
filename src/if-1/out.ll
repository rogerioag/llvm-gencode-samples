; ModuleID = 'meu_modulo'

define i64 @main() {
entry:
  %retorno = alloca i64
  store i64 0, i64* %retorno
  %n = alloca i64
  store i64 10, i64* %n
  %n1 = load i64* %n
  %if_test = icmp slt i64 %n1, 1024
  br i1 %if_test, label %iftrue, label %iffalse

end:                                              ; preds = %ifend
  %0 = load i64* %retorno
  ret i64 %0

iftrue:                                           ; preds = %entry
  store i64 1, i64* %retorno
  br label %ifend

iffalse:                                          ; preds = %entry
  store i64 2, i64* %retorno
  br label %ifend

ifend:                                            ; preds = %iffalse, %iftrue
  br label %end
}
