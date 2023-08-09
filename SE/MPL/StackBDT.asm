%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .data

msg db 10,"ALP to perform BDT without using string related instruction",10
msglen equ $-msg

msg1 db 10,"Source Block Contain Before Transfer ",10
msglen1 equ $-msg1

msg2 db 10,"Destination Block Contain After transfer ",10
msglen2 equ $-msg2

space db " "
sl equ $-space

cnt equ 5

scrblk db 10h,20h,30h,40h,50h
dstblk db 00,00,00,00,00

section .bss
ans resb 2

section .text

global _start:
_start:

print msg,msglen
print msg1,msglen1

mov rsi,scrblk
call display

print msg2,msglen2
mov rsi,scrblk
mov rdi,dstblk
mov rcx,05

cld 
rep movsb

mov rsi,dstblk
call display

exit:
mov rax,60
mov rdi,0
syscall

display:
mov rbp,cnt
up:
mov al,[rsi]
push rsi
call display1
print space,1
pop rsi
inc rsi
dec rbp
jnz up
ret

display1:
mov rdi,ans
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
print ans,2
ret



