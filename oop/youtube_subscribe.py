

class Youtube:
    def __init__(self, username,subscriber=0,subscription=0):
        self.username=username
        self.subscriber=subscriber
        self.subscription=subscription

    def subscribe(self,user):
        user.subscriber=+1
        self.subscription=+1



user1=Youtube("Ali")
user2=Youtube("Rafi")
user1.subscribe(user2)
print(user1.subscriber)
print(user1.subscription)
print(user2.subscriber)
print(user2.subscription)

