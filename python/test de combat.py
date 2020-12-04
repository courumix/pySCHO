from class_monstre import *

def combat_iter (monstre1, monstre2):
    #désigne le monstre qui attaquera en premier
    if monstre1.getVit() > monstre2.getVit():
        unite_A = monstre1
        unite_B = monstre2
    else:
        unite_A = monstre2
        unite_B = monstre1
            
    while unite_A.getPv() > 0 and unite_B.getPv() > 0:
        dmg_pv = unite_A.att(unite_B)
        print (unite_A.getNom(), "attaque", dmg_pv,"a", unite_B.getNom())
                
        dmg_pv = unite_B.att(unite_A)
        print (unite_B.getNom(), "attaque", dmg_pv,"a", unite_A.getNom())
            
        print (unite_A.getNom(), "a", unite_A.getPv(), "PV et", unite_B.getNom(), "a", unite_B.getPv(), "PV \n")


    
    ################## TEST ##################


combat_iter(tobi, victor)