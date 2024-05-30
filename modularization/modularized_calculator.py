#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    return number, index


def read_module(line, index):
    module = ""
    while index < len(line) and line[index].isalpha():
        module += line[index]
        index += 1
    return module, index


def evaluate_parentheses(stack, index):
    #括弧の中を計算する
    temp_stack = [] #一時的なstack
    temp_index = len(stack)-1 #一時的なindex

    while stack[temp_index] != "(":
        temp_stack.insert(0, stack[temp_index])
        stack.pop(-1)
        temp_index -= 1

    stack.pop(-1) # pop "("
    answer_in_parentheses = evaluate_plus_minus(temp_stack)

    #括弧の前に関数が書いてある場合
    if stack[-1] == 'abs':
        stack.pop()
        return abs(answer_in_parentheses)
    elif stack[-1] == 'int':
        stack.pop()
        return int(answer_in_parentheses)
    elif stack[-1] == 'round':
        stack.pop()
        return round(answer_in_parentheses)

    return answer_in_parentheses


def evaluate(line):
    stack = ["+"]  # Insert a dummy '+' operator
    index = 0
    while index < len(line):
        # print(stack,line[index])
        if line[index].isdigit():
            (num, index) = read_number(line, index)
            if stack[-1] in ["*", "/"]:
                operator = stack.pop() # pop a operator
                if operator == "*":
                    stack.append(stack.pop() * num)
                if operator == "/":
                    # print("!!!", stack, line[index-1], num)
                    stack.append(stack.pop() / num)
            else:
                stack.append(num)

        elif line[index].isalpha():
            (module, index) = read_module(line, index)
            stack.append(module)

        elif line[index] == '+':
            stack.append("+")
            index += 1

        elif line[index] == '-':
            stack.append("-")
            index += 1

        elif line[index] == '*':
            stack.append("*")
            index += 1
            
        elif line[index] == '/':
            stack.append("/")
            index += 1
        
        elif line[index] == '(':
            stack.append("(")
            index += 1

        elif line[index] == ')':
            num = evaluate_parentheses(stack, index)
            # print(stack)
            if stack[-1] in ["*", "/"]:
                operator = stack.pop() # pop a operator
                if operator == "*":
                    stack.append(stack.pop() * num)
                if operator == "/":
                    stack.append(stack.pop() / num)
            else:
                stack.append(num)
            # print(stack)
            index += 1

        else:
            print('Invalid character found: ' + line[index])
            exit(1)
    print(stack)
    return stack


def evaluate_plus_minus(stack):
    print(stack)
    answer = stack[0]
    index = 2
    # print(stack, stack[0])
    while index < len(stack):
        if stack[index-1] == '+':
            answer += stack[index]
        elif stack[index-1] == '-':
            answer -= stack[index]
        index += 1
    # print(answer)
    return answer


def test(line):
    evaluate = evaluate(line)
    # print(evaluated)
    actual_answer = evaluate_plus_minus(evaluated)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2") #足し算のみ、整数のみ
    test("2.3+5.4") #足し算のみ、小数のみ
    test("11+2.43") #足し算のみ、整数と小数
    test("2.43+11") #足し算のみ、整数と小数、位置を交換

    test("2-1") #引き算のみ、整数のみ、答えが正の場合
    test("1-2") #引き算のみ、整数のみ、答えが負の場合
    test("5.4-2.3") #引き算のみ、小数のみ、答えが正の場合
    test("2.3-5.4") #引き算のみ、小数のみ、答えが負の場合
    test("11-2.43") #引き算のみ、整数と小数、答えが正の場合
    test("11-12.24") #引き算のみ、整数と小数、答えが負の場合

    test("2*1") #掛け算のみ、整数のみ
    test("5.4*2.3") #掛け算のみ、小数のみ
    test("11*2.43") #掛け算のみ、整数と小数
    test("2.43*11") #掛け算のみ、整数と小数、位置を交換

    test("9/3") #割り算のみ、整数のみ、余りなし
    test("13/2") #割り算のみ、整数のみ、余りあり
    test("6.4/3.2") #割り算のみ、小数のみ、余りなし
    test("4.2/3.2") #割り算のみ、小数のみ、余りあり
    test("9/2.43") #割り算のみ、整数と小数、余りなし
    test("11*2.43") #割り算のみ、整数と小数、余りあり

    test("6+2.1-3") #足し算、引き算
    test("1.0+2.1*3") #足し算、掛け算
    test("1.0+2.1/3") #足し算、割り算
    test("2.1-3*6") #引き算、掛け算
    test("2.1-3/3") #引き算、割り算
    test("6*4/2.6") #掛け算、割り算
    test("1.0+2.1-3*4.2") #足し算、引き算、掛け算
    test("1.0+2.1-3*6/2.9") #足し算、引き算、掛け算、割り算

    test("1.0+2.1-3*8/4/3*5+9.7-0.7+3/3*6") #足し算、引き算、掛け算、割り算、式ロングバージョン
    test("1") #演算子がない場合

    test("(3.0+4*(2-1))/5") #括弧の計算
    test("(3.0+4*(1))/5") #括弧の計算
    test("abs(-2.2)") #モジュールが正常に動くか
    test("int(1.55)") #モジュールが正常に動くか
    test("round(1.55)") #モジュールが正常に動くか
    test("12+abs(int(round(-1.55)+abs(int(-2.3+4))))") #全てのモジュール入り
    print("==== Test finished! ====\n")

run_test()

# while True:
#     print('> ', end="")
#     line = input()
#     tokens = tokenize(line)
#     answer = evaluate(tokens)
#     print("answer = %f\n" % answer)