#apis
# import requests


 
# print("***RHYMING WORD GENERATOR*****")

# endpoint = f"https://api.datamuse.com/words?ml=i%20am%20student"
 
# response = requests.get(endpoint)
 
# data = response.json()
 
# if response.status_code == 200:
#     for item in data:
#         print(item.get('tags'))


# #question2
# import requests

 
# print("***RHYMING WORD GENERATOR*****")
# choice = input('Enter a word:')
# endpoint = f"https://api.datamuse.com/words?rel_jjb=ocean"
 
# response = requests.get(endpoint)
 
# data = response.json()
 
# if response.status_code == 200:
#     for item in data:
#         if score > 950: 
        
#          print(item.get('word'))

import streamlit as st
import requests


st.title("Rhyming Words Finder")

word = st.text_input("Enter a word", placeholder="Eg. hipopatamus")
is_clicked = st.button("Generate", type='primary')

if is_clicked:
    endpoint = f"https://api.datamuse.com/words?sp=hipopatamus"
    response = requests.get(endpoint)

    data = response.json()

    if response.status_code == 200:
        for item in data:
            st.write(item.get('word'))
    else:
        st.toast("Something went wrong")


