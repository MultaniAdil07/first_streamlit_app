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
   fruit_choise = streamlit.text_input('what fruit would you like to get informtion about?')
   if not fruit_choice:
      streamlit.error("please select a fruit to get information")
   else:
      fruityvice_response = request.get("https://fruityvice.com/api/fruit/" + frui_choice)
      fruityvice_normalized = panda.json_normalized(fruityvice_responase.json())
       streamlit.dataframe(fruityvice_normalized)
                                        
 except URLError as e:
        streamlit.error()

#don't run anything past here while we troubleshoot
stremlit.stop();

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like add ?')
streamlit.write('thanks for adding', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from stremlit')")

