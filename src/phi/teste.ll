; ModuleID = 'main.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.LLVMOpaqueType = type opaque
%struct.LLVMOpaqueContext = type opaque
%struct.LLVMOpaqueModule = type opaque
%struct.LLVMOpaqueBuilder = type opaque
%struct.LLVMOpaqueValue = type opaque
%struct.LLVMOpaqueBasicBlock = type opaque

@.str = private unnamed_addr constant [6 x i8] c"mytop\00", align 1
@.str1 = private unnamed_addr constant [5 x i8] c"main\00", align 1
@.str2 = private unnamed_addr constant [6 x i8] c"entry\00", align 1
@.str3 = private unnamed_addr constant [10 x i8] c"predicate\00", align 1
@.str4 = private unnamed_addr constant [5 x i8] c"then\00", align 1
@.str5 = private unnamed_addr constant [5 x i8] c"else\00", align 1
@.str6 = private unnamed_addr constant [6 x i8] c"merge\00", align 1
@.str7 = private unnamed_addr constant [3 x i8] c"xp\00", align 1
@.str8 = private unnamed_addr constant [5 x i8] c"eq10\00", align 1
@.str9 = private unnamed_addr constant [2 x i8] c"x\00", align 1

; Function Attrs: nounwind uwtable
define i32 @main(i32 %argc, i8** nocapture readnone %argv) #0 {
  %mainFnParamTypes = alloca [1 x %struct.LLVMOpaqueType*], align 8
  tail call void @llvm.dbg.value(metadata !{i32 %argc}, i64 0, metadata !27), !dbg !67
  tail call void @llvm.dbg.value(metadata !{i8** %argv}, i64 0, metadata !28), !dbg !68
  %1 = tail call %struct.LLVMOpaqueContext* @LLVMGetGlobalContext() #3, !dbg !69
  tail call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueContext* %1}, i64 0, metadata !29), !dbg !70
  %2 = tail call %struct.LLVMOpaqueModule* @LLVMModuleCreateWithNameInContext(i8* getelementptr inbounds ([6 x i8]* @.str, i64 0, i64 0), %struct.LLVMOpaqueContext* %1) #3, !dbg !71
  tail call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueModule* %2}, i64 0, metadata !33), !dbg !72
  %3 = tail call %struct.LLVMOpaqueBuilder* @LLVMCreateBuilderInContext(%struct.LLVMOpaqueContext* %1) #3, !dbg !73
  tail call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueBuilder* %3}, i64 0, metadata !37), !dbg !74
  tail call void @llvm.dbg.declare(metadata !{[1 x %struct.LLVMOpaqueType*]* %mainFnParamTypes}, metadata !41), !dbg !75
  %4 = getelementptr inbounds [1 x %struct.LLVMOpaqueType*]* %mainFnParamTypes, i64 0, i64 0, !dbg !76
  %5 = tail call %struct.LLVMOpaqueType* @LLVMInt64TypeInContext(%struct.LLVMOpaqueContext* %1) #3, !dbg !77
  store %struct.LLVMOpaqueType* %5, %struct.LLVMOpaqueType** %4, align 8, !dbg !77, !tbaa !78
  %6 = tail call %struct.LLVMOpaqueType* @LLVMInt64TypeInContext(%struct.LLVMOpaqueContext* %1) #3, !dbg !82
  tail call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueType* %6}, i64 0, metadata !48), !dbg !83
  %7 = call %struct.LLVMOpaqueType* @LLVMFunctionType(%struct.LLVMOpaqueType* %6, %struct.LLVMOpaqueType** %4, i32 1, i32 0) #3, !dbg !84
  %8 = call %struct.LLVMOpaqueValue* @LLVMAddFunction(%struct.LLVMOpaqueModule* %2, i8* getelementptr inbounds ([5 x i8]* @.str1, i64 0, i64 0), %struct.LLVMOpaqueType* %7) #3, !dbg !85
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueValue* %8}, i64 0, metadata !49), !dbg !86
  %9 = call %struct.LLVMOpaqueBasicBlock* @LLVMAppendBasicBlockInContext(%struct.LLVMOpaqueContext* %1, %struct.LLVMOpaqueValue* %8, i8* getelementptr inbounds ([6 x i8]* @.str2, i64 0, i64 0)) #3, !dbg !87
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueBasicBlock* %9}, i64 0, metadata !53), !dbg !88
  %10 = call %struct.LLVMOpaqueBasicBlock* @LLVMAppendBasicBlockInContext(%struct.LLVMOpaqueContext* %1, %struct.LLVMOpaqueValue* %8, i8* getelementptr inbounds ([10 x i8]* @.str3, i64 0, i64 0)) #3, !dbg !89
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueBasicBlock* %10}, i64 0, metadata !57), !dbg !90
  %11 = call %struct.LLVMOpaqueBasicBlock* @LLVMAppendBasicBlockInContext(%struct.LLVMOpaqueContext* %1, %struct.LLVMOpaqueValue* %8, i8* getelementptr inbounds ([5 x i8]* @.str4, i64 0, i64 0)) #3, !dbg !91
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueBasicBlock* %11}, i64 0, metadata !58), !dbg !92
  %12 = call %struct.LLVMOpaqueBasicBlock* @LLVMAppendBasicBlockInContext(%struct.LLVMOpaqueContext* %1, %struct.LLVMOpaqueValue* %8, i8* getelementptr inbounds ([5 x i8]* @.str5, i64 0, i64 0)) #3, !dbg !93
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueBasicBlock* %12}, i64 0, metadata !59), !dbg !94
  %13 = call %struct.LLVMOpaqueBasicBlock* @LLVMAppendBasicBlockInContext(%struct.LLVMOpaqueContext* %1, %struct.LLVMOpaqueValue* %8, i8* getelementptr inbounds ([6 x i8]* @.str6, i64 0, i64 0)) #3, !dbg !95
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueBasicBlock* %13}, i64 0, metadata !60), !dbg !96
  call void @LLVMPositionBuilderAtEnd(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %9) #3, !dbg !97
  %14 = call %struct.LLVMOpaqueType* @LLVMInt64TypeInContext(%struct.LLVMOpaqueContext* %1) #3, !dbg !98
  %15 = call %struct.LLVMOpaqueValue* @LLVMBuildAlloca(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueType* %14, i8* getelementptr inbounds ([3 x i8]* @.str7, i64 0, i64 0)) #3, !dbg !99
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueValue* %15}, i64 0, metadata !61), !dbg !100
  %16 = call %struct.LLVMOpaqueValue* @LLVMBuildBr(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %10) #3, !dbg !101
  call void @LLVMPositionBuilderAtEnd(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %10) #3, !dbg !102
  %17 = call %struct.LLVMOpaqueValue* @LLVMGetParam(%struct.LLVMOpaqueValue* %8, i32 0) #3, !dbg !103
  %18 = call %struct.LLVMOpaqueType* @LLVMInt64TypeInContext(%struct.LLVMOpaqueContext* %1) #3, !dbg !104
  %19 = call %struct.LLVMOpaqueValue* @LLVMConstInt(%struct.LLVMOpaqueType* %18, i64 10, i32 0) #3, !dbg !105
  %20 = call %struct.LLVMOpaqueValue* @LLVMBuildICmp(%struct.LLVMOpaqueBuilder* %3, i32 32, %struct.LLVMOpaqueValue* %17, %struct.LLVMOpaqueValue* %19, i8* getelementptr inbounds ([5 x i8]* @.str8, i64 0, i64 0)) #3, !dbg !106
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueValue* %20}, i64 0, metadata !62), !dbg !107
  %21 = call %struct.LLVMOpaqueValue* @LLVMBuildCondBr(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueValue* %20, %struct.LLVMOpaqueBasicBlock* %11, %struct.LLVMOpaqueBasicBlock* %12) #3, !dbg !108
  call void @LLVMPositionBuilderAtEnd(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %11) #3, !dbg !109
  %22 = call %struct.LLVMOpaqueType* @LLVMInt64TypeInContext(%struct.LLVMOpaqueContext* %1) #3, !dbg !110
  %23 = call %struct.LLVMOpaqueValue* @LLVMConstInt(%struct.LLVMOpaqueType* %22, i64 11, i32 0) #3, !dbg !111
  %24 = call %struct.LLVMOpaqueValue* @LLVMBuildStore(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueValue* %23, %struct.LLVMOpaqueValue* %15) #3, !dbg !112
  %25 = call %struct.LLVMOpaqueValue* @LLVMBuildBr(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %13) #3, !dbg !113
  call void @LLVMPositionBuilderAtEnd(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %12) #3, !dbg !114
  %26 = call %struct.LLVMOpaqueType* @LLVMInt64TypeInContext(%struct.LLVMOpaqueContext* %1) #3, !dbg !115
  %27 = call %struct.LLVMOpaqueValue* @LLVMConstInt(%struct.LLVMOpaqueType* %26, i64 22, i32 0) #3, !dbg !116
  %28 = call %struct.LLVMOpaqueValue* @LLVMBuildStore(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueValue* %27, %struct.LLVMOpaqueValue* %15) #3, !dbg !117
  %29 = call %struct.LLVMOpaqueValue* @LLVMBuildBr(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %13) #3, !dbg !118
  call void @LLVMPositionBuilderAtEnd(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueBasicBlock* %13) #3, !dbg !119
  %30 = call %struct.LLVMOpaqueValue* @LLVMBuildLoad(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueValue* %15, i8* getelementptr inbounds ([2 x i8]* @.str9, i64 0, i64 0)) #3, !dbg !120
  call void @llvm.dbg.value(metadata !{%struct.LLVMOpaqueValue* %30}, i64 0, metadata !63), !dbg !121
  %31 = call %struct.LLVMOpaqueValue* @LLVMBuildRet(%struct.LLVMOpaqueBuilder* %3, %struct.LLVMOpaqueValue* %30) #3, !dbg !122
  call void @LLVMDumpModule(%struct.LLVMOpaqueModule* %2) #3, !dbg !123
  ret i32 0, !dbg !124
}

; Function Attrs: nounwind readnone
declare void @llvm.dbg.declare(metadata, metadata) #1

declare %struct.LLVMOpaqueContext* @LLVMGetGlobalContext() #2

declare %struct.LLVMOpaqueModule* @LLVMModuleCreateWithNameInContext(i8*, %struct.LLVMOpaqueContext*) #2

declare %struct.LLVMOpaqueBuilder* @LLVMCreateBuilderInContext(%struct.LLVMOpaqueContext*) #2

declare %struct.LLVMOpaqueType* @LLVMInt64TypeInContext(%struct.LLVMOpaqueContext*) #2

declare %struct.LLVMOpaqueValue* @LLVMAddFunction(%struct.LLVMOpaqueModule*, i8*, %struct.LLVMOpaqueType*) #2

declare %struct.LLVMOpaqueType* @LLVMFunctionType(%struct.LLVMOpaqueType*, %struct.LLVMOpaqueType**, i32, i32) #2

declare %struct.LLVMOpaqueBasicBlock* @LLVMAppendBasicBlockInContext(%struct.LLVMOpaqueContext*, %struct.LLVMOpaqueValue*, i8*) #2

declare void @LLVMPositionBuilderAtEnd(%struct.LLVMOpaqueBuilder*, %struct.LLVMOpaqueBasicBlock*) #2

declare %struct.LLVMOpaqueValue* @LLVMBuildAlloca(%struct.LLVMOpaqueBuilder*, %struct.LLVMOpaqueType*, i8*) #2

declare %struct.LLVMOpaqueValue* @LLVMBuildBr(%struct.LLVMOpaqueBuilder*, %struct.LLVMOpaqueBasicBlock*) #2

declare %struct.LLVMOpaqueValue* @LLVMBuildICmp(%struct.LLVMOpaqueBuilder*, i32, %struct.LLVMOpaqueValue*, %struct.LLVMOpaqueValue*, i8*) #2

declare %struct.LLVMOpaqueValue* @LLVMGetParam(%struct.LLVMOpaqueValue*, i32) #2

declare %struct.LLVMOpaqueValue* @LLVMConstInt(%struct.LLVMOpaqueType*, i64, i32) #2

declare %struct.LLVMOpaqueValue* @LLVMBuildCondBr(%struct.LLVMOpaqueBuilder*, %struct.LLVMOpaqueValue*, %struct.LLVMOpaqueBasicBlock*, %struct.LLVMOpaqueBasicBlock*) #2

declare %struct.LLVMOpaqueValue* @LLVMBuildStore(%struct.LLVMOpaqueBuilder*, %struct.LLVMOpaqueValue*, %struct.LLVMOpaqueValue*) #2

declare %struct.LLVMOpaqueValue* @LLVMBuildLoad(%struct.LLVMOpaqueBuilder*, %struct.LLVMOpaqueValue*, i8*) #2

declare %struct.LLVMOpaqueValue* @LLVMBuildRet(%struct.LLVMOpaqueBuilder*, %struct.LLVMOpaqueValue*) #2

declare void @LLVMDumpModule(%struct.LLVMOpaqueModule*) #2

; Function Attrs: nounwind readnone
declare void @llvm.dbg.value(metadata, i64, metadata) #1

attributes #0 = { nounwind uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind readnone }
attributes #2 = { "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!64, !65}
!llvm.ident = !{!66}

!0 = metadata !{i32 786449, metadata !1, i32 12, metadata !"Debian clang version 3.5.0-10 (tags/RELEASE_350/final) (based on LLVM 3.5.0)", i1 true, metadata !"", i32 0, metadata !2, metadata !16, metadata !17, metadata !16, metadata !16, metadata !"", i32 1} ; [ DW_TAG_compile_unit ] [/dados/rogerio/UTFPR/docencia/disciplinas/2017/COMP-BCC36B/1-2017/aulas/md/aula-21-geracao-de-codigo-ir-llvmir/src/phi/main.c] [DW_LANG_C99]
!1 = metadata !{metadata !"main.c", metadata !"/dados/rogerio/UTFPR/docencia/disciplinas/2017/COMP-BCC36B/1-2017/aulas/md/aula-21-geracao-de-codigo-ir-llvmir/src/phi"}
!2 = metadata !{metadata !3}
!3 = metadata !{i32 786436, metadata !4, null, metadata !"", i32 318, i64 32, i64 32, i32 0, i32 0, null, metadata !5, i32 0, null, null, null} ; [ DW_TAG_enumeration_type ] [line 318, size 32, align 32, offset 0] [def] [from ]
!4 = metadata !{metadata !"/usr/lib/llvm-3.5/include/llvm-c/Core.h", metadata !"/dados/rogerio/UTFPR/docencia/disciplinas/2017/COMP-BCC36B/1-2017/aulas/md/aula-21-geracao-de-codigo-ir-llvmir/src/phi"}
!5 = metadata !{metadata !6, metadata !7, metadata !8, metadata !9, metadata !10, metadata !11, metadata !12, metadata !13, metadata !14, metadata !15}
!6 = metadata !{i32 786472, metadata !"LLVMIntEQ", i64 32} ; [ DW_TAG_enumerator ] [LLVMIntEQ :: 32]
!7 = metadata !{i32 786472, metadata !"LLVMIntNE", i64 33} ; [ DW_TAG_enumerator ] [LLVMIntNE :: 33]
!8 = metadata !{i32 786472, metadata !"LLVMIntUGT", i64 34} ; [ DW_TAG_enumerator ] [LLVMIntUGT :: 34]
!9 = metadata !{i32 786472, metadata !"LLVMIntUGE", i64 35} ; [ DW_TAG_enumerator ] [LLVMIntUGE :: 35]
!10 = metadata !{i32 786472, metadata !"LLVMIntULT", i64 36} ; [ DW_TAG_enumerator ] [LLVMIntULT :: 36]
!11 = metadata !{i32 786472, metadata !"LLVMIntULE", i64 37} ; [ DW_TAG_enumerator ] [LLVMIntULE :: 37]
!12 = metadata !{i32 786472, metadata !"LLVMIntSGT", i64 38} ; [ DW_TAG_enumerator ] [LLVMIntSGT :: 38]
!13 = metadata !{i32 786472, metadata !"LLVMIntSGE", i64 39} ; [ DW_TAG_enumerator ] [LLVMIntSGE :: 39]
!14 = metadata !{i32 786472, metadata !"LLVMIntSLT", i64 40} ; [ DW_TAG_enumerator ] [LLVMIntSLT :: 40]
!15 = metadata !{i32 786472, metadata !"LLVMIntSLE", i64 41} ; [ DW_TAG_enumerator ] [LLVMIntSLE :: 41]
!16 = metadata !{}
!17 = metadata !{metadata !18}
!18 = metadata !{i32 786478, metadata !1, metadata !19, metadata !"main", metadata !"main", metadata !"", i32 4, metadata !20, i1 false, i1 true, i32 0, i32 0, null, i32 256, i1 true, i32 (i32, i8**)* @main, null, null, metadata !26, i32 5} ; [ DW_TAG_subprogram ] [line 4] [def] [scope 5] [main]
!19 = metadata !{i32 786473, metadata !1}         ; [ DW_TAG_file_type ] [/dados/rogerio/UTFPR/docencia/disciplinas/2017/COMP-BCC36B/1-2017/aulas/md/aula-21-geracao-de-codigo-ir-llvmir/src/phi/main.c]
!20 = metadata !{i32 786453, i32 0, null, metadata !"", i32 0, i64 0, i64 0, i64 0, i32 0, null, metadata !21, i32 0, null, null, null} ; [ DW_TAG_subroutine_type ] [line 0, size 0, align 0, offset 0] [from ]
!21 = metadata !{metadata !22, metadata !22, metadata !23}
!22 = metadata !{i32 786468, null, null, metadata !"int", i32 0, i64 32, i64 32, i64 0, i32 0, i32 5} ; [ DW_TAG_base_type ] [int] [line 0, size 32, align 32, offset 0, enc DW_ATE_signed]
!23 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !24} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from ]
!24 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !25} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from char]
!25 = metadata !{i32 786468, null, null, metadata !"char", i32 0, i64 8, i64 8, i64 0, i32 0, i32 6} ; [ DW_TAG_base_type ] [char] [line 0, size 8, align 8, offset 0, enc DW_ATE_signed_char]
!26 = metadata !{metadata !27, metadata !28, metadata !29, metadata !33, metadata !37, metadata !41, metadata !48, metadata !49, metadata !53, metadata !57, metadata !58, metadata !59, metadata !60, metadata !61, metadata !62, metadata !63}
!27 = metadata !{i32 786689, metadata !18, metadata !"argc", metadata !19, i32 16777220, metadata !22, i32 0, i32 0} ; [ DW_TAG_arg_variable ] [argc] [line 4]
!28 = metadata !{i32 786689, metadata !18, metadata !"argv", metadata !19, i32 33554436, metadata !23, i32 0, i32 0} ; [ DW_TAG_arg_variable ] [argv] [line 4]
!29 = metadata !{i32 786688, metadata !18, metadata !"context", metadata !19, i32 6, metadata !30, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [context] [line 6]
!30 = metadata !{i32 786454, metadata !4, null, metadata !"LLVMContextRef", i32 70, i64 0, i64 0, i64 0, i32 0, metadata !31} ; [ DW_TAG_typedef ] [LLVMContextRef] [line 70, size 0, align 0, offset 0] [from ]
!31 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !32} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from LLVMOpaqueContext]
!32 = metadata !{i32 786451, metadata !4, null, metadata !"LLVMOpaqueContext", i32 70, i64 0, i64 0, i32 0, i32 4, null, null, i32 0, null, null, null} ; [ DW_TAG_structure_type ] [LLVMOpaqueContext] [line 70, size 0, align 0, offset 0] [decl] [from ]
!33 = metadata !{i32 786688, metadata !18, metadata !"module", metadata !19, i32 7, metadata !34, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [module] [line 7]
!34 = metadata !{i32 786454, metadata !4, null, metadata !"LLVMModuleRef", i32 78, i64 0, i64 0, i64 0, i32 0, metadata !35} ; [ DW_TAG_typedef ] [LLVMModuleRef] [line 78, size 0, align 0, offset 0] [from ]
!35 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !36} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from LLVMOpaqueModule]
!36 = metadata !{i32 786451, metadata !4, null, metadata !"LLVMOpaqueModule", i32 78, i64 0, i64 0, i32 0, i32 4, null, null, i32 0, null, null, null} ; [ DW_TAG_structure_type ] [LLVMOpaqueModule] [line 78, size 0, align 0, offset 0] [decl] [from ]
!37 = metadata !{i32 786688, metadata !18, metadata !"builder", metadata !19, i32 8, metadata !38, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [builder] [line 8]
!38 = metadata !{i32 786454, metadata !4, null, metadata !"LLVMBuilderRef", i32 106, i64 0, i64 0, i64 0, i32 0, metadata !39} ; [ DW_TAG_typedef ] [LLVMBuilderRef] [line 106, size 0, align 0, offset 0] [from ]
!39 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !40} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from LLVMOpaqueBuilder]
!40 = metadata !{i32 786451, metadata !4, null, metadata !"LLVMOpaqueBuilder", i32 106, i64 0, i64 0, i32 0, i32 4, null, null, i32 0, null, null, null} ; [ DW_TAG_structure_type ] [LLVMOpaqueBuilder] [line 106, size 0, align 0, offset 0] [decl] [from ]
!41 = metadata !{i32 786688, metadata !18, metadata !"mainFnParamTypes", metadata !19, i32 10, metadata !42, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [mainFnParamTypes] [line 10]
!42 = metadata !{i32 786433, null, null, metadata !"", i32 0, i64 64, i64 64, i32 0, i32 0, metadata !43, metadata !46, i32 0, null, null, null} ; [ DW_TAG_array_type ] [line 0, size 64, align 64, offset 0] [from LLVMTypeRef]
!43 = metadata !{i32 786454, metadata !4, null, metadata !"LLVMTypeRef", i32 85, i64 0, i64 0, i64 0, i32 0, metadata !44} ; [ DW_TAG_typedef ] [LLVMTypeRef] [line 85, size 0, align 0, offset 0] [from ]
!44 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !45} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from LLVMOpaqueType]
!45 = metadata !{i32 786451, metadata !4, null, metadata !"LLVMOpaqueType", i32 85, i64 0, i64 0, i32 0, i32 4, null, null, i32 0, null, null, null} ; [ DW_TAG_structure_type ] [LLVMOpaqueType] [line 85, size 0, align 0, offset 0] [decl] [from ]
!46 = metadata !{metadata !47}
!47 = metadata !{i32 786465, i64 0, i64 1}        ; [ DW_TAG_subrange_type ] [0, 0]
!48 = metadata !{i32 786688, metadata !18, metadata !"mainFnReturnType", metadata !19, i32 11, metadata !43, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [mainFnReturnType] [line 11]
!49 = metadata !{i32 786688, metadata !18, metadata !"mainFn", metadata !19, i32 12, metadata !50, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [mainFn] [line 12]
!50 = metadata !{i32 786454, metadata !4, null, metadata !"LLVMValueRef", i32 92, i64 0, i64 0, i64 0, i32 0, metadata !51} ; [ DW_TAG_typedef ] [LLVMValueRef] [line 92, size 0, align 0, offset 0] [from ]
!51 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !52} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from LLVMOpaqueValue]
!52 = metadata !{i32 786451, metadata !4, null, metadata !"LLVMOpaqueValue", i32 92, i64 0, i64 0, i32 0, i32 4, null, null, i32 0, null, null, null} ; [ DW_TAG_structure_type ] [LLVMOpaqueValue] [line 92, size 0, align 0, offset 0] [decl] [from ]
!53 = metadata !{i32 786688, metadata !18, metadata !"entryblock", metadata !19, i32 14, metadata !54, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [entryblock] [line 14]
!54 = metadata !{i32 786454, metadata !4, null, metadata !"LLVMBasicBlockRef", i32 99, i64 0, i64 0, i64 0, i32 0, metadata !55} ; [ DW_TAG_typedef ] [LLVMBasicBlockRef] [line 99, size 0, align 0, offset 0] [from ]
!55 = metadata !{i32 786447, null, null, metadata !"", i32 0, i64 64, i64 64, i64 0, i32 0, metadata !56} ; [ DW_TAG_pointer_type ] [line 0, size 64, align 64, offset 0] [from LLVMOpaqueBasicBlock]
!56 = metadata !{i32 786451, metadata !4, null, metadata !"LLVMOpaqueBasicBlock", i32 99, i64 0, i64 0, i32 0, i32 4, null, null, i32 0, null, null, null} ; [ DW_TAG_structure_type ] [LLVMOpaqueBasicBlock] [line 99, size 0, align 0, offset 0] [decl] [from ]
!57 = metadata !{i32 786688, metadata !18, metadata !"predicateblock", metadata !19, i32 15, metadata !54, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [predicateblock] [line 15]
!58 = metadata !{i32 786688, metadata !18, metadata !"thenblock", metadata !19, i32 16, metadata !54, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [thenblock] [line 16]
!59 = metadata !{i32 786688, metadata !18, metadata !"elseblock", metadata !19, i32 17, metadata !54, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [elseblock] [line 17]
!60 = metadata !{i32 786688, metadata !18, metadata !"mergeblock", metadata !19, i32 18, metadata !54, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [mergeblock] [line 18]
!61 = metadata !{i32 786688, metadata !18, metadata !"xpVar", metadata !19, i32 21, metadata !50, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [xpVar] [line 21]
!62 = metadata !{i32 786688, metadata !18, metadata !"cmpVal", metadata !19, i32 25, metadata !50, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [cmpVal] [line 25]
!63 = metadata !{i32 786688, metadata !18, metadata !"xVar", metadata !19, i32 37, metadata !50, i32 0, i32 0} ; [ DW_TAG_auto_variable ] [xVar] [line 37]
!64 = metadata !{i32 2, metadata !"Dwarf Version", i32 4}
!65 = metadata !{i32 2, metadata !"Debug Info Version", i32 1}
!66 = metadata !{metadata !"Debian clang version 3.5.0-10 (tags/RELEASE_350/final) (based on LLVM 3.5.0)"}
!67 = metadata !{i32 4, i32 15, metadata !18, null}
!68 = metadata !{i32 4, i32 27, metadata !18, null}
!69 = metadata !{i32 6, i32 27, metadata !18, null}
!70 = metadata !{i32 6, i32 17, metadata !18, null}
!71 = metadata !{i32 7, i32 25, metadata !18, null}
!72 = metadata !{i32 7, i32 16, metadata !18, null}
!73 = metadata !{i32 8, i32 27, metadata !18, null} ; [ DW_TAG_imported_declaration ]
!74 = metadata !{i32 8, i32 17, metadata !18, null} ; [ DW_TAG_imported_declaration ]
!75 = metadata !{i32 10, i32 14, metadata !18, null}
!76 = metadata !{i32 10, i32 2, metadata !18, null}
!77 = metadata !{i32 10, i32 37, metadata !18, null}
!78 = metadata !{metadata !79, metadata !79, i64 0}
!79 = metadata !{metadata !"any pointer", metadata !80, i64 0}
!80 = metadata !{metadata !"omnipotent char", metadata !81, i64 0}
!81 = metadata !{metadata !"Simple C/C++ TBAA"}
!82 = metadata !{i32 11, i32 33, metadata !18, null}
!83 = metadata !{i32 11, i32 14, metadata !18, null}
!84 = metadata !{i32 12, i32 57, metadata !18, null}
!85 = metadata !{i32 12, i32 24, metadata !18, null}
!86 = metadata !{i32 12, i32 15, metadata !18, null}
!87 = metadata !{i32 14, i32 33, metadata !18, null}
!88 = metadata !{i32 14, i32 20, metadata !18, null}
!89 = metadata !{i32 15, i32 37, metadata !18, null}
!90 = metadata !{i32 15, i32 20, metadata !18, null}
!91 = metadata !{i32 16, i32 32, metadata !18, null}
!92 = metadata !{i32 16, i32 20, metadata !18, null}
!93 = metadata !{i32 17, i32 32, metadata !18, null}
!94 = metadata !{i32 17, i32 20, metadata !18, null}
!95 = metadata !{i32 18, i32 33, metadata !18, null}
!96 = metadata !{i32 18, i32 20, metadata !18, null}
!97 = metadata !{i32 20, i32 2, metadata !18, null}
!98 = metadata !{i32 21, i32 49, metadata !18, null}
!99 = metadata !{i32 21, i32 23, metadata !18, null}
!100 = metadata !{i32 21, i32 15, metadata !18, null}
!101 = metadata !{i32 22, i32 2, metadata !18, null}
!102 = metadata !{i32 24, i32 2, metadata !18, null}
!103 = metadata !{i32 25, i32 59, metadata !18, null}
!104 = metadata !{i32 25, i32 100, metadata !18, null}
!105 = metadata !{i32 25, i32 86, metadata !18, null}
!106 = metadata !{i32 25, i32 24, metadata !18, null}
!107 = metadata !{i32 25, i32 15, metadata !18, null}
!108 = metadata !{i32 26, i32 2, metadata !18, null}
!109 = metadata !{i32 28, i32 2, metadata !18, null}
!110 = metadata !{i32 29, i32 41, metadata !18, null}
!111 = metadata !{i32 29, i32 27, metadata !18, null}
!112 = metadata !{i32 29, i32 2, metadata !18, null}
!113 = metadata !{i32 30, i32 2, metadata !18, null}
!114 = metadata !{i32 32, i32 2, metadata !18, null}
!115 = metadata !{i32 33, i32 41, metadata !18, null}
!116 = metadata !{i32 33, i32 27, metadata !18, null}
!117 = metadata !{i32 33, i32 2, metadata !18, null}
!118 = metadata !{i32 34, i32 2, metadata !18, null}
!119 = metadata !{i32 36, i32 2, metadata !18, null}
!120 = metadata !{i32 37, i32 22, metadata !18, null}
!121 = metadata !{i32 37, i32 15, metadata !18, null}
!122 = metadata !{i32 38, i32 2, metadata !18, null}
!123 = metadata !{i32 40, i32 2, metadata !18, null}
!124 = metadata !{i32 41, i32 1, metadata !18, null}
