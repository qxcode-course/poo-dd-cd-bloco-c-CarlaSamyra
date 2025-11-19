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
        self.capacidade = capacidade
        self.seats: list[Cliente | None] = []
        for i in range (capacidade):
            self.seats.append(None)
    
    def __str__ (self):
        if len(self.seats) == 0:
            return "[]"
        capacidade = " ".join(["-" if x is None else str(x) for x in self.seats])
        return f"[{capacidade}]"
    
    def verifyIndex (self, index: int):
        if index < 0 or index >= len(self.seats):
            return False
        return True
    
    def search (self, nome: str):
        for i, cliente in enumerate (self.seats):
            if cliente != None and cliente.get_id() == nome: 
                return i
        return -1

    def reserve (self, cliente: Cliente, index: int):
        if self.verifyIndex(index) is not True:
            print("fail: cadeira nao existe")
            return False
        if self.search(cliente.get_id()) != -1:
            print ("fail: cliente ja esta no cinema")
            return False
        if self.seats[index] != None:
            print("fail: cadeira ja esta ocupada")
            return False
        self.seats[index] = cliente 

    def cancel (self, id: str):
        index = self.search(id)
        if index == -1:
            print ("fail: cliente nao esta no cinema")
            return
        self.seats[index] = None
    
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
            index = int(args[3])
            sala.reserve(cliente, index)
        elif args[0] == "cancel":
            id = args[1]
            sala.cancel(id)
        else:
            print("fail: comando inválido")

main()