from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import os
bot=ChatBot('Bot')
#conv=open('chat.txt')
#bot.set_trainer(ListTrainer)
#bot.train(conv)
trainer=ChatterBotCorpusTrainer(bot)
#trainer.train(conv)
for file in os.listdir('C:/Users/dell/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english'):
  trainer.train('C:/Users/dell/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/' + file)
  
while True:
    message = input('You:')
    print(message)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        print('ChatBot:', reply)
