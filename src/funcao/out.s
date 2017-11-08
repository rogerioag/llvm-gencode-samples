	.text
	.file	"meu_modulo"
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	movq	$0, -8(%rsp)
	movq	$1, -16(%rsp)
	movq	$2, -24(%rsp)
	movq	$0, -32(%rsp)
	movq	-16(%rsp), %rax
	addq	-24(%rsp), %rax
	movq	%rax, -32(%rsp)
	movq	-8(%rsp), %rax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function

	.section	".note.GNU-stack","",@progbits
