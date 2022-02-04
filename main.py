import discord
import json
import os
import random
from webserver import keep_alive
from discord.ext import commands

#TODO

#429 too many requests error
#kill 1 in shell


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
#This is for !fgb adding it to the json when bot posts

    if message.channel.name == 'bike-archive':
        if message.content.lower().startswith('https'):

            await update_builds(message.content)

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


    #OktoberChallenges

        #----------------------------------------------#
            #Speed challenge
    if message.channel.name == '🏆challenges':

        if message.content.lower().startswith('!octoberspeed'):

            await okt21speed(users, message.author, message)

                

            #Fish and Chips
    if message.channel.name == '🏆challenges':

        if message.content.lower().startswith('!fishandchips'):

            await okt21trick(users, message.author, message)

                
        #--------------------------------------------#


    #November challenges

        #----------------------------------------------#
            #Pasta Picture
    if message.channel.name == '🏆challenges':

        if message.content.lower().startswith('!pastapaperazzi'):

            await nov21picture(users, message.author, message)

                

            #Commute Swichteroo
    if message.channel.name == '🏆challenges':

        if message.content.lower().startswith('!commuteswap'):

            await nov21commuteswap(users, message.author, message)

                
        #--------------------------------------------#

    
    #December challenges

            #----------------------------------------------#
                #Pasta Picture
        if message.channel.name == '🏆challenges':

            if message.content.lower().startswith('!luckyclimber'):

                await dec21climber(users, message.author, message)

                    

                #Commute Swichteroo
        if message.channel.name == '🏆challenges':

            if message.content.lower().startswith('!bigpinehunter'):

                await dec21treepic(users, message.author, message)

                    
            #--------------------------------------------#

    #January22 challenges

            #----------------------------------------------#
                #Speed Century
        if message.channel.name == '🏆challenges':

            if message.content.lower().startswith('!speedycentury'):

                await jan22century(users, message.author, message)

                    

                #No bars mo problems
        if message.channel.name == '🏆challenges':

            if message.content.lower().startswith('!nobarsmoproblems'):

                await jan22nobars(users, message.author, message)

                    
            #--------------------------------------------#

    #Febuary22 challenges

            #----------------------------------------------#
                #Long Skid
        if message.channel.name == '🏆challenges':

            if message.content.lower().startswith('!longskid'):

                await feb22skid(users, message.author, message)

                    

                #Sky High Snap
        if message.channel.name == '🏆challenges':

            if message.content.lower().startswith('!skyhighsnap'):

                await feb22snap(users, message.author, message)

                    
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
        'Signs point to yes',
        'If it feels right',
        'No.',
        'Better not',
        'For suure!',
        '100%, unless...',
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


#Oktober Challenges

#-----------------------------------------------#

#Speed Challenge

async def okt21speed(users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['oktober21speed'] = 0


    username = str(message.author.mention).split('#')[0]
    isokt21speedcomplete = int(users[str(message.author.id)]['oktober21speed'])
    wheelieokt21role = discord.utils.get(message.author.guild.roles, name = "October: Fastest on the Block")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "October: Fastest on the Block" in [y.name for y in message.author.roles]:
        await message.channel.send(f'No doubles')
        await oktober21speedchallenge (users, message.author)

    elif not isokt21speedcomplete == 1:

        await oktober21speedchallenge (users, message.author)

        await message.author.add_roles(wheelieokt21role)

        await message.channel.send(f'Congratulations {username} you have completed the Oktober speeeeed Challenge! Here is the role you have earned!')

        await message.channel.send('https://cdn.discordapp.com/attachments/868194193221251082/894861647833882634/inconnu.gif')



        

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)


#Fish and Chips Challenge

async def okt21trick (users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['oktober21trick'] = 0

    username = str(message.author.mention).split('#')[0]
    isokt21trickcomplete = int(users[str(message.author.id)]['oktober21trick'])
    okt21trickrole = discord.utils.get(message.author.guild.roles, name = "October: Crispy Trickster")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "October: Crispy Trickster" in [y.name for y in message.author.roles]:
        await message.channel.send(f'I see those fish and chips are getting better but only one role')
        await oktober21trickchallenge (users, message.author)

    elif not isokt21trickcomplete == 1:

        await oktober21trickchallenge (users, message.author)

        await message.author.add_roles(okt21trickrole)

        await message.channel.send(f'Congraulations {username} you have completed the fish and chips challenge! Here is the role you have earned!')

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#-----------------------------------------------#


#November Challenges

#-----------------------------------------------#

#Pasta Picture

async def nov21picture(users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['november21pastapic'] = 0


    username = str(message.author.mention).split('#')[0]
    isnov21picturecomplete = int(users[str(message.author.id)]['november21pastapic'])
    pastapicnov21role = discord.utils.get(message.author.guild.roles, name = "November: Pasta Paperazzi")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "November: Pasta Paperazzi" in [y.name for y in message.author.roles]:
        await message.channel.send(f'Second Pasta is cooking... please hold')
        await november21pastachallenge (users, message.author)

    elif not isnov21picturecomplete == 1:

        await november21pastachallenge (users, message.author)

        await message.author.add_roles(pastapicnov21role)

        await message.channel.send(f'Congratulations {username} you are a Pasta Paperazzi. Lets hope no police shows up after that heist')

        await message.channel.send('https://acegif.com/wp-content/gifs/spaghetti-65.gif')



        

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)


#Commute Handlebar Swap

async def nov21commuteswap (users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['nov21commuteswap'] = 0

    username = str(message.author.mention).split('#')[0]
    isnov21swapcomplete = int(users[str(message.author.id)]['nov21commuteswap'])
    nov21swaprole = discord.utils.get(message.author.guild.roles, name = "November: Switcharoo Master")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "November: Switcharoo Master" in [y.name for y in message.author.roles]:
        await message.channel.send(f'Maybe try swapping while riding for another role')
        await november21swapchallenge (users, message.author)

    elif not isnov21swapcomplete == 1:

        await november21swapchallenge (users, message.author)

        await message.author.add_roles(nov21swaprole)

        await message.channel.send(f'Congraulations {username} you have completed a pretty whacky Challenge! Here is the role you have earned')

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#-----------------------------------------------#

#December Challenges

#-----------------------------------------------#

#Lucky Climber

async def dec21climber(users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['december21climb'] = 0


    username = str(message.author.mention).split('#')[0]
    isdec21climbcomplete = int(users[str(message.author.id)]['december21climb'])
    dec21climbrole = discord.utils.get(message.author.guild.roles, name = "December: Lucky Climber")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "December: Lucky Climber" in [y.name for y in message.author.roles]:
        await message.channel.send(f'Im afraid the jackpot can only be won once')
        await december21climbchallenge (users, message.author)

    elif not isdec21climbcomplete == 1:

        await december21climbchallenge (users, message.author)

        await message.author.add_roles(dec21climbrole)

        await message.channel.send(f'Congratulations {username} you have got some good luck coming your way this month')

        #await message.channel.send('https://acegif.com/wp-content/gifs/spaghetti-65.gif')



        

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)


#big pine hunter

async def dec21treepic (users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['dec21treepic'] = 0

    username = str(message.author.mention).split('#')[0]
    isdec21treepiccomplete = int(users[str(message.author.id)]['dec21treepic'])
    dec21treepicrole = discord.utils.get(message.author.guild.roles, name = "December: Big Pine Hunter")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "December: Big Pine Hunter" in [y.name for y in message.author.roles]:
        await message.channel.send(f'If you post another pic maybe you get something special')
        await december21treepicchallenge (users, message.author)

    elif not isdec21treepiccomplete == 1:

        await december21treepicchallenge (users, message.author)

        await message.author.add_roles(dec21treepicrole)

        await message.channel.send(f'Congraulations {username} that was a sick picture! Im a bot but I definetely feel the christmas spirit!')

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#-----------------------------------------------#


#January22 Challenges

#-----------------------------------------------#

#Speed Century

async def jan22century(users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['jan22century'] = 0


    username = str(message.author.mention).split('#')[0]
    #isjan22centurycomplete = int(users[str(message.author.id)]['jan22century'])
    jan22centuryrole = discord.utils.get(message.author.guild.roles, name = "January: New Year, New Century")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "January: New Year, New Century" in [y.name for y in message.author.roles]:
        await message.channel.send(f'Too fast for two challenges')
        await jan22centurychelperfunction (users, message.author)

    else:

        #await jan22centurychelperfunction (users, message.author)

        await message.author.add_roles(jan22centuryrole)

        await message.channel.send(f'Good one {username}! That is some serious speed and endurance you got.')

        #await message.channel.send('https://acegif.com/wp-content/gifs/spaghetti-65.gif')



        

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)


#No bars more problems

async def jan22nobars (users, user, message):

    await update_data(users, message.author)

    users[str(message.author.id)]['jann22nobars'] = 0

    username = str(message.author.mention).split('#')[0]
    isjan22nobarscomplete = int(users[str(message.author.id)]['jann22nobars'])
    jan22nobarsrole = discord.utils.get(message.author.guild.roles, name = "January: No Bars Mo' Problems")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")
    #messagesplit = message.content.split(" ",8)[1:]

    if "January: No Bars Mo' Problems" in [y.name for y in message.author.roles]:
        await message.channel.send(f'Maybe it is time to put some bars back onto your bike')
        await jan22barshelperfunction (users, message.author)

    elif not isjan22nobarscomplete == 1:

        await jan22barshelperfunction (users, message.author)

        await message.author.add_roles(jan22nobarsrole)

        await message.channel.send(f'Well done {username}! I doubt alot of people have done that before so welcome to the no bars club')

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#-----------------------------------------------#

#Febuary22 Challenges

#-----------------------------------------------#

#long skid

async def feb22skid(users, user, message):

    username = str(message.author.mention).split('#')[0]
    feb22skidrole = discord.utils.get(message.author.guild.roles, name = "February: Skid Connoisseur")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")


    if "February: Skid Connoisseur" in [y.name for y in message.author.roles]:
        await message.channel.send(f'If you can skid even farther, maybe I will give you another reward')

    else:

        await message.author.add_roles(feb22skidrole)

        await message.channel.send(f'That was a sick Skid {username}! I hope you still have some tire left :o')


        

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)


#sky high snap

async def feb22snap (users, user, message):

    username = str(message.author.mention).split('#')[0]
    feb22snaprole = discord.utils.get(message.author.guild.roles, name = "February: Sky High Snap")
    challengerrole = discord.utils.get(message.author.guild.roles, name = "Challenger")

    if "February: Sky High Snap" in [y.name for y in message.author.roles]:
        await message.channel.send(f'The more pictures the merrier but I can sadly only give you one reward')
    

    else:

        await message.author.add_roles(feb22snaprole)

        await message.channel.send(f'Sweet Picture {username}! Here is your reward to commemorate your achievement')

    #This is for the Challenger role incase they don't have it
    if "Challenger" in [y.name for y in message.author.roles]:
        return
    elif "Challenger" not in [y.name for y in message.author.roles]:
        await message.author.add_roles(challengerrole)

#-----------------------------------------------#


##!fgb json helper function
#-----------------------------------

async def update_builds(message):

    with open('builds.json', 'r') as g:
        builds = json.load(g)
    
 
    jsoncountlist = list(builds.keys())

    getjsoncount = jsoncountlist[-1]

    setjsoncount = int(getjsoncount)

    setjsoncount +=1

   
    if ':' in message:

        builds[str(setjsoncount)] = message
        print('json reached')

    with open('builds.json', 'w') as g:
        json.dump(builds, g)
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

#Oktober21 Challenges
#-----------------------------------------#
async def oktober21speedchallenge(users, user):
    users[str(user.id)]['oktober21speed'] = 1

async def oktober21trickchallenge(users, user):
    users[str(user.id)]['oktober21trick'] = 1

#-----------------------------------------#

#November 21 Challenges
#-----------------------------------------#
async def november21pastachallenge(users, user):
    users[str(user.id)]['november21pastapic'] = 1

async def november21swapchallenge(users, user):
    users[str(user.id)]['nov21commuteswap'] = 1

#-----------------------------------------#

#December 21 Challenges
#-----------------------------------------#
async def december21climbchallenge(users, user):
    users[str(user.id)]['december21climb'] = 1

async def december21treepicchallenge(users, user):
    users[str(user.id)]['dec21treepic'] = 1

#-----------------------------------------#

#Jan 22 Challenges helper functions
#-----------------------------------------#
async def jan22centurychelperfunction(users, user):
    users[str(user.id)]['jan22century'] = 1

async def jan22barshelperfunction(users, user):
    users[str(user.id)]['jann22nobars'] = 1

#-----------------------------------------#


#list challenges

@client.command()
async def challenges(ctx):

    preventchannel = '🏆challenges'

    

    if ctx.channel.name != preventchannel:
        await ctx.send(f'Please only use this in the #🏆challenges channel')
        return

    challengeschannel = ctx.channel.name

    monthlytitle = "Febuary Challenges"

    challenge1name = 'Skid Connoisseur'
    challenge1 = (f'> Record yourself doing your longest skid possible! \n \n \n Use: ***!longskid*** in the `#{challengeschannel}` Channel to receive your reward!')

    challenge2name = 'Sky High Snap'
    challenge2 = (f'> Post a picture from a high point with a nice view such as the landscape or skyline. This can also be done inside an elevator or ontop / inside of a building \n \n \n Use : ***!nobarsmoproblems*** in the `#{challengeschannel}` Channel to receive your reward!')




    channel = ctx.message.channel
    embed = discord.Embed(
        title = f'{monthlytitle}',
        #description = 'These are the challenges of the month \n',
        color = discord.Color.blue()
    )


    embed.add_field(name=f'\u200b', value=f'\u200b', inline = False)
    embed.add_field(name=challenge1name, value = challenge1, inline = True)
    embed.add_field(name=challenge2name, value=challenge2, inline = True)
    embed.add_field(name=f'\u200b', value=f'\u200b', inline = False)

    embed.add_field(name=f'Leaderboard', value="also take a look at the leaderboard with ***!leaderboard***")
    #embed.add_field(name=f'\u200b', value=f'> Pro tip: use ***!aug21trackstand*** and ***!aug21ride*** to claim your rewards for the August challenges!', inline = False)


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


    #clears leaderboard first


    with open('leaderboard.json', 'r') as z:
        users = json.load(z)

        users = {}
    
    with open('leaderboard.json', 'w') as z:
        json.dump(users, z)


    

    with open('leaderboard.json', 'r') as z:
        users = json.load(z)


    #This regenerates the json every time
    #It's only called users but actually users the leaderboard.json

    for member in ctx.guild.members:

        users[str(member.id)] = {}
        users[str(member.id)]['username'] = member.display_name
        users[str(member.id)]['userid'] = member.id
        users[str(member.id)]['onlyonemessage'] = 0

        for role in member.roles:
            if role.name == "September: Wheelie Warrior":
                users[str(member.id)]["September: Wheelie Warrior"] = 1
            if role.name == "September: Endurance Expert":
                users[str(member.id)]["September: Endurance Expert"] = 1
            if role.name == "August: Track Stand Pro":
                users[str(member.id)]["August: Track Stand Pro"] = 1
            if role.name == "August: Steady Rider":
                users[str(member.id)]["August: Steady Rider"] = 1
            if role.name == "October: Crispy Trickster":
                users[str(member.id)]["October: Crispy Trickster"] = 1
            if role.name == "October: Fastest on the Block":
                users[str(member.id)]["October: Fastest on the Block"] = 1
            if role.name == "November: Pasta Paperazzi":
                users[str(member.id)]["November: Pasta Paperazzi"] = 1
            if role.name == "November: Switcharoo Master":
                users[str(member.id)]["November: Switcharoo Master"] = 1
            if role.name == "December: Lucky Climber":
                users[str(member.id)]["December: Lucky Climber"] = 1
            if role.name == "December: Big Pine Hunter":
                users[str(member.id)]["December: Big Pine Hunter"] = 1
            if role.name == "January: New Year, New Century":
                users[str(member.id)]["January: New Year, New Century"] = 1
            if role.name == "January: No Bars Mo' Problems":
                users[str(member.id)]["January: No Bars Mo' Problems"] = 1
            if role.name == "February: Skid Connoisseur":
                users[str(member.id)]["February: Skid Connoisseur"] = 1
            if role.name == "February: Sky High Snap":
                users[str(member.id)]["February: Sky High Snap"] = 1







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

        if len(value) > 3:

            #Sneaky trick to get the username without converting ID
            listofchallengers.append(users[key]["username"])


    #This generates the amount of challenges they have completed
    listofdonechallenges = []
    for key,value in users.items():

        if len(value) > 3:

            listofdonechallenges.append(len(value)-3)


    # This is to merge the lists and then convert them to a list

    zipleaderboardlist = zip(listofchallengers,listofdonechallenges)
    leaderboardlist = list(zipleaderboardlist)

    #Sorts the leaderboard by 2nd tuple aka listofdonechallenges (which is the amount) from large to small

    sortedleaderboard = sorted(leaderboardlist, key=lambda tup: tup[1], reverse = True)

    print(sortedleaderboard)

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

    with open('leaderboard.json', 'w') as z:
        json.dump(users, z)

@client.command()
async def fgb(ctx):

    with open('builds.json', 'r') as g:
        builds = json.load(g)

    getrandomimage = random.randint(1,len(builds))

    randomimage = builds[str(getrandomimage)]

    await ctx.channel.send(f'{randomimage}')

    

    with open('builds.json', 'w') as g:
        json.dump(builds, g)


keep_alive()
client.run(my_secret)