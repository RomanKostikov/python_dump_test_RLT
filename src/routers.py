from json.decoder import JSONDecodeError

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from pydantic_core._pydantic_core import ValidationError

from .service import Service


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f'Hi <a href="t.me/'f'{message.from_user.username}">'
        f'{message.from_user.first_name}</a>!',
        disable_web_page_preview=True,
        parse_mode="HTML",
    )


@router.message()
async def salary_data(
        message: Message,
        service: Service = Service()
):
    user_input = message.text
    try:
        input_data = service.get_input_data(user_input)
    except (JSONDecodeError, ValidationError):
        await message.answer(
            'Невалидный запрос. Пример запроса:'
            '{'
            '"dt_from": "2022-09-01T00:00:00", '
            '"dt_upto": "2022-12-31T23:59:00", '
            '"group_type": "month"'
            '}'
        )
    except ValueError:
        await message.answer(
            '"group_type" должен быть hour, day или month'
        )
    else:
        await message.answer(
            service.get_datas_from_db(input_data).__str__()
        )
