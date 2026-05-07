class Aluno(self):

    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.telefone = telefone
    
    def login(self, email, senha):
        print('Login realizado com sucesso!')

    def logout(self):
        print('Logout feito com sucesso!')