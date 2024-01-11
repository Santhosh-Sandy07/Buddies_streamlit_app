import streamlit as st
import streamlit.components.v1 as components
import random

# JavaScript code for moving the button on hover
js_move_button = """
const button = document.getElementById("no_button");

button.addEventListener("mouseover", function() {
    const x = Math.random() * 80;
    const y = Math.random() * 80;
    button.style.position = "absolute";
    button.style.left = x + "vw";
    button.style.top = y + "vh";
});
"""

# Streamlit app
def main():
    st.title("Interactive Buttons")

    # Display the YES button
    if st.button("YES"):
        st.success("You clicked YES!")

    # Display the NO button with custom JavaScript for movement
    components.html('<button id="no_button" style="position: relative;">NO</button>', height=50)
    st.markdown(f'<script>{js_move_button}</script>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
