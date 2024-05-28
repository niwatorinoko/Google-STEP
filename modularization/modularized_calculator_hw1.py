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

        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


#1回目の評価：掛け算と割り算を計算する
def first_evaluate(tokens):
    evaluated_tokens = []
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':

            if tokens[index - 1]['type'] == 'PLUS':
                evaluated_tokens.append(tokens[index-1])
                evaluated_tokens.append(tokens[index])

            elif tokens[index - 1]['type'] == 'MINUS':
                evaluated_tokens.append(tokens[index-1])
                evaluated_tokens.append(tokens[index])

            elif tokens[index - 1]['type'] == 'TIMES':
                #numには掛けられる数をevaluated_tokensの一番後ろから取り出し入れる
                num = evaluated_tokens.pop(-1)
                answer = num['number']*tokens[index]['number']
                evaluated_tokens.append({'type': 'NUMBER', 'number': answer})

            elif tokens[index - 1]['type'] == 'DIVIDED':
                #numには割られる数をevaluated_tokensの一番後ろから取り出し入れる
                num = evaluated_tokens.pop(-1)
                answer = num['number']/tokens[index]['number']
                evaluated_tokens.append({'type': 'NUMBER', 'number': answer})

            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return evaluated_tokens


#2回目の評価：足し算と引き算を計算する
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

    print("==== Test finished! ====\n")

run_test()

# while True:
#     print('> ', end="")
#     line = input()
#     tokens = tokenize(line)
#     answer = evaluate(tokens)
#     print("answer = %f\n" % answer)