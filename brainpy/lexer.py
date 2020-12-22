# ><+-.,[]

class Lexer:
    KNOWN_TOKENS = {
                        '>' : 'POINTER',
                        '<' : 'POINTER',
                        '+' : 'OP',
                        '-' : 'OP',
                        '.' : 'OI',
                        ',' : 'OI',
                        '[' : 'LOOP',
                        ']' : 'LOOP'
                   }

    @staticmethod
    def find_tokens(file):
        file   = open(file)
        tokens = []

        # Go through each line
        for line in file:

            # Go through each char
            for char in line:
                # Detect a true comment.
                # A true comment is different from normal comments.
                # A true comment will skip an entire line,
                # Wheras a normal comment might still have a token in it later on
                # EXAMPLE: >+ comment: this + 2 numbers
                # brain.py would still detect that second + unless there was a #
                if char == '#':
                    break

                # Every char that isn't part of KNOWN_TOKENS is considered a comment.
                if char in Lexer.KNOWN_TOKENS:
                    tokens.append([char, Lexer.KNOWN_TOKENS[char]])

        return tokens
