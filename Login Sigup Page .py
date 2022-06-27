import json
from datetime import date
import re
d=open("signup.json","a")
p=open("signup.json","r")
ope=open("signup.json","r")
print("welcome to Login Signup Page")
print("do you want to login or signup?")
answer=input("enter your answer :-")
dic={}
if answer=="Signup":
    name=input("enter the first name:-")
    surname=input("enter the surname:-")
    a=(name,surname)
    b=" ".join(a)
    dic.update({"Username":b})
    Gender=input("enter your gender:-")
    if Gender=="f" or Gender=="m" or Gender=="female" or Gender=="male" or Gender=="others" or Gender=="o":
        dic.update({"Gender":Gender})
        Phone_No=int(input("enter the Phone no.:-"))
        if Phone_No>=000000000 and Phone_No<=9999999999:
            dic.update({"Phone No":Phone_No})
            email_conditions="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
            email=input("enter the valid email:-")
            if re.search(email_conditions,email):
                comform_yor_emil=input("enter the conferm email:-")
                if email==comform_yor_emil:
                    dic.update({"Email":email})
                    def calculateAge(birthDate):
                        today = date.today()
                        age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
                        dic.update({"DOB":(year,month,day)})
                        return age    
                            # Driver code
                    year=int(input("enter the year:-"))
                    month=int(input("enter the month:-"))
                    day=int(input("enter tha date;-"))
                    print(calculateAge(date(year,month, day)), "years")
                    password_condition= "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
                    password=input("ener the password:-")
                    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
                            conferm_password=input("enter the password:-")
                            if conferm_password==password:
                                dic.update({"password":password})
                            else:
                                print("your conferm_password is wrong")
                    else:
                        print("in valid password")
                else:
                    print("invalid conferm mail ")
            else:
                print("invalid email") 
        else:
            print("invalid phone no.")
    else:
        print("invalid  Gender")       
    b=open("signup.json","a")
    c=json.dump(dic,b,indent=1)  
    b.close()                     

elif answer=="Login":  
        op=open("signup.json","r")
        c=json.load(op) 
        name=input("enter your name")
        mail=input("enter the mail:-")
        Pass=input("enter the password:-")
        if name==c.get("Username"):
            if mail==c.get("Email"):
                if Pass==c.get("password"):
                        print("yes")
                else:
                        print("your password in incorrect")    
            else:
                    print("your Mail is in valid")
        else:
                print("You are not regestered")



