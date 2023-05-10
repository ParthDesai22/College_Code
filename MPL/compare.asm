%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

%macro end 0
mov rax,60
mov rdi,0
syscall
%endmacro

section .data

array db 11h,59h,23h,66h,89h

space db "  "

msg1 db "PROGRAM TO FIND GREATEST NUMBER IN THE ARRAY",10
msglen1 equ $-msg1

msg2 db "The Greatest Number In The Array Is",10
msglen2 equ $-msg1

msg3 db "The Array Contain The Following Values",10
msglen3 equ $-msg3

section .bss
counter resb 1
result resb 4 

section .text
global _start:
_start:

print msg1,msglen1

print msg2,msglen2

mov byte[counter],05
mov rsi,array

next:
mov al,[rsi]
push rsi
call disp
print space,1
pop rsi
inc rsi
dec byte[counter]
jnz next

mov byte[counter],05
mov rsi,array
mov al,0

repeat:
cmp al,[rsi]
jg skip
mov al,[rsi]
skip:
inc rsi
dec byte[counter]
jnz repeat

call disp

disp:
mov rdi,result
mov rcx,02
up1:
rol al,4
mov dl,al
and dl,0fh
add dl,30h
cmp dl,39h
jbe display2
add dl,07h

display2:
mov [rdi],dl
inc rdi
loop up1
print result,4
ret

end