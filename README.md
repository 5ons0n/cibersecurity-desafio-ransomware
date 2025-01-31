**:::::::::::::::::: RANSOMWARE PARA FINS EDUCACIONAIS :::::::::::::::::::::::::**

Criar um ransomware e uma vacina para fins didáticos pode ser uma excelente maneira de entender como a criptografia funciona e como os ataques de ransomware operam. No entanto, é crucial lembrar que esse tipo de software pode ser extremamente prejudicial se usado de forma maliciosa. Nunca use esse código para causar danos a sistemas ou dados de outras pessoas.
Os arquivos contém exemplos simples de como você pode criar um script em Python que criptografa arquivos ".txt" em uma pasta específica e, em seguida, criar um script de descriptografia para reverter o processo.

Arquivos anexados:

- ransomware.py
- vacina.py

Como Funciona:

1. Criptografia:

O script de criptografia gera uma chave usando a biblioteca "cryptography.fernet".

Ele percorre todos os arquivos ".txt" na pasta "projeto_ransomware", criptografa o conteúdo e renomeia o arquivo para incluir "_private-root-win" no nome.

A chave de criptografia é salva em um arquivo chamado "chave_privada.key".

2. Descriptografia:

O script de descriptografia carrega a chave do arquivo "chave_privada.key".

Ele percorre todos os arquivos criptografados na pasta "projeto_ransomware", descriptografa o conteúdo e renomeia o arquivo de volta para o nome original.

Requisitos:
Instale a biblioteca cryptography usando pip:

> pip install cryptography


***TESTANDO EM UM INSTÂNCIA KALI LINUX***

Para testar os scripts de criptografia e descriptografia em um terminal do Kali Linux, siga os passos abaixo. Certifique-se de que você tem permissão para executar esses scripts e que está trabalhando em um ambiente controlado (por exemplo, uma máquina virtual ou um diretório isolado).

**PASSO 1: PREPARE O AMBIENTE**

1. Instale o Python e o pip (se ainda não estiver instalado):
> sudo apt update
sudo apt install python3 python3-pip

2. Instale a biblioteca cryptography:
> pip install cryptography

3. Crie a pasta projeto_ransomware:
> mkdir projeto_ransomware

4. Crie alguns arquivos ".txt" de teste dentro da pasta:
> echo "Arquivo 1 de teste" > projeto_ransomware/arquivo1.txt
> 
> echo "Arquivo 2 de teste" > projeto_ransomware/arquivo2.txt
>
> echo "Arquivo 3 de teste" > projeto_ransomware/arquivo3.txt

**Passo 2: Executar o Script de Criptografia**

1. Salve o script de criptografia em um arquivo chamado ransomware.py:
> nano ransomware.py

Cole o código do script de criptografia fornecido anteriormente, salve e saia do editor (Ctrl + X, depois Y para confirmar).

2. Execute o script de criptografia:
> python3 ransomware.py

3. Verifique os arquivos criptografados:
 - Os arquivos ".txt" originais serão substituídos por versões criptografadas com o sufixo "_private-root-win.txt".
 - Use o comando ls para listar os arquivos na pasta:
> ls projeto_ransomware

 - Você verá algo como:
> arquivo1_private-root-win.txt
> 
> arquivo2_private-root-win.txt
> 
> arquivo3_private-root-win.txt
> 
> chave_privada.key

**Passo 3: Executar o Script de Descriptografia**

1. Salve o script de descriptografia em um arquivo chamado "vacina.py":
> nano vacina.py

Cole o código do script de descriptografia fornecido anteriormente, salve e saia do editor.

2. Execute o script de descriptografia:
> python3 vacina.py

3. Verifique os arquivos descriptografados:
 - Os arquivos criptografados serão descriptografados e renomeados de volta para seus nomes originais.
 - Use o comando ls para listar os arquivos na pasta:
> arquivo1.txt
> 
> arquivo2.txt
> 
> arquivo3.txt
> 
> chave_privada.key

4. Verifique o conteúdo dos arquivos:
 - Use o comando cat para verificar o conteúdo de um arquivo:
> cat projeto_ransomware/arquivo1.txt

 - O conteúdo deve ser o mesmo que antes da criptografia:
> Arquivo 1 de teste



**Aviso Final:**
**Este código é apenas para fins educacionais. Nunca use esse código para causar danos a sistemas ou dados de outras pessoas. O uso indevido de ransomware é ilegal e antiético. Use esse conhecimento de forma responsável e sempre com permissão explícita para testar em sistemas que você possui ou controla.**

**Observações Importantes:**
**1. Ambiente Seguro:**
- Execute esses testes em um ambiente isolado, como uma máquina virtual ou um diretório dedicado.
- Nunca execute scripts de criptografia em sistemas de produção ou em arquivos importantes.

**2. Permissões:**
- Certifique-se de que você tem permissão para executar esses scripts no ambiente em que está trabalhando.

**3. Uso Responsável:**
- Esses scripts são apenas para fins educacionais. O uso indevido de ransomware é ilegal e antiético.

**Se seguir esses passos, você poderá testar os scripts de criptografia e descriptografia com segurança no Kali Linux.**

