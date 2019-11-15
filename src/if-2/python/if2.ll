; ModuleID = "if2.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"a" = alloca i32, align 4
  %"b" = alloca i32, align 4
  %"c" = alloca i32, align 4
  %"a < b" = icmp slt i32* %"a", %"b"
  br i1 %"a < b", label %"entry.if", label %"entry.else"
entry.if:
  store i32 5, i32* %"c"
  br label %"entry.endif"
entry.else:
  store i32 6, i32* %"c"
  br label %"entry.endif"
entry.endif:
  %"1024_temp" = alloca i32
  %"a < 1024" = icmp slt i32* %"a", %"1024_temp"
  br i1 %"a < 1024", label %"entry.endif.if", label %"entry.endif.else"
entry.endif.if:
  store i32 10, i32* %"c"
  br label %"entry.endif.endif"
entry.endif.else:
  store i32 20, i32* %"c"
  br label %"entry.endif.endif"
entry.endif.endif:
  br label %"exit"
exit:
  ret i32 0
}
