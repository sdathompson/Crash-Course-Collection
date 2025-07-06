# classes are PascalCase
class User:
    # Initialize the constructor
    # Attributes are added to the constructor can be called at class declaration time
    def __init__(self, user_id, username):
        self.id =  user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # Methods are functions inside classes
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","Shane")
user_2 = User("002", "David")

user_1.follow(user_2)

