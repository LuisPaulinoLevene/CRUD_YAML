import yaml
def ver_computadores(computadores):
    for computador in computadores:
        print(computador)

def ver_computadores_da_base_de_dados_yaml():
    dict_ds ={}
    with open('./base_de_dados.yaml', 'r') as ds:
        dict_ds = yaml.load(ds, Loader=yaml.FullLoader)
        ver_computadores(dict_ds['computadores'])