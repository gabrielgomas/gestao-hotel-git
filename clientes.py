class Cliente:
    def __init__(self, id_cliente, nome, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"ID: {self.id_cliente} | Nome: {self.nome} | Email: {self.email}"