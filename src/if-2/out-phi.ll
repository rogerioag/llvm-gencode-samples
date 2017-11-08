; ModuleID = '<stdin>'

define i64 @main() {
entry:
  br label %predicate

predicate:                                        ; preds = %entry
  %if_test = icmp slt i64 10, 1024
  br i1 %if_test, label %then, label %else

then:                                             ; preds = %predicate
  br label %merge

else:                                             ; preds = %predicate
  br label %merge

merge:                                            ; preds = %else, %then
  %retorno.0 = phi i64 [ 11, %then ], [ 22, %else ]
  br label %end

end:                                              ; preds = %merge
  ret i64 %retorno.0
}
