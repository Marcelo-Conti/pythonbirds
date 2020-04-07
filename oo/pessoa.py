class Pessoa:
    def __init__(self, *filhos, nome=None, idade=55):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__=='__main__':
    Ana = Pessoa(nome='Ana')
    Bruna = Pessoa(nome='Bruna')
    Marcelo = Pessoa(Ana,Bruna,nome='Marcelo')
    print(Pessoa.cumprimentar(Marcelo))
    print(id(Marcelo))
    print(Marcelo.cumprimentar())
    print(Marcelo.nome)
    print(Marcelo.idade)
    for filhos in Marcelo.filhos:
        print(filhos.nome)
    Marcelo.sobrenome='De Conti'
    del Marcelo.filhos
    print(Marcelo.__dict__)
    print(Ana.__dict__)