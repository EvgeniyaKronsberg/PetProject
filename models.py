class User:
    def __init__(self, login, password_hash):
        self.login = login
        self.password = password_hash
       

class Good:
    def __init__(self, producer, model, price, stock=0):
        self.producer = producer
        self.model = model
        self.producer = price
        self.model = stock
        