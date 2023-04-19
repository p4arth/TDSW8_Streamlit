import streamlit as st

def largest_number(a, b, c):
    """
    Returns the largest number among the three given numbers.
    """
    return max(a, b, c)

st.title("Find the Largest Number")
st.write("Enter three numbers below to find the largest among them.")

# Input fields for the three numbers
num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)
num3 = st.number_input("Enter the third number", value=0, step=1)

# Call the largest_number function to get the largest number
largest = largest_number(num1, num2, num3)

# Display the largest number
st.write("The largest number is:", largest)
