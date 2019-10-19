These are notes for the reversing and pwning intro.

Note that reversing in this context means understanding (mainly) x86(_64) binaries.

## Useful Programs

#### Debugging
* gdb
* gef
* valgrind

#### Reading binaries
* radare2/Cutter
* ghidra
* objdump

#### Libraries
* angr
* pwntools
* claripy

#### Misc
* file
* checksec
* pwntools
* hexedit/bless/...

## Topics

### General
* x86/x86_64
* C structures
* OS structures

### Reversing
* Stack strings
* Dynamic string generation
* Constrained string testing
* Anti-debug patterns
* Dynamic code generation/polymorphic code

### Pwning
* Buffer Overflows
* Stack cookies
* ASLR
* Ret2Libc
* ROP
* format string
* Heap overflows

## Examples
There will be examples provided with exploit for:
* Buffer overflow with `win` function
* Buffer overflow with `win` function and Cookies
* Buffer overflow with `win` function and ASLR
* Buffer overflow without `win` function and ASLR