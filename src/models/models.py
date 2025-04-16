from typing import Literal

from pydantic import BaseModel


class Proxy(BaseModel):
    address: str
    port: str
    user: str | None = None
    password: str | None = None

    @property
    def url(self) -> str:
        """Генерирует proxy-URL"""
        if self.user and self.password:
            return f"http://{self.user}:{self.password}@{self.address}:{self.port}"
        else:
            return f"http://{self.address}:{self.port}"

    @property
    def proxies(self) -> dict[str, str]:
        """Генерирует словарь proxies для передачи в requests"""
        return {
            'http': self.url,
            'https': self.url
        }

class AIMessage(BaseModel):
    role: Literal['system', 'assistant', 'user']
    content: str
