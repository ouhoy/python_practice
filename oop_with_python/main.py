class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("0001", "Alice")
user_2 = User("0002", "John")

user_1.follow(user_2)

print(f"User 1 has {user_1.followers} followers and is following {user_1.following} ")
print(f"User 2 has {user_2.followers} followers and is following {user_2.following} ")
