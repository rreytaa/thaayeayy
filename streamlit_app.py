import streamlit as st

st.title("🎈thaayeayy 🐨 ")
st.write(
    "mapupupusyalala"
)
st.image("IMG_7026.jpg",width=200)
st.header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0: 
  st.write (f"{angka} adalah bilangan genap")
else:
st.write (f"{angka} adalah bilangan genap")
else:
st.write (f"{angka} adalah bilangan ganjil") 
