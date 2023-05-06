from math import*
def kostīmaCena(a,b):
    c = a/100*b*0.5 #50 ir procenti no cilvēka auguma, daļa, ko pārklās kostīms
    return c
sum=0
print("Sveiki! Šī programma palīdzēs Jums uzskaitīt izdevumus mākslas vingrošanas sacensībām, balstoties uz datiem, ko Jūs ievadīsiet")
ms=[["poliesters", 20], ["spandeks", 50], ["bifleks", 70], ["kokvilna", 85] #materiāli un cena par materiala vienu kvadratmetru    
print("pieejamie materiāli:")
for i in range (len(ms)):
    print(i+1,ms[i][0])
while(True):
    ind=int(input("ievadiet vēlāmā materiālā attiecīgu ciparu - "))-1 #1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā numurējās no 0
    if ind>=0 and ind<len(ms): #do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditais cipars neatbilst materialam, ludzu ievadiet vēlreiz")
        continue  
while(True):
    augums=(int(input("ievadiet augumu cm - "))) 
    if augums>0: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditais cipars neder, ludzu ievadiet vēlreiz")
        continue
cena = kostīmaCena(augums,ms[ind][1])
print("Kostīms maksā", cena, "euro")
    
ps=[["bumba", 90,50] , ["aplis", 40,20] , ["vāles", 80,40] , ["lente", 20,8]] #priekšmeti un cenas par jauniem/lietotiem priekšmetiem
print("pieejamie priekšmeti:")
for i in range (len(ps)):
    print(i+1, " - ", ps[i][0])       
while(True):
        ind2=int(input("ievadiet vēlāmā priekšmeta attiecīgu ciparu - "))-1 #ind2 ir indekss ; 1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā numurējās no 0
        if ind2>=0 and ind2<len(ps): # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
            break
        else:
            print("Jusu ievaditais cipars neatbilst priekšmetam, ludzu ievadiet vēlreiz")
            continue
print("ievadiet priekšmeta stāvokli: 1 - jauns 2 - lietots")
while(True):
    cip=(int(input("ievadiet stāvokļa ciparu - "))) 
    if cip==1 or cip==2: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditais cipars neatbilst stāvoklim, ludzu ievadiet vēlreiz")
        continue   
while(True):
    ind3=int(input("ievadiet naudas summu pārējiem izdevumiem, mazākā vērtīva - 20 eiro, lielākā - 120 eiro - ")) 
    if ind3>=20 and ind3<=120: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditā vērtība ir kļūdaina, ludzu ievadiet vēlreiz")
        continue
sum=ps[ind][cip] + kostīmaCena(augums, ms[ind][1]) + ind3
print("Braukšana uz sacensībām izmaksās", sum, "eiro")
