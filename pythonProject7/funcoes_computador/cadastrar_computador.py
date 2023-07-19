import yaml
from yaml.loader import SafeLoader
import secrets


def cadastrar_computador(computadores):
        a = secrets.randbits(9)
        b = secrets.randbits(12)
        marca = input('Escreva a marca: ')
        modelo = input('Escreva o modelo: ')
        ano_de_fabrico = input('Escreva o ano de fabrico: ')
        ID = f'86{a}{b}'
        print(
        f'A marca do seu computador e: {marca} \nO Modelo do seu computador e: {modelo} \nAno de fabrico: {ano_de_fabrico}, \nO Codigo atribuido e: {ID}\nN.B.: Guarde o codigo atribuido pelo sistema.')

        computador = {
            "Marca": marca,
            "Modelo": modelo,
            "Ano_de_fabrico": ano_de_fabrico,
            "ID": ID
        }
        computadores.append(computador)

def cadastrar_computador_da_base_de_dados_yamil():

    dict_ds={}
    # Open the file and load the file
    with open('./base_de_dados.yaml','r') as ds:
        dict_ds = yaml.load(ds, Loader=yaml.FullLoader)
        '''print(dict_ds)'''

    with open('./base_de_dados.yaml', 'w') as ds:
        try:
            cadastrar_computador(dict_ds['computadores'])
            yaml.dump(dict_ds,ds)
        except Exception as _:
            yaml.dump(dict_ds,ds)


