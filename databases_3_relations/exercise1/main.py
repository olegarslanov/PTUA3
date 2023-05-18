from models import User, Task
from session import session

print("Welcome TO DO list application")


class Useris:
    def __init__(self):
        self.name = None
        self.surname = None
        self.email = None
        self.password = None

    def email_check(self, login):
        user_exists = False
        user_list = session.query(User).all()
        for user in user_list:
            if user.email == login:
                user_exists = True
                print("User email exists in users table")
                self.name = user.name
                self.surname = user.surname
                self.email = user.email
                self.password = user.password
        if user_exists is False:
            print("You are new User, please register")
            self.register_user(login)

    def password_check(self, password):
        user = session.query(User).filter_by(email=self.email).one()
        if password == user.password:
            print("password matches")
            return True
        else:
            print("password does not match")
            return False

    def register_user(self, login):
        name = input("Enter name ")
        surname = input("Enter surname ")
        password = input("Enter password ")

        new_user = User(name=name, surname=surname, email=login, password=password)
        session.add(new_user)
        session.commit()
        print("Registered succesfully !")
        exit()


class Taskas:
    def __init__(self):
        self.title = None
        self.description = None
        self.deadline = None
        self.user_id = None

    def add_task(self):
        self.title = input("Please input title:")
        self.description = input("Please input description:")
        self.deadline = input("Please input deadline:")
        self.user_id = int(input("Please enter user id for this task:"))

        task = Task(self.title, self.description, self.deadline, self.user_id)
        session.add(task)
        session.commit()

    def update_task(self):
        # retrieve all tasks from the database
        tasks = session.query(Task).all()
        for task in tasks:
            print(task)

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

    def delete_task(self):
        # retrieve all tasks from the database
        tasks = session.query(Task).all()
        for task in tasks:
            print(task)

        delete_id = int(input("Please enter delete task id:"))
        task_delete = session.query(Task).get(delete_id)
        session.delete(task_delete)
        session.commit()


# User interface
useris = Useris()
login = input("Please enter email:")
useris.email_check(login)
password = input("Please enter password:")
useris.password_check(password)

print("Please manage tasks")

taskas = Taskas()

while True:
    choose = int(
        input("Your choice: \n1 - create task \n2 - update task \n3 - delete task")
    )
    if choose == 1:
        taskas.add_task()

    if choose == 2:
        taskas.update_task()

    if choose == 3:
        taskas.delete_task()
