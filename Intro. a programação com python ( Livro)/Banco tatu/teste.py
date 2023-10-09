from Conta import Conta, ContaEspecial
from Cliente import Cliente

jao = Cliente("Jão da silva" , 5758)
mary = Cliente("Da Silva Santos" , 8054)
nietzche = Cliente('Frederico',1900)
plato = Cliente('Socrates', 1300)
conta1 = Conta([jao], 1,1000, [jao])
conta2 = ContaEspecial([mary], 2, 2000, 5000)
conta3 = Conta([nietzche],3,500,[nietzche])
conta4 = Conta([plato],4,500,[plato])
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()