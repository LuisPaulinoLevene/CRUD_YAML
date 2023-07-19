import yaml
def ver_computador(computadores):
    ID = input('Escreva o codigo computador: ')
    for computador in computadores:
        if computador['ID'] == ID:
            print(computador)

def ver_computador_da_base_de_dados_yaml():
    dict_ds ={}
    with open('./base_de_dados.yaml', 'r') as ds:
        dict_ds = yaml.load(ds, Loader=yaml.FullLoader)
        ver_computador(dict_ds['computadores'])