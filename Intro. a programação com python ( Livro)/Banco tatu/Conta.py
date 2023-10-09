class Conta:
    def __init__(self, clientes, número, saldo=0, telefone = 0):
        self.telefone = telefone
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N°{self.número} Saldo: {self.saldo:10.2f} ")
        print(f'Nome de proprietário C.C: {self.clientes}. Número de telefone: {self.telefone}')

    def verifica(self,valor):
        if self.saldo >= valor:
            return True
        else:
            return False

    def saque(self, valor):
        if valor.verifica:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            print('Saldo não suficiente!')

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:%10.2f}\n")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo =0,limite = 0):
        Conta.__init__(self,clientes,numero,saldo)
        self.limite = limite
    #Override:
    def saque(self, valor):
        return self.saldo + self.limite >= valor
    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        print(f'Limite Crédito: {self.limite} ')
        print(f'Saldo Disponível: {self.saldo}')
