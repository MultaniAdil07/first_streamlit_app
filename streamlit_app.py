import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my perants new helthy diner')
streamlit.header('breakfast manu')
streamlit.text('🥣omega 3 & blueberry oatmeal')
streamlit.text('🥗kale,Spinach & Rocker Smoothie')
streamlit.text('🐔Hard boiled Free-Range Egg')
streamlit.text('🥑🍞Avocardo Tost')
streamlit.title('Build Your Own Fruit Smooothie')
   
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")  
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#new section to display fruitvice api responce 
streamlit.header('Fruityvice Advice')
try:
   fruit_choice = streamlit.text_input('what fruit would you like to get informtion about?')
   if not fruit_choice:
        streamlit.error("please select a fruit to get information")
   else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)

except URLError as e:
   streamlit.error()
 
#create repateble code block (called a funtion)
def get_fruityvice_data(this_fruit_choice);
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#new section to display fruitvice api responce 
streamlit.header('Fruityvice Advice!')
try:
   fruit_choice = streamlit.text_input('what fruit would you like to get informtion about?')
   if not fruit_choice:
        streamlit.error("please select a fruit to get information")
   else:
       back_from_function = get_fruityvice_data (fruit_choice)
       streamlit.dataframe(back_from_function)
