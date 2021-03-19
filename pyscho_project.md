# Comment coder un jeux de rôle en python?
## Définition d'un jeux de rôle
RPG = un personnages + des stats + un niveau + des équipements + des épreuves
## Notre jeux de rôle
### Des épreuves basé sur le combat et les enigmes

exemple d'énigme : le labyrinthe

**combat** : possibilité de coruption (don d'or = évité combat); possibilité de persuation (dépend du charisme du personnage). Si persuation ou corruption réussie alors on évite le combat sinon on a un malus pendant le combat. les monstres on un attribut résistance a la persuation et un attribut résistance a la corruption. !TO CODE!
les statistiques du personnage sont modifié par son équipement pour le combat.

### Monde

!TO WRITE! elf; gobelins == fantasy...

### Histoire

Une grande épidémie dans tous le royaume (peuplé de différentes espéces mais dominé par les hommes). On recherche un reméde et on sait que dans le nord les elf blanc garde une recette secréte qui donnerons au personnage car nous auront sauver son fils sans faire exprés. dans la recettes il y a 5 ingrédients qui nous amménerons dans 5 regions différentes.

- region du nord : elf blanc, tuto (on connais les stats des monstres)
- région du désert
- région des montagne
- région des marais
- région des attols
- région de la jungle

## gestion du code
gestion des modifications (historique + travail en commun) grâce au protocole git et au site github.
github permet aussi de gerer les bugs et les demande d'amélioration des utilisateurs (issues).

## Stockage des données
utilisation d'une base de donnée SQL. !TO WRITE!
importation vers python via du CSV

### Pourquoi une base de donnée plutôt que des multiple tableaux ?
!TO WRITE!

## Python
### Gestion du parcour
6 zones (régions) avec chacune un réseaux d'événnement (combat, énigme, rencontre).

### Programmation orienté objet
#### Utilisation des *class*
!TO DO MERMAID CLASS!
- méthode
- accesseur
- mutateurs

*class* monstre:

*class* personnage:
- equipement (coder sous formes de dictionnaires en fonction des emplacements sur le code) !TO CODE!

## Perspective
graphisme avec TKINTER ou Turtle.