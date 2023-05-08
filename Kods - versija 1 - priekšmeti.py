pj=["bumba/jauna", "aplis/jauns", "vāles/jaunās", "lente/jauna"]
pl=["bumba/lietota", "aplis/lietots", "vāles/lietotās", "lente/lietota"]
pcj=[90, 40, 80, 20]
pcl=[50, 20, 40, 8]
print("pieejamie priekšmeti - ", pj)
print("pieejamie priekšmeti - ", pl) 
prieks=(input("ievadiet velamo priekšmetu un vai tas ir jauns vai lietots - "))
if prieks in pj:
    print("šīs priek mets maksās", pcj[pj.index(prieks)], "eiro")
elif prieks in pl:
    print("šīs priekšmets maksās", pcl[pl.index(prieks)], "eiro")
else:
    print("kļūda, pamēģiniet ievadīt vēlreiz")
