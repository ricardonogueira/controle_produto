import json

def gravar_registro_usuario(usuario, senha):
    usuarios = []

    with open('usuarios.json', 'r') as arq:
        usuarios = json.load(arq)

    usuarios.append({"usuario": usuario,"senha": senha})

    usuarios_json = json.dumps(usuarios)
    with open('usuarios.json', 'w') as arq:
        arq.write(usuarios_json)