from aiogram import Router, F
from aiogram.types import Message

from utils.ai_responder import send_ai_response
from models import AIMessage, Proxy
from services.ai_api import GroqModel, get_chat_response
from settings import Settings

router = Router()

settings = Settings()
ai_client = GroqModel(
    api_key=settings.AI_API_TOKEN,
    proxy=Proxy(
        address=settings.PROXY_ADDRESS,
        port=settings.PROXY_PORT,
        user=settings.PROXY_USER,
        password=settings.PROXY_PASSWORD
    )
)

@router.message(F.text)
async def message_to_ai(message: Message) -> None:
    response = get_chat_response(ai_client, [
        AIMessage(role='user', content=str(message.text))
    ], stream=True)
    print(response)
    await send_ai_response(message, response)
