f = open('temp.txt', 'r')
out_lat = open('out_lat.txt', 'w')
out_rus = open('out_rus.txt', 'w')
res = f.read().split('\n')
try:
    while True:
            res.remove("")
except ValueError:
    pass
print(res)
length = len(res)
for i in range(length):
    if i % 2:
        out_rus.write(res[i] + '\n')
    else:
        out_lat.write(res[i] + '\n')
