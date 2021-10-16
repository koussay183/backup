chn = input("give input :").split()
chnaf = []

for word in chn:
    x = word[1:] + word[0] + "ay"
    chnaf.append(x)

chnaf = ' '.join(chnaf)
print(chnaf)
    

    


