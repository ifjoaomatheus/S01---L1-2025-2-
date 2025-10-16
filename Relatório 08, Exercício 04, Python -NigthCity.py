from abc import ABC, abstractmethod

class Cibernetico(ABC):
    @abstractmethod
    def realizar_hack(self):
        pass


class Implante:
    def __init__(self, custo, funcao):
        self.custo = custo
        self.funcao = funcao


class NetRunner(Cibernetico):
    def __init__(self, nome, custo_implante, funcao_implante):
        self.nome = nome
        self.implante = Implante(custo_implante, funcao_implante)

    def realizar_hack(self):
        print(f"{self.nome} usa o implante de {self.implante.funcao} para invadir o sistema!")


class Faccao:
    def __init__(self, membros):
        self.membros = membros

    def executar_hack_em_massa(self):
        print("Facção iniciando invasão coordenada...\n")
        for membro in self.membros:
            membro.realizar_hack()


if __name__ == "__main__":
    n1 = NetRunner("V", 5000, "Neural Link")
    n2 = NetRunner("Lucy", 7000, "Cérebro Cibernético")
    n3 = NetRunner("Kiwi", 6000, "Interface Neural Avançada")

    faccao = Faccao([n1, n2, n3])
    faccao.executar_hack_em_massa()
