; ModuleID = "if3.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"a" = alloca i32, align 4
  store i32 30, i32* %"a"
  %"b" = alloca i32, align 4
  store i32 30, i32* %"b"
  br label %"if"
if:
  %".5" = load i32, i32* %"a"
  %"a >= 10" = icmp sge i32 %".5", 10
  br i1 %"a >= 10", label %"if.if", label %"if.endif"
if.if:
  %".7" = load i32, i32* %"b"
  store i32 %".7", i32* %"a"
  br label %"if.endif"
if.endif:
  br label %"exit"
exit:
  %".11" = load i32, i32* %"b"
  ret i32 %".11"
}
