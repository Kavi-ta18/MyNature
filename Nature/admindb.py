import mysql.connector

class Admin():

  clgid = self.clgid_text_input.text
  clgname = self.clgname_text_input.text
  location = self.loc_text_input.text
  pwd = self.pwd_text_input.text

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#lilu@5%",
    database="nature"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO nature.adminsignup (clgid, clgname, location, pwd) VALUES (%s, %s, %s, %s)"
  val = (11,"John", "Highway 21","abc")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  toast('Successfully Registered!!')