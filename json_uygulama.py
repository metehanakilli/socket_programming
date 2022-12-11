import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # json dosyası üzerinden kullanıcıları yükleme
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users_json'):  # dosya mevcut mu onu kontrol eder.
            with open('users_json', 'r', encoding='utf-8') as file:  # dosya okuma
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'], password=user['password'], email=user['email'])

                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)  # gönderilen bilgi listeye eklenir
        self.savetofile()  # Kayıt işleminden sonra dosyaya kaydeder.
        print("Kullanıcı oluşturuldu.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login yapıldı')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Giriş yapılmadı')

    def savetofile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))  # Bütün bilgileri dictionary formatına çevirir ve listeye atar.

        with open('users_json', 'w') as file:  # dosyayı yazma modunda açar.
            json.dump(list, file)  # listeyi dosyaya json formatında kaydeder.

repository = UserRepository()

while True:
    print('Menü'.center(50, "*"))
    secim = input('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nseçiminiz: ')

    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            repository.register(user)
        elif secim == '2':
            if repository.isLoggedIn:
                print('Zaten login oldunuz.')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif secim == '3':
            repository.logout()
        elif secim == '4':
            repository.identity()
        else:
            print("Yanlış Seçim!!!")
