class Estado:
    def __init__(self,nome,sigla, cidade, populacao):
        self.nome = nome
        self.sigla = sigla
        self.cidade = cidade
        self.populacao = populacao
    def calcula(self, valor):
        return sum([c.população for c in self.cidade])
        
