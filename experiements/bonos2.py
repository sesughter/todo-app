'''user_name = input("enter name: ")
while True:
    print(user_name.capitalize())'''

waiting_list = ['john', 'henry', 'marcy']
waiting_list.sort()

for i, j in enumerate(waiting_list):
    row = f"{i+1}.{j.capitalize()}"
    print(row)

