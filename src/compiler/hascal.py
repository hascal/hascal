# ---------------------------------------------
# | Hascal Compiler v1.2 - The Cross Compiler |
# ---------------------------------------------

#from sys import argv
from lexer import Lexer
from h_parser import Parser




# Main 
if __name__ == '__main__':
    print("Hascal Compiler v1.2 --- REPL")
    print("Type \"help\" for more information")
    lexer = Lexer()
    parser = Parser()
    while True:
        try:
            text = input('Hascal >>> ')
        except EOFError:
            break
        if text == "build":
            print("Compiling...")
            file = open("compiled.c","w")
            file.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)
            file.close()
            print("Compiled succesfully!")
            continue
        if text == "about":
            print("Hascal Development Team\nHascal Official Website : https://hascal.github.io")
            continue
        if text == "help":
            print("build : compile your hascal code")
            print("about : show about inforamation")
            continue
        if text:
            x = lexer.tokenize(text)
            parser.parse(x)

