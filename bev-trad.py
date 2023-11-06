import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
def main():
    # Input
    st.title("Confronto Costi Auto Elettrica vs. Auto a Combustione")
    costo_auto_combustione = st.number_input("Inserisci il costo dell'auto a combustione: ")
    costo_auto_elettrica = st.number_input("Inserisci il costo dell'auto elettrica: ")
    km_annuali = st.number_input("Inserisci il numero di chilometri percorsi annualmente: ")
    costo_rifornimento_combustione = st.number_input("Inserisci il costo al litro per il rifornimento dell'auto a combustione: ")
    costo_ricarica_casa = st.number_input("Inserisci il costo di ricarica elettrica a casa (costo al Kwh): ")
    costo_ricarica_colonnina = st.number_input("Inserisci il costo di ricarica elettrica in colonnina fast (costo al Kwh): ")
    ricarica_casa_percentuale = st.slider("Fornisci una stima percentuale approssimativa che indichi la proporzione di ricarica effettuata a casa:", min_value=0, max_value=100, value=0, step=1)


    anni_utilizzo= st.number_input("Per quanto tempo vuoi usare quest'auto (anni)? ")
    kwh_100= st.number_input("Quanti kwh consuma l'auto elettrica ogni 100 km? ")
    Litri=st.number_input("Quanti litri di carburante consuma l'auto a combustione ogni 100km? ")
    costo_assicurazione_combustione = st.number_input("Inserisci il costo dell'assicurazione per l'auto a combustione: ")
    costo_assicurazione_elettrica = st.number_input("Inserisci il costo dell'assicurazione per l'auto elettrica: ")
    costo_bollo_combustione = st.number_input("Inserisci il costo del bollo per l'auto a combustione: ")
    costo_bollo_elettrica = st.number_input("Inserisci il costo del bollo per l'auto elettrica: ")
    costo_manutenzione_combustione = st.number_input("Inserisci una stima del costo di manutenzione annuale per l'auto a combustione: ")
    costo_manutenzione_elettrica = st.number_input("Inserisci una stima del costo di manutenzione annuale per l'auto elettrica: ")
    costo_tagliando_combustione = st.number_input("Inserisci il costo di un tagliando per l'auto a combustione: ")
    costo_tagliando_elettrica = st.number_input("Inserisci il costo di un tagliando per l'auto elettrica: ")
    costo_wallbox = st.number_input("Inserisci il costo del wallbox per l'auto elettrica: ")
    costo_installazione_wallbox = st.number_input("Inserisci il costo di installazione del wallbox: ")
    Detrazione= st.slider("inserisci se c'è una detrazione per il wallbox e l'installazione in termini percentuali ", min_value=0, max_value=100, value=0, step=1)

    if st.button("Calcola"):
        # Calcolo dei costi auto elettrica
        ricarica_casa = ricarica_casa_percentuale / 100  # Converte la percentuale in frazione
        calcolo_kwh=kwh_100*km_annuali/100
        costo_ricarica_annuale=ricarica_casa*costo_ricarica_casa*calcolo_kwh+(1-ricarica_casa)*calcolo_kwh*costo_ricarica_colonnina
        Detrazione=Detrazione/100
        costo_fisso_auto_elettrica=costo_auto_elettrica+costo_wallbox*(1-Detrazione)+costo_installazione_wallbox*(1-Detrazione)
        costo_variabile_auto_elettica=costo_ricarica_annuale+costo_assicurazione_elettrica+costo_bollo_elettrica+costo_manutenzione_elettrica+costo_tagliando_elettrica

        #Calcolo dei costi auto a combustione
        calcolo_litri=km_annuali*Litri/100
        costo_fisso_auto_combustione=costo_auto_combustione
        costo_variabile_auto_combustione=costo_rifornimento_combustione*calcolo_litri+costo_assicurazione_combustione+costo_bollo_combustione+costo_manutenzione_combustione+costo_tagliando_combustione

        #calcolo break event
        BEP=(costo_fisso_auto_combustione-costo_fisso_auto_elettrica)/(costo_variabile_auto_elettica-costo_variabile_auto_combustione)

        #costo complessivo auto elettrica
        costo_complessivo_auto_elettrica=costo_variabile_auto_elettica*anni_utilizzo+costo_fisso_auto_elettrica

         #costo complessivo auto combustione
        costo_complessivo_auto_combustione=costo_variabile_auto_combustione*anni_utilizzo+costo_fisso_auto_combustione


        # Confronto dei costi variabili
        if costo_variabile_auto_combustione < costo_variabile_auto_elettica:
            meno_costosa = "a combustione"
            risparmio = costo_variabile_auto_elettica - costo_variabile_auto_combustione
             #calcolo risparmio costi variabili
            risparmio_variabile=1-costo_variabile_auto_combustione/costo_variabile_auto_elettica
        else:
            meno_costosa = "elettrica"
            risparmio = - costo_variabile_auto_elettica + costo_variabile_auto_combustione
            #calcolo risparmio costi variabili
            risparmio_variabile=1-costo_variabile_auto_elettica/costo_variabile_auto_combustione

        #confronto su BEP
        if BEP>anni_utilizzo:
          vantaggio="auto a combustione"
        else:
          BEP<anni_utilizzo
          vantaggio="auto elettrica"

        # Output
        st.write("\nRisultati del confronto:")
        st.write(f"Costo variabile annuale dell'auto a combustione: €{round(costo_variabile_auto_combustione, 2)}")
        st.write(f"Costo variabile annuale dell'auto elettrica: €{round(costo_variabile_auto_elettica, 2)}")
        st.write(f"L'auto meno costosa da gestire annualmente è quella {meno_costosa}")
        st.write(f"Risparmio annuale: €{round(risparmio, 2)}")
        st.write(f"Risparmio annuale in termini percentuali: {round(risparmio_variabile * 100)}%")
        st.write(f"Break even (anni): {round(BEP, 2)} anni")
        st.write(
            f"Costo totale auto elettrica dopo {anni_utilizzo:.2f} anni di utilizzo: €{round(costo_complessivo_auto_elettrica, 2)}")
        st.write(
            f"Costo totale auto a combustione dopo {anni_utilizzo:.2f} anni di utilizzo: €{round(costo_complessivo_auto_combustione, 2)}")
        st.write(
            f"In termini di BEP, analizzando sia costi fissi che costi variabili, in {round(anni_utilizzo, 2)} anni, alla luce dei parametri imposti come ipotesi è più conveniente acquistare un'{vantaggio}")

        anni = np.arange(int(anni_utilizzo) + 1)
        costi_auto_elettrica = [costo_fisso_auto_elettrica + anno * costo_variabile_auto_elettica for anno in anni]
        costi_auto_combustione = [costo_fisso_auto_combustione + anno * costo_variabile_auto_combustione for anno in anni]

        labels = ['Auto Elettrica', 'Auto a Combustione']

        costo_fisso = [costo_fisso_auto_elettrica, costo_fisso_auto_combustione]
        costo_variabile = [costo_variabile_auto_elettica * anni_utilizzo,
                           costo_variabile_auto_combustione * anni_utilizzo]

        fig_bar = go.Figure()

        fig_bar.add_trace(go.Bar(
            x=['Costi Fissi', 'Costi Variabili'],
            y=[costo_fisso[1], costo_variabile[1]],
            name='Auto a Combustione'
        ))

        fig_bar.add_trace(go.Bar(
            x=['Costi Fissi', 'Costi Variabili'],
            y=[costo_fisso[0], costo_variabile[0]],
            name='Auto Elettrica'
        ))

        fig_bar.update_layout(barmode='group', title='Suddivisione Costi Totali (Fissi + Variabili)',
                              yaxis_title='Costo in Euro')

        st.plotly_chart(fig_bar)

        # Grafico Plotly a linee
        anni = np.arange(int(anni_utilizzo) + 1)
        fig_line = go.Figure()

        fig_line.add_trace(go.Scatter(
            x=anni,
            y=costi_auto_elettrica,
            mode='lines+markers',
            name='Auto Elettrica'
        ))

        fig_line.add_trace(go.Scatter(
            x=anni,
            y=costi_auto_combustione,
            mode='lines+markers',
            name='Auto a Combustione'
        ))

        fig_line.update_layout(title='Confronto Costi Auto Elettrica vs. Auto a Combustione',
                               xaxis_title='Anni',
                               yaxis_title='Costo in Euro')

        st.plotly_chart(fig_line)


if __name__ == "__main__":
    main()

