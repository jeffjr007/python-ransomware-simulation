import os
import pyaes

# Função para descriptografar um arquivo
def decrypt_file(file_name):
    # Abrir o arquivo criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Chave para descriptografia
    key = b"testeransomwares"  # A chave para descriptografia deve ser a mesma usada para criptografar

    # Inicializar o AES no modo CTR
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar os dados
    decrypted_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Criar o arquivo descriptografado
    decrypted_file_name = file_name.replace(".ransomwaretroll", "")
    with open(decrypted_file_name, "wb") as new_file:
        new_file.write(decrypted_data)

    print(f"Arquivo descriptografado com sucesso: {decrypted_file_name}")

# Exemplo de uso
if __name__ == '__main__':
    file_name = input("Digite o caminho do arquivo para descriptografar: ")
    decrypt_file(file_name)
