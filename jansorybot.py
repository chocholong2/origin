from tokens import jtoken
from tokens2 import jtoken2
import discord
from discord.ext import commands, tasks
from discord import app_commands, ButtonStyle, Interaction, ui
import datetime
from datetime import datetime
import pytz
import tracemalloc
import random
import asyncio
import json
import os

to = jtoken+jtoken2
MCHID = "1346345402626080788"
TCHID = "1346345402626080788"

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix='!',intents=intents,**kwargs)
        self.synced = False

    async def on_ready(self):
        print(f'봇이 로그인되었습니다: {self.user.name}')
        if not self.synced:
            await self.tree.sync()
            print("슬래시 명령어가 동기화되었습니다.")
            self.synced = True
        tracemalloc.start()

bot = MyBot()


@bot.tree.command(name='안녕',description="봇한테 인사를 합니다")
async def 안녕(interaction: discord.Interaction):
    await interaction.response.send_message("안녕하세요")


@bot.tree.command(name='청소하자',description="청소하자는 잔소리")
async def 청소(interaction: discord.Interaction):
    await interaction.response.send_message("본인자리를 깨끗이 청소해주세요.")


async def main():
    async with bot:
        await bot.start(to)

import asyncio
asyncio.run(main())
