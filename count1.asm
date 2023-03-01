section .data

msg1 db 9,"Counting Positive And Negative Element Of An Array"
msglen1 equ $-msg1
msg2 db 10, "Positive Numbers Are : "
msglen2 equ $-msg2
msg3 db 10, "Negative Numbers Are : "
msglen3 equ $-msg3

array db 12h,90h,87h,88h,8ah,0ah,02h
pcnt db 0
ncnt db 0
newline db 10

%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .bss

dispbuff resb 2

section .txt

global _start:
_start: 

print msg1,msglen1
print newline,1

mov rsi,array
mov rcx,07

again:
bt qword[rsi],07

;bt stand for bit test

jnc pnxt

;pnxt is a label

inc byte[ncnt]
jmp pskip
pnxt: inc byte[pcnt]
pskip: inc rsi
loop again
print msg2,msglen2
mov bl,[pcnt]

;bl is a bit register which can store 2 digit

call disp_result

;call is privilage instruction
print newline,1

print msg3,msglen3
mov bl,[ncnt]
call disp_result
print newline,1

mov rax,60
mov rdi,0
syscall

disp_result:
mov rdi,dispbuff
mov rcx,02
dispup:
rol bl,4

;rol is Rotate To Left

mov dl,bl
and dl,0fh
add dl,30h
cmp dl,39h

;cmp is compare

jbe dispskip

;jbe is Jump when Below or Equal

add dl,07h
dispskip: 
mov [rdi],dl
inc rdi
loop dispup
print dispbuff,2
ret 


;while storing elements in array we declare the type of data with element ex: 11h,12d
;h=Hexa decimal
;d=Decimal
;o=Octal

;rsi is source index register
;rcx is a counter register

