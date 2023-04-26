from math import*
#from random import randint
def kostīmaCena(a,b):
    c = a/100*b*0.5 #50 ir procenti no cilvēka auguma, daļa, ko pārklās kostīms
    return c

sum=0
print("Sveiki! �� programma pal�dz�s Jums uzskait�t izdevumus m�kslas vingro�anas sacens�b�m, balstoties uz datiem, ko J�s iev�d�siet")
ms=[["poliesters", 20], ["spandeks", 50], ["bifleks", 70], ["kokvilna", 85] #materiāli un to cena par vienu kvadratmetru
    
print("pieejamie materi�li:")
for i in range (len(ms)):
    print(i+1,ms[i][0])

while(True):
    ind=int(input("ievadiet vēlāmā materiālā attiecīgu ciparu - "))-1 #ind ir indekss ; 1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā numurējās no 0
    if ind>=0 and ind<len(ms): # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
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
    
ps=[["bumba", 90,50] , ["aplis", 40,20] , ["vāles", 80,40] , ["lente", 20,8]] #priekšmeti un to stāvoklis 
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
print("ievadiet priekšmeta stāvokli:\n1-jauns\n2-lietots")
while(True):
    cip=(int(input("ievadiet stāvokļa ciparu - "))) 
    if cip==1 or cip==2: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditais cipars neatbilst stāvoklim, ludzu ievadiet vēlreiz")
        continue
    
print("Tagad jūsu izdevumi ir", ps[ind][cip]+ kostīmaCena(augums,ms[ind][1]))
    
while(True):
    ind3=int(input("ievadiet naudas summu pārējiem izdevumiem, mazākā vērtīva - 20 eiro, lielākā - 120 eiro - ")) #ind ir indekss ; 1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā numurējās no 0
    if ind3>=20 and ind3<=120: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditā vērtība ir kļūdaina, ludzu ievadiet vēlreiz")
        continue

sum=ps[ind][cip] + kostīmaCena(augums,ms[ind][1]) + ind3
print("Braukšana uz sacensībām izmaksās", sum, "eiro")

  
    
    
    
    
    
    
    
    
    
    
    
    
    #while(True):
        #augums=(int(input("ievadiet augumu cm - "))) 
        #if augums>0: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
            #break
        #else:
            #print("Jusu ievaditais cipars neatbilst materialam, ludzu ievadiet vēlreiz")
            #continue
    #cenam2 = mc[ind]
    #cena = kostimaCena(augums,cenam2)
    #print(cena)
    
    
    
    
    
    
#pj=["bumba/jauna", "�plis/jauns", "v�les/jaun�s", "lente/jauna"]
#pl=["bumba/lietota", "�plis/lietots", "v�les/lietot�s", "lente/lietota"]
#pcj=[90, 40, 80, 20]
#pcl=[50, 20, 40, 8]
#print("pieejamie priek�meti - ", pj)
#print("pieejamie priek�meti - ", pl) 
#prieks=(input("ievadiet vel�mo priek�metu un vai t�s ir jauns vai lietots - "))
#if prieks in pj:
    #print("��s priek�mets maks�s", pcj[pj.index(prieks)], "eiro")
#elif prieks in pl:
    #print("��s priek�mets maks�s", pcl[pl.index(prieks)], "eiro")
#else:
    #print("k��da, pam��iniet ievad�t v�lreiz")
 
 
 
 
   
#a=(int(input("Cik naudas J�s atliksiet par�jiem izdevumiem, ievadiet summu no 20 l�dz 120")
     



    
    
    
