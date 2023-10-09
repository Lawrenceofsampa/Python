from Estado import Estado
from Cidade import Cidade
Guarulhos = Cidade('Guarulhos', 500000)
Porto_Alegre = Cidade('Porto Alegre', 1000000)
Rio_grande = Estado('Rio granbde do sul' , 'RS', [Porto_Alegre], [Porto_Alegre])
Sao_paulo = Estado('São Paulo' , 'Gua', [Guarulhos], [Guarulhos])
Sao_paulo.calcula(Guarulhos)
Rio_grande.calcula(Porto_Alegre)

