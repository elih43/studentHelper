import os
import discord
import asyncio
from dotenv import load_dotenv


path='/Users/dogsa/Desktop/ttr/token.env'
load_dotenv(dotenv_path=path,verbose=True)



TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
server = discord.Server

def getSpecificRole(gender, grade):
    if gender == 'male':
        if grade == '6':
            return '6th Grade Boys'
        if grade == '7':
            return '7th Grade Boys'
        if grade == '8':
            return '8th Grade Boys'
        if grade == '9':
            return '9th Grade Boys'
        if grade == '10':
            return '10th Grade Boys'
        if grade == '11':
            return '11th Grade Boys'
        if grade == '12':
            return '12th Grade Boys'
    else:
        if grade == '6':
            return '6th Grade Girls'
        if grade == '7':
            return '7th Grade Girls'
        if grade == '8':
            return '8th Grade Girls'
        if grade == '9':
            return '9th Grade Girls'
        if grade == '10':
            return '10th Grade Girls'
        if grade == '11':
            return '11th Grade Girls'
        if grade == '12':
            return '12th Grade Girls'

@client.event
async def assignStudent(member, nick, gender, grade):
    #change users nickname to real name
    await client.change_nickname(member, nick)

    roleName = getSpecificRole(gender, grade)
    role = discord.utils.get(member.server.roles, name= roleName)
    await client.add_roles(member, role)
        
    


@client.event  # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user.name}")
    
    
    
    



@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
 
    if "close" == message.content.lower():
        await client.send_typing(message.channel)
        await client.send_message(message.channel, 'closing')
        await client.close()
   
    elif "change status" == message.content.lower():
        await client.change_presence(game=discord.Game(name='test'))
        
    #student setup command
    elif "!setup" == message.content.lower():
        
        #start dm with user, and begin student setup
        await client.start_private_message(message.author)
        await client.send_message(message.author, f'Welcome, {message.author}, to the CityLine Students Discord Server.')
        await client.send_typing(message.author)
        await client.send_message(message.author, 'I have just a couple of questions to ask you, so that you can get situated into the server.')
        await client.send_typing(message.author)
        await client.send_message(message.author, f'respond with "ok" whenever you are ready to continue')
        await client.wait_for_message(author=message.author, content='ok')
        
        #ask for first and last name
        await client.send_typing(message.author)
        await client.send_message(message.author, 'What is your first and last name?')
        response = await client.wait_for_message(author=message.author)
        name = response.content
        #firstName, lastName = name.split(' ', 1)
        
        
        #ask for gender
        await client.send_typing(message.author)
        await client.send_message(message.author, 'What is your gender? (m/f)')
        response = await client.wait_for_message(author=message.author)
        gender = response.content
        
        #gender logic
        while not (gender == 'm' or gender == 'f'):
            await client.send_typing(message.author)
            await client.send_message(message.author, 'Please enter in your gender as (m or f)')
            response = await client.wait_for_message(author=message.author)
            gender = response.content

        if gender == 'm':
            gender = 'male'
        else:
            gender = 'female'

        #ask for grade
        await client.send_typing(message.author)
        await client.send_message(message.author, 'What is your current grade? (enter a digit)')
        response = await client.wait_for_message(author=message.author)
        curGrade  = response.content

        #grade logic
        while not curGrade.isdigit():
            await client.send_typing(message.author)
            await client.send_message(message.author, 'Please enter in your current grade as a number.')
            response = await client.wait_for_message(author=message.author)
            curGrade = response.content

        smallGroup = getSpecificRole(gender, curGrade)
        await assignStudent(message.author, name, gender, curGrade)
        await client.send_typing(message.author)
        await client.send_message(message.author, 'You\'re all setup, go say "Hi" to your small group members')
        await client.send_message(discord.Object(id='695099605091876884'), f'**{name}** *just setup their account: they\'re in the* **{smallGroup}** *group*')

        




        


# Student Setup on Join       
@client.event
async def on_member_join(member):
    await client.start_private_message(member)
    #start dm with user, and begin student setup
    await client.send_message(member, f'Welcome, {member}, to the CityLine Students Discord Server.')
    await client.send_typing(member)
    await client.send_message(member, 'I have just a couple of questions to ask you, so that you can get situated into the server.')
    await client.send_typing(member)
    await client.send_message(member, f'respond with "ok" whenever you are ready to continue')
    await client.wait_for_message(author=member, content='ok')
    
    #ask for first and last name
    await client.send_typing(member)
    await client.send_message(member, 'What is your first and last name?')
    response = await client.wait_for_message(author=member)
    name = response.content
    #firstName, lastName = name.split(' ', 1)
    
    
    #ask for gender
    await client.send_typing(member)
    await client.send_message(member, 'What is your gender? (m/f)')
    response = await client.wait_for_message(author=member)
    gender = response.content
    
    #gender logic
    while not (gender == 'm' or gender == 'f'):
        await client.send_typing(member)
        await client.send_message(member, 'Please enter in your gender as (m or f)')
        response = await client.wait_for_message(author=member)
        gender = response.content

    if gender == 'm':
        gender = 'male'
    else:
        gender = 'female'

    #ask for grade
    await client.send_typing(member)
    await client.send_message(member, 'What is your current grade? (enter a digit)')
    response = await client.wait_for_message(author=member)
    curGrade  = response.content

    #grade logic
    while not curGrade.isdigit():
        await client.send_typing(member)
        await client.send_message(member, 'Please enter in your current grade as a number.')
        response = await client.wait_for_message(author=member)
        curGrade = response.content

    smallGroup = getSpecificRole(gender, curGrade)
    await assignStudent(member, name, gender, curGrade)
    await client.send_typing(member)
    await client.send_message(member, 'You\'re all setup, go say "Hi" to your small group members')
    await client.send_message(discord.Object(id='695099605091876884'), f'**{name}** *just setup their account: they\'re in the* **{smallGroup}** *group*')



    

client.run(TOKEN)

