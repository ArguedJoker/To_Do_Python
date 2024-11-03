todos = []

while True:
    user_input = input("What do you want to do? (Type 'add', 'show', 'edit', 'complete' or exit):  ")
    user_input = user_input.strip()
    
    match user_input:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1} - {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case x:
            print("Sorry, please enter either 'add' to add to your list, 'show' to show the list so far, 'edit' to edit the list, 'complete' to remove an item from the list. Alternatively, type 'exit' to exit the application")
print("Thank you and have a good day! Bye!")
    
