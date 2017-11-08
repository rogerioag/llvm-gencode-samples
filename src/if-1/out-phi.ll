; ModuleID = '<stdin>'

define i64 @main() {
entry:
  %if_test = icmp slt i64 10, 1024
  br i1 %if_test, label %iftrue, label %iffalse

end:                                              ; preds = %ifend
  ret i64 %retorno.0

iftrue:                                           ; preds = %entry
  br label %ifend

iffalse:                                          ; preds = %entry
  br label %ifend

ifend:                                            ; preds = %iffalse, %iftrue
  %retorno.0 = phi i64 [ 1, %iftrue ], [ 2, %iffalse ]
  br label %end
}
