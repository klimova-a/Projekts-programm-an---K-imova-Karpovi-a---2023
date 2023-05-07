from math import*
def kostīmaCena(a,b):
    c = a/100*b*0.5 #0.5 ir vienāds ar 50%, tie ir procenti no cilvēka auguma, ko pārklās kostīms
    return c
sum=0
print("Sveiki! Šī programma palīdzēs Jums uzskaitīt izdevumus mākslas vingrošanas sacensībām, balstoties uz datiem, ko Jūs ievadīsiet")
print("Piezīme: ja Jums ir vajadzīgs kostīms pēc 2-5 dienām, tiek uzskaitīta papildus maksa par steidzamību 10 eiro/dienā apmērā; viena šūvējas darba diena ir 80 eiro vērta.")
ms=[["poliesters", 20], ["spandeks", 50], ["bifleks", 70], ["kokvilna", 85]] #materiāli un cena par materiāla kvadratmetru    
print("pieejamie materiāli:")
for i in range (len(ms)):
    print(i+1, " - ", ms[i][0])
while(True):
    ind=int(input("ievadiet vēlāmā materiālā attiecīgu ciparu - "))-1 #1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā elementi numurējās no 0
    if ind>=0 and ind<len(ms): #do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievadītais cipars neatbilst materiālam, ludzu ievadiet vēlreiz")
        continue  
while(True):
    augums=(int(input("ievadiet augumu cm - "))) 
    if augums>100: #do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditais augums neder, lūdzu ievadiet vēlreiz")
        continue
while(True):
    ds=int(input("Ievadiet, pēc cik dienām Jums ir vajadzīgs kostīms, mazākais skaits - 2 dienas, lielākais - 10 dienas - "))
    if ds>5 and ds<=10: #do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        ds=ds*80 
        break
    elif ds<=5 and ds>=2:
        ds=ds*90
        print(ds)
        break 
    else:
        print("Kāda no Jūsu ievadītām vērtībam ir kļūdaina, lūdzu ievadiet vēlreiz")
        continue
cena = kostīmaCena(augums,ms[ind][1])+ds
print("Kostīms izmaksās", cena, "eiro")  
ps=[["bumba", 90,50] , ["aplis", 40,20] , ["vāles", 80,40] , ["lente", 20,8]] #priekšmeti un cenas par jauniem/lietotiem priekšmetiem
print("pieejamie priekšmeti:")
for i in range (len(ps)):
    print(i+1, " - ", ps[i][0])       
while(True):
        ind2=int(input("ievadiet vēlāmā priekšmeta attiecīgu ciparu - "))-1 #ind2 ir indekss ; 1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā elementi numurējās no 0
        if ind2>=0 and ind2<len(ps): # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
            break
        else:
            print("Jusu ievadītais cipars neatbilst priekšmetam, lūdzu ievadiet vēlreiz")
            continue
print("ievadiet priekšmeta stāvokli: 1 - jauns 2 - lietots")
while(True):
    cip=(int(input("ievadiet stāvokļa ciparu - "))) 
    if cip==1 or cip==2: #do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievadītais cipars neatbilst stāvoklim, lūdzu ievadiet vēlreiz")
        continue
print("Tagad braukšana uz sacensībām izmaksās", ps[ind][cip]+kostīmaCena(augums,ms[ind][1])+ds, "eiro")
while(True):
    ind3=int(input("Ievadiet naudas summu pārējiem izdevumiem, mazākā vērtība - 20 eiro, lielākā vērtība - 120 eiro - ")) 
    if ind3>=20 and ind3<=120: #do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditā vērtība ir kļūdaina, lūdzu ievadiet vēlreiz")
        continue
sum=ps[ind][cip]+kostīmaCena(augums,ms[ind][1])+ds+ind3
print("Braukšana uz sacensībām izmaksās", sum, "eiro")