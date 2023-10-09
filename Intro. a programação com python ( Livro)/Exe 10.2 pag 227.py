class Televisão:
    def __init__(self, inicio, max = 14, min = 2):
        self.ligada = False
        self.cmin = min
        self.cmax = max
        self.canal = inicio


    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal += self.cmin


tv = Televisão( max = 300)
tv2 = Televisão(max=600, min= 40)

print(tv.canal)
