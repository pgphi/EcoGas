from gasApi import create_metrics, GAS_PROVIDERS
from predictions import make_prediction
import streamlit as st
from datetime import datetime, date
import time

if __name__ == '__main__':

    while True:  # Daemon Thread Architecture

        st.title("Überblick Deutscher Gasspeicher")
        today = datetime.today().strftime("%d-%m-%Y")
        print(today)
        st.subheader(today)
        st.text("")
        st.text("")

        st.markdown(
            "Die Gaspreise in Deutschland steigen - immens. Dadurch droht im Winter eine hohe finanzielle Belastung \n "
            "für private Haushalte und eine Gefahr für die deutsche Wirtschaft. Um diese Situation angemessen zu bewältigen, werden Werte \n"
            " wie Verbundenheit, Weitsicht und Sicherheit von uns gefordert. Verständnis, Klarheit und Betroffenheit sind hier drei Wegweiser, die diesen"
            " Wertewandel vorantreiben. Hier setzt diese Bildungsinitiative aus dem Edtech-Bereich an.")
        st.text("")
        st.markdown("**Beispielsweise verbraucht 10-minütiges"
            " Duschen 6,1 kWh. Für einen Einzelnen mag das wenig erscheinen. Für eine Gemeinschaft bedeutet das 506,30 GWh/Tag einzusparen**.")
        st.text("")
        st.text("")
        st.text("In einer echten Gemeinschaft wird aus vielen Ich ein Wir.")
        st.write("Erwin Ringel")
        st.markdown("***")
        st.text("")
        st.subheader("Gaspreisentwicklung in Abhängigkeit der Füllstände")
        st.text("")
        st.text("")
        st.image("Images/Entwicklung.png")
        st.text("")
        st.markdown("***")
        st.subheader("Mit welchen Gaskosten sollten wir rechnen?")

        number = st.number_input(
            'Tragen Sie ihren vergangenen bzw. momentanen Gasverbrauch ein z.B. 10000kWh:')  # i.e. number = 10000

        date = st.date_input(
            "Zu welchem Zeitpunkt möchten Sie ihre Gaskosten vorhersagen z.B. am 31.12.2022?",
            date(2019, 7, 6))  # i.e. date = "2022/08/01"

        error = 0.008515221391126407 # mae price related
        costs = make_prediction(date, number, error)[0]
        cost_variance = make_prediction(date, number, error)[1]

        if st.button('Kosten berechnen'):

            my_bar = st.progress(0)

            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1)

            st.write(f'Die ungefähren Gaskosten werden {costs} Euro betragen am {date}.')
            st.write(
                f'Aufgrund von Ungenauigkeiten im Model können Abweichungen von ca. +- {cost_variance} Euro auftreten.')
            st.write(
                'Berücksichtigen Sie außerdem Steuerersparnisse, kurzfristige Änderungen und andere externe Faktoren, die sich auf die Kosten auswirken können.')
            st.write("Für weitere Informationen siehe:")
            st.write("https://www.bundesregierung.de/breg-de/themen/klimaschutz/energiemarkt-stabilisieren-2059778")
        st.text("")
        st.text("")
        st.text("")
        st.subheader("Füllstände einzelner Gasspeicher in Deutschland")
        st.text("")
        st.markdown("***")
        st.text("")

        create_metrics(GAS_PROVIDERS)

        with st.expander("Siehe Quelle"):
            st.write("https://agsi.gie.eu/")
            st.write("Für mehr Informationen zum Gasstand siehe:")
            st.write("https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Versorgungssicherheit/aktuelle_gasversorgung/start.html")
        st.text("")
        st.text("")

        st.subheader("Tipps zum Gas sparen")

        tab1, tab2, tab3 = st.tabs(["Duschen", "Kochen und Backen", "Temperatur reduzieren"])

        with tab1:
            st.subheader("Duschen statt Baden")
            st.write("Durch das Duschen anstelle eines Vollbades sinkt der Wasser und Stromverbrauch erheblich."
                     " Durch ein Sparduschkopf kann der Verbrauch zusätzlich minimiert werden.")
            st.image("Images/Duschen.jpg", width=300)

        with tab2:
            st.subheader("Sparsam Kochen und Backen")
            st.write(
                "Gerade im Winter ist es schwierig auf das Backen zu verzichten. Vorheizen können wir uns jedoch sparen."
                " So sparen wir bis zu 20% an Energie. Benötigen Sie heißes Wasser beim Kochen, nutzen sie einen Wasserkocher."
                " Das senkt den Energieverbrauch nochmal erheblich.")
            st.image("Images/Kochen.jpg", width=300)

        with tab3:
            st.subheader("Allgemein gilt: Temperatur reduzieren")
            st.write("Gas als Energiequelle benötigen wir, um Wärme zu erzeugen und zu erhalten. Vor allem in kälteren"
                     " Zeiten sollten wir unsere Temperatur bedacht regeln, um zu hohe Kosten zu vermeiden.")
            st.image("Images/Temperatur.jpg", width=300)

        with st.expander("Weitere Tipps"):
            st.write("Siehe Bundesministerium für Wirtschaft und Klimaschutz:")
            st.write(
                "https://www.energiewechsel.de/KAENEF/Navigation/DE/Thema/energiespartipps.html?etcc_cmp=energiewechsel&etcc_med=sea&etcc_par=google-ads&etcc_ctv=energieeffizienz-energie-sparen")
        st.markdown("***")
        st.caption("Philipp Ganster © www.linkedin.com/in/pganster")
        time.sleep(60 * 60 * 24)  # Request API data every 10 hours
