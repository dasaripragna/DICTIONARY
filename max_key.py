my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
max1=0
max2=0
max3=0
l=[]
for i in my_dict:
    for j in my_dict:
        if my_dict[j]>max1:
            max1=my_dict[j]
            max1_key=i


        elif max1>my_dict[j] and max2<my_dict[j]:
            max2=my_dict[j]
            max2_key=j
        elif max2>my_dict[j] and max3<my_dict[j]:
            max3=my_dict[j]
            max3_key=i
l.append(max1)
l.append(max2)
l.append(max3)
print(l)