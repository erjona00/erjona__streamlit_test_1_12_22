import streamlit as st

#1: Take this input as a string. (hint: you can use st.text_input )
str = st.text_input("Enter the string: ")

#2: Declare a function called “convert_list”  that takes this string 
# and returns a list of words from this string.(hint: you can use .split() method ).
#  Connect this function with a button called “Return List”.
# When you press this button list of words is printed on streamlit.
#  (hint: you can use st.write() )
def convert_list(str):
    return str.split()

if st.button("Return List"):
    list = convert_list(str)
    st.write(list)

#3:  Declare another function called “convert_lower” 
# that takes the list from the function called “convert_list”
#  and converts them to a list with all upper case.(hint: you need to use for loop, .lower() and .append() methods ). 
# Connect this function to a button called “upper” that activates
#  this function and prints te result.(hint: you need to use st.
def convert_lower(list):
    list1 = []
    for element in list:
        list2.append(element.upper())
    return list1
list1 = convert_lower(list)
upper_btn = st.button("upper")
if upper_btn:
    st.write(list1)

#4: Declare a function called ‘count” that returns the number of elements in the list .
#Connect this function to a button called “print_count”.
# This button will print the number of elements generated from the function “count”(hint: you can use st.write)
def count(list):
    count = 0
    for element in list:
        count += 1
    return count
count_btn = st.button("print_count")
length = count(list)
if count_btn:
    st.write("This list has " + str(length) + " elements.")