# ---------------------------------------------
# | Hascal Compiler v1.2 - The Cross Compiler |
# ---------------------------------------------
import os
import sys
from lexer import Lexer
from h_parser import Parser




# Main 
if __name__ == '__main__':
    print("Hascal Compiler v1.2 --- REPL")
    print("Type \"help\" for more information")
    lexer = Lexer()
    parser = Parser()
    if len(sys.argv) < 2:
        while True:
            try:
                text = input('>>> ')
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
      elif sys.argv[1].endswith('.has'):
        if not os.path.exists(sys.argv[1]):
            print("File Not Found")
            sys.exit(1)
        if os.path.isdir(sys.argv[1]):
            print("This is a directory , Not a File")
            sys.exit(1)
        with open(sys.argv[1], encoding="utf-8") as fp:
            line = "# somecomment"
            while line:
                print("Compiling...")
                file = open("compiled.c","w")
                file.write(parser.src_imports +parser.src_before_main+ parser.src_all + parser.src_main + parser.src_end)
                file.close()
                print("Compiled succesfully!")
                line = fp.readline()
                continue
