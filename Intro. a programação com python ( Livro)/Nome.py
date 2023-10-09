from functools import total_ordering
@total_ordering
class Nome:
    def __init__(self,nome):
        self.nome = nome
    #Overrides methods of Py. Just like Java
    def __str__(self):
        return self.nome
    def __repr__(self):
        return f'<Classe {type(self).__name__}em 0x{id(self):x} Nome: {self.nome} Chave: {self.__chave}>'
    def __eq__(self, other):
        return self.nome == other.pedeParametro
    #Less than:
    def __lt__(self, other):
        return self.nome < other.pedeParametro
    @property
    #Encapsulamento através do property
    def nome(self): #private String nome
        return self.__nome
    #public setNome()
    @nome.setter
    def nome(self,valor):
        if valor is None or not valor.strip():
            raise ValueError('Nome não pode ser nulo nem ter espaços em branco!')
        self.__nome = valor
        self.__chave = Nome.criaChave(valor)
    @staticmethod
    def criaChave(nome):
        return nome.strip().lower()