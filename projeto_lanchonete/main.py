from Pedido import Pedido

#criar um objeto - representar um elemento - dar valores
novoPedido = Pedido(1, "2026-14-09", "21:10", "Gabriel", ["X salada", "X bacon"], "Pix")

#O que eu posso fazer com o objeto? - Ações - Métodos
#acessar um atributo do objeto
print(novoPedido.numero)
print(novoPedido.status)

#alterar os dados de um atibuto.
novoPedido.cliente="Gabriel Cristaldo"
print(novoPedido.cliente)

#chamando os métodos.
novoPedido.imprimir()
novoPedido.atualizar_Pedido("Em preparo")
novoPedido.status = "Em preparo"