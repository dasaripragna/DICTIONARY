d1={1:10,2:20}
d2={3:30,2:40}
d3={5:50,6:60}
d4={}
# d4.update(d2)
for i,j in d1.items():
    # print(i,j)
    for x,y in d2.items():
        # print(x,y)
        if i==x:
            d4[i]=j+y
        else:
            d4[i]=j
d4[3]=d2[3]
d4.update(d3)       
print(d4)