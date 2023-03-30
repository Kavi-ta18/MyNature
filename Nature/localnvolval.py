import mysql.connector

class Val():

    #get email and password from Screen
    app = App.get_running_app()
    input_email = app.manager.get_screen('login').ids['input_email'].text
    input_password = app.manager.get_screen('login').ids['input_password'].text


    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#lilu@5%",
    database="nature"
    )

    cursor = mydb.cursor()
            #run query to check email/password
            query = "SELECT count(*) FROM volsignup where email='"+str(input_email)+"' and pwd='"+str(input_password)+"'"
            cursor.execute(query)
            data = cursor.fetchone()
            count = data[0]
            #verif login/email
            #if invalid
            if count == 0:
                toast('Invalid Login/Password')
            #else, if valid
            else:
                toast('Login and Password are correct!')
                
                mydb.commit()
            mydb.close()
            pass