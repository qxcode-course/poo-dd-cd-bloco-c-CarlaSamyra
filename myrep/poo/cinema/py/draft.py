class Cliente:
    def __init__ (self, id: str, telefone: int):
        self.__id = id 
        self.__telefone = telefone
    
    def get_phone (self):
        return self.__telefone
    
    def get_id (self):
        return self.__id
    
    def set_phone (self, phone: int):
        self.__telefone = phone 
    
    def set_id (self, nome: str):
        self.__id = nome 
    
    def __str__ (self):
        return f"{self.__id}:{self.__telefone}"

class Theater:
    def __init__ (self, capacidade: int):
        self.seats: list[Cliente | None] = []
        for i in range (capacidade):
            self.seats.append(None)
    
    def __str__ (self):
        if len(self.seats) == 0:
            return "[]"
        capacidade = " ".join(["-" if x is None else str(x) for x in self.seats])
        return f"[{capacidade}]"

    
    def reserve (self, cliente: Cliente, index: int):
        if self.seats[index] != None:
            print("fail: cadeira ja esta ocupada")
            return
        self.seats.append(cliente)
    
def main():
    sala = Theater(0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(sala)
        elif args[0] == "init":
            sala = Theater(int(args[1]))
        elif args[0] == "reserve":
            id = args[1]
            telefone = int(args[2])
            cliente = Cliente(id, telefone)
            index = args[3]
            sala.reserve(cliente, index)
        else:
            print("fail: comando inválido")

main()