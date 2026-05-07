class Aluno(self):

    def __init__(self, nome, email, senha, telefone, data_nasc):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.telefone = telefone
        self.data_nasc = data_nasc
    
    def login(self, email, senha):
        print('Login realizado com sucesso!')

    def logout(self):
        print('Logout feito com sucesso!')