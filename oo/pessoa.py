class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=55):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__=='__main__':
    Ana = Pessoa(nome='Ana')
    Bruna = Pessoa(nome='Bruna')
    Marcelo = Homem(Ana,Bruna,nome='Marcelo')
    print(Pessoa.cumprimentar(Marcelo))
    print(id(Marcelo))
    print(Marcelo.cumprimentar())
    print(Marcelo.nome)
    print(Marcelo.idade)
    for filhos in Marcelo.filhos:
        print(filhos.nome)
    Marcelo.sobrenome='De Conti'
    del Marcelo.filhos
    Ana.olhos = 1
    del Ana.olhos
    print(Marcelo.__dict__)
    print(Ana.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Ana.olhos)
    print(id(Pessoa.olhos),id(Ana.olhos))
    print(Pessoa.metodo_estatico(), Marcelo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Marcelo.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(Marcelo,Pessoa))
    print(isinstance(Marcelo,Homem))