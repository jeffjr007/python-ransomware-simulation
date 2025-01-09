# Ransomware Educacional em Python

Este repositório contém uma simulação de ataque de **Ransomware** utilizando Python. O objetivo é demonstrar como a criptografia de arquivos pode ser realizada de forma simples, com foco no aprendizado sobre segurança cibernética e criptografia. **Este projeto é para fins educacionais e deve ser utilizado apenas em ambientes controlados**.

## 🚨 Aviso Importante
Este projeto é uma **simulação de Ransomware** e deve ser utilizado com **responsabilidade**. Não use este código em ambientes de produção ou sem permissão. O uso indevido pode resultar em sérias consequências legais. Este projeto deve ser executado apenas para fins educacionais e de aprendizado em ambientes de teste controlados.

## 🔑 Objetivo
Simular um ataque de Ransomware para criptografar e descriptografar arquivos utilizando a biblioteca `pyaes` em modo CTR. O projeto tem como foco o aprendizado de conceitos de criptografia e segurança, demonstrando como a criptografia de arquivos pode ser realizada de forma simples.

## ⚙️ Ferramentas Utilizadas
- **Python 3.x**
- **pyaes** (biblioteca para criptografia AES)
- **Sistema Operacional**: Qualquer sistema que suporte Python e `pyaes`.

## 📂 Arquivos do Projeto
- `encrypter.py`: Código para criptografar arquivos.
- `decrypter.py`: Código para descriptografar arquivos criptografados.

## 🚀 Como Executar o Código

### Passo 1: Instalar a biblioteca `pyaes`
Para executar este projeto, é necessário ter a biblioteca `pyaes` instalada. Você pode instalá-la utilizando o `pip`:

pip install pyaes

## Passo 2: Criptografar um arquivo
- Execute o script encrypter.py para criptografar um arquivo.
- O código pedirá o caminho do arquivo a ser criptografado.
- O arquivo será criptografado e a versão criptografada será salva com a extensão .ransomwaretroll.

python encrypter.py

## Passo 3: Descriptografar um arquivo
- Execute o script decrypter.py para descriptografar um arquivo criptografado.
- O código pedirá o caminho do arquivo criptografado (com a extensão .ransomwaretroll).
- O arquivo será restaurado ao seu estado original.

python decrypter.py

## 📝 Exemplo de Uso
- Criptografando o arquivo:

- Arquivo original: documento.txt
- Arquivo criptografado: documento.txt.ransomwaretroll
##  Descriptografando o arquivo:

- Arquivo criptografado: documento.txt.ransomwaretroll
- Arquivo restaurado: documento.txt
## 📜 Licença
Este repositório é apenas para fins educacionais. O uso indevido pode resultar em consequências legais. Este projeto deve ser utilizado apenas em ambientes controlados e com permissão explícita para realizar testes de segurança. Ao utilizar este código, você concorda em usá-lo de forma responsável e ética.
