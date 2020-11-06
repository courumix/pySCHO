class monstre:
    def __init__(self, nom, type_monstre='Humain', pv = 10, force = 10, resistance = 10,
                 agilite = 10, intelligence = 10, cri = 'grrrr'):
        self._nom = str(nom)
        self._type = str(type_monstre)
        self._pv = int(pv)
        self._pv_max = int(pv)
        self._force = int(force)
        self._resi = int(resistance)
        self._agi = int(agilite)
        self._intel = int(intelligence)
        self._cri = str(cri)
        
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
            
            
            
    
        
    
    
    def __repr__(self):
        return self.getNom() + " est un " + str(self.getType()) + "\n PV :" + str(self.getPv()) + "/" + str(self.getPvMax())
  
        
        
        
        
        
        
        
        
        
victor = monstre("Victor", pv= 1500000)