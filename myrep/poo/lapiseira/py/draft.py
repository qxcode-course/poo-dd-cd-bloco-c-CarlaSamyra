class Grafite:
    def __init__ (self, thikness: float, hardness: str, size: int):
        self.__size = size
        self.__hardness = hardness
        self.__thikness = thikness
    
    def __str__ (self):
        return f"[{self.__thikness}:{self.__hardness}:{self.__size}]"
    
    def get_thikness (self):
        return self.__thikness
    
    def get_hardness (self):
        return self.__hardness
    
    def get_size (self):
        return self.__size
    
    def set_size (self, tamanho: int):
        self.__size = tamanho

    def usagePerSheet (self):
        if self.__hardness == "HB":
            self.__size -= 1
            return 1
        if self.__hardness == "2B":
            self.__size -= 2
            return 2 
        if self.__hardness == "4B":
            self.__size -= 4
            return 4 
        if self.__hardness == "6B":
            self.__size -= 6
            return 6 
    
class Pencil:
    def __init__ (self, thikness: float, barrel: int):
        self.__thikness = thikness
        self.__tip = None
        self.__barrel: list[Grafite] = []
    
    def __str__ (self):
        tip_str = str(self.__tip) if self.__tip else "[]"
        barrel_str = "".join(str(i) for i in self.__barrel)
        return f"calibre: {self.__thikness}, bico: {tip_str}, tambor: <{barrel_str}>"
    
    def set_thikness (self, amount: float):
        self.__thikness = amount

    def insert (self, calibre: float, dureza: str, tamanho: int):
        grafite = Grafite(calibre, dureza, tamanho)
        if calibre != self.__thikness:
            print ("fail: calibre incompatível")
            return False
        if calibre == self.__thikness:
            self.__barrel.append(grafite)
            return True
        
    def pull (self):
        if self.__tip != None:
            print("fail: ja existe grafite no bico")
            return
        else:
            grafite = self.__barrel.pop(0)            
            self.__tip = grafite

    def remove (self):
        self.__tip = None

    def writePage (self):
        if self.__tip == None:
            print("fail: nao existe grafite no bico")
            return
        
        tamanho = self.__tip.get_size()

        if tamanho == 10: 
            print ("fail: tamanho insuficiente")
            return

        gasto = self.__tip.usagePerSheet()
        tamanhoUsado = tamanho - gasto 

        if tamanhoUsado < 10: 
            self.__tip.set_size(10)
            print("fail: folha incompleta")
            return

def main():
    lapiseira = Pencil(0, 0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)   
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            amount = float(args[1])
            lapiseira.set_thikness(amount)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            lapiseira.insert(calibre, dureza, tamanho)
        elif args[0] == "pull":
            lapiseira.pull()
        elif args[0] == "remove":
            lapiseira.remove()
        elif args[0] == "write":
            lapiseira.writePage()
        else: 
            print("fail: comando inválido")
main()     

    