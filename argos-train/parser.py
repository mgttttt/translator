f = open('temp.txt', 'r')
out_lat = open('out_lat.txt', 'w')
out_rus = open('out_rus.txt', 'w')
alp_lat = set(chr(i) for i in range (ord('A'),ord('Z')+1))
alp_rus = set(chr(i) for i in range (ord('А'),ord('Я')+1))
digits = '0123456789'

for line in f:
    while '[' in line and ']' in line:
        ind_start, ind_end = line.find('['), line.find(']')
        length = ind_end - ind_start + 1
        for i in range(ind_start, ind_end + 1):
            line = line.replace(line[ind_start], '', 1)

    start, end = 0, 0
    for i in range(len(line)):
        if line[i].upper() in alp_rus:
            end = i
            break
    string = line[start:end]
    i = end - 1
    while (string[i].upper() not in alp_lat and string[i].upper() not in alp_rus):
        string = string[:i]
        i -= 1
    i = 0
    while (string[i].upper() not in alp_lat and string[i].upper() not in alp_rus):
        string = string[1:]
    out_lat.write(string + '\n')
    out_rus.write(line[end:])
    print(string)
    print(line[end:])
