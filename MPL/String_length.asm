%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

%macro read 2
mov rax,0
mov rdi,0
mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .data

m1 db 10,"To Find The Length Of The Entered String",10
ml1 equ $-m1
m2 db 10,"Enter The String",10
ml2 equ $-m2
m3 db 10,"Entered String Is: ",10
ml3 equ $-m3
m4 db 10,"Length Of Yhe Entered String Is : ",10
ml4 equ $-m4

section .bss

string resb 50
buffer equ $-string
count resb 1
dispnum resb 16

section .text

global _start:
_start:

input:
print m1,ml1
print m2,ml2
read string,buffer
mov [count],rax
print m3,ml3
print string,[count]
call display
;call display1

exit:
mov rax,60
mov rbx,0
syscall

display:      
mov rsi,dispnum+15          
mov rax,[count]             
mov rcx,16                   
dec rax                     
UP1:                                
mov rdx,0                   
mov rbx,10                  
div rbx                    
add dl,30h                  
mov [rsi],dl                 
dec rsi                     
loop UP1                    
print m4,ml4            
print dispnum+14,2        
ret

;display1:
;mov rdi,dispnum
;mov rcx,02
;dispup:
;rol al,04
;mov dl,al
;and dl,0fh
;add dl,30h
;cmp dl,39h
;add dl,07h
;dispskip: 
;mov [rdi],dl
;inc rdi
;loop dispup
;print dispnum,2
;ret 




