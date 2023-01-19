import streamlit

streamlit.title('my perants new helthy diner')

streamlit.header('breakfast manu')

streamlit.text('🥣omega 3 & blueberry oatmeal')

streamlit.text('🥗kale,Spinach & Rocker Smoothie')

streamlit.text('🐔Hard boiled Free-Range Egg')

streamlit.text('🥑🍞Avocardo Tost')
   
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")  
streamlit.dataframe(my_fruit_list)
