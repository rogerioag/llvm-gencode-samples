	.text
	.file	"out.ll"
	.globl	soma
	.align	16, 0x90
	.type	soma,@function
soma:                                   # @soma
	.cfi_startproc
# BB#0:                                 # %entry
	addq	%rsi, %rdi
	movq	%rdi, %rax
	retq
.Ltmp0:
	.size	soma, .Ltmp0-soma
	.cfi_endproc

	.globl	main
	.align	16, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	subq	$24, %rsp
.Ltmp1:
	.cfi_def_cfa_offset 32
	movq	$0, 16(%rsp)
	movq	$1, 8(%rsp)
	movq	$2, (%rsp)
	movq	8(%rsp), %rdi
	movl	$2, %esi
	callq	soma
	movq	%rax, 16(%rsp)
	movq	16(%rsp), %rax
	addq	$24, %rsp
	retq
.Ltmp2:
	.size	main, .Ltmp2-main
	.cfi_endproc


	.section	".note.GNU-stack","",@progbits
