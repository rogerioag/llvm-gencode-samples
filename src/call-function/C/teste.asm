	.text
	.abicalls
	.section	.mdebug.abi32,"",@progbits
	.nan	legacy
	.file	"meu_modulo.bc"
	.text
	.globl	soma
	.align	2
	.type	soma,@function
	.set	nomicromips
	.set	nomips16
	.ent	soma
soma:                                   # @soma
	.cfi_startproc
	.frame	$sp,0,$ra
	.mask 	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	.set	noat
# BB#0:                                 # %entry
	addu	$3, $5, $7
	sltu	$1, $3, $7
	addu	$1, $1, $6
	jr	$ra
	addu	$2, $4, $1
	.set	at
	.set	macro
	.set	reorder
	.end	soma
$tmp0:
	.size	soma, ($tmp0)-soma
	.cfi_endproc

	.globl	main
	.align	2
	.type	main,@function
	.set	nomicromips
	.set	nomips16
	.ent	main
main:                                   # @main
	.cfi_startproc
	.frame	$sp,48,$ra
	.mask 	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	.set	noat
# BB#0:                                 # %entry
	lui	$2, %hi(_gp_disp)
	addiu	$2, $2, %lo(_gp_disp)
	addiu	$sp, $sp, -48
$tmp1:
	.cfi_def_cfa_offset 48
	sw	$ra, 44($sp)            # 4-byte Folded Spill
$tmp2:
	.cfi_offset 31, -4
	addu	$gp, $2, $25
	sw	$zero, 36($sp)
	sw	$zero, 32($sp)
	addiu	$1, $zero, 1
	sw	$1, 28($sp)
	sw	$zero, 24($sp)
	addiu	$1, $zero, 2
	sw	$1, 20($sp)
	sw	$zero, 16($sp)
	lw	$5, 28($sp)
	lw	$4, 24($sp)
	lw	$25, %call16(soma)($gp)
	addiu	$6, $zero, 0
	jalr	$25
	addiu	$7, $zero, 2
	sw	$3, 36($sp)
	sw	$2, 32($sp)
	lw	$2, 32($sp)
	lw	$3, 36($sp)
	lw	$ra, 44($sp)            # 4-byte Folded Reload
	jr	$ra
	addiu	$sp, $sp, 48
	.set	at
	.set	macro
	.set	reorder
	.end	main
$tmp3:
	.size	main, ($tmp3)-main
	.cfi_endproc


