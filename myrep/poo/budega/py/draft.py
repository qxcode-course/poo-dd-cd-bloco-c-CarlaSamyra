class Pessoa:
    def __init__ (self, nome: str):
        self.nome = nome
    def __str__ (self):
        return self.nome
    
class Budega:
    def __init__ (self, num_caixas: int):
        self.caixas: list[Pessoa | None] = []
        self.espera: list[Pessoa] = []
        for i in range (num_caixas):
            self.caixas.append(None)
    
    def __str__ (self):
        caixas = ", ".join(["-----" if x is None else str(x) for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
    def enter (self, cliente: Pessoa):
        self.espera.append(cliente)
    
    def call (self, index: int):
        if self.espera == []:
            print("fail: sem clientes")
            return
        if self.caixas[index] != None:
            print ("fail: caixa ocupado")
            return
        self.caixas[index] =  self.espera[0]
        del self.espera[0]

    def finish (self, index: int): 
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] == None:
            print ("fail: caixa vazio")
            return
        self.caixas[index] = None
    
def main():
    budega = Budega(0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(budega)
        elif args[0] == "init":
            budega = Budega(int(args[1]))
        elif args[0] == "arrive":
            cliente = (args[1])
            budega.enter(Pessoa(cliente))
        elif args[0] == "call":
            fila = int(args[1])
            budega.call(fila)
        elif args[0] == "finish":
            terminar = int(args[1])
            budega.finish(terminar)
        else:
            print ("fail: comando inválido")

main()