.intel_syntax noprefix

.globl _start
_start:
    mov r8, 1
    inc r8
    add r8, 25
    add r8, r8
    imul r8, 10
    # Ignore below, padding + cleaning up with exit(0) sycall
    nop
    nop
    nop
    nop
    mov rax, 60
    xor rdi, rdi
    syscall