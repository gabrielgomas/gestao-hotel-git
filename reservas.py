class Reserva:
    def __init__(self, id_reserva, cliente, quarto, noites):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.quarto = quarto
        self.noites = noites
        self.total = quarto.preco * noites
        # Ao criar reserva, o quarto fica ocupado
        quarto.disponivel = False

    def __str__(self):
        return (f"Reserva #{self.id_reserva}: {self.cliente.nome} "
                f"no Quarto {self.quarto.numero} por {self.noites} noites. "
                f"Total: {self.total}€")