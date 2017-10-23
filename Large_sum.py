a = int(input())
l = []
for i in range(a):
    l.append(long(raw_input()))
s_int = sum(l)
s = str(s_int)
s1 = s[:10]
print s1