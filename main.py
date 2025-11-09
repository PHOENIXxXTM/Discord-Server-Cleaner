import discord
from discord.ext import commands
import datetime

TOKEN = "YOUR_BOT_TOKEN_HERE"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ make sure both confirmation keys exist
confirmations = {"clean": {}, "kick": {}}

# function to log actions to file
def log_action(action: str):
    with open("cleanup_log.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {action}\n")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    log_action(f"Bot started as {bot.user}")

# ===========================================================
# CLEAN SERVER (Channels + Roles)
# ===========================================================
@bot.command(aliases=["serverclean"])
@commands.has_permissions(administrator=True)
async def cleanserver(ctx):
    guild_id = ctx.guild.id

    # set confirmation flag
    confirmations["clean"][guild_id] = True

    await ctx.send(
        "⚠️ **WARNING!** This will delete **all channels and roles** (except @everyone)."
        "\nType `!confirmclean` to confirm within 30 seconds or ignore to cancel."
    )
    log_action(f"[{ctx.guild.name}] Cleanup requested by {ctx.author}")

@bot.command()
@commands.has_permissions(administrator=True)
async def confirmclean(ctx):
    guild = ctx.guild
    guild_id = guild.id

    # ✅ safely check the flag
    if confirmations.get("clean", {}).get(guild_id, False):
        log_action(f"[{guild.name}] Server cleanup started by {ctx.author}")
        await ctx.send("🧹 Cleaning the server... This channel may be deleted soon.")

        # delete channels
        for channel in guild.channels:
            try:
                await channel.delete()
                log_action(f"Deleted channel: {channel.name}")
            except Exception as e:
                log_action(f"Failed to delete channel {channel.name}: {e}")

        # delete roles
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    log_action(f"Deleted role: {role.name}")
                except Exception as e:
                    log_action(f"Failed to delete role {role.name}: {e}")

        # create a new log channel
        new_channel = await guild.create_text_channel("cleanup-log")
        await new_channel.send("✅ Server cleanup complete! (see `cleanup_log.txt`)")
        log_action(f"[{guild.name}] Cleanup completed successfully.")
        confirmations["clean"][guild_id] = False

    else:
        await ctx.send("❌ No active cleanup request. Use `!cleanserver` first.")
#kick
@bot.command()
@commands.has_permissions(administrator=True)
async def kickall(ctx):
    """Ask for confirmation before kicking all members."""
    guild_id = ctx.guild.id
    confirmations["kick"][guild_id] = True
    await ctx.send(
        "⚠️ **WARNING!** This will kick **all non-bot members** from the server.\n"
        "Type `!confirmkick` within 30 seconds to confirm, or ignore to cancel."
    )
    log_action(f"[{ctx.guild.name}] Kick request started by {ctx.author}")

@bot.command()
@commands.has_permissions(administrator=True)
async def confirmkick(ctx):
    """Kick all non-bot members after confirmation."""
    guild = ctx.guild
    guild_id = guild.id

    if confirmations.get("kick", {}).get(guild_id):
        await ctx.send("👢 Starting mass kick... please wait.")
        log_action(f"[{guild.name}] Kick started by {ctx.author}")

        kicked = 0
        failed = 0

        for member in guild.members:
            # skip self and bots
            if member.bot or member == ctx.author:
                continue

            try:
                await member.kick(reason=f"Mass kick by {ctx.author}")
                kicked += 1
                log_action(f"Kicked member: {member} (ID: {member.id})")
            except Exception as e:
                failed += 1
                log_action(f"Failed to kick {member}: {e}")

        confirmations["kick"][guild_id] = False
        await ctx.send(f"✅ Kicked {kicked} members. ❌ Failed: {failed}.")
        log_action(f"[{guild.name}] Kick finished: Kicked={kicked}, Failed={failed}")
    else:
        await ctx.send("❌ No active kick request. Use `!kickall` first.")


bot.run(TOKEN)
