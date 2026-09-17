class Pedido:
    #não difinir os atributos
    status="Recebido"

    #método construtor - instaciar recebe o valor dos objetos
    def __init__(self, numero, data, hora, cliente, itens, pag):
        #self é chamar os atributos;
        self.numero = numero
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.itens = itens
        self.pagamento = pag

    
    #Metódo - Ação
    def  atualizar_Pedido(self, novoStatus):
        self.status=novoStatus

    def imprimir(self):             
        print(f"\n--------Pedido n {self.numero} ----------- ", self.numero)
        print(f"\nData: {self.data} - Hora: {self.hora} |")
        print(f"\nCliente;{self.cliente.nome} | Pagamento: {self.pagamento}")
        