a = [1,2,3,4];

result = []
res  = 1;

for i in range(0, len(a)):
    for j in range((len(a)-1), -1, -1):
        if(a[i]!=a[j]):
            res*=a[j]
        # result.append(a[i]*a[j]);
    result.append(res);
    res = 1;    

print(result)
