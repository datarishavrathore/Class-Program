# # # write a program to create a file in folder using in list
# # # emp_list=["Mike","Jim","Adam","Neha","Tanya"]

# # # emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

# # # for emp in emp_list:
# # #     with open(emp + ".txt", "w") as file:
# # #         file.write("Employee Name: " + emp)

# # # print("All files created successfully.")


# # # import os

# # # emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

# # # for i in emp_list:
# # #     os.remove(f"{i}.txt")
# # #     print(i, "removed")

# # # create employee details folder and show all file in same folder
# # import os

# # # Create folder
# # folder_name = "Employee Details"
# # os.makedirs(folder_name, exist_ok=True)

# # # Employee list
# # emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

# # # Create files inside the folder
# # for emp in emp_list:
# #     file_path = os.path.join(folder_name, f"{emp}.txt")
# #     with open(file_path, "w") as file:
# #         file.write(f"Employee Name: {emp}")

# # print("Files created successfully.\n")

# # # Show all files in the folder
# # print("Files in Employee Details folder:")
# # for file in os.listdir(folder_name):
# #     print(file)

# # with open('Employee details','w')as f:import os

# # folder_name = "Employee Details"

# # emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

# # emp_id = 456

# # for emp in emp_list:
# #     file_path = os.path.join(folder_name, f"{emp}.txt")

# #     with open(file_path, "a") as file:
# #         file.write(f"\nName = {emp}")
# #         file.write(f"\nEmp_ID = {emp_id}\n")
# import os

# def add_employee_details():
#     folder_name = "Employee Details"

#     emp_data = {
#         "Mike": 456,
#         "Jim": 345,
#         "Adam": 234,
#         "Neha": 574,
#         "Tanya": 678
#     }

#     for emp, emp_id in emp_data.items():
#         file_path = os.path.join(folder_name, f"{emp}.txt")

#         with open(file_path, "w") as file:
#             file.write(f"Name = {emp}\n")
#             file.write(f"Emp_ID = {emp_id}\n")

#     print("Employee details written successfully.")

# # Function Call
# add_employee_details()


import os
import random
import string
ID="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(9)])
meeting_id="".join([random.choice(string.digits+string.ascii_uppercase) for i in range(25)])

def create_details(files):
    for i in files:
        if ".txt" in i:
            print(f"Files : {i}")
    select=input("Select your file without ext : ")
    with open(f"{select}.txt","w") as file:
        file.write(f"Name : {select}"+"\n")
        file.write(f"CANDIDATE_ID : {ID}"+"\n")
        file.write(f"MEETING_ID : http://{meeting_id}"+"\n")
        file.write(f"CANDIDATE_EMAIL : {input("Enter Your Email : ")}"+"\n")

    print(f"{select} file updated...")
files=os.listdir()
create_details(files)



