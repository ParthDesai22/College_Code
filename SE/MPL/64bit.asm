;write a program to accept 5 64 bit hexadecimal numbers from user and store them in an array and display the accepted number
%macro IO 4
mov rax,%1
mov rdi,%2
mov rsi,%3
add rsi,rbx
mov rdx,%4
syscall
%endmacro

%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro


section .data
msg1 db "Please Enter Five Number Of 64 Bits",10
len1 equ $-msg1
msg2 db"Entered Number Are: ",10
len2 equ $-msg2

count db 05

section .bss
array resb 9

section .text

global _start:
_start:
mov rbx,00 
print msg1,len1

up:
IO 0,0,array,17
;mov rax,00
;mov rdi,00
;mov rsi,array
;mov rdx,17
;syscall

add rbx,17
dec byte[count]
jnz up

mov byte[count],05
mov rbx,00
print msg2,len2

up1:
IO 1,1,array,17
;mov rax,1
;mov rdi,1
;mov rsi,array
;mov rdx,17
;syscall

add rbx,17
dec byte[count]
jnz up1

exit:
mov rax,60
mov rdi,00
syscall
