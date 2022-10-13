program = """[ This program prints "Hello World!" and a newline to the screen, its
  length is 106 active command characters. [It is not the shortest.]

  This loop is an "initial comment loop", a simple way of adding a comment
  to a BF program such that you don't have to worry about any command
  characters. Any ".", ",", "+", "-", "<" and ">" characters are simply
  ignored, the "[" and "]" characters just have to be balanced. This
  loop and the commands it contains are ignored because the current cell
  defaults to a value of 0; the 0 value causes this loop to be skipped.
]
++++++++               Set Cell #0 to 8
[
    >++++               Add 4 to Cell #1; this will always set Cell #1 to 4
    [                   as the cell will be cleared by the loop
        >++             Add 2 to Cell #2
        >+++            Add 3 to Cell #3
        >+++            Add 3 to Cell #4
        >+              Add 1 to Cell #5
        <<<<-           Decrement the loop counter in Cell #1
    ]                   Loop until Cell #1 is zero; number of iterations is 4
    >+                  Add 1 to Cell #2
    >+                  Add 1 to Cell #3
    >-                  Subtract 1 from Cell #4
    >>+                 Add 1 to Cell #6
    [<]                 Move back to the first zero cell you find; this will
                        be Cell #1 which was cleared by the previous loop
    <-                  Decrement the loop Counter in Cell #0
]                       Loop until Cell #0 is zero; number of iterations is 8

The result of this is:
Cell no :   0   1   2   3   4   5   6
Contents:   0   0  72 104  88  32   8
Pointer :   ^

>>.                     Cell #2 has value 72 which is 'H'
>---.                   Subtract 3 from Cell #3 to get 101 which is 'e'
+++++++..+++.           Likewise for 'llo' from Cell #3
>>.                     Cell #5 is 32 for the space
<-.                     Subtract 1 from Cell #4 for 87 to give a 'W'
<.                      Cell #3 was set to 'o' from the end of 'Hello'
+++.------.--------.    Cell #3 for 'rl' and 'd'
>>+.                    Add 1 to Cell #5 gives us an exclamation point
>++.                    And finally a newline from Cell #6"""

instruction_pointer = 0
data_pointer = 0
left_bracket_stack = []
data = [0] * 30000


def find_right_bracket(left_bracket_index, prog):
    depth = 0
    for i in range(left_bracket_index + 1, len(prog)):
        if prog[i] == "[":
            depth += 1
        elif prog[i] == "]":
            if depth == 0:
                return i
            else:
                depth -= 1
    raise Exception("missing closing bracket")


while instruction_pointer < len(program):
    instruction = program[instruction_pointer]
    value = data[data_pointer]

    if instruction == ">":
        data_pointer += 1
        instruction_pointer += 1
    elif instruction == "<":
        data_pointer -= 1
        instruction_pointer += 1
    elif instruction == "+":
        data[data_pointer] += 1
        instruction_pointer += 1
    elif instruction == "-":
        data[data_pointer] -= 1
        instruction_pointer += 1
    elif instruction == ".":
        print(chr(data[data_pointer]), end="")
        instruction_pointer += 1
    elif instruction == ",":
        raise NotImplementedError()
    elif instruction == "[":
        if data[data_pointer] == 0:
            # skip over loop
            instruction_pointer = find_right_bracket(instruction_pointer, program) + 1
            assert instruction_pointer >= 0
        else:
            # enter loop
            left_bracket_stack.append(instruction_pointer)
            instruction_pointer += 1
    elif instruction == "]":
        if data[data_pointer] != 0:
            # continue loop
            instruction_pointer = left_bracket_stack[-1] + 1
        else:
            # exit loop
            left_bracket_stack.pop()
            instruction_pointer += 1
    else:
        instruction_pointer += 1
