from core.sly import Lexer


class Lexer(Lexer):
    tokens = {
        NAME,
        FOR,
        WHILE,
        TO,
        DOWNTO,
        IF,
        ELSE,  #ELIF,
        RETURN,
        AS,
        PRINT,
        INTVAR,
        STRINGVAR,
        FLOATVAR,
        CHARVAR,
        BOOLVAR,
        CONST,
        VAR,
        LOCAL,
        GREATER,
        LESS,
        EQEQ,
        NOTEQ,
        GREATEREQ,
        ARROW,
        LESSEQ,
        PLUS,
        TIMES,
        MINUS,
        DIVIDE,
        DOT,
        ALFA,
        ASSIGN,
        PASS,
        COMMA,
        LPAREN,
        RPAREN,
        DOTDOT,
        #FLOAT,
        SEM,
        STRING,
        NUMBER,
        CHAR,
        USE,
        FUNCTION,
        LBRACE,
        RBRACE,
        TRUE,
        FALSE,
        STRUCT,
        ENUM,
        AND,
        OR,
        NEW,
        NOT,
        ANDCHAR,
        #IN,
        LBC,
        RBC,
        ARRAY,
        EXT,
        BREAK,
        CONTINUE,
        PUTS,
        PTR
    }
    ignore = ' \t'
    ignore_comment_slash = r'#.*'

    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    #FLOAT = r'\d+\.\d+'
    # Special symbols
    DOTDOT = r':'
    PLUS = r'\+'
    EQEQ = r'=='
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    SEM = r';'
    COMMA = r','
    NOTEQ = r'!='
    LESSEQ = r'<='
    GREATEREQ = r'>='
    LESS = r'<'
    GREATER = r'>'
    DOT = r'\.'
    LBRACE = r'\['
    RBRACE = r'\]'
    NOT = r'\!'
    LBC = r'\{'
    RBC = r'\}'
    ALFA = r'~'
    ANDCHAR = r'&'
    NAME["use"] = USE
    NAME["function"] = FUNCTION
    NAME["int"] = INTVAR
    NAME["string"] = STRINGVAR
    NAME["char"] = CHARVAR
    NAME["bool"] = BOOLVAR
    NAME["float"] = FLOATVAR
    NAME["var"] = VAR
    NAME["print"] = PRINT
    NAME["puts"] = PUTS
    NAME["ptr"] = PTR
    NAME["if"] = IF
    #NAME["elif"] = ELIF
    NAME["else"] = ELSE
    NAME["return"] = RETURN
    NAME["as"] = AS
    NAME["for"] = FOR
    NAME["downto"] = DOWNTO
    NAME["to"] = TO
    NAME["while"] = WHILE
    NAME["true"] = TRUE
    NAME["false"] = FALSE
    NAME["const"] = CONST
    NAME["struct"] = STRUCT
    NAME["and"] = AND
    NAME["or"] = OR
    NAME["new"] = NEW
    NAME["local"] = LOCAL
    #NAME["in"] = IN
    NAME["array"] = ARRAY
    NAME["enum"] = ENUM
    NAME["ext"] = EXT
    NAME["break"] = BREAK
    NAME["continue"] = CONTINUE
    NAME["pass"] = PASS
    # Ignored pattern
    ignore_newline = r'\n'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

    @_(r'\".*?(?<!\\)(\\\\)*\"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        #t.value = t.value.replace(r"\\", "\\")
        #t.value = t.value.replace(r"\"", "\"")
        return t

    @_(r'\'.*?(?<!\\)(\\\\)*\'')
    def CHAR(self, t):
        t.value = t.value[1:-1]
        return t
