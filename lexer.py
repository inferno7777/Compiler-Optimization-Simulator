from token_types import Token, TokenType

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def peek(self):
        return self.code[self.pos] if self.pos < len(self.code) else '\0'

    def advance(self):
        char = self.code[self.pos] if self.pos < len(self.code) else '\0'
        self.pos += 1
        # FIX 1: Track line and column correctly on every character consumed
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char

    def skip_whitespace(self):
        # FIX 2: Use advance() so line/column are updated while skipping
        while self.peek().isspace():
            self.advance()

    def read_identifier(self):
        result = ""
        while self.peek().isalnum() or self.peek() == "_":
            result += self.advance()
        return result

    def read_number(self):
        result = ""
        while self.peek().isdigit():
            result += self.advance()
        return result

    def tokenize(self):
        while self.pos < len(self.code):
            self.skip_whitespace()

            # Guard: skip_whitespace may have consumed everything
            if self.pos >= len(self.code):
                break

            char = self.peek()
            col = self.column 

            if char.isdigit():
                num = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, num, self.line, col))
            elif char.isalpha() or char == '_':
                ident = self.read_identifier()
                self.tokens.append(Token(TokenType.IDENTIFIER, ident, self.line, col))
            elif char == '=':
                self.advance()
                self.tokens.append(Token(TokenType.ASSIGNMENT, '=', self.line, col))
            elif char in '+-*/':
                self.tokens.append(Token(TokenType.OPERATOR, self.advance(), self.line, col))
            # FIX 3: Emit tokens for punctuation defined in TokenType
            elif char == '(':
                self.advance()
                self.tokens.append(Token(TokenType.LPAREN, '(', self.line, col))
            elif char == ')':
                self.advance()
                self.tokens.append(Token(TokenType.RPAREN, ')', self.line, col))
            elif char == ',':
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ',', self.line, col))
            elif char == ';':
                self.advance()
                self.tokens.append(Token(TokenType.SEMICOLON, ';', self.line, col))
            else:
                self.advance()  # skip truly unknown characters

        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
