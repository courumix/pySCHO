class personnage:
    def __init__(self,nom, pv=100, resistance=10, agilite=8, inteligence=25, chance=1, experience=0, niveau=1, force=10, vitesse=20, mana=50):
        
        self._nom = str(nom) #Nom ou pseudo (Nindjini,courumix,poilopopo,ect) il le garderas toute la partie
        self._pv = int(pv) #PV vie du personnage pourras l'augmenter en montant de niveaux ou avec des armures
        self._resi = int(resistance) #Resistance attribut qui induit sur les degats reçu
        self._agi = int(agilite) #Agilité permet d'influer sur les chances d'esquives
        self._intel = int(inteligence) #L'intéligence sert a l'utilisation des objet ou même de l'utilisation de certain sort
        self._chance = int(chance) #Chance influras sur les loots des énemit et les coûts critiques
        self._exp = int(experience) #Expérience du joueur qui lui sert a monté de niveau
        self._niv = int(niveau) #Les niveaux servirant a l'augmentation des attributs et des ajuts des points de compétences
        self._force = int(force) #La force serviras au dégats reçus a l'ennemi
        self._vit = int(vitesse) #La vitesse serviras a l'initiatives (plus de précision plus la vitesse est haute, plus il auras de chance d'attaqué au premier tour lors d'un combat ex: perso a une vitesse de 20 et un gobelin a une vitesse de 15 alors le perso commenceras a attaquer)
        self._mana = int(mana) #Energie qu'as le personnages qui est utilisé pour la magie

#accesseur    
def getNom(self):
    return self._nom
def getPv(self):
    return self._pv
def getDegats(self):
    return self._degats
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

#mutateurs
def setPv (self,new_pv):
    if new_pv < 0:
        self._pv = 0
    else:
        self._pv = new_pv
            
#méthodes
def att(self, monstre, dmg_pv):
    new_pv = monstre.getPv() - dmg_pv
    monstre.setPv(new_pv)   