import streamlit as st
import pandas as pd
import numpy as np

# print("Hello")

st.title("Welcome To the Streamlit Test Pages")
# st.header("Hello World...!")


st.header("Below is the Test Data")
data = {'Fruit': ['Apple','Banana','Orange','Mango'],
        'Weight':[200,150,300,250],
        'Price':[90,40,100,50]
        }
df= pd.DataFrame(data)
st.write(df)

st.header("Chart for the random values :- ")
random_data = pd.DataFrame(
    np.random.randint(0, 100, size=(50, 3)),
)
st.line_chart(random_data)

# Function to add the Button on FE
st.link_button(url='https://github.com/IshanJoshi92',label='Click Here to redirect on My GitHub accnt!')
# st.bar_chart(random_data)
# new_msg = st.chat_input("Enter Your msg here")
# st.write(new_msg)

# num1 = int(input())
# num2 = int(input())
num1 = st.chat_input("Enter First Number")
check = st.checkbox(label='Check')

if check==True:
    st.write("Checking done")
    st.status(label=' Current Status',state='complete')
else: st.write ("Checking pending")
if num1 is None:
    pass
else:
    st.write(f"The first entered number is {num1}")
# else:
#     st.write("Please Enter the Numerical Input")

new_input = st.text_input(label="Give Input",key='safsf')
# st.write(type(new_input))
if new_input == None:
    st.write('')
elif new_input == 'Ishan':
    st.write(new_input)
else :
    st.write("You are not Ishan")
