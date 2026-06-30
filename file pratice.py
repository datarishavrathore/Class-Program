# write a program to create a file in folder using in list
# emp_list=["Mike","Jim","Adam","Neha","Tanya"]

# emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

# for emp in emp_list:
#     with open(emp + ".txt", "w") as file:
#         file.write("Employee Name: " + emp)

# print("All files created successfully.")


# import os

# emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

# for i in emp_list:
#     os.remove(f"{i}.txt")
#     print(i, "removed")

# create employee details folder and show all file in same folder
import os

# Create folder
folder_name = "Employee Details"
os.makedirs(folder_name, exist_ok=True)

# Employee list
emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

# Create files inside the folder
for emp in emp_list:
    file_path = os.path.join(folder_name, f"{emp}.txt")
    with open(file_path, "w") as file:
        file.write(f"Employee Name: {emp}")

print("Files created successfully.\n")

# Show all files in the folder
print("Files in Employee Details folder:")
for file in os.listdir(folder_name):
    print(file)
    