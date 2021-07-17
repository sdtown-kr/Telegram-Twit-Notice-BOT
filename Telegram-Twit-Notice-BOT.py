import telepot
import requests
import twitter

bot_token = 'BOT TOKEN HERE'
chat_id = 'CHAT ID HERE'
bot = telepot.Bot(bot_token)

#chat_id = bot.getUpdates()[-1].message.chat.id #가장 최근 메세지의 chatID 불러옴

twitter_consumer_key = 'TWITTER API KEY HERE'
twitter_consumer_secret = 'TWITTER API SECRET HERE'
twitter_access_token = 'TWITTER ACCESS TOKEN HERE'
twitter_access_secret = 'TWITTER ACCESS SECRET HERE'

twitter_api = twitter.Api(consumer_key = twitter_consumer_key,
                         consumer_secret = twitter_consumer_secret,
                         access_token_key = twitter_access_token,
                         access_token_secret = twitter_access_secret)

account = '@ACCOUNT ID'
statuses = twitter_api.GetUserTimeline(screen_name = account, count = 1,
                                      include_rts = True, exclude_replies = False)
print(statuses[0].text)

bot.sendMessage(chat_id, statuses[0].text)

while True:
    pass
