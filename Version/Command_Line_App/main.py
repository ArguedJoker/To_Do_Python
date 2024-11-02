todos = []

while True:
    user_input = input("What do you want to do? (Type 'add', 'show' or exit):  ")
    user_input = user_input.strip()
    
    match user_input:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case x:
            print("Sorry, please enter either 'add' to add to your list, 'show' to show the list or 'exit' to exit")
print("Thank you and have a good day! Bye!")
    
