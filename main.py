# Класс для обычных пользователей
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id  # Инкапсуляция ID
        self.__name = name        # Инкапсуляция имени
        self.__access_level = 'user'  # Уровень доступа по умолчанию для обычных сотрудников

    # Методы доступа (геттеры и сеттеры)
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_access_level(self):
        return self.__access_level

# Класс для администраторов (наследуется от User)
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)  # Вызов конструктора родительского класса
        self.__access_level = 'admin'  # Уровень доступа для администраторов

    # Статический метод для добавления пользователя
    @staticmethod
    def add_user(user_list, new_user):
        user_list.append(new_user)
        print(f"Пользователь {new_user.get_name()} добавлен в систему")

    # Статический метод для удаления пользователя
    @staticmethod
    def remove_user(user_list, user_id_to_remove):
        for user_to_remove in user_list:
            if user_to_remove.get_user_id() == user_id_to_remove:
                user_list.remove(user_to_remove)
                print(f"Пользователь с ID {user_id_to_remove} удален из системы")
                return
        print(f"Пользователь с ID {user_id_to_remove} не найден")

# Пример использования
user1 = User(1, "Алексей")
user2 = User(2, "Мария")
admin1 = Admin(100, "Админ Иван")

# Список для хранения пользователей
all_users = [user1, user2]

# Администратор добавляет нового пользователя
Admin.add_user(all_users, User(3, "Николай"))

# Администратор удаляет пользователя
Admin.remove_user(all_users, 1)

# Вывод информации о пользователях
for user in all_users:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
