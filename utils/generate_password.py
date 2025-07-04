import secrets
import string
import random


class PasswordGenerator:
    def __init__(self, length=12, use_digits=True, use_symbols=True) -> None:
        self.length = length
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def set_length(self, length: int) -> None:
        self.length = length

    def set_options(self, use_digits=None, use_symbols=None) -> None:
        if use_digits is not None:
            self.use_digits = use_digits
        if use_symbols is not None:
            self.use_symbols = use_symbols

    def generate(self) -> str:
        if self.length < 3:
            raise ValueError("Длина пароля должна быть больше 2")
        letter_chars = string.ascii_letters
        digit_chars = string.digits
        symbol_chars = string.punctuation
        password = []
        chars = letter_chars
        password.append(secrets.choice(letter_chars))
        if self.use_digits:
            chars += digit_chars
            password.append(secrets.choice(digit_chars))
        if self.use_symbols:
            chars += symbol_chars
            password.append(secrets.choice(symbol_chars))

        while len(password)<self.length:
            password.append(secrets.choice(chars))

        random.shuffle(password)

        return ''.join(password)


if __name__ == "__main__":
    gen = PasswordGenerator()
    gen.set_length(23)
    gen.set_options(use_digits=False)
    print(gen.generate())