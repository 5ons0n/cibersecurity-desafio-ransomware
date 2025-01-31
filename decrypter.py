import os
from cryptography.fernet import Fernet

# Pasta onde os arquivos criptografados estão localizados
pasta = "projeto_ransomware"

# Carregar a chave de criptografia
with open("chave_privada.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Função para descriptografar arquivos
def descriptografar_arquivos(pasta):
    for root, dirs, files in os.walk(pasta):
        for file in files:
            if file.endswith("_private-root-win.txt"):
                caminho_completo = os.path.join(root, file)
                with open(caminho_completo, "rb") as f:
                    dados_criptografados = f.read()
                dados_descriptografados = cipher_suite.decrypt(dados_criptografados)
                novo_nome = file.replace("_private-root-win.txt", ".txt")
                novo_caminho = os.path.join(root, novo_nome)
                with open(novo_caminho, "wb") as f:
                    f.write(dados_descriptografados)
                os.remove(caminho_completo)

# Descriptografar os arquivos na pasta
descriptografar_arquivos(pasta)

print("Arquivos descriptografados com sucesso!")
