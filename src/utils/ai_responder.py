from typing import Generator
import time

from aiogram.types import Message

from utils.translator import translate_to_ru

async def send_ai_response(message: Message, response: Generator[str, None, None] | str):
    """Отправляет пользователю ответ от ИИ, может отправлять и частями и целиком"""
    if isinstance(response, Generator):
        sent_message = await message.answer('...')
        last_update_time = 0  # Время последнего обновления
        full_response = ''
        for chunk in response:
            if chunk: 
                full_response += chunk
                current_time = time.time()

                if current_time - last_update_time >= 1.1:
                    try:
                        ru_text = await translate_to_ru(full_response)
                        await sent_message.edit_text(ru_text+'...')
                        last_update_time = time.time()
                    except Exception as e:
                        pass

        ru_text = await translate_to_ru(full_response)
        await sent_message.edit_text(ru_text)
    else:
        await message.answer(await translate_to_ru(response))

