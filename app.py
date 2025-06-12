import streamlit as st

st.title("Calcolatore proporzione pasta cotta")

# Inserimento dei valori come testo per permettere il campo vuoto
a = st.text_input("Pasta non cotta totale", value="", placeholder="es. 220g")
b = st.text_input("Pasta cotta totale", value="", placeholder="es. 350g")
c = st.text_input("Pasta non cotta Mari", value="", placeholder="di solito 60g")
d = st.text_input("Pasta non cotta Fra", value="", placeholder="di solito sui 160g (adora mangiare)")

# Controlla che tutti i campi siano stati riempiti e siano numerici
if all([a, b, c, d]):
    try:
        a = float(a.replace(",", "."))
        b = float(b.replace(",", "."))
        c = float(c.replace(",", "."))
        d = float(d.replace(",", "."))
        if a > 0:
            # Calcolo proporzione
            pasta_cotta_Mari = (c / a) * b
            pasta_cotta_Fra = (d / a) * b

            # Output
            st.subheader("Ecco quanta pasta dobbiamo mangiaree!!")
            st.markdown("### 🍝")
            st.write(f"Pasta cotta per Mari: **{pasta_cotta_Mari:.2f}g**")
            st.write(f"Pasta cotta per Fra: **{pasta_cotta_Fra:.2f}g**")
        else:
            st.warning("Inserisci un valore maggiore di zero per 'Pasta non cotta totale'.")
    except ValueError:
        st.warning("Inserisci solo valori numerici validi (usa il punto o la virgola per i decimali).")
else:
    st.info("Inserisci quanta pasta hai calato e vuoi mangiare per vedere i risultati")
