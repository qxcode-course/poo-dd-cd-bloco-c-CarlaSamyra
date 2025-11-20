class Criança:
    def __init__ (self, name: str, age: int):
        self.__name = name 
        self.__age = age

    def __str__ (self):
        return f"{self.__name}:{self.__age}"
    
    def get_name (self):
        return self.__name
    
class Trampolim:
    def __init__ (self):
        self.brincando: list[Criança] = []
        self.esperando: list[Criança] = []
    
    def __str__(self):
        espera = ", ".join([str(i) for i in self.esperando])
        brincando = ", ".join([str(i) for i in self.brincando])
        return f"[{espera}] => [{brincando}]"
    
    def arrive (self, criança: Criança):
        self.esperando.insert(0, criança)

    def enter (self):
        criança = self.esperando.pop()
        self.brincando.insert(0, criança)
        del criança

    def leave (self):
        if len(self.brincando) == 0:
            return
        criança = self.brincando.pop()
        self.esperando.insert(0, criança)
        del criança

    def remove (self, nome: str):
        for i, criança in enumerate(self.esperando):
            if criança.get_name() == nome:
                self.esperando.remove(criança)
                return
        for i, criança in enumerate(self.brincando):
            if criança.get_name() == nome:
                self.brincando.remove(criança)
                return
        print (f"fail: {nome} nao esta no pula-pula")
        

def main():
    trampolim = Trampolim()
    while True: 
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            criança = Criança(nome, idade)
            trampolim.arrive(criança)
        elif args[0] == "show":
            print (trampolim)
        elif args[0] == "enter":
            trampolim.enter()
        elif args[0] == "leave":
            trampolim.leave()
        elif args[0] == "remove":
            nome = args[1]
            trampolim.remove(nome)
        else:
            print("fail: comando inválido")

main()