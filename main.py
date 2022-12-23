import streamlit as st

#1: Take this input as a string. (hint: you can use st.text_input )
input_txt = st.text_input("Enter the string: ")

#2: Declare a function called “convert_list”  that takes this string 
# and returns a list of words from this string.(hint: you can use .split() method ).
#  Connect this function with a button called “Return List”.
# When you press this button list of words is printed on streamlit.
#  (hint: you can use st.write() )
def convert_list(input_txt):
    str_list = str.split(input_txt)
    return str_list
list = convert_list(input_txt)
list_elements = st.button("Return List")
if list_elements:
    st.write(list)

#3:  Declare another function called “convert_lower” 
# that takes the list from the function called “convert_list”
#  and converts them to a list with all upper case.(hint: you need to use for loop, .lower() and .append() methods ). 
# Connect this function to a button called “upper” that activates
#  this function and prints te result.(hint: you need to use st.
def convert_lower(list):
    listt = []
    for element in list:
        listt.append(element.upper())
    return listt
listt = convert_lower(list)
upper_elements = st.button("upper")
if upper_elements:
    st.write(listt)

#4: Declare a function called ‘count” that returns the number of elements in the list .
#Connect this function to a button called “print_count”.
# This button will print the number of elements generated from the function “count”(hint: you can use st.write)
def count(list):
    count = 0
    for element in list:
        count += 1
    return count
count_elements = st.button("Print")
length = count(list)
if count_elements:
    st.write("This list has " + str(length) + " elements.")