from math import*
#from random import randint
def kostimaCena(a,b):
    d = a*0.50/100 #50 ir procenti no cilvēka auguma, daļa, ko pārklās kostīms
    c = d*b
    return c

sum=0
count=0
#print("Sveiki! �� programma pal�dz�s Jums uzskait�t izdevumus m�kslas vingro�anas sacens�b�m, balstoties uz datiem, ko J�s iev�d�siet")
ms=["poliesters","spandeks", "bifleks", "kokvilna"] #materiāli un to stāvoklis
mc=[220, 350, 420, 550] #attiecīgas cenas, izmainīt, lai printētu cenas par materiāla m2

print("pieejamie materi�li:")
for i in range (len(ms)):
    print(i+1,ms[i])

while(True):
    ind=int(input("ievadiet vēlāmā materiālā attiecīgu ciparu - "))-1 #ind ir indekss ; 1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā numurējās no 0
    if ind>=0 and ind<len(ms)+1: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditais cipars neatbilst materialam, ludzu ievadiet vēlreiz")
        continue
    
while(True):
    augums=(int(input("ievadiet augumu cm - "))) 
    if augums>0: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
        break
    else:
        print("Jusu ievaditais cipars neatbilst materialam, ludzu ievadiet vēlreiz")
        continue
cenam2 = mc[ind]
cena = kostimaCena(augums,cenam2)
print(cena)
    
ps=["bumba","aplis", "vāles", "lente"] #materiāli un to stāvoklis
mc=[220, 350, 420, 550] #attiecīgas cenas, izmainīt, lai printētu cenas par prieksmetiem

print("pieejamie priekšmeti:")
for i in range (len(ps)):
    print(i+1,ps[i])   

    
while(True):
        ind=int(input("ievadiet vēlāmā priekšmeta attiecīgu ciparu - "))-1 #ind ir indekss ; 1 ir jāatņem, lai uzskaitītu vajadzīgo elementu, nevis nākamo, jo sarakstā numurējās no 0
        if ind>=0 and ind<len(ms)+1: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
            break
        else:
            print("Jusu ievaditais cipars neatbilst materialam, ludzu ievadiet vēlreiz")
            continue
        
    while(True):
        augums=(int(input("ievadiet augumu cm - "))) 
        if augums>0: # do while ir vajadzīgs lai ja būs kļūda lietotājs varētu ievadīt vēlreiz
            break
        else:
            print("Jusu ievaditais cipars neatbilst materialam, ludzu ievadiet vēlreiz")
            continue
    cenam2 = mc[ind]
    cena = kostimaCena(augums,cenam2)
    print(cena)
    
    
    
    
    
    
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
     



    
    
    
