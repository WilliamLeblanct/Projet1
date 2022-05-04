import streamlit as st

st.title("Calculateur des intérêts sur plusieurs types d'emprunts")

st.write("Ce programme permet de calculer le montant d'intérêts versés lors d'un emprunt à terme, en surplus du montant emprunté!")


Vn = st.sidebar.number_input("Quel est le montant de l'emprunt?", step = 100)

nb_années = st.sidebar.number_input("Quelle est la durée du prêt (en années)?", step = 1)

taux = st.sidebar.number_input("Quel est le taux d'intérêts de l'emprunt? (1% = 0.01) ", 0.01, 0.40)



def coût_en_intérêts(Vn, nb_années, taux,):
    Vf = Vn * (1+taux)**(nb_années)  ##Valeur totale de l'emprunt (avec intérêts)

    return Vf-Vn          ##Somme des parts d'intérêt payés

st.write(f"Dans cette situation, le montant versé en intérêts sera de: {coût_en_intérêts(Vn, nb_années, taux):,.2f} $")




