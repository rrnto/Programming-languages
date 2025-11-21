bits 32

extern _GetStdHandle@4
extern _WriteConsoleA@20
extern _ExitProcess@4

section .data
    message db 'hello world !', 10

section .bss
    written resd 1

section .text
    global main
    main:
        push -11
        call _GetStdHandle@4

        push 0
        push written
        push 13
        push message
        push eax
        call _WriteConsoleA@20

        push 0
        call _ExitProcess@4

        ; [compilation] 
        ;    nasm -f win32 <code_source>.asm -o <nom>.obj
        ;    golink <nom>.obj /entry main / console kernel32.dll
        
