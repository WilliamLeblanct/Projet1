import streamlit as st


st.title("Calculateur pour projets personnels (investissements et emprunts)")


st.header("Les emprunts:")

##Programme 1: Comparer le coût des intérêts
st.subheader("Comparer le coût des intérêts")

##P1: le montant emprunté
Vn = st.number_input("Quel est le montant de l'emprunt?", step = 100)

##P1: Le nombre d'année(s) de l'emprunt (durée)
nb_années = st.number_input("Quelle est la durée du prêt (en années)?", step = 1)

##P1: Le taux d'intérêt affecté au prêt
taux = st.number_input("Quel est le taux d'intérêt annuel de l'emprunt? (1% = 0.01) ", step=0.0001, min_value=0.01, max_value=0.4000)

##P1.1: formule - calcul des intérêts d'un prêt à terme
def coût_intérêts_terme(Vn, nb_années, taux):
    Vf = Vn * (1+(taux))**(nb_années)     ##Calcul du montant final versé à la fin du prêt

    return Vf-Vn                          ##Calcul du coût total en intérêts

##P1.2: formule - calcul des intérêts d'un prêt avec paiements mensuels
def coût_intérêts_mensuel(Vn, nb_années, taux):
    cap1 = 12                              ##Nombre de paiements par an
    taux_period1 = ((1+taux)**(1/cap1))-1  ##Calcul du taux d'intérêt périodique (mensuel)
    pmt1 = (Vn * taux_period1 * ((1+taux_period1)**(nb_années*cap1))) / (((1+taux_period1)**(nb_années*cap1))-1)   ##Calcul des versements périodiques (mensuels)
    int1 = (pmt1 * cap1 * nb_années) - Vn   ##Calcul du coût total en intérêts

    return int1

##P1.3: formule - calcul des intérêts d'un prêt avec paiements hebdomadaires
def coût_intérêts_hebdo(Vn, nb_années, taux):
    cap2 = 52                              ##Nombre de paiements par an
    taux_period2 = ((1+taux)**(1/cap2))-1  ##Calcul du taux d'intérêt périodique (hebdomadaire)
    pmt2 = (Vn * taux_period2 * ((1+taux_period2)**(nb_années*cap2))) / (((1+taux_period2)**(nb_années*cap2))-1)   ##Calcul des versememts périodiques (hebdomadaires)
    int2 = (pmt2 * cap2 * nb_années) - Vn  ##Calcul du coût total en intérêts

    return int2

##P1.2.1: formule - calcul des paiements mensuels
def pmt_mensuel(Vn, nb_années, taux):
    cap1 = 12                              ##Nombre de paiements par an
    taux_period1 = ((1+taux)**(1/cap1))-1  ##alcul du taux d'intérêt périodique (mensuel)
    pmt1 = (Vn * taux_period1 * ((1+taux_period1)**(nb_années*cap1))) / (((1+taux_period1)**(nb_années*cap1))-1)   ##Calcul des versements périodiques (mensuels)
    
    return pmt1

##P1.3.1: formule - calcul des paiements hebdomadaires
def pmt_hebdo(Vn, nb_années, taux):
    cap2 = 52                               ##Nombre de paiements par an (chaque début de semaine)
    taux_period2 = ((1+taux)**(1/cap2))-1   ##Calcul du taux d'intérêt périodique (hebdomadaire)
    pmt2 = (Vn * taux_period2 * ((1+taux_period2)**(nb_années*cap2))) / (((1+taux_period2)**(nb_années*cap2))-1)   ##Calcul des versements périodiques (hebdomadaires)
    
    return pmt2



##P1: Comparaison des intérêts et des versements en fonction des 3 types d'emprunts
col1, col2, col3 = st.columns(3)

##P1.Colonne 1: Emprunt à terme
with col1:
    st.caption("Emprunt à terme")
    st.write(f"Aucun paiement requis avant l'échéance.")
    st.write(f"Dans cette situation, le montant versé en intérêts sera de {coût_intérêts_terme(Vn, nb_années, taux):,.2f} $.")

##P1.Colonne 2: Emprunt avec paiements mensuels
with col2:
    st.caption("Emprunt avec paiements mensuels")
    st.write(f"Paiements mensuels de {pmt_mensuel(Vn, nb_années, taux):,.2f} $.")
    st.write(f"Dans cette situation, le montant versé en intérêts sera de {coût_intérêts_mensuel(Vn, nb_années, taux):,.2f} $.")

##P1.Colonne 3: Emprunt avec paiements hebdomadaires
with col3:
    st.caption("Emprunt avec paiements hebdomadaires")
    st.write(f"Paiements hebdomadaires de {pmt_hebdo(Vn, nb_années, taux):,.2f} $.")
    st.write(f"Dans cette situation, le montant versé en intérêts sera de {coût_intérêts_hebdo(Vn, nb_années, taux):,.2f} $.")





st.header("Les investissements:")

##Programme 2: Calculer la VAN d'un projet d'investissement
st.subheader("Calculer la VAN (valeur actuelle nette) d'un projet:")

##P2: La durée du projet (en années)
i = st.number_input("Quel est la durée du projet en années?", step = 1)

##P2: Le taux de rendement miminimal espéré (%)
r1 = st.number_input("Quel est le rendement minimal désiré pour ce projet (%) ?", 1, 50)
r1_1 = float(r1/100)

##P2: Montant emprunté ($) (si nécessaire)
emprunt = st.number_input("Est-ce qu'un emprunt à terme est nécessaire? Si oui, quelle est la somme empruntée?", step = 100)

##P2: Taux d'intérêts de l'emprunt (si nécessaire)
t = st.number_input("Quel est le taux d'intérêts de l'emprunt? (si nécessaire) (0.01 = 1%)", 0.01, 0.4)

##P2: Montant investit au départ du projet ($)
f0 = st.number_input(f"Quel est l'investissement initial nécessaire pour réaliser le projet:", step = 100)



VA1 = []     ##Liste vide pour acceuillir les flux monétaires actualisés

##P2: formule - Boucle "for" - ajuster le programme en fonction du nombre d'année(s) du projet
for i in range(i):
    fm = st.number_input(f"Entrez le flux monétaire de l'année {i+1} du projet:", step = 100)   ##Montant nets générés par le projet lors des années suivantes
    va = (fm/((1+r1_1)**(i+1)))   ##Calcul d'actualisation des flux monétaires
    VA1.append(va)                ##Ajout des flux monétaires actualisés à la liste

VAN1 = -(f0) + sum(VA1) - coût_intérêts_terme(Vn=emprunt, nb_années=i, taux=t)   ##Calcul de la VAN du projet

st.write(f"La VAN de ce projet est de {(VAN1):,.2f} $.")     ##P2: Texte pour indiquer la VAN du projet

##P2: Texte inscrit si le projet est favorable
if VAN1 < 0:
    st.write("Le projet ne devrait pas être envisagé, puisqu'il ne sont rendement est inférieur à celui espéré.")

##P2: Texte inscrit si le projet est défavorable
if VAN1 > 0:
    st.write("Le projet devrait être envisagé, puisque son rendement est suffisant considérant le rendement espéré.")






##Programme 3: Calculer la valeur future d'un placement en début de période
st.subheader("Calculer la valeur future d'un placement en début de période")

##P3: Montant investit au départ
cap_depart = st.number_input("Quel est le montant de départ?", step = 1, min_value=0)

##P3: Montant fixe versé périodiquement
pmt = st.number_input("Quel est le montant versé périodiquement?", step = 10)

##P3: Nombre de versements par an
nb_pmt_an = st.number_input("Combien de fois les versements sont-ils effectués au cours d'une année?", 1, 365)

##P3: Taux d'intérêts annuel espéré
taux5 = st.number_input("Quel est le taux de rendement annuel moyen espéré (%) ?", step =1, min_value=1, max_value=40)
taux6 = taux5/100

##P3: Durée de l'investissment en année(s)
horizon = st.number_input("Quel est l'horizon de placement en années ?", step = 1)

##P3: formule - Calcul de la valeur future du placement
def valeur_future(cap_depart, pmt, nb_pmt_an, taux6, horizon):
    R_cap = cap_depart * (1+taux6)**horizon                                   ##Calcul de la valeur future du capital de départ
    taux_period3 = ((1+taux6)**(1/nb_pmt_an))-1                               ##Cacul du taux périodique effectif (selon le nombre de versements par an)
    R_pmt = pmt * (((1+taux_period3)**(nb_pmt_an*horizon))-1)/taux_period3    ##Calcul de la valeur future des versements périodiques - Partie 1
    R_pmt2 = R_pmt*(1+taux_period3)                                           ##Calcul de la valeur future des versements périodiques - Partie 2
    return (R_cap+R_pmt2)

##P3: Inscrire la valeur future du placement
st.write(f"Le placement aura une valeur de {valeur_future(cap_depart, pmt, nb_pmt_an, taux6, horizon):,.2f} $.")



