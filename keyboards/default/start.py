from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

share_contact = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="☎️ Share phone number", request_contact=True)
    ]], resize_keyboard=True
)

share_location = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="📍 Share my location", request_location=True)
    ]], resize_keyboard=True
)

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎓 Course"),
            KeyboardButton(text="🎉 Events")
        ],
        [
            KeyboardButton(text="☎️ Contacts"),
            KeyboardButton(text="⚙️ Settings")
        ]
    ], resize_keyboard=True
)

courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🐍 Backend (Python)"),
            KeyboardButton(text="🔒 Cyber Security")
        ],
        [
            KeyboardButton(text="🧩 Graphic Design"),
            KeyboardButton(text="📸 Mobilography")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)
