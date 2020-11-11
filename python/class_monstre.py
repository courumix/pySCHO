#la class monstre sert a créer les monstres de pySCHO
class monstre:
    def __init__(self, nom, type_monstre='Humain', pv = 10, force = 10, resistance = 10,
                 agilite = 10, intelligence = 10, cri = 'grrrr'):
        self._nom = str(nom) #le nom du monstre (louis, casimir, etc...)
        self._type = str(type_monstre) #le type du monstre (elf, gobelins, orc, dragon, etc...)
        self._pv = int(pv) #le pv actuel du monstre
        self._pv_max = int(pv) #les pv max du monstre (utiles pour le __repr__)
        self._force = int(force) #les points de forces du monstre
        self._resi = int(resistance) #les points de résistances du monstre
        self._agi = int(agilite) #les points d'agilités du monstre
        self._intel = int(intelligence) #les points d'intélligences du monstre
        self._cri = str(cri) #le cri de guerre du monstre (grrrr, gniark, etc...)
        
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
    def getAgi (self):
        return self._agi
    def getIntel (self):
        return self._intel
    def getCri (self):
        return self._cri    
    
    #mutateurs
    def setPv (self,new_pv):
        if new_pv < 0:
            self._pv = 0
        else:
            self._pv = new_pv
            
            
            
    
        
    
    
    def __repr__(self): #le __repr__ sert à afficher les caractéristiques du monstre
        return self.getNom() + " est un " + str(self.getType()) + "\n PV : " + str(self.getPv()) + "/" + str(self.getPvMax()) + "\n Force : " + str(self.getForce()) + "\n Résistance : " + str(self.getResi()) + "\n Agilité : " + str(self.getAgi()) + "\n Intélligence : " + str(self.getIntel()) +"\n sont cri est : " + self.getCri()
            
            
           
           
        
  
        
        
        
        
        
        
        
        
        
victor = monstre("Victor", pv= 1500000) #victor est cobaye de la class monstre