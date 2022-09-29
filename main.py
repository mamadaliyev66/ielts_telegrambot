#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

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
    ["Essential Words"],

]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


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
    markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)
    await update.message.reply_html(
        "Questions Menu",
        reply_markup=markup2,
    )
    
    
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_html(
        "Main Menu",
        reply_markup=markup,
    )
reply_keyboard3 = [
        ["Essential 1"],
        ["Back◀️"]


    ]   

 
async def essential_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    markup3= ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True)
    await update.message.reply_html(
        "Essential Words Menu",
        reply_markup=markup3,
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


reply_keyboard4=[
    ["Unit 1","Unit 2","Unit 3"],
    ["Unit 4","Unit 5","Unit 6"],
    ["Unit 7","Unit 8","Unit 7"],
    ["Unit 8","Unit 9","Unit 10"],
    ["Unit 11","Unit 12","Unit 13"],
    ["Unit 14","Unit 15","Unit 16"],
    ["Unit 17","Unit 18","Unit 19"],
    ["Unit 20","Unit 21","Unit 22"],
    ["Unit 23","Unit 24","Unit 25"],
    ["Unit 26","Unit 27","Unit 28"],
    ["Unit 29","Unit 30"],
    
    ["Back🔙","Main Menu⬅️"],
]

reply_keyboardut=[
    ["Part A","Part B"],
    ["Back","Main Menu⬅️"],

]

async def testmenu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    markuput= ReplyKeyboardMarkup(reply_keyboardut, one_time_keyboard=True)

    await update.message.reply_text(
        update.message.text,
        reply_markup=markuput,
    )    

async def parta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # markuput= ReplyKeyboardMarkup(reply_keyboardut, one_time_keyboard=True)
    await update.message.reply_text(
        "Part 🅰️: Choose the right word for the given definition."
    )
    questions = ["A: Afraid", "B: Clever", "C: Cruel", "D: Hunt"]
    message0 = await update.effective_message.reply_poll(
        "1. bad or hurting others ", questions, type=Poll.QUIZ, correct_option_id=2
    )
    questions = ["A: Angry", "B: Clever", "C: Finally", "D: Reply"]
    message1 = await update.effective_message.reply_poll(
        "2. at last or at the end ", questions, type=Poll.QUIZ, correct_option_id=2
    )
    questions = ["A: Attack", "B: Middle ", "C: Pleased ", "D: Trick"]
    message2 = await update.effective_message.reply_poll(
        "3. to try to fight or hurt ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["A: Agree ", "B: Hide", "C: Safe", "D: Well"]
    message3 = await update.effective_message.reply_poll(
        "4. to not let others see", questions, type=Poll.QUIZ, correct_option_id=1
    )
    questions = ["A: Bottom", "B: Lot", "C: Moment", "D: Promise"]
    message4 = await update.effective_message.reply_poll(
        "5. the lowest part", questions, type=Poll.QUIZ, correct_option_id=0
    )

async def partb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Part 🅱️: Choose the right definition for the given word."
    )
    questions = ["A: Happy", "B: Low", "C: Mad", "D: Scared"]
    message0 = await update.effective_message.reply_poll(
        "1. Angry - ...", questions, type=Poll.QUIZ, correct_option_id=3
    )
    questions = ["A: A hole with water in it", "B: a short time", "C: at the center", "D: at the end"]
    message1 = await update.effective_message.reply_poll(
        "2. Moment - ... ", questions, type=Poll.QUIZ, correct_option_id=1
    )
    questions = ["A: to say ``good job``", "B: to say ``I will``", "C: to say ``the end``", "D: to say ``maybe``"]
    message2 = await update.effective_message.reply_poll(
        "3. Promise", questions, type=Poll.QUIZ, correct_option_id=1
    )
    questions = ["A: to answer ", "B: to get to a place", "C: to look for in order to kill", "D: to try fight or hunt"]
    message3 = await update.effective_message.reply_poll(
        "4. Reply - ...", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["A: Fool", "B: having much or many ", "C: not seen", "D: not worried about being hurt"]
    message4 = await update.effective_message.reply_poll(
        "5. Safe -...", questions, type=Poll.QUIZ, correct_option_id=3
    )   



reply_keyboardu = [
        ["Words"],
        ["Tests"],
        ["Back🔙","Main Menu⬅️"]


    ]   

 
async def unit1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    markupu= ReplyKeyboardMarkup(reply_keyboardu, one_time_keyboard=True)

    await update.message.reply_text(
        update.message.text,
        reply_markup=markupu,
    )    

essential_unit_1=pd.read_excel("essential_unit_1.xlsx")
essential_unit_1_english=essential_unit_1["english"].tolist()
rfe=0

async def unit2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    markupu= ReplyKeyboardMarkup(reply_keyboardu, one_time_keyboard=True)
    
    
    
    
    
    
    await update.message.reply_html(
        "Coming Soon ... ",
        reply_markup=markupu,
    )    



async def unit3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    markupu= ReplyKeyboardMarkup(reply_keyboardu, one_time_keyboard=True)
    await update.message.reply_html(
        "Coming Soon ... ",
        reply_markup=markupu,
    )    













async def essential1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    markup4= ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=True)
    await update.message.reply_html(
        "Essential 1 \n"
        "The bot sends you English words,\n you translate them into Uzbek and send them.",
        
        reply_markup=markup4,
    )    






reply_keyboard5=[
    ["Next"],
    ["Back🔙","Main Menu⬅️"]
]




async def start_essential_words(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    markup5= ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=True)
    global rfe
    # rfe=randint(0,len(essential_unit_1)-1)
    
    questions = ["Hidlamoq", "Qo'rqqan,cho'chigan", "Xovotirlangan", "Yakunlamoq"]
    message0 = await update.effective_message.reply_poll(
        "Afraid - ... ? ", questions, type=Poll.QUIZ, correct_option_id=1
    )
    questions = ["Rozi bo'lmoq", "Afsuslanmoq", "Jahli chiqqan", "Yakunlamoq"]
    message1 = await update.effective_message.reply_poll(
        "Agree - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Hidlamoq", "Xovotirlangan", "Yumush, mahsus topshiriq", "Jahli chiqqan, badjahl"]
    message2 = await update.effective_message.reply_poll(
        "Angry - ... ? ", questions, type=Poll.QUIZ, correct_option_id=3
    )
    questions = ["Hujum Qilmoq", "Qarshi Turmoq", "Afsuslanmoq", "Yakunlamoq"]
    message3 = await update.effective_message.reply_poll(
        "Attack - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Javob Bermoq", "o'rta", "tag, pastki qism", "Xavfsiz,bexatar"]
    message4 = await update.effective_message.reply_poll(
        "Bottom - ... ? ", questions, type=Poll.QUIZ, correct_option_id=2
    )
    
    
    questions = ["Yaxshi", "Aqilli", "Hursand,mamnun", "Javob Bermoq"]
    message5 = await update.effective_message.reply_poll(
        "Clever - ... ? ", questions, type=Poll.QUIZ, correct_option_id=1
    )
    questions = ["Shafqatsiz,berahim", "Hujum qilmoq", "Va'da Bermoq", "Javob Bermoq"]
    message6 = await update.effective_message.reply_poll(
        "Cruel  - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Juda ko'p", "Ov qilmoq", "Sekun,on,zum", "Axiyri,vanihoyat"]
    message7 = await update.effective_message.reply_poll(
        "Finally  - ... ? ", questions, type=Poll.QUIZ, correct_option_id=3
    )
    questions = ["Yashirinmoq,berkinmoq", "Yaratmoq", "Tajriba,Sinov", "Yoqolib,qolmoq"]
    message8 = await update.effective_message.reply_poll(
        " Hide - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Fikriga qo'shilmoq", "Alilli", "Ov qilmoq,ovlamoq", "Yashirinmoq"]
    message9 = await update.effective_message.reply_poll(
        "Hunt  - ... ? ", questions, type=Poll.QUIZ, correct_option_id=2
    )
    questions = ["Juda Ko'p", "Sekun,on.zum", "Yetib kelmoq,kelmoq", "axiyri,vanihoyat"]
    message10 = await update.effective_message.reply_poll(
        " Lot - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Yetib kelmoq,kelmoq", "Shafqatisiz,Berahim", "Hursand,mamnun", "Javob bermoq"]
    message11 = await update.effective_message.reply_poll(
        " Arrive - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Jahli chiqqan", "Pastki", "Yuqori", "O'rta"]
    message12 = await update.effective_message.reply_poll(
        " Middle - ... ? ", questions, type=Poll.QUIZ, correct_option_id=3
    )
    
    questions = ["Secund,on,zum", "O'rta", "juda Ko'p", "Va'da bermoq"]
    message13 = await update.effective_message.reply_poll(
        "Moment  - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Aqilli,Ziyrak", "Xiyla,nayrang;fokus", "Hursand,mamnun", "tag,pastki qisim"]
    message14 = await update.effective_message.reply_poll(
        " Pleased - ... ? ", questions, type=Poll.QUIZ, correct_option_id=2
    )
    questions = ["Va'da Bermoq", "Xavfsiz", "Yaxshi", "Fokus"]
    message15 = await update.effective_message.reply_poll(
        " Promise - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    questions = ["Yomon,yovuz", "Qo'rqan,cho'chigan", "Javob Bermoq", "Yetib kelmoq"]
    message16 = await update.effective_message.reply_poll(
        " Reply - ... ? ", questions, type=Poll.QUIZ, correct_option_id=2
    )
    questions = ["Yaxshi", "Xavfsiz,bexatar", "Xiyla,nayrang", "Kulgi"]
    message17 = await update.effective_message.reply_poll(
        " Safe - ... ? ", questions, type=Poll.QUIZ, correct_option_id=1
    )
    questions = ["ehtiyotkorlik blan", "Va'da bermoq", "Firibgar", "Xiyla,nayrang;fokus"]
    message18 = await update.effective_message.reply_poll(
        " Trick - ... ? ", questions, type=Poll.QUIZ, correct_option_id=3
    )
    questions = ["Jahli chiqqan", "Yaxshi", "Aqilli", "Yomon"]
    message19 = await update.effective_message.reply_poll(
        " Well - ... ? ", questions, type=Poll.QUIZ, correct_option_id=1
    )

    
    
    
    payload = {
        message0.poll.id: {"chat_id": update.effective_chat.id, "message_id": message0.message_id}
    }
    print(payload)
    context.bot_data.update(payload)
    # await update.message.reply_text(essential_unit_1_english[rfe], reply_markup=markup5,)
       





answer=excel_data_df['answer'].tolist()

async def qanswer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]

    await update.message.reply_text(
        answer[b],
        
    )
 
 
 
 
    

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a predefined poll"""
    questions = ["One", "Two", "Three", "Four"]
    message = await update.effective_message.reply_poll(
        "Bir - ... ? ", questions, type=Poll.QUIZ, correct_option_id=0
    )
    # Save some info about the poll the bot_data for later use in receive_quiz_answer
    payload = {
        message.poll.id: {"chat_id": update.effective_chat.id, "message_id": message.message_id}
    }
    context.bot_data.update(payload)


async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    # the bot can receive closed poll updates we don't care about
    if update.poll.is_closed:
        return
    if update.poll.total_voter_count == 3:
        try:
            quiz_data = context.bot_data[update.poll.id]
        # this means this poll answer update is from an old poll, we can't stop it then
        except KeyError:
            return
        await context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])
 
 
 
 
 
      

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
    markup_admin= ReplyKeyboardMarkup(reply_keyboard_admin, one_time_keyboard=True)
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
                MessageHandler(filters.Regex("^Essential Words$"),essential_menu),
                MessageHandler(
                    filters.Regex("Next➡️"),qnext
                ),
                MessageHandler(
                    filters.Regex("Answer✅"),qanswer,  
                ),
                MessageHandler(filters.Regex("Back◀️"),back),
                MessageHandler(filters.Regex("Essential 1"),essential1),
                MessageHandler(filters.Regex("Back🔙"),essential_menu),            
                MessageHandler(filters.Regex("Main Menu⬅️"),back),
                MessageHandler(filters.Regex("Next",),start_essential_words),
                MessageHandler(filters.Regex("Words"),start_essential_words),
                MessageHandler(filters.Regex("Tests"),testmenu),
                MessageHandler(filters.Regex("Part A"),parta ),
                MessageHandler(filters.Regex("Part B"),partb ),
                MessageHandler(filters.Regex("Back"),unit1),
                MessageHandler(filters.Regex("Unit 1"),unit1),
                MessageHandler(filters.Regex("Unit 2"),unit2),
                MessageHandler(filters.Regex("Unit 3"),unit3),
                MessageHandler(filters.Regex("Unit 4"),unit3),
                MessageHandler(filters.Regex("Unit 5"),unit3),
                MessageHandler(filters.Regex("Unit 6"),unit3),
                MessageHandler(filters.Regex("Unit 7"),unit3),
                MessageHandler(filters.Regex("Unit 8"),unit3),
                MessageHandler(filters.Regex("Unit 9"),unit3),
                MessageHandler(filters.Regex("Unit 10"),unit3),
                MessageHandler(filters.Regex("Unit 11"),unit3),
                MessageHandler(filters.Regex("Unit 12"),unit3),
                MessageHandler(filters.Regex("Unit 13"),unit3),
                MessageHandler(filters.Regex("Unit 14"),unit3),
                MessageHandler(filters.Regex("Unit 15"),unit3),
                MessageHandler(filters.Regex("Unit 16"),unit3),
                MessageHandler(filters.Regex("Unit 17"),unit3),
                MessageHandler(filters.Regex("Unit 18"),unit3),
                MessageHandler(filters.Regex("Unit 19"),unit3),
                MessageHandler(filters.Regex("Unit 20"),unit3),
                MessageHandler(filters.Regex("Unit 21"),unit3),
                MessageHandler(filters.Regex("Unit 22"),unit3),
                MessageHandler(filters.Regex("Unit 23"),unit3),
                MessageHandler(filters.Regex("Unit 24"),unit3),
                MessageHandler(filters.Regex("Unit 25"),unit3),
                MessageHandler(filters.Regex("Unit 26"),unit3),
                MessageHandler(filters.Regex("Unit 27"),unit3),
                MessageHandler(filters.Regex("Unit 28"),unit3),
                MessageHandler(filters.Regex("Unit 29"),unit3),
                MessageHandler(filters.Regex("Unit 30"),unit3),             
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
