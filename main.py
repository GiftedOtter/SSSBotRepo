import discord
import json
import os
import random
from webserver import keep_alive
from discord.ext import commands

#TODO


intents = discord.Intents.default()
intents.members = True
my_secret = os.environ['TOKEN']

client = commands.Bot(command_prefix = '!', intents=intents)
#os.chdir(r'C:\Users\Pepeg\Desktop\RGB\SlowSpinSociety\BOT\Attempt_2')



@client.event
async def on_ready():
    print('We online lets get it')

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    #await update_data(users, member)



    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)    

# ---------------------------
#Fun commands go here

    if message.content.lower().startswith('.testimages'):
        finallist = []
        
        async for msg in message.channel.history(limit=None):

            testattach = msg.content

            if not 'https' in testattach:
                pass
            else:
                finallist.append(testattach)

                print(testattach)
                
        print(finallist)
        print("done")

#8Ball:


    if message.content.lower().startswith('!8ball'):
        await eightball(users, message.author, message)

    #variables for the status message - useful for kmadd function
    #kmstoadd = 0
    #total = 100

    #functions for the update stuff
    if message.author.bot:
                return
    

    #this is the !add command with progress message and adding to json 
    #if message.channel.name == 'botstuff':
        #if message.content.lower().startswith('!add'):
            #messagesplit = message.content.split(" ",4)[1:]

            #kmstoadd = float(messagesplit[0])


            #users[str(user.id)]['kilometers'] = 0
            

            #await add_kilometers(users, message.author, kmstoadd)

            #progress = float(users[str(message.author.id)]['kilometers'])

            #await message.channel.send(f'Your kilometers have been added! Your progress is now {progress}/{total}')

    #list the challenges
    #This is now a command

    #if message.channel.name == 'botstuff':
        #if message.content.lower().startswith('!challenges'):

            #await message.channel.send(f'Challenges for this month are \n 1: Do a nohanded wheelie for 5s \n 2: Complete a 200km ride ')

    #AugustChallenges

    #AugustChallenges

    #----------------------------------------------#

        #trackstand challenge
    if message.channel.name == '🏆challenges':
    
        if message.content.lower().startswith('!aug21trackstand'):

            await aug21trackstand(users, message.author, message)
    
        #400km ride Challenge
    if message.channel.name == '🏆challenges':

        if message.content.lower().startswith('!aug21ride'):

            await aug21ride(users, message.author, message)

    #--------------------------------------------#

    #SeptemberChallenges

    #----------------------------------------------#
        #Wheelie challenge
    if message.channel.name == '🏆challenges':

        if message.content.lower().startswith('!wheelie'):

            await sep21wheelie(users, message.author, message)

            

        #200km ride Challenge
    if message.channel.name == '🏆challenges':

        if message.content.lower().startswith('!200ride'):

            await sep21200ride(users, message.author, message)

            
    #--------------------------------------------#

    

    #leaderboard - This now works as an embed

    #if message.channel.name == 'botstuff':
        #if message.content.lower().startswith('!leaderboard'):
            
            
            #listofchallengers = []
            #for key, value in users.items():
                #listofchallengers.append(users[key]["username"])

            #This generates the amount of challenges they have completed

            #listofdonechallenges = []
            #for key,value in users.items():

                #listofdonechallenges.append(len(value)-3)

            
            #zipleaderboardlist = zip(listofchallengers,listofdonechallenges)
            #leaderboardlist = list(zipleaderboardlist)

            #sortedleaderboard = sorted(leaderboardlist, key=lambda tup: tup[1], reverse = True)

            #await message.channel.send(f'{sortedleaderboard}')

            

            #for index, tuple in enumerate(leaderboardlist):
                #name = tuple[0]
                #challenges = tuple[1]
                #await message.channel.send(f'{name} has {challenges} challenges complete')
                
    

    #variables for the goal message - This is for km add

    #reachedgoal = float(users[str(message.author.id)]['kilometers'])
    #username = str(message.author.mention).split('#')[0]
    #singlemessage = int(users[str(message.author.id)]['onlyonemessage'])

    #goal message
    #if reachedgoal + kmstoadd >= total:
        #await onlyonemessageplease(users, message.author, 1)
        
        #if singlemessage <= 0:
            
            #This adds the role

            #kmrole = discord.utils.get(message.author.guild.roles, name = "KilometerBoy")
            #await message.author.add_roles(kmrole)

            #await message.channel.send(f'Congrats {username} you have reached the monthly ride goal! Here is the role you have earned!')
        
        

    #This is really important for commands to work such as the embed
    await client.process_commands(message)
    


    with open('users.json', 'w') as f:
        json.dump(users, f)


#Fun Commands
#8ball:
#-------------------------------------------------

async def eightball(users, user, message):

    answerlist = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes, definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs pint to yes',
        'Replay hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'very doubtful',
        'CDTrack says yes']

    randomanswer = random.randint(0,len(answerlist)-1)

    await message.channel.send(f' ***8Ball says:*** `{answerlist[randomanswer]}`')

#August Challenges

#-----------------------------------------------#

#Trackstandchallenge

async def aug21trackstand(users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['aug21trackstand'] = 0

    username = str(message.author.mention).split('#')[0]
    isaug21trackstandcomplete = int(users[str(message.author.id)]['aug21trackstand'])
    aug21trackstandrole = discord.utils.get(message.author.guild.roles, name = "August: Track Stand Pro")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "August: Track Stand Pro" in [y.name for y in message.author.roles]:
        await message.channel.send(f'You can travel back in time and do it again? Insane but still only one role')
        await aug21trackstandchallenge (users, message.author)

    elif not isaug21trackstandcomplete == 1:

        await aug21trackstandchallenge (users, message.author)

        await message.author.add_roles(aug21trackstandrole)

        await message.channel.send(f'Congratulations {username} you have completed the August trackstand Challenge! Here is the role you have earned!')


        #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#RideChallenge

async def aug21ride(users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['aug21ride'] = 0

    username = str(message.author.mention).split('#')[0]
    isaug21ride = int(users[str(message.author.id)]['aug21ride'])
    aug21riderole = discord.utils.get(message.author.guild.roles, name = "August: Steady Rider")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "August: Steady Rider" in [y.name for y in message.author.roles]:
        await message.channel.send(f'Only. One. Role.')
        await aug21ridechallenge (users, message.author)

    elif not isaug21ride == 1:

        await aug21ridechallenge (users, message.author)

        await message.author.add_roles(aug21riderole)

        await message.channel.send(f'Congratulations {username} you have completed the August ride Challenge! Here is the role you have earned!')

        #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#-----------------------------------------------#

#September Challenges

#-----------------------------------------------#

#Wheelie Challenge

async def sep21wheelie(users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['september21wheelie'] = 0


    username = str(message.author.mention).split('#')[0]
    issep21wheeliecomplete = int(users[str(message.author.id)]['september21wheelie'])
    wheeliesep21role = discord.utils.get(message.author.guild.roles, name = "September: Wheelie Warrior")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "September: Wheelie Warrior" in [y.name for y in message.author.roles]:
        await message.channel.send(f'I mean good that you did it again but you only get one role')
        await september21wheeliechallenge (users, message.author)

    elif not issep21wheeliecomplete == 1:

        await september21wheeliechallenge (users, message.author)

        await message.author.add_roles(wheeliesep21role)

        await message.channel.send(f'Congratulations {username} you have completed the September wheelie Challenge! Here is the role you have earned!')

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)


    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#200Ride Challenge

async def sep21200ride (users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['september21ride200km'] = 0

    username = str(message.author.mention).split('#')[0]
    issep21ridecomplete = int(users[str(message.author.id)]['september21ride200km'])
    ridesep21role = discord.utils.get(message.author.guild.roles, name = "September: Endurance Expert")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "September: Endurance Expert" in [y.name for y in message.author.roles]:
        await message.channel.send(f'I mean good that you did it again, 2 200km rides a month maybe go pro? But you only get one role')
        await september21ridechallenge (users, message.author)

    elif not issep21ridecomplete == 1:

        await september21ridechallenge (users, message.author)

        await message.author.add_roles(ridesep21role)

        await message.channel.send(f'Congraulations {username} you have completed the 200km ride! Absolutely mental :o Here is the role you have earned!')

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#-----------------------------------------------#

#Helper function to add the kms to the json

async def add_kilometers(users, user, kilometers):
    users[str(user.id)]['kilometers'] += kilometers

#Helperfunction to prevent bot message spam

async def onlyonemessageplease(users, user, onlyone):
    users[str(user.id)]['onlyonemessage'] += onlyone

#helper function to create the json with data

async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]['username'] = user.display_name
        users[str(user.id)]['userid'] = user.id
        users[str(user.id)]['onlyonemessage'] = 0

#August21 Challenges
#-------------------------------------------#
async def aug21trackstandchallenge(users, user):
    users[str(user.id)]['aug21trackstand'] = 1

async def aug21ridechallenge(users, user):
    users[str(user.id)]['aug21ride'] = 1
#---------------------------------------------#



#September21 Challenges
#-----------------------------------------#
async def september21wheeliechallenge(users, user):
    users[str(user.id)]['september21wheelie'] = 1

async def september21ridechallenge(users, user):
    users[str(user.id)]['september21ride200km'] = 1

#-----------------------------------------#


#list challenges

@client.command()
async def challenges(ctx):

    preventchannel = '🏆challenges'

    

    if ctx.channel.name != preventchannel:
        await ctx.send(f'Please only use this in the #🏆challenges channel')
        return

    challengeschannel = ctx.channel.name
    
    monthlytitle = "September Challenges"

    channel = ctx.message.channel
    embed = discord.Embed(
        title = f'{monthlytitle}',
        #description = 'These are the challenges of the month \n',
        color = discord.Color.blue()
    )


    embed.add_field(name=f'\u200b', value=f'\u200b', inline = False)
    embed.add_field(name="Wheelie Challenge", value = (f'> Do a nohanded wheelie for a minimum of 5 seconds - Good Luck!\n \n \n Use: ***!wheelie*** in the `#{challengeschannel}` Channel to receive your reward!' ), inline = True)
    embed.add_field(name="Ride Challenge", value=(f'> Complete a 200km ride - also known as a double century \n \n \n Use : ***!200ride*** in the `#{challengeschannel}` Channel to receive your reward!'), inline = True)
    embed.add_field(name=f'\u200b', value=f'\u200b', inline = False)
    embed.add_field(name=f'\u200b', value=f'> Pro tip: use ***!aug21trackstand*** and ***!aug21ride*** to claim your rewards for the August challenges!', inline = False)


    embed.set_footer(text='Go complete the challenges!')
    #embed.set_image(url='https://i.imgur.com/vYUb8zi.jpeg')
    embed.set_thumbnail(url='https://i.postimg.cc/656CzmFf/FW-Sticker-14-copy.png')
    #embed.set_author(name='BotHasTitlesIfYouHaveChallenges', icon_url='https://i.postimg.cc/656CzmFf/FW-Sticker-14-copy.png')

    await ctx.send(embed=embed)

#Leaderboard

@client.command()
async def leaderboard(ctx):

    preventchannel = '🏆challenges'

    if ctx.channel.name != preventchannel:
        await ctx.send(f'Please only use this in the #🏆challenges channel')
        return

    with open('users.json', 'r') as f:
        users = json.load(f)

    #This was just for testing still interesting though
    #member_count = 0

    #for member in ctx.guild.members:
        #member_count += 1
    
    #print(member_count)

    
    # For loops attempt with useful things

    #for key, values in users.items():
        #keyconverter = int(key)

        #print(users[key]["username"])

        #print('Salary:', users.get(key, {}.get("username","nothinghere")))

    #for key, value in users.items():
        
        #keyconverter = int(key)
        #await client.fetch_user(keyconverter)

        #userobject = ctx.guild.get_member(keyconverter)
        #print(type(userobject))


        #challengers = len(users)

        #challenges_list.extend((len(value)-3, userobject))

        #print(challenges_list)



    #This generates the list of ids of people doing challenges
    listofchallengers = []
    for key, value in users.items():

            #Sneaky trick to get the username without converting ID
            listofchallengers.append(users[key]["username"])


    #This generates the amount of challenges they have completed
    listofdonechallenges = []
    for key,value in users.items():

        listofdonechallenges.append(len(value)-3)


    # This is to merge the lists and then convert them to a list

    zipleaderboardlist = zip(listofchallengers,listofdonechallenges)
    leaderboardlist = list(zipleaderboardlist)

    #Sorts the leaderboard by 2nd tuple aka listofdonechallenges (which is the amount) from large to small

    sortedleaderboard = sorted(leaderboardlist, key=lambda tup: tup[1], reverse = True)

    #Leaderboardembed

    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'SSS Challenges Leaderboard',
        description = 'All Legends are listed here',
        color = discord.Color.purple()
    )

    
    embed.add_field(name = f'\u200b', value=f'__**Rank**__', inline = True)
    embed.add_field(name = f'\u200b', value=f'__**Name**__', inline = True)
    embed.add_field(name = f'\u200b', value=f'__**Challenges Completed**__', inline = True)
    rank = 0
    for index, tuple in enumerate(sortedleaderboard):
            usernames = tuple[0]
            completedchallenges = tuple[1]

            rank += 1

            fields = [  
            (f'\u200b', f' `{rank}`', True),
            (f'\u200b',f'{usernames}', True),
            (f'\u200b', f'**{completedchallenges}**', True)
            ]
            
            for name, value, inline in fields:
                embed.add_field(name=name, value = value, inline = inline)


    #for name, value, inline in fields:
        #embed.add_field(name=name, value = value, inline = inline)


    embed.set_footer(text='Go get that Rank 1!')
    #embed.set_image(url='https://i.imgur.com/vYUb8zi.jpeg')
    embed.set_thumbnail(url='https://i.postimg.cc/s2k3gxkD/stickers-winners-podium-jpg-2.jpg')
    #embed.set_author(name='BotHasTitlesIfYouHaveChallenges', icon_url='https://i.postimg.cc/656CzmFf/FW-Sticker-14-copy.png')

    #the value should be a sorted list

    userids = []
    for A_tuple in leaderboardlist:

        userids.append(A_tuple[0])

    challengesdone = []
    for B_tuple in leaderboardlist:

        challengesdone.append(B_tuple[1])

    await ctx.send(embed=embed)

    with open('users.json', 'w') as f:
        json.dump(users, f)


keep_alive()
client.run(my_secret)