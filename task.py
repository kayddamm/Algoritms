import math

string = input()

list = []
output = []

def function(str, k): 
      
    for i in range(len(str)):
        if i%k == 0:
            sub = str[i:i+k]
            lst=[]
            for j in sub: 
                lst.append(j)
            list.append(lst)


sqr = math.sqrt(len(string))

if(string==""):
    print("string is empty")
elif sqr%1 == 0:
    
    word = input()
    
    function(string, int(sqr))
    for k in range(len(word)):
        match=0
        for i in range(len(list)): 
            for j in range(len(list[i])): 
                if(word[k] == list[i][j]):
                    match=1
                    output.append("["+str(i)+","+str(j)+"]")
                    break
            else:
                continue
            break
        if match==0:
            output.append("doesn't match")
    
else:
    print("length of string must be square of natural number")

print(list)
print(output)
