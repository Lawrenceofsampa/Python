
class Banco:
    def __init__(self,nome):
        self.nome = nome
        self.cliente = []
        self.conta = []
    def abre_conta(self,conta):
        self.conta.append(conta)
    def lista_conta(self):
        for c in self.conta:
            c.resumo()


