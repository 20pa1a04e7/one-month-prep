word = input()
lst = []
opp = {'}':'{',')':'(',']':'['}
for i in range(len(word)):
    if word[i]=='{' or word[i]=='(' or word[i]=='[':
        lst.append(word[i])
    else:
        if len(lst)==0:
            print(i+1)
            
            break
        else:
            if lst.pop()!=opp[word[i]]:
                print(i+1)
                break
else:
    if(len(lst)!=0):
        print(len(word))
    else:
        print(0)
#print(lst)

