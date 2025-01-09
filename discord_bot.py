import discord
from discord.ext import commands
from dotenv import load_dotenv
import typing
import os
load_dotenv()
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    slash_commands = await bot.tree.sync()
    print("\n".join([f"已註冊: {sc.name}"for sc in slash_commands]))
    print(f"{bot.user} logged in!") 

@bot.tree.command(name="help", description="指令資訊 \n輸入 /help 指令名稱 來獲得詳細資訊")
async def help(interaction: discord.Interaction, cmd: str = None):
    if cmd is None:
        await interaction.response.send_message(
        """# chillythacat's bot
### 處理2048相關任務的機器人
```ansi
[0;0m指令介紹
[1;38m輸入 /help 指令名稱 來獲得詳細資訊
[0;30m------------------------------------
[0;0m/help 指令資訊
/draw 畫出使用者輸入的2048棋盤
```""")
    else:
        if cmd.lower() == 'draw':
            await interaction.response.send_message("""# chillythacat's bot
### 處理2048相關任務的機器人
```ansi
[0;0m指令介紹
[1;38m/draw 畫出使用者輸入的2048棋盤
[0;30m-------------------------------------
[0;0m引數:
[0;34msize [0;0m棋盤大小，接受4x4, 3x3, 2x4, 3x4
[0;34mtheme [0;0m色彩主題，為2048verse內建
[0;34mboard [0;0m棋盤狀態，由左到右以直列輸入
[0;34mdark_enable [0;0m暗色模式，接受布林值
[0;30m-------------------------------------
[1;38m使用例:
[0;0m/draw size: 4x4 theme: default board: 216114ad37be29cf dark_enable: true
可以利用選項來減少輸入
```""")
        else:await interaction.response.send_message(f'目前並沒有 `{cmd}` 指令', ephemeral=True)




@bot.tree.command(name="draw", description="畫出使用者輸入的2048棋盤。")
async def draw(interaction: discord.Interaction, size: typing.Literal['4x4', '3x3', '3x4', '2x4'],\
               theme: typing.Literal['default', 'classic', 'pink', 'eight', 'dice', 'spooky', 'holiday', 'kaiser', 'mochiica', 'fruitsational', 'tropical', 'supernova']\
                    ,board: str ,dark_enable: bool):
    dark_enable = str(dark_enable).lower()
    await interaction.response.send_message(f"https://board.2048verse.com/{board}/{theme}/{dark_enable}/{size}")
#f'board.2048verse.com/{board}/classic/false/4x4'

bot.run(os.getenv("TOKEN"))




