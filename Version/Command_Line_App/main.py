todos = []

while True:
    user_input = input("What do you want to do? (Type 'add', 'show' or exit):  ")
    match user_input:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
print("Thank you and have a good day! Bye!")
    
