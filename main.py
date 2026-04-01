chambres = []
reservations = []


def ajouter_une_chambre():

    global chambres

    id = input("Identifiant unique (exemple: '001') : ")
    type = input("Simple, Double ou Suite : ")
    prix = float(input("Prix par nuit en francs : "))
    disponible = True
    
    for chambre in chambres :
        if chambre["ID"] == id :
            print("❌❌chambre est deja ajoute!")
            disponible = False
            break

    else : 

        nouvellechambre = {

            "ID" : id,
            "type" : type,
            "Prix" : prix,
            "disponible" : disponible
        }
        
        chambres.append(nouvellechambre)
        print("Chambre ajoute✅")

def afficher_les_chambres():

    global chambres

    if len(chambres) == 0:
        print("Aucun chambre n'est ajouter 🔴🔴🔴")
    else :
        print("-------Nos chambres-----")
        for chambre in chambres:
            print(f"chambre : {chambre["ID"]}")
            print(f"Type : {chambre["type"]}")
            print(f"PRIX: {chambre["Prix"]} franc")
            print(f"Disponible : {chambre["disponible"]}")
            print("========================")
            
def faire_une_reservation():

    global reservations

    try:
        nom =  input("Nom du client : ")
        chambreid =  input("Lien vers la chambre : ")
        dateArrivee = int(input("Jour d'arrivée (nombre) : "))
        dateDepart = int(input("Jour de départ (nombre) : "))
        numero = "R" + str(len(reservations) + 1).zfill(3) 
        statut = "Annuler"

        if len(chambres) == 0:
            print("❌❌Pas de chambres")
            return 
        else : 
            for chambretrouve in chambres:
                if chambretrouve["ID"] == chambreid:
                    print("cette chambre existe✅")
                    statut= "confirmee"
                    break
            else:
                print("Chambres inexistant 🔴❌")
                return
            
            if dateDepart <= dateArrivee:
                print("❌ La date de départ doit être après l'arrivée!")
                return
            
            for reservation_existante in reservations:
                date_arr = reservation_existante["DateArrivee"]
                date_dep = reservation_existante["DateDepard"]

                if date_arr < dateDepart and date_dep > dateArrivee: 
                    print("❌Conflit ")
                    print(f"Chambre occupee de [{date_arr} a {date_dep}]")
                    return     
                                     
            else : 
                print("pas de conflit")
                  
            nombrenuits =  dateDepart - dateArrivee
            prixtotal =  nombrenuits * chambretrouve["Prix"]

            nouvellereservation = {
                "Numero" : numero,
                "Nom" : nom,
                "ChambreID" : chambreid,
                "DateArrivee" : dateArrivee,
                "DateDepard" : dateDepart,
                "NombreNuits" : nombrenuits,
                "Prix" : prixtotal,
                "Statut" : statut
            }
            reservations.append(nouvellereservation)
            print("reservation terminer🟢")  
    except ValueError : 
        print("❌❌❌le formulaire n'est pas bien rempli")


def afficher_les_reseration():

    global reservations

    if len(reservations) == 0:
        print("--LISTE VIDE--")
        return
    else :
        print("---NOS RESERVATIONS--")
        for reservation in reservations:
            print(f"NUMERO : {reservation["Numero"]}")
            print(f"NOM : {reservation["Nom"]}")
            print(f"CHAMBRE_ID : {reservation["ChambreID"]}")
            print(f"Date_d'arrivee : {reservation["DateArrivee"]}")
            print(f"Date_depard : {reservation["DateDepard"]}")
            print(f"NombreNuits: {reservation["NombreNuits"]}")
            print(f"Prix : {reservation["Prix"]}")
            print(f"Statut : {reservation["Statut"]}")
            print("------------------------------")

def cherche_une_reservation():

    global reservations

    if len(reservations) == 0:
        print("Pas de reservation Pour le moment 🔴")
        return
    print("-----BIENVENUE-----")

    numero = input(" Numéro de réservation (exemple: 'R001') : ")

    for reach in reservations:
        if reach["Numero"] == numero:
            print("Cette chambre est reservee par 🟢")
            print(f"Nom : {reach["Nom"]}")
            print(f"ChambreID : {reach["ChambreID"]}")
            print(f"DATE D'ARR : {reach["DateArrivee"]}")
            print(f"DATE DEP : {reach["DateDepard"]}")
            print(f"NombreNuits : {reach["NombreNuits"]}")
            print(f"Prix : {reach["Prix"]}")
            print(f"Statut : {reach["Statut"]}")
            return  
        else : 
            print(f"❌ Réservation {numero} non trouvée!")
        

def annuler_une_reservation():
    global reservations

    if len(reservations) == 0 :
        print("Pas de reservation ❌❌")
        return
    
    numero = input(" Numéro de réservation (exemple: 'R001') : ")

    for num in reservations:
        if num["Numero"] == numero:
            print("--NOUS TROUVONS VOTRE CHAMBRE--")
            num["Statut"] = "Annuler"
            print(f"Nom : {num["Nom"]}")
            print(f"ChambreID : {num["ChambreID"]}")
            print(f"DATE D'ARR : {num["DateArrivee"]}")
            print(f"DATE DEP : {num["DateDepard"]}")
            print(f"NombreNuits : {num["NombreNuits"]}")
            print(f"Prix : {num["Prix"]}")
            print(f"Statut : {num["Statut"]}")
            print("-------------------------")
            print("✅ Réservation annulée!")
            return 
    else : 
        print(f"PAS CE NUMERO {numero}")
        return

def statistique():

    global reservations, chambres
    if len(reservations) == 0 and len(chambres) == 0:
        print("Pas de Chambre Ni Reservation ❌❌")
        return
    print("=====STATISTIQUE=====")
    print(f"📍CHAMBRES : {len(chambres)}")
    print(f"🔑RESERVATIONS : {len(reservations)}")
    
    reserve = 0
    revenu_total = 0
    for reser in reservations:
        if reser["Statut"] == "confirmee":
            revenu_total += reser["Prix"]   #Reveue total
            reserve += 1
    print(f"CONFIRMEE🟢  : {reserve}")
    print(f"PRIX_TAL💰 : {revenu_total}")
    
    annuler = 0
    for annul in reservations:
        if annul["Statut"] == "Annuler":
            annuler +=1
    print(f"ANNULER ❌ : {annuler}")

    #TAUX D"OCCUPATION
    if len(chambres) > 0:
        taux = (reserve / len(chambres)) * 100
        print(f"TAUX : {taux} %")
    else : 
        taux = 0
        print(f"TAUX : {taux} %")

   

def quitter():
    print("MERCI ET A BIENTOT👅")
    quit()


def menu():
    
    while True :
        menu = """
        =====================================
            -----FAIRE UNE RESERVATION-----
        =====================================
            1. ➕ Ajouter une chambre
            2. 📋 Afficher les chambres
            3. ➕ Faire une réservation
            4. 📋 Afficher les réservations
            5. 🔍 Chercher une réservation
            6. ❌ Annuler une réservation
            7. 📊 Statistiques
            8. 🚪 Quitter           
        """
        print(menu)
        choix = input("🔵CHOIX : ")

        if choix == "1":
            ajouter_une_chambre()

        elif choix == "2":
            afficher_les_chambres()
        elif choix == "3":
            faire_une_reservation()
        elif choix == "4":
            afficher_les_reseration()
        elif choix == "5":
            cherche_une_reservation()
        elif choix == "6":
            annuler_une_reservation()
        elif choix == "7":
            statistique()
        elif choix == "8":
            quitter()
        else : 
            print("❌❌❌Faire les choix entre 1-8")

if __name__== "__main__":
    menu()