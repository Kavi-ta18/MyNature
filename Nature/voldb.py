import mysql.connector

name = self.name_text_input.text
email = self.email_text_input.text
contact = self.contact_text_input.text
clg = self.clg_text_input.text
location = self.loc_text_input.text
pwd = self.pwd_text_input.text

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#lilu@5%",
  database="nature"
)

mycursor = mydb.cursor()

sql = "INSERT INTO nature.volsignup (name, email, contact, clg, location, pwd) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("Kavi","kavi321", 123, "SCOE", "Thane","abc")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
toast('Successfully Registered!!')