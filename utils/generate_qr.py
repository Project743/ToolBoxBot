import qrcode
from io import BytesIO
from abc import ABC, abstractmethod
from typing import Optional


class QRCodeGenerator(ABC):
    """Абстрактный родительский класс"""

    def __init__(self, filename: str = "qr.png") -> None:
        self.filename: str = filename

    @abstractmethod
    def build_data(self) -> str:
        """Метод для возврата строки для кодирования"""
        pass

    def generate(self) -> BytesIO:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.build_data())
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        return buffer


class WiFiQRCode(QRCodeGenerator):
    def __init__(self, ssid: str, password: str, security: str = "wpa", filename: str = "wifi_qr.png") -> None:
        super().__init__(filename)
        self.ssid: str = ssid
        self.password: str = password
        self.security = security if self.password else ""


    def build_data(self) -> str:
        return f"WIFI:T:{self.security};S:{self.ssid};P:{self.password};;"


class VCardQRCode(QRCodeGenerator):
    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
        org: Optional[str] = None,
        filename: str = "vcard_qr.png",
    ) -> None:
        super().__init__(filename)
        self.name: str = name
        self.phone: str = phone
        self.email: str = email
        self.org: Optional[str] = org

    def build_data(self) -> str:
        vcard = (
            "BEGIN:VCARD\n"
            "VERSION:3.0\n"
            f"N:{self.name}\n"
            f"TEL:{self.phone}\n"
            f"EMAIL:{self.email}\n"
        )
        if self.org:
            vcard += f"ORG:{self.org}\n"
        vcard += "END:VCARD"
        return vcard


class TextQRCode(QRCodeGenerator):
    def __init__(self, text: str, filename: str = "text_qr.png") -> None:
        super().__init__(filename)
        self.text: str = text

    def build_data(self) -> str:
        return self.text


if __name__ == "__main__":
    wifi_qr = WiFiQRCode(ssid="MyWiFi", password="12345678")
    # Пример сохранения для проверки
    with open("wifi_qr_test.png", "wb") as f:
        f.write(wifi_qr.generate().getbuffer())

    vcard_qr = VCardQRCode(name="Иван Иванов", phone="+79998887766", email="ivan@example.com", org="")
    with open("vcard_qr_test.png", "wb") as f:
        f.write(vcard_qr.generate().getbuffer())

    text_qr = TextQRCode(text="https://example.com")
    with open("text_qr_test.png", "wb") as f:
        f.write(text_qr.generate().getbuffer())
