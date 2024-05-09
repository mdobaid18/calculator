import streamlit as st

def add(x,y):
  return x+y
def sub(x,y):
  return x-y  
def multiply(x,y):
  return x*y
def divide(x,y):
  if y==0:
    return "sorry not possible"
  else:
    return x/y 
      
st.title("SIMPLE CALCULATOR")

num1= st.number_input("Enter a first number: ")
num2= st.number_input("Enter a second number: ")

choice= st.radio("select ur choice",("ADD","SUBTRACT","MULTIPLY","DIVIDE")) # radio is type of button

if choice=="ADD":
    result=add(num1,num2)
elif choice=="SUBTRACT":
    result=sub(num1,num2)
elif choice=="MULTIPLY":
    result=multiply(num1,num2)
elif choice=="DIVIDE":
    result=divide(num1,num2)
  
st.write("result is ",result)