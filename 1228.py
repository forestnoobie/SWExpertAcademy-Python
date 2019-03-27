## Anwser

for _ in range(1, 11):
    code_length = int(input())
    code = list(map(int, input().split()))
    comNum = int(input())
    commands = str(input())
    commands = commands.split('I')[1:]
    for command in commands:
        command2num = [int(x) for x in command.split(" ")[1:-1]]
        pos = command2num[0]
        code = code[:pos] + command2num[2:] + code[pos:]

    print("#{} ".format(_), end="")
    for num in code[:10]:
        print(num, end=" ")
    print()

## Test
codeLength = 11
code = '449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205'
code = [int(x) for x in code.split(" ")]
comNum = 7
commands = 'I 1 5 400905 139831 966064 336948 119288 I 8 6 436704 702451 762737 557561 810021 771706 I 3 8 389953 706628 552108 238749 661021 498160 493414 377808 I 13 4 237017 301569 243869 252994 I 3 4 408347 618608 822798 370982 I 8 2 424216 356268 I 4 10 512816 992679 693002 835918 768525 949227 628969 521945 839380 479976'
commands = commands.split('I')[1:]

for command in commands:
    command2num =[int(x) for x in command.split(" ")[1:-1]]
    pos = command2num[0]
    print(pos,code)
    code = code[:pos] + command2num[2:] + code[pos:]
