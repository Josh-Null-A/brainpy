class Interpreter:
    # Create a memory variable of 255 bits and a memory pointer.
    memory  = [0]*1000
    pointer = 0

    @staticmethod
    def interpret(tokens):
        i = 0

        # Go through each token type
        while i < len(tokens):

            # Check for pointer movements.
            if tokens[i][1] == 'POINTER':
                if tokens[i][0] == '>':
                    Interpreter.pointer += 1
                else:
                    Interpreter.pointer -= 1

            # Check for operations.
            elif tokens[i][1] == 'OP':
                if tokens[i][0] == '+':
                    Interpreter.memory[Interpreter.pointer] += 1
                else:
                    Interpreter.memory[Interpreter.pointer] -= 1

            # Check for input/output.
            elif tokens[i][1] == 'OI':
                if tokens[i][0] == '.':
                    print(chr(Interpreter.memory[Interpreter.pointer]), end='')
                else:
                    Interpreter.memory[Interpreter.pointer] = ord(input())

            # Check for loops.
            elif tokens[i][1] == 'LOOP':
                if tokens[i][0] == '[':
                    # If loop is valid then find the correct open brace and continue.
                    if Interpreter.memory[Interpreter.pointer] == 0:
                        # temp_count is used to track the number of loops encountered.
                        temp_count = 0
                        while True:
                            i += 1
                            if tokens[i][0] == '[':
                                temp_count += 1
                            elif tokens[i][0] == ']' and temp_count > 0:
                                temp_count -= 1
                            elif tokens[i][0] == ']' and temp_count == 0:
                                i -= 1
                                break

                else:
                    # If loop is invalid then find the correct closing brace and continue.
                    if Interpreter.memory[Interpreter.pointer] != 0:
                        # temp_count is used to track the number of loops encountered.
                        temp_count = 0
                        while True:
                            i -= 1
                            if tokens[i][0] == ']':
                                temp_count += 1
                            elif tokens[i][0] == '[' and temp_count > 0:
                                temp_count -= 1
                            elif tokens[i][0] == '[' and temp_count == 0:
                                i -= 1
                                break

            i += 1
