import discord
import signal
import time
import traceback

import healthcheck

client = discord.Client()

@client.event
async def on_ready():
    while True:
        start = time.monotonic()
        await run_and_upload()
        end = time.monotonic()
        time.sleep(120 - (end - start))

async def run_and_upload():
  try:
    healthcheck.main()
    with open("result.txt", "r") as f:
      results = f.read(2000)
  except Exception:
    results = "[FATAL] Healthcheck died:\n```" + traceback.format_exc() + "```"
  if len(results) >= 2000:
    results = results[:1985] + "``` (truncated)"
  server = client.get_guild(761313515490639873)
  channel = server.get_channel(1079509634991259648)
  edited = False
  async for message in channel.history(limit=1):
    if message.author == client.user:
      await message.edit(content=results)
      edited = True
  if not edited:
    await channel.send(content=results)

with open("token.txt", "r") as file:
  token = file.readline().strip()
client.run(token)
