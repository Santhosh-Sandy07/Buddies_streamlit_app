import streamlit as st
import time
import random

def move_button():
    # Random initial position
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    button_location = st.empty()

    while True:
        # Display the button at the current position
        button = st.button('NO', key='no_button', on_click=st.stop)
        button_location.button_area.button_components[0].plotly_chart({'data': []}, use_container_width=True)
        button_location.button_area.button_components[0].update_layout(
            {'xaxis': {'range': [x, x + 0.1]}, 'yaxis': {'range': [y, y + 0.1]}}
        )

        # Update position every 0.5 seconds
        time.sleep(0.5)
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

if __name__ == '__main__':
    move_button()
