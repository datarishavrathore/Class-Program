# write a program to create a file in folder using in list
emp_list=["Mike","Jim","Adam","Neha","Tanya"]

emp_list = ["Mike", "Jim", "Adam", "Neha", "Tanya"]

for emp in emp_list:
    with open(emp + ".txt", "w") as file:
        file.write("Employee Name: " + emp)

print("All files created successfully.")
