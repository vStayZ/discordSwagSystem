import discord
import STATIC
import asyncio
import random

bot = discord.Client()

def is_not_pinned(mess):
    return not mess.pinned

@bot.event
async def on_ready():
    global giveaway
    global helpmessagebool

    print("\n" * 50)
    print(f"{bot.user} is now Online!")
    for i in bot.guilds:
        print(f"Connected on: {i.name}")
    bot.loop.create_task(task_game())

    ### Giveaway ###
    giveaway = False

async def task_game():
    while True:
        await bot.change_presence(activity=discord.Game("Ticket System"), status=discord.Status.online)
        await asyncio.sleep(12)
        await bot.change_presence(activity=discord.Game("Thanks vStayZ#6018 for making me :p"), status=discord.Status.online)
        await asyncio.sleep(12)
        await bot.change_presence(activity=discord.Game("Giveaway System"), status=discord.Status.online)
        await asyncio.sleep(12)
        await bot.change_presence(activity=discord.Game("System Bot for Swag Nation"), status=discord.Status.online)
        await asyncio.sleep(12)

########################################################################################################################

@bot.event
async def on_message(message):
    global ticketmessage

    if message.content.startswith(STATIC.PREFIX) and not bot.user == message.author:
        Dictator = "Dictator"
        Lieutenant = "👨‍💻 | Lieutenant"
        Dictator = discord.utils.get(message.author.guild.roles, name=Dictator)
        Lieutenant = discord.utils.get(message.author.guild.roles, name=Lieutenant)
        invoke = message.content[len(STATIC.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]

        invokelower = invoke.lower()

        if Dictator in message.author.roles or Lieutenant in message.author.roles and bot != message.author:

            #### Giveaway System ####
            if invokelower == "giveaway":
                global giveawaymessage
                global giveawaymsg
                global giveaway

                done = args[0].lower()
                await message.delete()
                if done == "done":
                    if giveaway == True:
                        giveaway = False
                        ### winner ###
                        giveawaymsg = await message.channel.fetch_message(giveawaymsg.id)
                        users = await giveawaymsg.reactions[0].users().flatten()
                        import random
                        winner = random.choice(users)
                        while True:
                            if winner:
                                if winner == bot.user:
                                    winner = random.choice(users)
                                else:
                                    break
                            else:
                                print(f"ERROR Winner konnte nicht ausgegeben werden: {winner.mention}")

                        embed = discord.Embed(title="🎉 Giveaway Results 🎉", color=discord.Color.green(),
                                              description=f"Congratulations to {winner.mention}")
                        file = discord.File("image/gif/giveawayclap.gif", filename="giveawayclap.gif")
                        embed.set_image(url="attachment://giveawayclap.gif")
                        await giveawaymsg.delete()
                        await asyncio.sleep(3)
                        await message.channel.send(file=file, embed=embed)
                    else:
                        error = await message.author.create_dm()
                        await error.send("Hey, no giveaway is currently running.")
                elif len(args[0]) >= 1:
                    if giveaway == False:
                        giveaway = True
                        count = 1000
                        await message.channel.purge(limit=count)
                        embed = discord.Embed(title=message.content.replace("s!giveaway", ""), color=discord.Color.green(),
                                              description="React to this message with 🎉")
                        giveawaymsg = await message.channel.send(embed=embed)
                        await giveawaymsg.add_reaction('🎉')

                    else:
                        error = await message.author.create_dm()
                        await error.send("Hey, a giveaway is currently running!")

            #### Ticket System ####
            if invokelower == "reaction_role_ticket":
                await message.delete()
                await asyncio.sleep(1)
                count = 5000
                await message.channel.purge(limit=count, check=is_not_pinned)
                await asyncio.sleep(3)
                embed = discord.Embed(title="Ticket", color=discord.Color.green(),
                                      description="Welcome to the ticket-support channel.\n"
                                      "If you need help react with 🎰 to create a new ticket!")
                ticketmessage = await message.channel.send(embed=embed)
                await ticketmessage.add_reaction("🎰")

            #### Ticket close System ####
            if invokelower == "ticket" and args[0] == "close":
                guild = message.author.guild
                role = "in support"
                role = discord.utils.get(guild.roles, name=role)
                channel = f"{message.channel}"
                channel = discord.utils.get(guild.channels, name=f"{channel}")
                if message.channel.name.startswith("ticket-"):
                    for member in channel.members:
                        await member.remove_roles(role)
                    await channel.delete()

            #### Reaction Role System ####
            if invokelower == "reaction_role":
                global reactionrolesystemping

                count = 50000
                await asyncio.sleep(1)
                await message.channel.purge(limit=count, check=is_not_pinned)

                #### Ping ####
                embed = discord.Embed(title="Pings", color=0xa2e8b5,
                                      description="If it is ok to ping, **react with** 🔔\n"
                                                  "If you don't want to be pinged, react with 🔕")
                reactionrolesystemping = await message.channel.send(embed=embed)
                await reactionrolesystemping.add_reaction("🔔")
                await reactionrolesystemping.add_reaction("🔕")

                await asyncio.sleep(2)
                #### Continents ####
                embed = discord.Embed(title="Continents", color=0xa2e8b5,
                                      description="🌍 -> Africa/Europe\n"
                                                  "🌏 -> Asia/Oceania\n"
                                                  "🌎 -> North/South America\n"
                                                  "🧊 -> Antarctica")
                reactionrolesystemcontinents = await message.channel.send(embed=embed)
                await reactionrolesystemcontinents.add_reaction("🌍")
                await reactionrolesystemcontinents.add_reaction("🌏")
                await reactionrolesystemcontinents.add_reaction("🌎")
                await reactionrolesystemcontinents.add_reaction("🧊")

                await asyncio.sleep(3)
                #### DM ####
                embed = discord.Embed(title="DM", color=0xa2e8b5,
                                      description="👍 -> Ok to DM \n"
                                                  "🙋 -> Ask to DM \n"
                                                  "👎 -> Do Not DM")
                reactionrolesystemdm = await message.channel.send(embed=embed)
                await reactionrolesystemdm.add_reaction("👍")
                await reactionrolesystemdm.add_reaction("🙋")
                await reactionrolesystemdm.add_reaction("👎")

                await asyncio.sleep(2)
                #### AGE ####
                embed = discord.Embed(title="Age", color=0xa2e8b5,
                                      description="💍 -> I am 21+ years old.\n"
                                                  "🍦 -> I am 18-20 years old.\n"
                                                  "🐟 -> I am 15-17 years old.\n"
                                                  "⚽ -> I am 13-14 years old.\n"
                                                  "👻 -> I am not following Discord's ToS (12 or under)")
                reactionrolesystemage = await message.channel.send(embed=embed)
                await reactionrolesystemage.add_reaction("💍")
                await reactionrolesystemage.add_reaction("🍦")
                await reactionrolesystemage.add_reaction("🐟")
                await reactionrolesystemage.add_reaction("⚽")
                await reactionrolesystemage.add_reaction("👻")

                await asyncio.sleep(4)
                #### Gender = Geschlecht ####
                embed = discord.Embed(title="Gender", color=0xa2e8b5,
                                      description="👦 -> Boy\n"
                                                  "👧 -> Girl\n"
                                                  "🐻 -> Non-Binary")
                reactionrolesystemgender = await message.channel.send(embed=embed)
                await reactionrolesystemgender.add_reaction("👦")
                await reactionrolesystemgender.add_reaction("👧")
                await reactionrolesystemgender.add_reaction("🐻")

                await asyncio.sleep(2)
                #### Helper ####
                embed = discord.Embed(title="Helper", color=0xa2e8b5,
                                      description="💀 -> Reviver of the Server \n"
                                                  "👮‍♀️ -> Welcomer \n"
                                                  "👊 -> Bump Ping")
                reactionrolesystemhelper = await message.channel.send(embed=embed)
                await reactionrolesystemhelper.add_reaction("💀")
                await reactionrolesystemhelper.add_reaction("👮‍♀️")
                await reactionrolesystemhelper.add_reaction("👊")

                await asyncio.sleep(2)
                #### Hobbies ####
                embed = discord.Embed(title="Hobbies", color=0xa2e8b5,
                                      description="👾 -> | Gamer\n"
                                                  "💩 -> Weeb \n"
                                                  "🎙 -> Musician \n"
                                                  "👩‍🎨 -> Artist \n"
                                                  "✍️-> Writer")
                reactionrolesystemhobbies = await message.channel.send(embed=embed)
                await reactionrolesystemhobbies.add_reaction("👾")
                await reactionrolesystemhobbies.add_reaction("💩")
                await reactionrolesystemhobbies.add_reaction("🎙")
                await reactionrolesystemhobbies.add_reaction("👩‍🎨")
                await reactionrolesystemhobbies.add_reaction("✍️")

                await asyncio.sleep(4)
                #### Announcement Pings ####
                embed = discord.Embed(title="Announcement Pings", color=0xa2e8b5,
                                      description="📣 -> Announcements Ping\n"
                                                  "🎥 -> Movie Night Pings\n"
                                                  "🎉 -> Giveaway Ping")
                reactionrolesystemhelper = await message.channel.send(embed=embed)
                await reactionrolesystemhelper.add_reaction("📣")
                await reactionrolesystemhelper.add_reaction("🎥")
                await reactionrolesystemhelper.add_reaction("🎉")

@bot.event
async def on_reaction_add(reaction, user):
    try:
        if reactionrolesystemping.id:
            if bot.user == user:
                return

            if reaction.emoji == "🔔":
                role = "🔔 | Ok to ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🔕":
                role = "🔕 | Do not ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            #### continent ####
            elif reaction.emoji == "🌍":
                role = "🌍 | Africa/Europe"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🌏":
                role = "🌏 | Asia/Oceania"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🌎":
                role = "🌎 | North/South America"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🧊":
                role = "🧊 | Antarctica"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            #### DM ####
            elif reaction.emoji == "👍":
                role = "👍 | Ok to DM"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🙋":
                role = "🙋 | Ask to DM"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "👎":
                role = "👎 | Do Not DM"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            #### AGE ####
            elif reaction.emoji == "💍":
                role = "💍 I am 21+ years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🍦":
                role = "🍦 I am 18-20 years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🐟":
                role = "🐟 I am 15-17 years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "⚽":
                role = "⚽ I am 13-14 years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "👻":
                role = "👻 I am not following Discord's ToS (12 or under)"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            #### GENDER ####
            elif reaction.emoji == "👦":
                role = "Boy"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "👧":
                role = "Girl"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🐻":
                role = "Non-Binary"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            #### Helper ####
            elif reaction.emoji == "💀":
                role = "💀 | Reviver of the Server"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "👮‍♀️":
                role = "👮‍♀️ | Welcomer"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "👊":
                role = "👊 | Bump Ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            #### Hobbies ####
            elif reaction.emoji == "👾":
                role = "👾 | Gamer"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "💩":
                role = "💩 | Weeb"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🎙":
                role = "🎙 | Musician"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "👩‍🎨":
                role = "👩‍🎨 | Artist"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "✍️":
                role = "✍️ | Writer"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            #### Announcement Pings ####
            elif reaction.emoji == "📣":
                role = "Announcements Ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🎥":
                role = "Movie Night Pings"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)
            elif reaction.emoji == "🎉":
                role = "Giveaway Ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.add_roles(role)

            if ticketmessage.id:

                if bot.user == user:
                    return

                if reaction.emoji == "🎰":
                    guild = user.guild
                    role = "in support"
                    role = discord.utils.get(guild.roles, name=role)
                    await ticketmessage.remove_reaction("🎰", user)

                    if role not in user.roles:
                        await user.add_roles(role)

                        name = f"{user}".replace('#', '-')
                        ticketchannel = await guild.create_text_channel(f"ticket-{name}")
                        await ticketchannel.set_permissions(guild.default_role, read_messages=False,
                                                            send_messages=False)

                        Dictator = "Dictator"
                        Lieutenant = "👨‍💻 | Lieutenant"
                        TrialModPolice = "👨‍🏭 | Trial Mod/Police"
                        Colonel = "🔨 | Colonel"
                        helperandsupport = "👸🏼 | Helper and Support"

                        Dictator = discord.utils.get(guild.roles, name=Dictator)
                        Lieutenant = discord.utils.get(guild.roles, name=Lieutenant)
                        TrialModPolice = discord.utils.get(guild.roles, name=TrialModPolice)
                        Colonel = discord.utils.get(guild.roles, name=Colonel)
                        helperandsupport = discord.utils.get(guild.roles, name=helperandsupport)
                        await ticketchannel.set_permissions(Dictator, read_messages=True, send_messages=True)
                        await ticketchannel.set_permissions(Lieutenant, read_messages=True, send_messages=True)
                        await ticketchannel.set_permissions(TrialModPolice, read_messages=True, send_messages=True)
                        await ticketchannel.set_permissions(Colonel, read_messages=True, send_messages=True)
                        await ticketchannel.set_permissions(helperandsupport, read_messages=True, send_messages=True)

                        await ticketchannel.set_permissions(user, read_messages=True, send_messages=True)

                        embed = discord.Embed(title=f"{ticketchannel}", color=discord.Color.red(),
                                              timestamp=ticketchannel.created_at,
                                              description=f"Hey {user.mention},\n"
                                                          f"**Please feel free to describe your issue below, so that we waste no time in helping you out.**\n\n"
                                                          f"__Ticket can be closed at any time with the__ `s!ticket close`")
                        file = discord.File("image/gif/ticketwelcome.gif", filename="ticketwelcome.gif")
                        embed.set_image(url="attachment://ticketwelcome.gif")
                        await ticketchannel.send(embed=embed, file=file)
    except:
        print("NOO")

@bot.event
async def on_reaction_remove(reaction, user):
    try:
        if reactionrolesystemping.id:
            if bot.user == user:
                return

            if reaction.emoji == "🔔":
                role = "🔔 | Ok to ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🔕":
                role = "🔕 | Do not ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            #### continent ####
            elif reaction.emoji == "🌍":
                role = "🌍 | Africa/Europe"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🌏":
                role = "🌏 | Asia/Oceania"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🌎":
                role = "🌎 | North/South America"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🧊":
                role = "🧊 | Antarctica"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            #### DM ####
            elif reaction.emoji == "👍":
                role = "👍 | Ok to DM"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🙋":
                role = "🙋 | Ask to DM"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "👎":
                role = "👎 | Do Not DM"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            #### AGE ####
            elif reaction.emoji == "💍":
                role = "💍 I am 21+ years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🍦":
                role = "🍦 I am 18-20 years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🐟":
                role = "🐟 I am 15-17 years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "⚽":
                role = "⚽ I am 13-14 years old."
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "👻":
                role = "👻 I am not following Discord's ToS (12 or under)"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            #### GENDER ####
            elif reaction.emoji == "👦":
                role = "Boy"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "👧":
                role = "Girl"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🐻":
                role = "Non-Binary"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            #### Helper ####
            elif reaction.emoji == "💀":
                role = "💀 | Reviver of the Server"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "👮‍♀️":
                role = "👮‍♀️ | Welcomer"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "👊":
                role = "👊 | Bump Ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            #### Hobbies ####
            elif reaction.emoji == "👾":
                role = "👾 | Gamer"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "💩":
                role = "💩 | Weeb"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🎙":
                role = "🎙 | Musician"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "👩‍🎨":
                role = "👩‍🎨 | Artist"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "✍️":
                role = "✍️ | Writer"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            #### Announcement Pings ####
            elif reaction.emoji == "📣":
                role = "Announcements Ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🎥":
                role = "Movie Night Pings"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
            elif reaction.emoji == "🎉":
                role = "Giveaway Ping"
                role = discord.utils.get(user.guild.roles, name=role)
                await user.remove_roles(role)
    except:
        print("NO")

bot.run(STATIC.TOKEN)
