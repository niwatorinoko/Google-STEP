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
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_times(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1


def read_divided(line, index):
    token = {'type': 'DIVIDED'}
    return token, index + 1


def read_left_parenthesis(line, index):
    token = {'type': 'LEFT_PARENTHESIS'}
    return token, index + 1


def read_module(line, index):
    module = ""
    while index < len(line) and line[index].isalpha():
        module += line[index]
        index += 1
    token = {'type': 'MODULE', 'module': module}
    return token, index


def evaluate_parentheses(tokens, index):
    #括弧の中を計算する
    temp_tokens = []
    temp_index = len(tokens)-1
    while tokens[temp_index] != {'type': 'LEFT_PARENTHESIS'}:
        temp_tokens.insert(0, tokens[temp_index])
        tokens.pop(-1)
        temp_index -= 1
    tokens.pop(-1)
    evaluated_tokens = first_evaluate(temp_tokens)
    answer_in_parentheses = second_evaluate(evaluated_tokens)
    #括弧の前に関数が書いてある場合
    if len(tokens) > 0 and tokens[-1]['type'] == 'MODULE':
        module = tokens.pop(-1)
        if module['module'] == 'abs':
            answer_in_parentheses = abs(answer_in_parentheses)
        elif module['module'] == 'int':
            answer_in_parentheses = int(answer_in_parentheses)
        elif module['module'] == 'round':
            answer_in_parentheses = round(answer_in_parentheses)
    token = {'type': 'NUMBER', 'number': answer_in_parentheses}
    return tokens, token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)

        elif line[index] == '+':
            (token, index) = read_plus(line, index)

        elif line[index] == '-':
            (token, index) = read_minus(line, index)

        elif line[index] == '*':
            (token, index) = read_times(line, index)
            
        elif line[index] == '/':
            (token, index) = read_divided(line, index)
        
        elif line[index] == '(':
            (token, index) = read_left_parenthesis(line, index)

        elif line[index] == ')':
            (tokens, token, index) = evaluate_parentheses(tokens, index)
        
        elif line[index].isalpha():
            (token, index) = read_module(line, index)

        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def first_evaluate(tokens):
    evaluated_tokens = []
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        #print(tokens)
        if tokens[index]['type'] == 'NUMBER':

            if tokens[index - 1]['type'] == 'PLUS':
                evaluated_tokens.append(tokens[index-1])
                evaluated_tokens.append(tokens[index])

            elif tokens[index - 1]['type'] == 'MINUS':
                evaluated_tokens.append(tokens[index-1])
                evaluated_tokens.append(tokens[index])

            elif tokens[index - 1]['type'] == 'TIMES':
                num = evaluated_tokens.pop(-1)
                answer = num['number'] * tokens[index]['number']
                evaluated_tokens.append({'type': 'NUMBER', 'number': answer})

            elif tokens[index - 1]['type'] == 'DIVIDED':
                num = evaluated_tokens.pop(-1)
                answer = num['number'] / tokens[index]['number']
                evaluated_tokens.append({'type': 'NUMBER', 'number': answer})

            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return evaluated_tokens

def second_evaluate(tokens):
    answer = 0
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer


def test(line):
    tokens = tokenize(line)
    evaluated_tokens = first_evaluate(tokens)
    actual_answer = second_evaluate(evaluated_tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    # test("1+2") #足し算のみ、整数のみ
    # test("2.3+5.4") #足し算のみ、小数のみ
    # test("11+2.43") #足し算のみ、整数と小数
    # test("2.43+11") #足し算のみ、整数と小数、位置を交換

    # test("2-1") #引き算のみ、整数のみ、答えが正の場合
    # test("1-2") #引き算のみ、整数のみ、答えが負の場合
    # test("5.4-2.3") #引き算のみ、小数のみ、答えが正の場合
    # test("2.3-5.4") #引き算のみ、小数のみ、答えが負の場合
    # test("11-2.43") #引き算のみ、整数と小数、答えが正の場合
    # test("11-12.24") #引き算のみ、整数と小数、答えが負の場合

    # test("2*1") #掛け算のみ、整数のみ
    # test("5.4*2.3") #掛け算のみ、小数のみ
    # test("11*2.43") #掛け算のみ、整数と小数
    # test("2.43*11") #掛け算のみ、整数と小数、位置を交換

    # test("9/3") #割り算のみ、整数のみ、余りなし
    # test("13/2") #割り算のみ、整数のみ、余りあり
    # test("6.4/3.2") #割り算のみ、小数のみ、余りなし
    # test("4.2/3.2") #割り算のみ、小数のみ、余りあり
    # test("9/2.43") #割り算のみ、整数と小数、余りなし
    # test("11*2.43") #割り算のみ、整数と小数、余りあり

    # test("6+2.1-3") #足し算、引き算
    # test("1.0+2.1*3") #足し算、掛け算
    # test("1.0+2.1/3") #足し算、割り算
    # test("2.1-3*6") #引き算、掛け算
    # test("2.1-3/3") #引き算、割り算
    # test("6*4/2.6") #掛け算、割り算
    # test("1.0+2.1-3*4.2") #足し算、引き算、掛け算
    # test("1.0+2.1-3*6/2.9") #足し算、引き算、掛け算、割り算

    # test("1.0+2.1-3*8/4/3*5+9.7-0.7+3/3*6") #足し算、引き算、掛け算、割り算、式ロングバージョン
    # test("1") #演算子がない場合

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