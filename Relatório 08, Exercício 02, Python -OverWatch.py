class Heroi:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

    def usar_ultimate(self):
        raise NotImplementedError("As classes filhas devem implementar este método.")


class Tanque(Heroi):
    def usar_ultimate(self):
        print(f"{self.nome} usa o escudo impenetrável!")


class Dano(Heroi):
    def usar_ultimate(self):
        print(f"{self.nome} dispara uma rajada devastadora!")


if __name__ == "__main__":
    herois = [
        Tanque("Reinhardt", "Tanque"),
        Dano("Soldado 76", "Dano")
    ]

    for heroi in herois:
        heroi.usar_ultimate()
