# Understanding Program Execution in Py
# Program runs line by line, executing instructions in sequence

# Pyhon does not excute src code line-by-line directly.
# instead compile it into an intermediate format called Bytecode, which is then 
# run by virtual machine.

# 1. Complilation Stage: src code to bytecode
    # >> Lexical analysis: break down text based src code into small chunks 
    # called as tokens. 
    # >> Parsing: Tokens are structured into a hierrachial tree callde 
    # Abstract Syntax Tree (AST)
    # >> Bytecode generated
    # >> Caching (__pycache__): .pyc file 
# 2. Interpretation Stage: (Python Virtual Machine)
    # Bytecode is passed to core runtime engine: PVM
# 3. Execution architecture
    # Execution Frames : Stack created for function call
    # Memory & GC: Heap memory. Garbage Collector.
    # GIL: Global Interpretor Lock: only one thread executes bytecode 
    # at a time