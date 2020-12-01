import random # importation de plusieurs fonction utile


class monstre:
    """
    La class monstre sert a créer les monstres de pySCHO
    """
    def __init__(self, nom, type_monstre='Humain', pv = 10, force = 10, resistance = 10,
                 vitesse = 10, agilite = 10, intelligence = 10, cri = 'grrrr'):
        self._nom = str(nom) # Le nom du monstre (louis, casimir, etc...)
        self._type = str(type_monstre) # Le type du monstre (elf, gobelins, orc, dragon, etc...)
        self._pv = int(pv) # Le pv actuel du monstre
        self._pv_max = int(pv) # Les pv max du monstre (utiles pour le __repr__)
        self._force = int(force) # Les points de forces du monstre
        self._resi = int(resistance) # Les points de résistances du monstre
        self._vit = int(vitesse) # la vitesse du monstre
        self._agi = int(agilite) # Les points d'agilités du monstre
        self._intel = int(intelligence) # Les points d'intélligences du monstre
        self._cri = str(cri) # Le cri de guerre du monstre (grrrr, gniark, etc...)
        
    # accesseurs
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
    def getCri (self):
        return self._cri    
    
    # mutateurs
    def setPv (self,new_pv):
        if new_pv < 0:
            self._pv = 0
        else:
            self._pv = new_pv
            
    # méthodes
    def att(self, perso, dmg_pv):
        new_pv = perso.getPv() - dmg_pv
        perso.setPv(new_pv)        
            
    
        
    
    
    def __repr__(self): # Le __repr__ sert à afficher les caractéristiques du monstre
        return self.getNom() + " est un " + str(self.getType()) + "\n PV : " + str(self.getPv()) + "/" + str(self.getPvMax()) + "\n Force : " + str(self.getForce()) + "\n Résistance : " + str(self.getResi()) + "\n vitesse : " + str(self.getVit()) + "\n Agilité : " + str(self.getAgi()) + "\n Intelligence : " + str(self.getIntel()) + "\n sont cri est : " + self.getCri()
            
            
           
           
    
  
        
        
    def combat (self, perso):
        if self.getVit > perso.getVit:
            unite_A = self
            unite_B = perso
        else:
            unite_A = perso
            unite_B = self
            
        while unite_A.getPV() > 0 and unite_B.getPV()
            print (unite_A.getNom() + "attaque" + unite_B.getNom())
            unite_A.att(unite_B, randint(1,5) * unite_A.getForce())
                
            print (unite_B.getNom() + "attaque" + unite_A.getNom())
            unite_B.att(unite_Z, randint(1,5) * unite_B.getForce())