from gasApi import create_metrics, GAS_PROVIDERS
import streamlit as st
from datetime import datetime
import time

if __name__ == '__main__':

    while True:  # Daemon Thread Architecture

        st.title("Überblick deutscher Gasspeicher")
        today = datetime.today().strftime("%d-%m-%Y")
        print(today)
        st.subheader(today)
        st.text("")
        st.text("")
        st.markdown(
            "Die Gaspreise in Deutschland steigen immens. Dadurch droht im Winter eine hohe finanzielle Belastung \n "
            "für private Haushalte. Auch die deutsche Wirtschaft bleibt hiervon nicht unberührt und ist gefährdet. \n"
            " Diese Situation erfordert Verbundenheit, Weitsicht und Sicherheit. Diese tägliche Übersicht "
            "der deutschen Gasspeicher soll uns daran erinnern, dass jeder Einzelne zum Gemeinwohl "
            "Deutschlands beitragen kann. So verbraucht 11-minütiges Duschen 6,1 kWh. **Verzichten wir an einem Tag darauf sparen wir alle als Gemeinschaft"
            " 506,30 GWh/Tag ein**.")
        st.text("")
        st.text("")
        st.markdown("###### In einer echten Gemeinschaft wird aus vielen Ich ein Wir. \n"
                    "Erwin Ringel")
        st.markdown("***")
        st.text("")
        st.write("")
        
        st.subheader("Füllstände einzelner Gasspeicher in Deutschland")
        create_metrics(GAS_PROVIDERS)

        with st.expander("Siehe Quelle"):
            st.write("https://agsi.gie.eu/")

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
        st.caption("Philipp Ganster © | contact me via www.linkedin.com/in/pganster")
        time.sleep(60 * 60 * 10)  # Request API data every 10 hours
