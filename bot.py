import discord
from discord import app_commands, Intents, Client, Interaction
from dotenv import load_dotenv
import os
import azure_module

load_dotenv
token = os.getenv("TOKEN")

class AIBot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()

client = AIBot(intents=Intents.none())

@client.event
async def on_ready():
    if not client.user:
        raise RuntimeError("on_ready() somehow got called before Client.user was set!")

    print((f"""
        Logged in as {client.user} (ID: {client.user.id})
        Invite URL for {client.user}:
        https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot
    """), end="\n\n")

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@client.tree.command(name="ai", description="Ask anything from ChatGPT")
async def ai(interaction: Interaction, user_input: str):
    await interaction.response.send_message(azure_module.response_req(user_input))


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@client.tree.command(name = "about", description = "Show information about this bot and its developer")
async def about(interaction: Interaction):
    await interaction.response.send_message("Bot powered by Azure and GitHub Modules, developed by @miscom_mon")


client.run(token)