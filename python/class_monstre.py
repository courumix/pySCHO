import random #importation de plusieurs fonction utile


class monstre:
    """
    La class monstre sert a créer les monstres de pySCHO
    """
    def __init__(self, nom, type_monstre='Humain', pv = 10, force = 10, resistance = 10,
                 vitesse = 10, agilite = 10, intelligence = 10, chance = 10, cri = 'grrrr'):
        self._nom = str(nom) #Le nom du monstre (louis, casimir, etc...)
        self._type = str(type_monstre) #Le type du monstre (elf, gobelins, orc, dragon, etc...)
        self._pv = int(pv) #Le pv actuel du monstre
        self._pv_max = int(pv) #Les pv max du monstre (utiles pour le __repr__)
        self._force = int(force) #Les points de forces du monstre
        self._resi = int(resistance) #Les points de résistances du monstre
        self._vit = int(vitesse) #la vitesse du monstre
        self._agi = int(agilite) #Les points d'agilités du monstre
        self._intel = int(intelligence) #Les points d'intélligences du monstre
        self._chance = int(chance) #les points de chance du monstre
        self._cri = str(cri) #Le cri de guerre du monstre (grrrr, gniark, etc...)
        
    #accesseurs
    def getNom (self):
        return self._nom
    def getPv (self):
        return self._pv
    def getPvMax (self):
        return self._pv_max
    def getType (self):
        return self._type
    def getForce (self):
        return self._force
    def getResi (self):
        return self._resi
    def getVit (self):
        return self._vit
    def getAgi (self):
        return self._agi
    def getIntel (self):
        return self._intel
    def getChance (self):
        return self._chance
    def getCri (self):
        return self._cri    
    
    #mutateurs
    def setPv (self,new_pv):
        if new_pv < 0:
            self._pv = 0
        else:
            self._pv = new_pv
            
    #méthodes
    def attTmp(self, perso, dmg_pv):
        new_pv = perso.getPv() - dmg_pv
        perso.setPv(new_pv)        
    
    def att(self, perso):
        dmg_pv = (randint(1,self.getChance()) * self.getForce()) / perso.getResi()
        new_pv = perso.getPv() - dmg_pv
        perso.setPv(new_pv)
    
        
    
    
    def __repr__(self): #Le __repr__ sert à afficher les caractéristiques du monstre
        return self.getNom() + " est un " + str(self.getType()) + "\n PV : " + str(self.getPv()) + "/" + str(self.getPvMax()) + "\n Force : " + str(self.getForce()) + "\n Résistance : " + str(self.getResi()) + "\n vitesse : " + str(self.getVit()) + "\n Agilité : " + str(self.getAgi()) + "\n Intelligence : " + str(self.getIntel()) + "\n Chance : " + str(self.getChance()) + "\n sont cri est : " + self.getCri()
            
            
           
           
    
  
victor = monstre(nom="Victor", type_monstre="cobaye", pv=250, force=20, resistance=12, vitesse=5, agilite=7, intelligence=30, chance=10, cri="zzzzzzzzz")
tobi = monstre(nom="Tobi", type_monstre="cobaye", pv=125, force=15, resistance=9, vitesse=16, agilite=17, intelligence=50, chance=15, cri="coucou")