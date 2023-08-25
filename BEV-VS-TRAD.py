import matplotlib.pyplot as plt
def main():
    # Input
    costo_auto_combustione = float(input("Inserisci il costo dell'auto a combustione: "))
    costo_auto_elettrica = float(input("Inserisci il costo dell'auto elettrica: "))
    km_annuali = int(input("Inserisci il numero di chilometri percorsi annualmente: "))
    costo_rifornimento_combustione = float(input("Inserisci il costo al litro per il rifornimento dell'auto a combustione: "))
    costo_ricarica_casa = float(input("Inserisci il costo di ricarica elettrica a casa (costo al Kwh): "))
    costo_ricarica_colonnina = float(input("Inserisci il costo di ricarica elettrica in colonnina fast (costo al Kwh): "))
    ricarica_casa = float(input("fornisci una stima percentuale approssimativa che indichi la proporzione di ricarica effettuata a casa: "))
    anni_utilizzo= float(input("Per quanto tempo vuoi usare quest'auto (anni)? "))
    kwh_100= float(input("Quanti kwh consuma l'auto elettrica ogni 100 km? "))
    Litri=float(input("Quanti litri di carburante consuma l'auto a combustione ogni 100km? "))
    costo_assicurazione_combustione = float(input("Inserisci il costo dell'assicurazione per l'auto a combustione: "))
    costo_assicurazione_elettrica = float(input("Inserisci il costo dell'assicurazione per l'auto elettrica: "))
    costo_bollo_combustione = float(input("Inserisci il costo del bollo per l'auto a combustione: "))
    costo_bollo_elettrica = float(input("Inserisci il costo del bollo per l'auto elettrica: "))
    costo_manutenzione_combustione = float(input("Inserisci una stima del costo di manutenzione annuale per l'auto a combustione: "))
    costo_manutenzione_elettrica = float(input("Inserisci una stima del costo di manutenzione annuale per l'auto elettrica: "))
    costo_tagliando_combustione = float(input("Inserisci il costo di un tagliando per l'auto a combustione: "))
    costo_tagliando_elettrica = float(input("Inserisci il costo di un tagliando per l'auto elettrica: "))
    costo_wallbox = float(input("Inserisci il costo del wallbox per l'auto elettrica: "))
    costo_installazione_wallbox = float(input("Inserisci il costo di installazione del wallbox: "))
    Detrazione= float(input("inserisci se c'è una detrazione per il wallbox e l'installazione in termini percentuali "))


    # Calcolo dei costi auto elettrica
    calcolo_kwh=kwh_100*km_annuali/100
    costo_ricarica_annuale=ricarica_casa*costo_ricarica_casa*calcolo_kwh+(1-ricarica_casa)*calcolo_kwh*costo_ricarica_colonnina
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
    print("\nRisultati del confronto:")
    print(f"Costo variabile annuale dell'auto a combustione: {costo_variabile_auto_combustione:.2f} euro")
    print(f"Costo variabile annuale dell'auto elettrica: {costo_variabile_auto_elettica:.2f} euro")
    print(f"L'auto meno costosa da gestire annualmente è quella {meno_costosa}")
    print(f"Risparmio annuale: {risparmio:.2f} euro")
    print(f"Risparmio annuale in termini percentuali: {risparmio_variabile:.0%}")
    print(f"Break even (anni): {BEP:.2f} anni")
    print(f"Costo totale auto elettrica dopo {anni_utilizzo:.2f} anni di utilizzo: {costo_complessivo_auto_elettrica:.2f} euro")
    print(f"Costo totale auto a combustione dopo {anni_utilizzo:.2f} anni di utilizzo: {costo_complessivo_auto_combustione:.2f} euro")
    print(f"In termini di BEP, analizzando sia costi fissi che costi variabili, in {anni_utilizzo: .2f} anni, alla luce dei parametri imposti come ipotesi è più conveniente acquistare un'{vantaggio}")

    anni = list(range(int(anni_utilizzo) + 1))
    costi_auto_elettrica = [costo_fisso_auto_elettrica + anno * costo_variabile_auto_elettica for anno in anni]
    costi_auto_combustione = [costo_fisso_auto_combustione + anno * costo_variabile_auto_combustione for anno in anni]

    labels = ['Auto Elettrica', 'Auto a Combustione']

    costo_fisso = [costo_fisso_auto_elettrica, costo_fisso_auto_combustione]
    costo_variabile = [costo_variabile_auto_elettica * anni_utilizzo, costo_variabile_auto_combustione * anni_utilizzo]

    plt.figure(figsize=(24, 12))

    plt.subplot(1, 2, 1)
    plt.bar(labels, costo_fisso, color='blue', label='Costi Fissi')
    plt.bar(labels, costo_variabile, bottom=costo_fisso, color='orange', label='Costi Variabili')
    plt.xlabel('Tipo di Auto')
    plt.ylabel('Costo Totale in Euro')
    plt.title('Suddivisione Costi Totali (Fissi + Variabili) delle Auto Elettrica e a Combustione')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(anni, costi_auto_elettrica, label='Auto Elettrica', marker='o')
    plt.plot(anni, costi_auto_combustione, label='Auto a Combustione', marker='o')

    plt.xlabel('Anni')
    plt.ylabel('Costo in Euro')
    plt.title('Confronto Costi Auto Elettrica vs. Auto a Combustione')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()

