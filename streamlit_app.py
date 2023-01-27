import streamlit

streamlit.title('my perants new helthy diner')

streamlit.header('breakfast manu')

streamlit.text('🥣omega 3 & blueberry oatmeal')

streamlit.text('🥗kale,Spinach & Rocker Smoothie')

streamlit.text('🐔Hard boiled Free-Range Egg')

streamlit.text('🥑🍞Avocardo Tost')

streamlit.title('Build Your Own Fruit Smooothie')
   
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")  

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('fruityvice fruit advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains")
streamlit.dataframe(my_data_rows)



