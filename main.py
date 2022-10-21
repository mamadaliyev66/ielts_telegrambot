

from ast import Str
from email.message import Message
import logging
from random import random
import re
from secrets import choice
import pandas as pd
from random import randint
from typing import Dict
from telegram import __version__ as TG_VER
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    MessageHandler,
    PollAnswerHandler,
    PollHandler,
    filters,
    
    
)
from telegram import (
    KeyboardButton,
    KeyboardButtonPollType,
    Poll,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
    
)
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ["Questions"],
]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True)


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])

userr=[]
user_len=len(userr)+1  
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask user for input."""
    user = update.effective_user
    userr.append(user.name)
    await update.message.reply_html(
        rf"Well Come {user.mention_html()}!"
        "\nPress Next➡️ Button For Start Questions ",
        reply_markup=markup,
    )

    return CHOOSING
reply_keyboard2 = [
        ["Next➡️","Answer✅"],
        ["Back◀️"]

    ]

excel_data_df = pd.read_excel('questions.xlsx')
question=excel_data_df['questions'].tolist()
b=0


async def regular_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True,resize_keyboard=True)
    await update.message.reply_html(
        "Questions Menu",
        reply_markup=markup2,
    )
    
    
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(
        "Main Menu",
        reply_markup=markup,
    )




async def qnext(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask the user for info about the selected predefined choice."""
    text = update.message.text
    from random import randint,choice
    global b
    b=randint(0,len(excel_data_df)-2)
    context.user_data["choice"] = text
    await update.message.reply_text(question[b])
    return CHOOSING





reply_keyboard5=[
    ["Next"],
    ["Back🔙","Main Menu⬅️"]
]

answer=excel_data_df['answer'].tolist()

async def qanswer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]

    await update.message.reply_text(
        answer[b],
        
    )
async def all_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    await update.message.reply_text(
        userr,
        
    )   
async def len_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    await update.message.reply_text(
        user_len,
        
    )   
  
reply_keyboard_admin = [
        ["Users👤"],
        ["Users Length🔢"],
        ["Main Menu⬅️"],


    ]   
   
async def typing_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    markup_admin= ReplyKeyboardMarkup(reply_keyboard_admin, one_time_keyboard=True,resize_keyboard=True)
    await update.message.reply_html(
       "Admin Menu",
       reply_markup=markup_admin
        
    )















def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("2109667277:AAF7H179Zj9baAIMwH2PZDstwFXx3Ky0oSk").build()

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [
                MessageHandler(
                    filters.Regex("^(Questions)$"), regular_choice
                ),
                MessageHandler(
                    filters.Regex("Next➡️"),qnext
                ),
                MessageHandler(
                    filters.Regex("Answer✅"),qanswer,  
                ),
                MessageHandler(filters.Regex("Back◀️"),back),
                        
                MessageHandler(filters.Regex("Users👤"),all_users),            
                MessageHandler(filters.Regex("Users Length🔢"),len_users)             

                
                ],
            TYPING_CHOICE: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^answer$")), regular_choice,
    
                
                )
            ],
            
            
        },
    
        fallbacks=[MessageHandler(filters.Regex("^369247591801Takoshi$"), typing_choice)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
