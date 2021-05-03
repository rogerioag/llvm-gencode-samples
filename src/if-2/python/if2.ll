; ModuleID = "if2.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entry:
  %"a" = alloca i32, align 4
  store i32 1, i32* %"a"
  %"b" = alloca i32, align 4
  store i32 2, i32* %"b"
  %"c" = alloca i32, align 4
  br label %"if"
if:
  %".5" = load i32, i32* %"a"
  %".6" = load i32, i32* %"b"
  %"a < b" = icmp slt i32 %".5", %".6"
  br i1 %"a < b", label %"if.if", label %"if.else"
if.if:
  store i32 5, i32* %"c"
  br label %"if.endif"
if.else:
  store i32 6, i32* %"c"
  br label %"if.endif"
if.endif:
  br label %"if.1"
if.1:
  %".13" = load i32, i32* %"a"
  %"a < 1024" = icmp slt i32 %".13", 1024
  br i1 %"a < 1024", label %"if.1.if", label %"if.1.else"
if.1.if:
  store i32 10, i32* %"c"
  br label %"if.1.endif"
if.1.else:
  store i32 20, i32* %"c"
  br label %"if.1.endif"
if.1.endif:
  br label %"exit"
exit:
  ret i32 0
}
