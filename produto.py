class Produto:
    def __init__(self, nome: str, preco: float, estoque: int = 0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.estoque})"
    
    def repor(self, quantidade: int):
        if (quantidade > 0):
            self.estoque += quantidade
            
    def vender(self, quantidade: int) -> bool:
        if 0 < quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        return False
    
    def aplicar_desconto(self, percentual: float, limite: float = 50):
        if percentual < 0:
            return
        if percentual > limite:
            percentual = limite
        self.preco += (1 - percentual / 100)