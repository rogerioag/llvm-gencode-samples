; ModuleID = '+'
source_filename = "+"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128-ni:10:11:12:13"
target triple = "x86_64-unknown-linux-gnu"

;  @ int.jl:87 within `+'
define i64 @"julia_+_40"(i64 signext %0, i64 signext %1) !dbg !5 {
top:
  %2 = call {}*** @julia.ptls_states()
  %3 = bitcast {}*** %2 to {} addrspace(10)**
  %4 = getelementptr inbounds {} addrspace(10)*, {} addrspace(10)** %3, i64 4
  %5 = bitcast {} addrspace(10)** %4 to i64**
  %6 = load i64*, i64** %5, align 8, !tbaa !7, !invariant.load !4
  %7 = add i64 %0, %1, !dbg !11
  ret i64 %7, !dbg !11
}

define nonnull {} addrspace(10)* @"jfptr_+_41"({} addrspace(10)* %0, {} addrspace(10)** %1, i32 %2) #0 {
top:
  %3 = call {}*** @julia.ptls_states()
  %4 = bitcast {}*** %3 to {} addrspace(10)**
  %5 = getelementptr inbounds {} addrspace(10)*, {} addrspace(10)** %4, i64 4
  %6 = bitcast {} addrspace(10)** %5 to i64**
  %7 = load i64*, i64** %6, align 8, !tbaa !7, !invariant.load !4
  %8 = getelementptr inbounds {} addrspace(10)*, {} addrspace(10)** %1, i32 0
  %9 = load {} addrspace(10)*, {} addrspace(10)** %8, align 8, !nonnull !4, !dereferenceable !12, !align !12
  %10 = bitcast {} addrspace(10)* %9 to i64 addrspace(10)*
  %11 = addrspacecast i64 addrspace(10)* %10 to i64 addrspace(11)*
  %12 = load i64, i64 addrspace(11)* %11, align 8
  %13 = getelementptr inbounds {} addrspace(10)*, {} addrspace(10)** %1, i32 1
  %14 = load {} addrspace(10)*, {} addrspace(10)** %13, align 8, !nonnull !4, !dereferenceable !12, !align !12
  %15 = bitcast {} addrspace(10)* %14 to i64 addrspace(10)*
  %16 = addrspacecast i64 addrspace(10)* %15 to i64 addrspace(11)*
  %17 = load i64, i64 addrspace(11)* %16, align 8
  %18 = call i64 @"julia_+_40"(i64 signext %12, i64 signext %17)
  %19 = call nonnull {} addrspace(10)* @jl_box_int64(i64 signext %18)
  ret {} addrspace(10)* %19
}

declare {}*** @julia.ptls_states()

declare nonnull {} addrspace(10)* @jl_box_int64(i64 signext)

attributes #0 = { "thunk" }

!llvm.module.flags = !{!0, !1}
!llvm.dbg.cu = !{!2}

!0 = !{i32 2, !"Dwarf Version", i32 4}
!1 = !{i32 2, !"Debug Info Version", i32 3}
!2 = distinct !DICompileUnit(language: DW_LANG_Julia, file: !3, producer: "julia", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !4, nameTableKind: GNU)
!3 = !DIFile(filename: "int.jl", directory: ".")
!4 = !{}
!5 = distinct !DISubprogram(name: "+", linkageName: "julia_+_40", scope: null, file: !3, line: 87, type: !6, scopeLine: 87, spFlags: DISPFlagDefinition | DISPFlagOptimized, unit: !2, retainedNodes: !4)
!6 = !DISubroutineType(types: !4)
!7 = !{!8, !8, i64 0, i64 1}
!8 = !{!"jtbaa_const", !9, i64 0}
!9 = !{!"jtbaa", !10, i64 0}
!10 = !{!"jtbaa"}
!11 = !DILocation(line: 87, scope: !5)
!12 = !{i64 8}

