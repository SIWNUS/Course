class WebUser:   #class name should be in PascalCase
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following =0

        print("new user being created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1  = WebUser("001", "Marcel")
user_2 = WebUser("002", "Diana")

user_1.follow(user_2)

print(user_1.following)

