from interactions import Client, Intents, listen, slash_command, SlashContext, OptionType, slash_option
from model import chat_handler
import json
import os

CHANNELS = []
GENERAL_CONTEXT = "You are an assistant for a rolePlay discord server. Here are the text formats to use:\n**action**\n*thinking*\n'talking'. Answer shortly."

bot = Client(intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT, debug_scope=123456789012345645)

@listen()  
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"This bot is owned by {bot.owner}")

@listen()
async def on_message_create(event):
    if(event.message.channel.id in CHANNELS) and (event.message.author.id != bot.user.id):
        if(not event.message.content.startswith("#")):
            await event.defer()
            chat = chat_handler(str(event.message.channel.id))
            message = chat.prompt(event.message.content)
            await event.message.channel.send(message)

@slash_command(name="add_channel", description="Adds the current channel to the list of channels observed by the AI")
@slash_option(
    name="identity",
    description="Which character would you like the AI to play?",
    required=True,
    opt_type=OptionType.STRING,
    max_length=512
)
async def open_chnl(ctx: SlashContext, identity: str):
    with open('./chats/' + str(ctx.channel.id) + '.json', 'w', encoding='utf-8') as f:
            json.dump([
                        {
                            "role": "user",
                            "content": GENERAL_CONTEXT
                        },
                        {
                            "role": "user",
                            "content": identity
                        }
                    ], f, ensure_ascii=False, indent=4)
    CHANNELS.append(ctx.channel.id)
    await ctx.send("The channel has been added successfully, please send only one message at a time!")
    print(CHANNELS)

@slash_command(name="remove_channel", description="Removes the current channel from the list of channels observed by the AI")
async def remove(ctx: SlashContext):
    CHANNELS.remove(ctx.channel.id)
    os.remove('./chats/' + str(ctx.channel.id) + '.json')
    await ctx.send("The channel has been successfully removed!")

@slash_command(name="general_context", description="Modifies the general execution context of the server.")
@slash_option(
    name="ex_context",
    description="Enter your context",
    required=True,
    opt_type=OptionType.STRING,
    max_length=512
)
async def general_ctx(ctx: SlashContext, ex_context: str):
    GENERAL_CONTEXT = ex_context
    await ctx.send(f"The new context is:\n{GENERAL_CONTEXT}")

bot.start("TOKEN")