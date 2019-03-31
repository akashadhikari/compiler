## Developing a compiler for a mini-language

Compiler design philosophy is primarily  based on language translation and optimization. The mini-languages like Decaf and C0 could come handy while developing a try-out compiler. The selection of these languages are self-explanatory. However, we'll discuss the key features of these languages for compiler developement scenario.


### The Decaf Language
According to the official documentation Decaf  is  a  "strongly-typed,  object-oriented  language  with  support  for  inheritance  and  encapsulation". One of the key features of language's usability boils down to the approach of Class-Object based architecture which Decaf seems to handle pretty well. Syntactically, Decaf uses 22 reserved keywords. On top of that, Decaf is a case sensitive language which means "isobject" and "isObject" are two distinct identifiers. Identifiers themselves can only be 31 characters long. Talking about the program structure, Decaf uses a sequence of deceleration where each of it establishes a function, variable, interface or a class. It supports several levels of scoping where the top-level is placed in the global scope.  Decaf supports data structures like Arrays in a very convenient way. Function declaration includes function name and its associated `typesignature`, which includes the return type as well as number and types of formal parameters.
Therefore, looking at all the inevitable features like OOP, Inheritance, convenient function, etc, Decaf seems to be an appropriate choice for compiler design environment.


### C0 Language
The C0 Language is primarily the subset of C programming language aimed at getting started with imperative programming and introductory algorithms. The C0 Language supports various types such as `int`, `bool`, `char`, `string`, `struct`, etc. Similarly, some command types supported by C0 are basic assignments, conditionals (`if` and `else`), loops (`while` and `for`), blocks, returns, assertion, etc. Arrays, pointers and structs are equally well supported by the language. Functions, on the other hand, are not first-class, but can only be defined at the top-level of a file. A function definition has the form  
`t g (t1 x1, ..., tn xn) { body }`. 
Just like the Decaf Language, C0 is only one of the mini-languages that could be used to develop a try-out compiler as it supports all kind of environments, data structures, syntax and program structures.