import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.produto.models import Produto


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random() * randint(10, 50),
                estoque=randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'apontador',
    'caderno 100 folhas',
    'caderno capa dura 200 folhas',
    'caneta esferográfica azul',
    'caneta esferográfica preta',
    'caneta esferográfica vermelha',
    'durex',
    'giz de cera 12 cores',
    'lapiseira 0.3 mm',
    'lapiseira 0.5 mm',
    'lapiseira 0.7 mm',
    'lápis de cor 24 cores',
    'lápis',
    'papel sulfite A4 pacote 100 folhas',
    'pasta elástica',
    'tesoura',
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)

toc = timeit.default_timer()

print(toc - tic)
