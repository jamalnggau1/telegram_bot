from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class isChangeMeetingStatus(BoundFilter):

    async def check(self, callback:types.CallbackQuery):

        print(f'''----------isChangeMeetingStatus callback.data.split(':')[0]{callback.data.split(':')[0]}----------------''')
        return callback.data.split(':')[0]=='meeting_status'