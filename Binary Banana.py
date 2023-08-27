TOKEN ='MTA2Mzg2NTM2NDk2ODEyMDM3MA.GirW3x.WnaeuEEs3K_e5FiWOnoigW-CHFWESTm5R0bF6A'

import discord
import numpy as np


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    sum=0
    if message.author == client.user:
        return
    
    if message.content[0] == '+':
        nums = message.content.split()
        nums.remove('+')
        print('Numbers are : ', nums) 
        

        for element in nums:
            sum+=float(element)

        await message.channel.send(f"Sum of the numbers is {str(sum)}")


    prod=1
    if message.content[0] == '*':
        nums = message.content.split()
        nums.remove('*')
        print('Numbers are : ', nums)
        

        for element in nums:
            prod*=float(element)

        await message.channel.send(f"The product of the numbers are {str(prod)}")

    if "roots" in message.content.lower():
        coeff = message.content.split()
        coeff.remove("roots")
        print("Coefficients are : ",coeff)
        coeff=[float(i) for i in coeff]
        r=np.roots(coeff)
        print("Roots are : ",r)
        await message.channel.send(f'The roots of the polynomial with given coefficients are {r} ')

    if message.content.find("diff") != -1:
        input = message.content[5::].split()
        arr = []
        for el in input:
            arr.append(float(el))
        deg = (arr.pop(0))
        res = []
        i = 0
        while i < len(arr)-1:
            res.append(arr[i]*(len(arr)-i-1))
            i += 1
        await message.channel.send(f"The derivateive of the function has degree {deg-1} and coefficients {res}")

    if message.content.lower() == "!help":
        await message.channel.send("""OPTIMUS_MEGABYTE can help you in the following ways: \n
1) The Plus function!, all you need to do is type '+ numbers' for example '+ 5 2 3 6 4' ans voila the sum is right there in front of you. \n
2) The Product function!, example '* 5 6 2 5 4' and as easy as that you can compute multiplication of as many numbers as you want !!! \n
3) Root finding of a Polynomial function, example:- 'roots a b c d' where a, b, c, d are the coefficients of the function of degree 4 in this case. \n
4) Differetiation of a Polynomial function !!, example:- 'diff n a b c' where n is the degree and a, b, c are the coefficients. #DON'T FORGET THE ZEROS!! """)

    


client.run(TOKEN)