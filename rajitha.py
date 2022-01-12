q=["which is the scientific name of mango",
"which country is the largest product of coffee",
"the terms 'bull and bear' is associated with",
"cataract is tha disease of?"]
options=[["mangifera indica","tamarindus indica","ficus benghalensis","rosa"],
["albania","angola","belize","brazil"],
["stock market","mobile","company","export market"],
["hand","eye","leg","skin"]]
ans=[1,4,1,2]
i=0
while i<len(q):
    print("the is your", i+1 ,"question")
    print(i+1,q[i])
    print("this is ur options")
    j=0
    while j<len(options[i]):
        print(j+1,options[i][j])
        j+=1
    n=int(input("plz select ur options"))
    if n==ans[i]:
        print("congrats")
    else:
        print("wrong answer")
        break    
    i=i+1       
print("game over")
