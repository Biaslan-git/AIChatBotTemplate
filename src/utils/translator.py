from langdetect import detect
from googletrans import Translator

async def translate_to_ru(text: str) -> str:
    async with Translator() as translator:
        try:
            lang = detect(text)
            if lang != 'ru':
                result = await translator.translate(text, dest='ru')
                return result.text
        except Exception as e:
            pass
        return text


