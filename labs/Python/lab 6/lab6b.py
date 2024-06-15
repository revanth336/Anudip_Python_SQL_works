lis=[1,2,2,3,4,5,5,7,9,1]
uni=[]
dup=[]
for ele in lis:
    if ele not in uni:
        uni.append(ele)
    elif ele not in dup:
        dup.append(ele)
print(dup)
