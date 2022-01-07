class MyError(Exception):
    pass

class CarrinhoDeCompras:

    def __init__(self, tamanho):
        self.carrinho = []
        self.produtos = {}
        self.total = 0
        self.tamanho = tamanho

    def adicionarAoCarrinhoDeCompras(self, produto, preco):
        if (len(self.carrinho)+ 1) >= self.tamanho: raise MyError("Carrinho cheio")
        self.produtos[produto] = preco
        self.carrinho.append(produto)

    def removerDoCarrinhoDeCompras(self, produto, todos=False):
        if len(self.carrinho) == 0:
            raise MyError("Carrinho vazio")
        while(True):
            if produto in self.carrinho: self.carrinho.remove(produto)
            else: break

            if not todos:
                break

    def tamanhoCarrinhoDeCompras(self):
        return len(self.carrinho)

    def exibirCarrinhoDeCompras(self):
        return self.carrinho

    def finalizarCompra(self):
        for produto in self.carrinho:
            self.total += self.produtos[produto]
        return self.total