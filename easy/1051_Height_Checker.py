l = [0,1,0,3,12]
ct = 0
for i in l:
    if i == 0:
        ct += 1
l = [x for x in l if x != 0]
for i in range(ct):
    try:
        l.append(0)
    except:
        pass
print(l)
        
