from Insta_bot import InstaFollower

bot = InstaFollower()

username = ""       #write your instagram username
password = ""       #write your instagram password


def bot_on():
    bot.login(username=username, password=password)
    bot.find_followers()
    bot.follow_people()


bot_on()
