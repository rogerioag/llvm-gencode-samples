; ModuleID = 'meu_modulo'

define i64 @main() {
entry:
  %retorno = alloca i64
  store i64 0, i64* %retorno
  %i = alloca i64
  store i64 0, i64* %i
  br label %body

predicate:                                        ; preds = %inc_var
  %i1 = load i64* %i
  %while_test = icmp slt i64 %i1, 1024
  br i1 %while_test, label %body, label %endloop

body:                                             ; preds = %predicate, %entry
  store i64 11, i64* %retorno
  br label %inc_var

inc_var:                                          ; preds = %body
  %0 = load i64* %i
  %i_inc = add i64 %0, 1
  store i64 %i_inc, i64* %i
  br label %predicate

endloop:                                          ; preds = %predicate
  br label %exit

exit:                                             ; preds = %endloop
  %1 = load i64* %retorno
  ret i64 %1
}
