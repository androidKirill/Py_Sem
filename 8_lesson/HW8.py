from os import path

file_base= "base.txt"

all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as f:
        f.writelines("0. Surname Patronymic Phone_number\n")
        pass
        


def read_record():
    global  all_data
   
    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        
    return all_data, []
    

def show_all():
    global  all_data
    if all_data:
        for line in all_data:
            print(line)
    else:
                print("Empty data")
                 

def add_new_contact():
    
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ''
    for i in array:
        string += " " + input(f"Enter {i} ") + " "
    with open(file_base, "a", encoding="utf-8") as f:
        f.write(str(len(all_data)) +"." + string + "\n")
    
def сhange_contact():
    path = "base.txt"
    text = open("base.txt","r", encoding="utf-8")
    arraycopy= list()
    for i in text:
        arraycopy.append(i)    
    text.close

    changeid = int(input("Введите порядковый номер строки которую хотите редактировать\n", ))

    array = ["surname", "name", "patronymic", "phone_number"]
    stringchange = ''
    for i in array:
        stringchange += " " + input(f"Enter {i} ") + " "
    stringchange= str(changeid) + "." + stringchange +"\n"

    text = open("base.txt","w", encoding="utf-8")
    string=""
    j=0
    for i in arraycopy:
        if j == changeid :
            string = stringchange
            j +=1
            
            text.write(string)
        else:
            string = str(j) + i[len(str(j)):]
            j +=1
            text.write(string)
    text.close
    

def sort():
    text = open("base.txt","r", encoding="utf-8")
    array= list()
    for i in text:
        array.append(i)
        text.close
    text = open("base.txt","w", encoding="utf-8")
    string=""
    j=0
    for i in array:
        if "deleted" in i:
            pass
        elif len(str(j)) < len(str(j+1)) and i[len(str(j))] != ".":
            string =str(j) + i[len(str(j))+1:]
            text.write(string)
            j +=1
        else:
            string =str(j) + i[len(str(j)):]
            text.write(string)
            j +=1
    text.close

def delete_contact():
    path = "base.txt"
    text = open("base.txt","r", encoding="utf-8")
    arraycopy= list()
    for i in text:
        arraycopy.append(i)
    print(arraycopy)
    text.close

    changeid = int(input("Введите порядковый номер строки которую хотите редактировать\n", ))

    text = open("base.txt","w", encoding="utf-8")
    string=""
    j=0
    for i in arraycopy:
        if j == changeid :
            text.write(str(j) +'. deleted\n')
            j +=1        
        else:
            string = str(j) + i[len(str(j)):]
            text.write(string)
            j +=1
            
    text.close


def main_menu():
    play = True 
    while play:
        read_record()
        
        answer = input("Phone_book:\n"
                        "1. Show all records\n"
                        "2. Add record\n"
                        "3. Change\n"
                        "4. Delete\n"
                        "5. Sort\n"
                        "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                сhange_contact()
            case "4":
                delete_contact()
            case "5":
                sort()
            case "6":         
                play = False
            case _:
                print("Try again\n")
        
main_menu()