q=["which is the scientific name of mango",
"which country is the largest product of coffee",
"the terms 'bull and bear' is associated with",
"cataract is tha disease of?"]
options=[["mangifera indica","tamarindus indica","ficus benghalensis","rosa"],
["albania","angola","belize","brazil"],
["stock market","mobile","company","export market"],
["hand","eye","leg","skin"]]
ans=[1,4,1,2]
ff=["rasa","magifera indica"],["angola","brazil"],["stock market","mobile"],["eye","skin"]
fo=[2,2,1,1]
i=0
count=0
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
    elif n==5050:
        if count==0:
            k=0
            while k<len(ff[i]):
                print(k+1,ff[i][k])
                k=k+1
            count=count+1
            n1=int(input("select ur options"))
            if n1==fo[i]:
                print("right answer")
            else:
                print("ur answer is wrong")
                break
        else:
            print("sorry ur already used")
            n2=int(input("select your options:"))
            if n2==ans[i]:
                print("congrtas*")
            else:
                print("wrong ans*")
                break
    else:
        print("wrong answer sorry")
        break
    i=i+1      
