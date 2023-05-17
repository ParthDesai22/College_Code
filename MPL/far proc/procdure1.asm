

extern	far_proc1		

global	filehandle, char, buf, abuf_len

%include	"file_macro.asm"


section .data
	nline		db	10
	nline_len	equ	$-nline

	ano		db 	10,10,10,10,"String Operation using Far Procedure"
			
	ano_len	equ	$-ano

	filemsg	db	10,"Enter filename for string operation	: "
	filemsg_len	equ	$-filemsg	
  
	charmsg	db	10,"Enter character to search	: "
	charmsg_len	equ	$-charmsg

	errmsg	db	10,"ERROR in opening File...",10
	errmsg_len	equ	$-errmsg

	exitmsg	db	10,10,"Exit from program...",10,10
	exitmsg_len	equ	$-exitmsg


section .bss
	buf			resb	4096
	buf_len		equ	$-buf		

	filename		resb	50	
	char			resb	2	
 
	filehandle		resq	1
	abuf_len		resq	1		


section .text
	global _start
		
_start:
		print	ano,ano_len		 

		print	filemsg,filemsg_len		
		read 	filename,50
		dec	rax
		mov	byte[filename + rax],0		

		print	charmsg,charmsg_len		
		read 	char,2
		
		fopen	filename			
		cmp	rax,-1H			
		jle	Error
		mov	[filehandle],rax	

		fread	[filehandle],buf, buf_len
		mov	[abuf_len],rax

		call	far_proc1
		jmp	Exit

Error:	print	errmsg, errmsg_len

Exit:		print	exitmsg,exitmsg_len
		exit

