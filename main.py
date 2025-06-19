import streamlit as st
import langchainhelper

st.title("🍽️ Restaurant Name & Menu Generator")

# Sidebar cuisine selection
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ["Pakistani", "Indian", "Mexican", "Chinese", "American", "Italian", "French", "Japanese", "Thai"]
)

if cuisine:
    response = langchainhelper.generate_restaurant_and_menu(cuisine)

    st.subheader("Suggested Restaurant Names:")
    for name in response['restaurant_names'].strip().split("\n"):
        st.markdown(f"- **{name.strip()}**")

    st.subheader("Delicios Menu:")
    menu_items = response['menu'].strip().split(",")
    for item in menu_items:
        st.write("- " + item.strip())
