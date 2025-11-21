from produto import Produto

def test_venda_sucesso():
    p = Produto("Mouse", 100, estoque=10)
    assert p.vender(2)
    assert p.estoque == 8

def test_venda_insuficiente():
    p = Produto("Mouse", 50, estoque=1)
    assert not p.vender(2)
    assert p.estoque == 1

def test_repor_produto():
    p = Produto("Teclado", 100, estoque=5)
    p.repor(3)
    assert p.estoque == 8