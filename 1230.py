file_path = r'C:\Users\Nakyilkim\Desktop\LIFE\swexpert\input\input_1230.txt'
with open(file_path) as f:
    lines = f.readlines()
    N = lines[0]
    code = list(map(int,lines[1].rstrip().split(" ")))
    comNum = int(lines[2])
    commands = lines[3]

commands = commands.rstrip().split(" ")
command2list = []
start_idx = 0
for i in range(comNum):
    commandtype = commands[start_idx]
    #print('command',commands[start_idx])
    pos = commands[start_idx+1]
    #print("pos",pos)
    if commandtype == 'I' :
        num = int(commands[start_idx+2])
        command2list.append(commands[start_idx: start_idx + int(num) + 3])
        start_idx =  start_idx+int(num) + 3

    elif commandtype == 'D':
        command2list.append(commands[start_idx:start_idx+3])
        start_idx = start_idx + 3

    elif commandtype == 'A':
        num = int(commands[start_idx+1])
        command2list.append(commands[start_idx:start_idx+num+2])
        start_idx = start_idx+num+2


for command in command2list:
    if command[0] == 'I':
        pos = int(command[1])
        code = code[:pos] + command[3:] + code[pos:]
    elif command[0] == 'D' :
        pos = int(command[1])
        num = int(command[2])
        code = code[:pos] + code[pos+num:]
    elif command[0] == 'A':
        for v in command[2:]:
            code.append(v)


print("#{}".format(1), end=" ")
for i in code[:10]:
    print(i, end=" ")




