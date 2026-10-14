class User:
    count = 0

    def __init__(self, name, login, password, grade):
        if not isinstance(name, str) or not isinstance(login, str) or not isinstance(password, str):
            raise TypeError("Имя, логин и пароль должны быть строками")
        if type(grade) is not int or grade <= 0:
            raise ValueError("Рейтинг должен быть положительным целым числом")

        self._name = name
        self.__login = login
        self.__password = password
        self.__grade = grade

        if type(self) is User:
            User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        self._name = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        self.__password = value

    @property
    def grade(self):
        return "Неизвестное свойство grade"

    @grade.setter
    def grade(self, value):
        print("Неизвестное свойство grade")

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}")

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.__grade == other.__grade

    def __lt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.__grade < other.__grade

    def __gt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.__grade > other.__grade


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade):
        if not isinstance(role, str):
            raise TypeError("Роль должна быть строкой")
        super().__init__(name, login, password, grade)
        self._role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if not isinstance(value, str):
            raise TypeError("Роль должна быть строкой")
        self._role = value

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}, Role: {self.role}")
