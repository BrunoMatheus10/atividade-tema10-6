# Solicitar a mensagem do usuário
mensagem = input("Digite a mensagem a ser criptografada: ")

# Definir o deslocamento (pode ser alterado conforme necessário)
deslocamento = 3

# Inicializar a mensagem criptografada
mensagem_criptografada = ""

# Criptografar a mensagem
for char in mensagem:
    if char.isalpha():
        ascii_offset = 65 if char.isupper() else 97
        mensagem_criptografada += chr((ord(char) - ascii_offset + deslocamento) % 26 + ascii_offset)
    else:
        mensagem_criptografada += char

# Mostrar a mensagem criptografada
print("Mensagem criptografada:", mensagem_criptografada)
