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
        return self.alturaCm / 10

p1 = Pessoa("jose", 2002, 190)
print(str(p1.getDescricao()))

p2 = Pessoa("ferreira", 2000, 180)
print(p2.getIdade())

p3 = Pessoa("Zeca", 1960, 150)
print(p3.getAlturaMetros())