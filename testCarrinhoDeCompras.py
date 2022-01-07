from carrinhoDeCompras import CarrinhoDeCompras 
from carrinhoDeCompras import MyError
import unittest

class TestCarrinhoDeCompras(unittest.TestCase):

  def setUp(self):
    self.carrinho = CarrinhoDeCompras(5)

  def test_total_is_zero_on_initialization(self):
    self.assertEqual(0, self.carrinho.total)

  def test_adicionar_um_produto_ao_carrinho_de_compras(self):
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.assertEqual(self.carrinho.carrinho[0], "Arroz")

  def test_adicionar_dois_produtos_ao_carrinho_de_compras(self):
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Frango", 15)
    self.assertEqual(len(self.carrinho.carrinho), 2)

  def test_remover_um_produto_do_carrinho_de_compras(self):
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Frango", 15)
    self.carrinho.removerDoCarrinhoDeCompras("Arroz")
    self.assertEqual(len(self.carrinho.carrinho), 1)

  def test_remover_todos_produtos_iguais_do_carrinho_de_compras(self):
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Frango", 15)
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Doce", 10)
    self.carrinho.removerDoCarrinhoDeCompras("Arroz", todos=True)
    self.assertEqual(len(self.carrinho.carrinho), 2)

  def test_remover_produto_carrinho_vazio(self):
    self.assertRaises(MyError, lambda: self.carrinho.removerDoCarrinhoDeCompras("Frango"))

  def test_tamanho_carrinho_de_compras_ao_adicionar_produtos(self):
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Frango", 15)
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Doce", 10)
    self.assertEqual(self.carrinho.tamanhoCarrinhoDeCompras(), 4)

  def test_tamanho_carrinho_de_compras_vazio(self):
    self.assertEqual(self.carrinho.tamanhoCarrinhoDeCompras(), 0)

  def test_adicionar_produto_carrinho_de_compras_cheio(self):
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Frango", 15)
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Doce", 10)
    self.assertRaises(MyError, lambda: self.carrinho.adicionarAoCarrinhoDeCompras("Bala", 5))

  def test_finalizar_compra(self):
    self.carrinho.adicionarAoCarrinhoDeCompras("Arroz", 20)
    self.carrinho.adicionarAoCarrinhoDeCompras("Frango", 15)
    self.assertEqual(self.carrinho.finalizarCompra(), 35)
  
if __name__ == "__main__":
  unittest.main()