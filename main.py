import discord
import random
import requests
from keep import keep
from replit import db
import time
import asyncio

db['points'] = False
db['jay'] = 0
db['suzy'] = 0

emoji = ["💕", "❤️", "😘", "😍", "🥰"]
if "bot" not in db.keys():
  db["bot"] = True

if "points" not in db.keys():
  db['points'] = False


class MyClient(discord.Client):

  async def on_ready(self):
    print("looged in as :", client.user)

  async def on_message(self, message):
    user_id = 575594260800471050
    suzy = 1042119362468905070
    user1 = await client.fetch_user(user_id)
    user = await client.fetch_user(user_id)
    msg = message.content.lower()

    if message.author == client.user:
      return
    if "gif" in msg:
      return

    if "point" in msg and "bot" in msg:
      if "on" in msg:

        await message.channel.send("Points will be added now ✨")
        await asyncio.sleep(2)
        await message.channel.send("whoever gets 5 points first wins")
        db['points'] = True
        return
      if "off" in msg:
        await message.channel.send("Points will not be added now 🙏")
        db['points'] = False
        return
      if "reset" in msg:
        if db['points'] == False:
          await message.channel.send("Please turn on points first")
          return
        db['jay'] = 0
        db['suzy'] = 0
        await message.channel.send("points are reseted 🙌😊")
        return
      if "view" or "show" in msg:
        if db['points'] == False:
          await message.channel.send("Please turn on points first")
          return
        await message.channel.send("👑  Queen's Points = " + str(db['suzy']))
        await message.channel.send("😊  master's Points= " + str(db['jay']))
        return

    if ("off" in msg and "turn" in msg) or ("sleep" in msg) and "bot" in msg:
      await message.channel.send(
        "Okay! i am going to sleep now💤,Please wake me up again when you need me! 👋"
      )
      db['bot'] = False
      return
    if ("on" in msg and "turn" in msg) or ("wake" in msg) and "bot" in msg:
      if db['bot'] == True:
        await message.channel.send("I am already awake 🤗")
        return
      await message.channel.send("I am back again 🙏")
      if message.author.id == user_id:
        await message.channel.send("heyyy master ✌️ ")

        if message.author.id == suzy:
          await message.channel.send("hello! Queen👑 ,I missed You " +
                                     random.choice(emoji))

        db['bot'] = True
    if db['bot'] == False:
      return

    elif (msg.startswith("hello") or msg.startswith("hi")
          or msg.startswith("hey")) and ("master" not in msg or "jayesh"
                                         not in msg or "husband" not in msg
                                         or "baby" not in msg):

      if message.author.id == user_id:
        await message.channel.send("heyyy master ✌️ where's Queen 👑?")
        return
      if message.author.id == suzy:
        await message.channel.send(
          "hello! Queen👑 ,thanks for choosing my master " +
          random.choice(emoji))
        await message.channel.send("")
        return
      await message.channel.send(
        f"hii! {message.author.mention} i am {client.user.mention}")

    elif "taco" in msg and "love" in msg:

      await message.channel.send(
        " yea my master told me you love tacos Queen 👑 Even my  Master Would Love it 😊"
      )
    elif "beautiful" in msg and "wife" in msg:
      if message.author.id == user_id:
        await message.channel.send("because she is a goddess! ✨")
    elif "protein" in msg:
      await message.channel.send(
        message.author.mention +
        " i guess Protein bar isn't enough, why not go out with my master " +
        user1.mention + " and eat something else 😉")
    elif "gender" in msg and "bot" in msg:
      async with message.channel.typing():
        msg = msg.replace("?", "")
        msg = msg.replace(" ?", "")
        f = msg.split(' of ')[1]
        result = requests.get(f"https://api.genderize.io/?name={f}")
        res = eval(result.text)
        await message.channel.send(f"i guess {res['gender']}")
    elif "marry" in msg or "marriage" in msg or "future" in msg:
      if "will" in msg:
        await message.channel.send(
          "yess!💕 " + message.author.mention +
          "my master and Queen👑 are meant to be together! 💑")
        await message.channel.send("I can't wait for your marriage 🙏😉")

    elif "miss" in msg:
      if message.author.id == suzy:
        await message.channel.send(
          " i am sure my Master Misses you more Queen 👑!")
      if message.author.id == user_id:
        if "missed" in msg:

          await message.channel.send(
            "yess Queen 👑 my master missed you so much " +
            random.choice(emoji))

          return
        await message.channel.send("I know master i miss Queen👑 too ")

    elif ("finished" in msg or "completed" in msg
          or "studied" in msg) and ("homework" in msg or "assingment" in msg
                                    or "subject" in msg or "chapter" in msg):
      if suzy == message.author.id:
        await message.channel.send(
          "Good Going Queen 👑 me and my master are so proud of you! 👌")
    elif "homework" in msg:
      await message.channel.send(message.author.mention +
                                 " Please do your homework! 🙏")
      if message.author.id == suzy:
        await message.channel.send("i am so proud of you Queen 👑💕")

    elif msg == "roll":
      await message.channel.send(random.randint(1, 6))
    elif "suzy" in msg:
      if "love" in msg and ("master" in msg or "jayesh" in msg
                            or "him" in msg):
        await message.channel.send(
          "yess! me and my master already know that Queen👑, thanks again for choosing my master and loving him so much"
          + random.choice(emoji))
        return
      if "know" in msg:
        await message.channel.send(
          "yess she is my Queen 👑 and my master's wife❤️" +
          random.choice(emoji))

      if "more" in msg:
        await message.channel.send("No my Master " + user.mention +
                                   " loves you more ❤️🥰 ")
        return
      if "tell" in msg:
        await message.channel.send(
          "Yess Queen 👑 My master Loves you so much " + random.choice(emoji))
        return

      await message.channel.send("my Master " + user.mention +
                                 " loves suzy! 💕🤗 ")
    elif "where" in msg and ("master" in msg or "jayesh" in msg
                             or "husband" in msg):
      if message.author.id == suzy:
        await message.channel.send(
          "my master Must be Probably lost  💕in your Beautiful eyes  👀 ,Queen 👑!"
        )
    elif "thanks" in msg:
      if "bot" in msg:
        if suzy == message.author.id:
          await message.channel.send("Always welcome Queen 👑" +
                                     random.choice(emoji))
        elif user_id == message.author.id:
          await message.channel.send("Always Welcome Master 🙏")
        else:
          await message.channel.send(message.author.mention +
                                     " You are always Welcome!")
    elif "jayesh" in msg:
      if "love" in msg:
        await message.channel.send(message.author.mention +
                                   " my master loves you too Queen 👑 " +
                                   random.choice(emoji))
        return
      if "how" in msg:
        await message.channel.send(
          "he is so happy since the day he met you Queen 👑✨")
        return
      await message.channel.send(
        "the only thing i know about jayesh is he loves suzy 💕 so much! " +
        random.choice(emoji))
      if suzy == message.author.id:
        await message.channel.send(file=discord.File('nuk-kiss.gif'))

    elif "pickup" in msg:

      response = requests.get("https://api.jcwyt.com/pickup")
      pic = eval(response)
      await message.channel.send(pic + " " + random.choice(emoji))
      if user_id == message.author.id and "wife" in message.content:
        await message.channel.send(file=discord.File('wife.gif'))

    elif "really" in msg:
      if message.author.id == suzy:

        await message.channel.send(message.author.mention + " yess! 😊")
    elif "bye" in msg:

      if message.author.id == suzy:
        await message.channel.send("Bye! 👋 Queen👑 i will miss you " +
                                   random.choice(emoji))
        await message.channel.send(file=discord.File('bye.gif'))
        await message.channel.send("Please take care of yourself! 💕🐶")
        return

      await message.channel.send("Bye! 👋 " + message.author.mention +
                                 " i will miss you .")
    elif ("kiss" in msg and "master" not in msg) and ("jayesh" not in msg
                                                      and "husband" not in msg
                                                      and "baby" not in msg):
      if suzy == message.author.id:
        await message.channel.send(
          "I can't kiss you queen 👑 only my master can 💕")

    elif ("fun" in msg and "master" not in msg) and (
        "jayesh" not in msg and "husband" not in msg
        and "baby" not in msg) and ("funny" not in msg and "no" not in msg):

      if suzy == message.author.id:

        await message.channel.send(
          "my master would kill me if i ever think of that queen 👑 i just want you both to have fun 😉❤️"
        )

    elif ("choose" in msg and "master" not in msg) and (
        "jayesh" not in msg and "husband" not in msg and "baby" not in msg):

      if suzy == message.author.id:
        await message.channel.send(
          "Please always choose my master over me queen 👑,he loves you so much ❤️"
          + random.choice(emoji))
    elif "fine" in msg:
      if suzy == message.author.id and user_id != message.author.id:
        await message.channel.send("yes Queen👑 " + random.choice(emoji) +
                                   " have a great day✨")

    elif "joke" in msg and "bot" in msg:
      async with message.channel.typing():
        a = random.randint(0, 1)
        if a == 0:
          api_url = 'https://api.api-ninjas.com/v1/jokes?limit=1'
          response = requests.get(
            api_url,
            headers={'X-Api-Key': 'hmjcZC2UD3UmfKxJTUbhew==EHafALpx0mzba3vh'})
          jo = eval(response.text)
          await message.channel.send(jo[0]['joke'])
        else:
          response = requests.get(
            "https://official-joke-api.appspot.com/random_joke")
          joke = eval(response.text)
          await message.channel.send(joke['setup'])
          time.sleep(2)
          await message.channel.send(joke['punchline'])
    elif "advice" in msg and "bot" in msg:
      result = requests.get("https://api.adviceslip.com/advice")
      res = eval(result.text)
      await message.channel.send(res['slip']['advice'])
    elif "quiz" in msg and "bot" in msg:
      async with message.channel.typing():
        result = requests.get(
          "https://opentdb.com/api.php?amount=1&type=multiple")
        res1 = result.text

        res = eval(
          res1.replace("&quot;", "'").replace("&amp;", "&").replace(
            "&lt;", "<").replace("&gt;", ">").replace("&#039;", "'"))
        a = res['results'][0]['incorrect_answers']
        b = res['results'][0]['correct_answer']
        print(b)
        c = random.randint(0, 3)
        a.insert(c, b)
        d = 1
        op = ""
        for i in a:
          op += f"{d} : {i}\n"
          d += 1
        c = int(c + 1)
        ques = (res['results'][0]['question']).encode('utf-8').decode()
        await message.channel.send(ques)
        await message.channel.send(f"and the options are :\n{op}")
        await message.channel.send("you have 15 seconds to think 🤔")
      try:
        guess = await self.wait_for('message', timeout=15.0)
      except asyncio.TimeoutError:
        return await message.channel.send(
          f'Sorry, you took too long the correct answer  was👉 {b} ')
      try:
        if int(guess.content) == c:

          await message.channel.send(guess.author.mention +
                                     ' You are right! 🙌')
          if db['points'] == True:
            if "jayesh" in str(guess.author):
              await message.channel.send("Master got one Point ✨")
              db['jay'] += 1
              if db['jay'] == 5:
                await message.channel.send("congratulations Master you Won!✨🙌")
            if "suzy" in str(guess.author):
              await message.channel.send("Queen got one Point ✨")

              db['suzy'] += 1
              if db['suzy'] == 5:
                await message.channel.send("congratulations Queen you Won!✨🙌")
        else:
          await message.channel.send(guess.author.mention +
                                     f' Oops. It is actually :  {b}.')
      except:
        await message.channel.send(
          guess.author.mention +
          f' Oops.you just have to enter number It is actually :  {b}.')

    elif "thought" in msg and "bot" in msg:
      async with message.channel.typing():
        url = "https://stapi-showerthoughts.p.rapidapi.com/api/v1/stapi/randomnew"

        headers = {
          "X-RapidAPI-Key":
          "4e8b5cdfeamsh3dfcb499f973702p10c20ejsn069568518310",
          "X-RapidAPI-Host": "stapi-showerthoughts.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        shower = eval(response.text)
        await message.channel.send(shower['showerthought'])

    elif "fact" in msg and "bot" in msg:
      async with message.channel.typing():
        api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'
        response = requests.get(
          api_url,
          headers={'X-Api-Key': 'hmjcZC2UD3UmfKxJTUbhew==EHafALpx0mzba3vh'})
        fact = eval(response.text)
        await message.channel.send(fact[0]['fact'])
    elif "riddle" in msg and "bot" in msg:
      async with message.channel.typing():
        response = requests.get('https://riddles-api.vercel.app/random')
        riddle = eval(response.text)

        await message.channel.send(riddle['riddle'])
        await message.channel.send("20 seconds to think..🤔")

      try:
        guess = await self.wait_for('message', timeout=20.0)
      except asyncio.TimeoutError:
        return await message.channel.send(
          f'Sorry, you took too long the correct answer  was👉 ' +
          riddle["answer"])

      if guess.content == riddle['answer']:
        await message.channel.send(guess.author.mention + ' You are right! 🙌')
      else:
        await message.channel.send(
          f'Oops. It is actually :  {riddle["answer"]}.')

    elif ("quote" in msg or "motivat" in msg) and "bot" in msg:
      async with message.channel.typing():
        response = requests.get('https://zenquotes.io/api/quotes')
        res = eval(response.text)
        await message.channel.send(res[0]["q"])
    elif ("activity" in msg or "bored" in msg) and "bot" in msg:
      async with message.channel.typing():
        lis = [
          "education", "recreational", "social", "diy", "cooking",
          "relaxation", "music", "busywork"
        ]
        await message.channel.send("thinking of a activity for you...🤔")
        cat = random.choice(lis)
        response = requests.get(
          f'https://www.boredapi.com/api/activity?type={cat}')
        ac = eval(response.text)
        await message.channel.send(ac['activity'])
        if ac['link']:
          await message.channel.send(" here is a link for your help : \n" +
                                     ac['link'])
    else:

      print(message.content)

  keep()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(
  'MTA5NzYwNDE3NTQ1MTM5ODIyNQ.Gvmxzz.jpE-y-jflaKbRHLgJTlfFBHbxJCfTyVCTD8sRQ')
from replit import db
from replit import db
