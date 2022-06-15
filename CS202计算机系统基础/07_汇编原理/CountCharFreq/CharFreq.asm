;
; Book example of counting freq of a char in a file;
; frequency between 0 and 9. 
;
.ORIG x3000
AND R2 R2 0	;R2 is the counter.
AND R4 R4 0	;R4 in the end is to test EOF
LEA R3 CHARPTR ;R3 holds the position of pointer to characters. Diff from book sample.
GETC
PUTC
LDR R1 R3 0  ;R1 loads the next char
;
; Test for EOF
;
TESTEOF LDR R4 R3 0	; Test whether R1 was loaded with 0, which means EOF
        BRz OUTPUT
;
; Test for character match
;
NOT R1 R1
ADD R1 R1 1
ADD R1 R1 R0
BRnp GETNEXTCHAR ; If not match, get the next char.
ADD R2 R2 1

GETNEXTCHAR ADD R3 R3 1
            LDR R1 R3 0
            BRnzp TESTEOF

; output the count.
;
OUTPUT LD R0 ASCIIBASE
       ADD R0 R0 R2
       PUTC
       HALT
;
;
ASCIIBASE .FILL 48
CHARPTR .STRINGZ "hello, world!"
.END