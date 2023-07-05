f = open('temp.txt', 'r')
out_lat = open('out_lat.txt', 'w')
out_rus = open('out_rus.txt', 'w')
alp_rus = set(chr(i) for i in range (ord('А'),ord('Я')+1))
for line in f:
    res = line.split(',')
    if len(res) > 1:
        if res[0][0] not in alp_rus:
            out_lat.write(res[0] + '\n')
            i = 0
            while (res[len(res) - 1][i].upper() not in alp_rus):
                res[len(res) - 1] = res[len(res) - 1][1:]
            for i in range(len(res[len(res) - 1])):
                if res[len(res) - 1][i] in '0123456789':
                    res[len(res) - 1] = res[len(res) - 1][:i] + '\n'
                    break
            out_rus.write(res[len(res) - 1])