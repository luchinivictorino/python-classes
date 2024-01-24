# Crie um programa para realizar a criptografia e a descriptografia uma mensagem informada pelo usuário.
# Utilize programação orientada a objeto e dentro do objeto adicione o alfabeto como uma lista.

class Cryptography:
    def __init__(self):
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

    def encrypt(self, message):
        encrypted_message = ''
        for letter in message:
            if letter in self.alphabet:
                encrypted_message += self.alphabet[(self.alphabet.index(letter) + 3) % len(self.alphabet)]
            else:
                encrypted_message += letter
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ''
        for letter in message:
            if letter in self.alphabet:
                decrypted_message += self.alphabet[(self.alphabet.index(letter) - 3) % len(self.alphabet)]
            else:
                decrypted_message += letter
        return decrypted_message


cryptography = Cryptography()

result = cryptography.encrypt('hello world')
print(result)

result = cryptography.decrypt(result)
print(result)