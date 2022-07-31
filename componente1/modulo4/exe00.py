class Pessoa:
    def __init__(self, nome, anoNascimento, alturaCm):
        self.nome = nome
        self.anoNascimento = anoNascimento
        self.alturaCm = alturaCm

    def getDescricao(self):
        return "Nome: {}, Nascimento: {} e Altura {}cm".format(
            self.nome, self.anoNascimento, self.alturaCm)

    def getIdade(self):
        return 2022 - self.anoNascimento

    def getAlturaMetros(self):
        return self.altura / 10

class Veiculo:
    def __init__(self, marca, cor, qtdPassageiro ):
        self.marca = marca
        self.cor = cor
        self.qtdPassageiro = qtdPassageiro

    def getMarca(self):
        return self.marca
    
    def setCor(self, cor):
        self.cor = cor

    def getCor(self):
        return self.cor

    def getDescricao(self):
        return "Marca: {}, Cor: {} e qtdPassageiro: {}".format(
            self.marca, self.cor, self.qtdPassageiro
        )

class login:
    def __init__(self, usuario, email, senha, token ):
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.token = token

    def getUsuario(self):
        return self.usuario

    def getEmail(self):
        return self.email

    def setSenha(self, senha):
        self.senha = senha

    def getToken(self):
        return self.token

class Api:
    def __init__(self, controlador, modelo, servico, repositorio):
        self.controlador = controlador
        self.modelo = modelo
        self.servico = servico
        self.repositorio = repositorio

    def getControlador(self):
        return self.controlador

    def getModelo(self):
        return self.modelo

    def getServico(self):
        return self.servico

    def getRepositorio(self):
        return self.repositorio