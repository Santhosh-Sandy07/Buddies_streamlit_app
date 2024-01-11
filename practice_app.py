import streamlit as st
import pandas as pd
import random

# Sample data for demonstration purposes
user_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 28, 24, 27, 26],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
})

# Function to find a match
def find_match(user_id):
    other_users = user_data[user_data.index != user_id]
    return random.choice(other_users.index)

# Streamlit app
def main():
    st.title('Simple Dating App')

    # User registration
    st.sidebar.header('User Registration')
    name = st.sidebar.text_input('Enter your name:')
    age = st.sidebar.number_input('Enter your age:', min_value=18, max_value=99)
    gender = st.sidebar.radio('Select your gender:', ['Male', 'Female'])

    if st.sidebar.button('Register'):
        user_data.loc[len(user_data)] = [name, age, gender]

    # Display registered users
    st.subheader('Registered Users')
    st.table(user_data)

    # Matchmaking
    user_id = st.sidebar.selectbox('Select your user ID:', user_data.index)
    st.sidebar.text(f'Hello, {user_data.loc[user_id]["Name"]}!')

    if st.sidebar.button('Find Match'):
        match_id = find_match(user_id)
        match_name = user_data.loc[match_id]['Name']
        st.success(f'Congratulations! You matched with {match_name}!')

if __name__ == '__main__':
    main()
