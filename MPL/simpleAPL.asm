section .data 

msg db 10, "My Name Is Parth"
msglen equ $-msg

msg1 db 9, "I Study In MESCOE Pune",9
msglen1 equ $-msg1

msg2 db 9, "Welcome To My ASM Program",10
msglen2 equ $-msg2

%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .bss


section .txt

global _start:
_start:

mov rax,1
mov rdi,1
mov rsi,msg
mov rdx,msglen
syscall

print msg1,msglen1
print msg2,msglen2

mov rax,60
syscall


