import streamlit as st
st.set_page_config(layout="wide",page_title="Taxi Management system",page_icon=":taxi:")
import pandas as pd
import numpy as np
import time
from datetime import datetime

pages=["Welcome","User Management","Driver Management","Add Bookings","View Past Bookings","Clear Records"]

def verify_userid(id):
	users=pd.read_csv('users.csv',index_col=0)
	for i in users["User ID"]:
		if(str(i)==id):
			return True
	return False
def verify_empid(id):
	drivers=pd.read_csv('drivers.csv',index_col=0)
	for i in drivers["Employee ID"]:
		if(str(i)==id):
			return True
	return False
def verify_bookid(id):
	drivers=pd.read_csv('bookings.csv',index_col=0)
	for i in drivers["Booking ID"]:
		if(str(i)==id):
			return True
	return False


def welcome():
	st.title("Welcome to Taxi Management Portal")
	st.header("Server IN | :flag-in:")
	st.write("Manage various databases in a convenient and interactive method. Hassle-free and Super-Quick. Grow and Manage your business in the smart way.")
	st.image('taxi.jpg',use_column_width=True)


def page_bookings():
	st.title("Booking History")
	bookings=pd.read_csv('bookings.csv',index_col=0)
	st.table(bookings)

def page_users():
	st.title("Users' Management")
	option = st.selectbox('Select an action',('View Users', 'Add User', 'Remove A User'))
	if(option=="View Users"):
		users=pd.read_csv('users.csv',index_col=0)
		st.table(users)
	if(option=='Add User'):
		st.header("Enter User Info:")
		form = st.form(key="my-form")
		name = form.text_input("Name")
		user_id=form.text_input("User ID")
		phone_number=form.text_input("Phone Number")
		submit = form.form_submit_button('Submit')
		if submit:
			if(verify_userid(user_id)):
				st.error("User ID exists")
			else:
				users=pd.read_csv('users.csv',index_col=0)
				data_to_add=[{'Name':name,'User ID':user_id,'Phone':phone_number}]
				tempdf=pd.DataFrame(data_to_add)
				users=users.append(tempdf, ignore_index=True)
				users.index+=1
				users.to_csv('users.csv')
				st.success("Added User")
	if(option=='Remove A User'):
		st.header("Enter User ID to remove a user:")
		form = st.form(key="my-form")
		user_id=form.text_input("User ID")
		submit = form.form_submit_button('Submit')
		if submit:
			if(not(verify_userid(user_id))):
				st.error("User ID does not exist")
			else:
				data = pd.read_csv("users.csv", index_col =0)
				sets=[]
				k=1
				for i in (data["User ID"]):
					if(str(i)==user_id):
						sets.append(k)
					k+=1
				data.drop(sets, inplace = True)
				data=data.reset_index(drop=True)
				data.index+=1
				data.to_csv('users.csv')
				st.success("User Removed")


def page_users_root():
	st.title("Users' Management")
	option = st.selectbox('Select an action',('View Users', 'Add User', 'Remove A User'))
	if(option=="View Users"):
		users=pd.read_csv('users.csv',index_col=0)
		st.table(users)
	if(option=='Add User'):
		st.header("Enter User Info:")
		form = st.form(key="my-form")
		name = form.text_input("Name")
		user_id=form.text_input("User ID")
		phone_number=form.text_input("Phone Number")
		submit = form.form_submit_button('Submit')
		if submit:
			if(verify_userid(user_id)):
				st.error("User ID exists")
			else:
				users=pd.read_csv('users.csv',index_col=0)
				data_to_add=[{'Name':name,'User ID':user_id,'Phone':phone_number}]
				tempdf=pd.DataFrame(data_to_add)
				users=users.append(tempdf, ignore_index=True)
				users.index+=1
				users.to_csv('users.csv')
				st.success("Added User")
	if(option=='Remove A User'):
		st.header("Enter User ID to remove a user:")
		form = st.form(key="my-form")
		user_id=form.text_input("User ID")
		submit = form.form_submit_button('Submit')
		if submit:
			if(not(verify_userid(user_id))):
				st.error("User ID does not exist")
			else:
				data = pd.read_csv("users.csv", index_col =0)
				sets=[]
				k=1
				for i in (data["User ID"]):
					if(str(i)==user_id):
						sets.append(k)
					k+=1
				data.drop(sets, inplace = True)
				data=data.reset_index(drop=True)
				data.index+=1
				data.to_csv('users.csv')
				st.success("User Removed")

def page_drivers():
	st.title("Drivers' Management")
	option = st.selectbox('Select an action',('View Drivers', 'Add Driver', 'Remove A Driver'))
	if(option=="View Drivers"):
		drivers=pd.read_csv('drivers.csv',index_col=0)
		st.table(drivers)
	if(option=='Add Driver'):
		st.header("Enter Driver Info:")
		form = st.form(key="my-form")
		name = form.text_input("Name")
		emp_id=form.text_input("Employee ID")
		veh_type=form.selectbox('Select a Vehicle Type',('Mini', 'Sedan', 'SUV'))
		reg=form.text_input("Registration")
		submit = form.form_submit_button('Submit')
		if submit:
			if(verify_empid(emp_id)):
				st.error("Employee ID exists")
			else:
				drivers=pd.read_csv('drivers.csv',index_col=0)
				data_to_add=[{'Name':name,'Employee ID':emp_id,'Type of Vehicle':veh_type,'Registration':reg}]
				tempdf=pd.DataFrame(data_to_add)
				drivers=drivers.append(tempdf, ignore_index=True)
				drivers.index+=1
				drivers.to_csv('drivers.csv')
				st.success("Added Driver")
	if(option=='Remove A Driver'):
		st.header("Enter Employee ID to remove a driver:")
		form = st.form(key="my-form")
		emp_id=form.text_input("Employee ID")
		submit = form.form_submit_button('Submit')
		if submit:
			if(not(verify_empid(emp_id))):
				st.error("Employee ID does not exist")
			else:
				data = pd.read_csv("drivers.csv", index_col =0)
				sets=[]
				k=1
				for i in (data["Employee ID"]):
					if(str(i)==emp_id):
						sets.append(k)
					k+=1
				data.drop(sets, inplace = True)
				data=data.reset_index(drop=True)
				data.index+=1
				data.to_csv('drivers.csv')
				st.success("Driver Removed")


def page_add_bookings():
	st.title("Create New Booking")
	st.header("Enter booking Info:")
	form = st.form(key="my-form")
	emp_id=form.text_input("Employee ID")
	user_id=form.text_input("User ID")
	date=form.date_input("Booking Date")
	now = datetime.now()
	booking_id=now.strftime("%S%M%H%d%m")
	submit = form.form_submit_button('Submit')
	if submit:
		if(not(verify_empid(emp_id))):
			st.error("Employee ID does not exist")
		elif(not(verify_userid(user_id))):
			st.error("User ID does not exist")
		else:
			drivers = pd.read_csv("drivers.csv", index_col =0)
			users=pd.read_csv('users.csv',index_col=0)
			bookings=pd.read_csv('bookings.csv',index_col=0)
			user_sets=[]
			k=1
			for i in (users["User ID"]):
				if(str(i)==user_id):
					user_sets.append(k)
				k+=1
			emp_sets=[]
			k=1
			for i in (drivers["Employee ID"]):
				if(str(i)==emp_id):
					emp_sets.append(k)
				k+=1
			data = [{'User Name':users['Name'][user_sets[0]],'User ID':users['User ID'][user_sets[0]],'Phone':users['Phone'][user_sets[0]],"Driver's Name":drivers['Name'][emp_sets[0]],"Employee ID":drivers['Employee ID'][emp_sets[0]],"Type of Vehicle":drivers['Type of Vehicle'][emp_sets[0]],"Registration":drivers['Registration'][emp_sets[0]],'Date':date,'Booking ID':booking_id}]
			tempdf=pd.DataFrame(data)
			bookings=bookings.append(tempdf, ignore_index=True)
			bookings.index+=1
			bookings.to_csv('bookings.csv')
			st.success("Added Booking")


def page_add_bookings_unrooted():
	st.title("Create New Booking")
	st.header("Enter booking Info:")
	form = st.form(key="my-form")
	emp_id=form.text_input("Employee ID")
	user_id=form.text_input("User ID")
	date=form.date_input("Booking Date")
	now = datetime.now()
	booking_id=now.strftime("%S%M%H%d%m")
	submit = form.form_submit_button('Submit')
	if submit:
		if(not(verify_empid(emp_id))):
			st.error("Employee ID does not exist")
		elif(not(verify_userid(user_id))):
			st.error("User ID does not exist")
		else:
			drivers = pd.read_csv("drivers.csv", index_col =0)
			users=pd.read_csv('users.csv',index_col=0)
			bookings=pd.read_csv('bookings.csv',index_col=0)
			user_sets=[]
			k=1
			for i in (users["User ID"]):
				if(str(i)==user_id):
					user_sets.append(k)
				k+=1
			emp_sets=[]
			k=1
			for i in (drivers["Employee ID"]):
				if(str(i)==emp_id):
					emp_sets.append(k)
				k+=1
			data = [{'User Name':users['Name'][user_sets[0]],'User ID':users['User ID'][user_sets[0]],'Phone':users['Phone'][user_sets[0]],"Driver's Name":drivers['Name'][emp_sets[0]],"Employee ID":drivers['Employee ID'][emp_sets[0]],"Type of Vehicle":drivers['Type of Vehicle'][emp_sets[0]],"Registration":drivers['Registration'][emp_sets[0]],'Date':date,'Booking ID':booking_id}]
			tempdf=pd.DataFrame(data)
			bookings=bookings.append(tempdf, ignore_index=True)
			bookings.index+=1
			bookings.to_csv('bookings.csv')
			st.success("Added Booking")



def page_clear():
	st.title("Clear History")
	st.header("Enter the Booking ID to remove a booking:")
	form = st.form(key="my-form")
	book_id=form.text_input("Booking ID")
	submit = form.form_submit_button('Submit')
	if submit:
		if(not(verify_bookid(book_id))):
			st.error("Booking ID does not exist")
		else:
			data = pd.read_csv("bookings.csv", index_col =0)
			sets=[]
			k=1
			for i in (data["Booking ID"]):
				if(str(i)==book_id):
					sets.append(k)
				k+=1
			data.drop(sets, inplace = True)
			data=data.reset_index(drop=True)
			data.index+=1
			data.to_csv('bookings.csv')
			st.success("Booking Removed")

def page_clear_rooted():
	st.title("Clear History")
	st.header("Enter the Booking ID to remove a booking:")
	form = st.form(key="my-form")
	book_id=form.text_input("Booking ID")
	submit = form.form_submit_button('Submit')
	if submit:
		if(not(verify_bookid(book_id))):
			st.error("Booking ID does not exist")
		else:
			data = pd.read_csv("bookings.csv", index_col =0)
			sets=[]
			k=1
			for i in (data["Booking ID"]):
				if(str(i)==book_id):
					sets.append(k)
				k+=1
			data.drop(sets, inplace = True)
			data=data.reset_index(drop=True)
			data.index+=1
			data.to_csv('bookings.csv')
			st.success("Booking Removed")

def main():
	st.sidebar.title("Navigation")
	selected=st.sidebar.radio("Go To:",pages)
	if(selected)=="Welcome":
		welcome()
	if(selected)=="View Past Bookings":
		page_bookings()
	if(selected)=="User Management":
		page_users()
	if(selected)=="Driver Management":
		page_drivers()
	if(selected=="Add Bookings"):
		page_add_bookings()
	if(selected=="Clear Records"):
		page_clear()
	#st.table(users)




if __name__ == "__main__":
	main()