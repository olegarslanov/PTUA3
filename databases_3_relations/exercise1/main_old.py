from models import User, Task
from session import session

print("//////////////////////////////")
print("Welcome TO DO list application")

# darau pildymo interfeisa models.py class "Task" (tai yra lent. Tasks uzpildymui)
while True:
    choose = int(
        input(
            "Your choice: \n1 - show tasks \n2 - create task \n3 - update task \n4 - delete task \n5 - exit"
        )
    )

    if choose == 1:
        tasks = session.query(Task).all()
        print("-------------------")
        for task in tasks:
            print(task)
        print("-------------------")

    if choose == 2:
        while True:
            try:
                title = input("Please input title:")
                description = input("Please input description:")
                deadline = input("Please input deadline:")
                user_id = input("Please enter user id for this task:")

                task = Task(title, description, deadline, user_id)
                session.add(task)
                session.commit()
                break
            except:
                print("Something wrong. Please enter correct data")

    if choose == 3:
        # retrieve all tasks from the database
        tasks = session.query(Task).all()
        print("-------------------")
        for task in tasks:
            print(task)
        print("-------------------")

        change_id = int(input("Please enter change task id:"))
        task_change = session.query(Task).get(change_id)
        change = int(
            input(
                "Enter change: 1 - title, 2 - description, 3 - deadline, 4 - user_id :"
            )
        )
        if change == 1:
            task_change.title = input("Please enter task title:")
        if change == 2:
            task_change.description = input("Please enter task description:")
        if change == 3:
            task_change.deadline = input("Please enter task deadline:")
        if change == 4:
            task_change.user_id = input("Please enter user id for this task:")
        session.commit()

    if choose == 4:
        tasks = session.query(Task).all()
        print("-------------------")
        for task in tasks:
            print(task)
        print("-------------------")
        change_id = int(input("Please enter delete task id:"))
        task_delete = session.query(Task).get(change_id)
        session.delete(task_delete)
        session.commit()

    if choose == 5:
        print("Exit tasks")
        break


# darau pildymo interfeisa models.py class "User" (tai yra lent. Users uzpildymui)
while True:
    choose = int(
        input(
            "Your choice: \n1 - show users \n2 - create user \n3 - update user \n4 - delete user \n5 - exit"
        )
    )

    if choose == 1:
        users = session.query(User).all()
        print("-------------------")
        for user in users:
            print(user)
        print("-------------------")

    if choose == 2:
        while True:
            try:
                name = input("Please input name:")
                surname = input("Please input surname:")
                email = input("Please input email:")
                password = input("Please password:")

                user = User(name, surname, email, password)
                session.add(user)
                session.commit()
                break
            except:
                print("Something wrong. Please enter correct data")

    if choose == 3:
        # retrieve all tasks from the database
        users = session.query(User).all()
        print("-------------------")
        for user in users:
            print(user)
        print("-------------------")

        change_id = int(input("Please enter change user id:"))
        user_change = session.query(User).get(change_id)
        change = int(
            input("Enter change: 1 - name, 2 - surname, 3 - email, 4 - password :")
        )
        if change == 1:
            user_change.name = input("Please enter user name:")
        if change == 2:
            user_change.surname = input("Please enter user surname:")
        if change == 3:
            user_change.email = input("Please enter task deadline:")
        if change == 4:
            task_change.deadline = input("Please enter task deadline:")
        session.commit()

    if choose == 4:
        users = session.query(User).all()
        print("-------------------")
        for user in users:
            print(user)
        print("-------------------")
        change_id = int(input("Please enter delete user id:"))
        user_delete = session.query(User).get(change_id)
        session.delete(user_delete)
        session.commit()

    if choose == 5:
        print("Exit users")
        break
