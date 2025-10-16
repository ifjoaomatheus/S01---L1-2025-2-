class ArmaCorpoACorpo:
    def __init__(self, nome):
        self.nome = nome


class PhantomThieves:
    def __init__(self, nome, arma):
        self.nome = nome
        self.arma = arma


class Joker:
    def __init__(self, membros):
        self.arma = ArmaCorpoACorpo("Faca")  # composição
        self.membros = membros               # agregação

    def mostrar_equipe(self):
        print(f"Joker empunha uma {self.arma.nome}.")
        print("Equipe Phantom Thieves:")
        for membro in self.membros:
            print(f"- {membro.nome} usa {membro.arma}")


if __name__ == "__main__":
    membro1 = PhantomThieves("Panther", "Chicote")
    membro2 = PhantomThieves("Skull", "Cano de ferro")
    membro3 = PhantomThieves("Queen", "Luva de combate")

    equipe = [membro1, membro2, membro3]

    joker = Joker(equipe)
    joker.mostrar_equipe()
