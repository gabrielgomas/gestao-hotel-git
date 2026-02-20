class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo  # Ex: 'Single', 'Double', 'Suite'
        self.preco = preco
        self.disponivel = True

    def __str__(self):
        estado = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} ({self.tipo}) - {self.preco}€/noite - [{estado}]"