	.text
	.file	"meu_modulo.bc"
	.globl	main
	.align	16, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	movq	$0, -8(%rsp)
	movq	$10, -16(%rsp)
	movb	$1, %al
	testb	%al, %al
	je	.LBB0_2
# BB#1:                                 # %iftrue
	movq	$1, -8(%rsp)
	movq	-8(%rsp), %rax
	retq
.LBB0_2:                                # %iffalse
	movq	$2, -8(%rsp)
	movq	-8(%rsp), %rax
	retq
.Ltmp0:
	.size	main, .Ltmp0-main
	.cfi_endproc


	.section	".note.GNU-stack","",@progbits
