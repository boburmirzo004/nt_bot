from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.start import courses, user_main_menu
from states.user import RegisterState

router = Router()


@router.message(F.text == "🎓 Course")
async def chat_course_handler(message: types.Message, state: FSMContext):
    text = "Information about all our courses"

    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "🐍 Backend (Python)")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = "📌 Backend kursi\n\nPython, PostgreSQL va API larni organasiz.\nDavomiyligi: 8 oy"
    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "🔒 Cyber Security")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = "🔒 Cyber Security"
    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "🧩 Graphic Design")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = "🧩 Graphic Design"
    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "📸 Mobilography")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = "📸 Mobilography"
    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "⬅️ Back")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = "⬅️ Back"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.clear()


@router.message(F.text == "☎️ Contacts")
async def chat_contacts_handler(message: types.Message):
    text = """Najot Talim filiallari:

        1 Shayxontohur
        📍 Manzil: Toshkent, Shayxontohur tumani
        📞 Telefon: +998 71 200-00-01

        2 Chilonzor
        📍 Manzil: Toshkent, Chilonzor tumani
        📞 Telefon: +998 71 200-00-02

        3 Yunusobod
        📍 Manzil: Toshkent, Yunusobod tumani
        📞 Telefon: +998 71 200-00-03

        4 Mirzo Ulugbek
        📍 Manzil: Toshkent, Mirzo Ulugbek tumani
        📞 Telefon: +998 71 200-00-04"""

    await message.answer(text=text, reply_markup=user_main_menu)
