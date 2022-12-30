#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add or show, edit or exit:")
    user_action = user_action.strip()#strip可以刪除首尾的空白，能更貼近使用者使用經驗
    filepath = "todos.txt"

    if user_action.startswith("add"):
        
        todo = user_action[4:]

        """ file= open('todos.txt', 'r')
            todos= file.readlines()
            file.close()#一定要寫close沒寫他都會只有戰存檔 關掉就沒了 """

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)
             
            
    elif user_action.startswith("show"): # | = or

        todos = functions.get_todos()
        new_todo= []
            
        """ for item in todos:
                new_item = item.strip("\n")
                new_todo.append(new_item)
            print(new_todo)  """  
        new_todo = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todo):
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number= int(user_action[5:])
            number = number-1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid. ")
            continue

        
    elif user_action.startswith("complete"):
        try:

            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
                

            functions.write_todos(todos)
            
                    
            print(F'Congratulations! You have finished {todo_to_remove}!')
        except IndexError:
            print("There is no item with that number")
            continue
            
        
    elif 'exit':
        
        """ if _: #非指令時 也可亂填一個變數名稱"""
        print("Have a great day!")
        break
    else:    
        print("Hey, you entered an unknow command") 



    
    