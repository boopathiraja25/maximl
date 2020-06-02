a=input()
l1=[]
for i in range(len(a)):
    for j in range(len(a),i,-1):
        l1.append(a[i:j])
l1.sort(reverse=True, key=len)
for i in l1:
    if len(i)==len(set(i)):
        print(len(i))
        break
