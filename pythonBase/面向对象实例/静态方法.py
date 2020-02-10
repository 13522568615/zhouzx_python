class Washer:

    def __init__(self,water=10,scour=2):
        self._water = water
        self.scour = scour

    #装饰器-静态方法
    @staticmethod
    def spins_ml(spins):
        return spins * 0.4

if __name__ == '__mian__':
    print(Washer.spins_ml(8))
    w = Washer()
    print(w.spins_ml(8))