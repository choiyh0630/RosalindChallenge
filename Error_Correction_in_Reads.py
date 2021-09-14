from collections import Counter

f = open('./Sample_Error_Correction_in_Reads.txt', 'r')
l = f.read().splitlines()
print(l)
d = {}
for i in l:
    if i.startswith('>'):
        d[i[1:]] = ''
        key = i[1:]
    else:
        d[key] = i

print(d)

print(Counter(d.values()))
print([k for k, v in Counter(d.values()).items() if v == 1])

def error_corrections(d):
    unique_reads = [k for k, v in Counter(d.values()).items() if v == 1]
