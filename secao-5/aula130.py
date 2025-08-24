class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print(msg)

#c1 = Connection()
#c1.set_user('Vinicius')
#c1.set_password('1234')

c1 = Connection.create_with_auth('Vinicius', '1234')
print(c1.user, c1.password, c1.host)

Connection.log('Conexão bem sucedida')
        