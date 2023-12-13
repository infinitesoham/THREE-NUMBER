import streamlit as st

def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Maximum Finder")

    # Input for three numbers
    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    # Button to find maximum
    if st.button("Find Maximum"):
        result = find_maximum(num1, num2, num3)
        st.success(f"The maximum among {num1}, {num2}, and {num3} is: {result}")

if __name__ == "__main__":
    main()