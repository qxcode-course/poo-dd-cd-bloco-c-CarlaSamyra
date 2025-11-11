class Criança: 
    def __init__ (self, nome: str, idade: int):
        self.__idade = idade
        self.__nome = nome 

    def __str__ (self):
        return f"{self.__nome}:{self.__idade}"
    
    def get_name (self):
        return self.__nome
    
    def get_age (self):
        return self.__idade
    
    def set_name (self, name: str):
        self.__nome = name
        return self.__nome
    
    def set_age (self, age: str):
        self.__idade = age
        return self.__idade
    
class Trampolim:
    def __init__ (self):
        self.brincando: list [Criança | None] = []
        self.espera: list [Criança | None] = []
    
    def __str__ (self):
        espera = ", ".join([str(x) for x in self.espera])
        brincando = ", ".join([str(x) for x in self.brincando])
        return f"[{espera}] => [{brincando}]"
    
    def arrive (self, criança: Criança):
        self.espera.insert(0, criança)

    def enter (self):
        criança = self.espera.pop()
        self.brincando.insert(0, criança)
        del criança
    
    def leave (self):
        if len(self.brincando) == 0:
            return
        criança = self.brincando.pop()
        self.espera.insert(0, criança)
        del criança

    def remove (self, nome: str):
        for i, criança in enumerate(self.espera):
            if criança.get_name() == nome:
                self.espera.pop(i)
                return
        for i, criança in enumerate(self.brincando):
            if criança.get_name() == nome:
                self.brincando.pop(i)
                return
        print(f"fail: {nome} nao esta no pula-pula")

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
            print(trampolim)
        elif args[0] == "enter":
            trampolim.enter()
        elif args[0] == "leave":
            trampolim.leave()
        elif args[0] == "remove":
            remover = args[1]
            trampolim.remove(remover)
        else:
            print("fail: comando inválido")
main()