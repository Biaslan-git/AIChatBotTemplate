from typing import Generator, List, Protocol, Text

from groq import DefaultHttpxClient, Groq

from models import AIMessage, Proxy


class TextModelProtocol(Protocol):
    def __init__(
        self, 
        api_key: str, 
        proxy: Proxy | None = None
    ) -> None:
        ...
    def generate(
        self, 
        stream: bool,
        messages: List[AIMessage],
        default_model: str = 'llama3-70b-8192'
    ) -> Generator[str, None, None] | str:
        ...

class GroqModel:
    def __init__(self, api_key: str, proxy: Proxy | None = None) -> None:
        self.client = Groq(
            api_key=api_key,
            http_client=DefaultHttpxClient(
                proxy=proxy.url if proxy else None,
            ),
        )

    def generate(
        self, 
        stream: bool,
        messages: list[AIMessage],
        default_model: str = 'llama3-70b-8192'
    ) -> Generator[str, None, None] | str:
        """Генерация ответа"""
        response = self.client.chat.completions.create(
            messages=[message.__dict__ for message in messages], # type: ignore 
            model=default_model,
            stop=None,
            stream=stream,
        )

        if stream: 
            for chunk in response:
                yield chunk.choices[0].delta.content
        else:
            return response.choices[0].message.content


def get_chat_response(model: TextModelProtocol, messages: list[AIMessage], stream: bool) -> Generator[str, None, None] | str:
    return model.generate(
        messages=messages,
        stream=stream
    )



