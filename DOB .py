# from datetime import date
# Date_of_bearth={}
# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
#     Date_of_bearth.update({"DOB":[year,month,day]})
#     return age
# year=int(input("enter the year:-")) 
# month=int(input("enter the month:-"))
# day=int(input("enter tha date;-")) 
# print(calculateAge(date(year,month, day)), "years")   
# print(Date_of_bearth)

# name=input("enter the first name:-")
# surname=input("enter the surname:-")
# a=(name,surname)
# b=" ".join(a)
# print(b)
# c=["riti sharma": [{"Email": "riti@gmail.com"}, {"DOB": [2003, 8, 4]}, {"password": "riti@123"}]}
# name=input("enter your name")
# email=input("enter the mail:-")
# password=input("enter the password:-")
# for i in c:
#     if i==name:
#         for j in c[i]:
#             for k in c[i][j]:
#                 print(c[i][j][k])

# c={"Username": "riti sharma","Email": "riti@gmail.com", "DOB": [2003, 8, 4],"password": "riti@123"}
# name=input("enter your name")
# mail=input("enter the mail:-")
# # DOB=input("enter the DOB:-")
# Pass=input("enter the password:-")
# if name==c.get("Username"):
#     if mail==c.get("Email"):
#         if Pass==c.get("password"):
#                             print("yes")
#         else:
#             print("no")    
#     else:
#         print("no")
# else:
#     print("no")

# import json
# f=[]
# d=open("signup.json","w")
# k=json.dump(f,d)
# d.close()
# p=open("signup.json","r")
# f=json.loads(p)
# f.append(3)


import json
b=open("data.json","w") 
b.close()
# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
y = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
     
write_json(y)