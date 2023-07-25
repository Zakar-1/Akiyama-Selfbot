"""
Disclaimer:
    
The following disclaimer applies to the use and distribution of the open-source Python software Despair developed by Synchronos Shop, owned by Takaso, Dante, and Zakar. By using or accessing the Software, you agree to be bound by the terms and conditions set forth in this disclaimer.

1. License and Ownership:
The Software is released under an open-source license, and its source code is made available to the public. However, Synchronos Shop, Takaso, Dante, and Zakar retain all ownership rights to the original codebase and any modifications made by them. The open-source license governs the terms of use, distribution, and modification of the Software.

2. Prohibited Resale and Distribution:
While the Software is open source, you are prohibited from reselling the Software or distributing it for commercial purposes without explicit written permission from Synchronos Shop, Takaso, Dante, and Zakar. Commercial purposes include selling the Software as part of a software package, standalone product, or bundled with other products. Additionally, you are not allowed to give away the Software for free as part of a commercial offering without prior written permission from the owners.

3. License Compliance:
When distributing the Software or any modifications thereof, you must comply with the terms and conditions of the open-source license under which the Software is released. This includes providing proper attribution, retaining copyright notices, and making the source code available to recipients of the Software.

4. Disclaimer of Warranty:
The Software is provided on an "as-is" basis, without any warranties or conditions, express or implied. Synchronos Shop, Takaso, Dante, and Zakar disclaim all warranties, including but not limited to the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. The entire risk arising out of the use or performance of the Software remains with you.

5. Limitation of Liability:
In no event shall Synchronos Shop, Takaso, Dante, or Zakar be liable for any direct, indirect, incidental, special, consequential, or exemplary damages, including but not limited to damages for loss of profits, data, or other intangible losses, arising out of or in connection with the use or inability to use the Software, even if they have been advised of the possibility of such damages.

6. Governing Law:
This disclaimer shall be governed by and construed in accordance with the laws of Italy, without regard to its conflict of laws principles.

By using or accessing the Software, you acknowledge that you have read, understood, and agreed to be bound by this disclaimer. If you do not agree with any part of this disclaimer, you must not use or access the Software.

For any questions or inquiries regarding this disclaimer, please contact the owners through the designated channels provided by Synchronos Shop.

Date: May 22, 2023
"""
import discord; from discord.ext import commands; from discord.ext.commands import CommandNotFound; import aiosonic; import asyncio; import json; import random;import pystyle; from pystyle import Colors, Colorate; import websocket; import threading;
with open("config.json", "r") as jsonfile: conf = json.load(jsonfile);
_token, _prefix, bottt, chann_names, guild_name, nuke_msg = conf['token'], "!" if conf['prefix']=="" else conf['prefix'], False if conf['bot'] == "false" else True, "synchronos" if conf['nuke-channels'] == "" else conf['nuke-channels'], "Synchronos" if conf['guild-name'] == "" else conf['guild-name'], "@everyone" if conf['nuke-msg'] == "" else conf['nuke-msg'];
def black(): return '\u001b[30;1m';
def red(): return '\u001b[31;1m';
def green(): return '\u001b[32;1m';
def yellow(): return '\u001b[33;1m';
def blue(): return '\u001b[34;1m';
def magenta(): return '\u001b[35;1m';
def cyan(): return '\u001b[36;1m';
def white(): return '\u001b[37;1m';
def reset(): return '\u001b[0m';
def b_black(): return '\u001b[40;1m';
def b_red(): return '\u001b[41;1m';
def b_green(): return '\u001b[42;1m';
def b_yellow(): return '\u001b[43;1m';
def b_blue(): return '\u001b[44;1m';
def b_magenta(): return '\u001b[45;1m';
def b_cyan(): return '\u001b[46;1m';
def b_white(): return '\u001b[47;1m';
if not __import__("discord").__version__ == "1.7.3":
    for _ in ["pip uninstall discord", "pip uninstall discord.py", "pip install discord.py==1.7.3", "pip install discord==1.7.3"]:
        __import__("os").system(_);
def logo(): 
    print(Colorate.Horizontal(Colors.blue_to_purple,"""


▓█████▄ ▓█████   ██████  ██▓███   ▄▄▄       ██▓ ██▀███  
▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▓██ ▒ ██▒
░██   █▌▒███   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▒██▒▓██ ░▄█ ▒
░▓█▄   ▌▒▓█  ▄   ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ░██░▒██▀▀█▄  
░▒████▓ ░▒████▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒░██░░██▓ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░▓  ░ ▒▓ ░▒▓░
 ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░ ▒ ░  ░▒ ░ ▒░
 ░ ░  ░    ░   ░  ░  ░  ░░         ░   ▒    ▒ ░  ░░   ░ 
   ░       ░  ░      ░                 ░  ░ ░     ░     
 ░                                                      
"""));
checkweb:bool = False;
def _headers_(token:str, bot:bool=False) -> set:
   if bot: return {"Authorization": "Bot %s" % token};
   return {"Authorization": token};
async def _token_check(token:str, bot:bool=False) -> list:
    if token == "": return ["Empty"];
    r = await aiosonic.HTTPClient().get("https://discord.com/api/v9/users/@me", headers=_headers_(_token, bot=bot));
    if r.status_code == 401: return [False];
    elif r.status_code == 429: return ["Rate Limited"];
    else: return [True];
_check = asyncio.run(_token_check(_token, bottt));
if _check[0] == "Empty": print("The token is empty, go to config.json and put one."); input(); exit(0x0);
elif _check[0] == False: print("The token is invalid!"); input(); exit(0x0);
loop = asyncio.new_event_loop(); asyncio.set_event_loop(loop);
_n = commands.Bot(command_prefix=_prefix, self_bot=not bottt); _n.remove_command("help");
__import__("os").system("cls" if __import__("os").name == "nt" else "clear");
def members_scrape(guid:str, chid:str, token:str, logs:bool=False) -> list:
    import discum; bot = discum.Client(token=token);
    def close_after_fetching(resp, guild_id):
        try:
            if bot.gateway.finishedMemberFetching(guild_id):
                try:
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members);
                except Exception as _: return [];
                if logs: print(str(lenmembersfetched)+' members fetched');
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}}); bot.gateway.close()
        except: pass;
    def get_members(guild_id, channel_id):
        try:
            bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1); bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}});
            bot.gateway.run(); bot.gateway.resetSession();
            return bot.gateway.session.guild(guild_id).members;
        except: pass;
    if logs: print('MEMBER SCRAPER\nCredits to https://github.com/Merubokkusu/Discord-S.C.U.M');
    members = get_members(guid, chid);
    if logs:
        for memberID in members: print(memberID);
    f = open("users.txt", "a");
    for element in members: f.write(element + "\n");
    f.close();
    return members;
async def listen(token:str=None):
    ws = websocket.WebSocket(); ws.connect("wss://gateway.discord.gg/?v=6&encording=json");
    def h(interval, ws):
        while True:
            __import__("time").sleep(interval);
            heartbeatJSON = {
                "op": 1,
                "d": "null"
            }
            ws.send(json.dumps(heartbeatJSON));
    def rec_j(ws):
        r = ws.recv();
        if r: return json.loads(r);
    event = rec_j(ws); h_interval = event['d']['heartbeat_interval']/0x3e8;
    threading._start_new_thread(h, (h_interval, ws));
    payload = {
        "op": 2,
        "d": {
            "token": _token,
            "properties": {
                "$os": "takaso",
                "$browser": "chrome",
                "$device": "pc"
                }
            }
        }
    ws.send(json.dumps(payload));
    while True:
        event = rec_j(ws);
        ee = event['d'];
        if not tasks_running: return;
        try:
            if ee['author']['id'] == str(_n.user.id): continue;
            print("[%s+%s] %s: %s" % (green(), reset(), ee['author']['username'], ee['content']));
        except: pass;
@_n.command()
async def log_msgs(ctx):
    try: await ctx.message.delete();
    except: pass;
    def between_callback_1():
        try:
            loop = asyncio.new_event_loop(); asyncio.set_event_loop(loop);
            loop.run_until_complete(listen()); loop.close();
        except: pass;
    __import__("threading").Thread(target=between_callback_1).start();
    await ctx.send("Started logging.", delete_after=delete_aft);
async def deletechannels_worker(queue):
    while True:
        try:
            channel = await queue.get();
            request = await aiosonic.HTTPClient().delete("https://discordapp.com/api/v9/channels/%s" % channel.id, headers=_headers_(_token, bot=bottt));
            if request.status_code == 200: print(f"Deleted Channel - {channel}"); queue.task_done();
            elif request.status_code == 429:
                json = await request.json(); print("Rate limited, retrying.."); await asyncio.sleep(json['retry_after']);
                queue.put_nowait(channel);
            elif request.status_code in [401, 404, 403]: return;
            else: print(await request.json()); return;
        except: pass;
@_n.command()
async def cdel(ctx):
    try: await ctx.message.delete();
    except: pass;
    queue = asyncio.Queue();
    print("Queuing all channels.. | %s" % len(ctx.guild.channels));
    for channel in ctx.guild.channels: queue.put_nowait(channel);
    tasks = [];
    for _ in range(10): task = asyncio.create_task(deletechannels_worker(queue)); tasks.append(task);
    await queue.join();
    for task in tasks: task.cancel();
    await asyncio.gather(*tasks, return_exceptions=True);
async def create_channel_worker(queue, guild):
    while True:
        channel = queue.get_nowait();
        payload = {
            "name": channel,
            "type": "0"
        };
        r = await aiosonic.HTTPClient().post("https://discord.com/api/v9/guilds/%s/channels" % guild, json=payload, headers=_headers_(_token, bot=bottt));
        if r.status_code in [200, 201, 204]: queue.task_done();
        elif r.status_code == 429:
            json = await r.json(); print("Rate limited, retrying.."); await asyncio.sleep(json['retry_after']);
            queue.put_nowait(channel);
        elif r.status_code in [401, 404, 403]: return;
        else: print(await r.json()); return;
@_n.command()
async def ccr(ctx):
    try: await ctx.message.delete();
    except: pass;
    queue = asyncio.Queue();
    for _ in range(500): queue.put_nowait(chann_names);
    tasks = [];
    for _ in range(10): task = asyncio.create_task(create_channel_worker(queue, guild=ctx.guild.id)); tasks.append(task);
    await queue.join();
    for task in tasks: task.cancel();
    await asyncio.gather(*tasks, return_exceptions=True);
@_n.command()
async def nuke(ctx):
    global checkweb; 
    checkweb = True;
    asyncio.gather(*[cdel(ctx), ccr(ctx)], return_exceptions=False);
tasks_running:bool = True;
@_n.command()
async def break_tasks(ctx):
    global tasks_running;
    try: await ctx.message.delete();
    except: pass;
    if tasks_running: tasks_running = False;
    else: tasks_running = True;
    await ctx.send("> **Tasks Running**: `%s`" % tasks_running, delete_after=delete_aft);
on_mode:bool = False;
delete_aft:bool = 3;
@_n.command()
async def mode(ctx, on:str="on", delete_af:int=3):
    global on_mode; global delete_aft;
    try: await ctx.message.delete();
    except: pass;
    if on=="on": on_mode = True;
    else: on_mode = False;
    delete_aft = delete_af;
    await ctx.send("> **Ghost Ping**: `%s`\n> **Delete After**: `%s`\n> **Webhook Spam**: `%s`\n\n*Note, if the member scraper isn't working run this in the CMD*```\npython -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum\n```" % (on_mode, delete_aft, checkweb), delete_after=delete_aft);
@_n.command()
async def massping(ctx, *, _message:str="."):
    try: await ctx.message.delete();
    except: pass;
    try: open("users.txt", "w").close();
    except Exception as x: await ctx.send("**Error**\n```\n%s\n```" % x); return;
    if not bottt:
        members_scrape(guid=str(ctx.guild.id), chid=str(ctx.message.channel.id), token=_token, logs=False);
        with open("users.txt", "r", encoding="UTF-8") as scraped_: scraped = scraped_.read().splitlines();
        scraped_.close();
    else: scraped = [member.id for member in ctx.guild.members];
    while True:
        if not tasks_running: break;
        spam_msg = "> "; random.shuffle(scraped);
        try: scraped.remove(str(_n.user.id));
        except: pass;
        for _ in scraped:
            if len(scraped) > 1900-len(_message)-2: break;
            spam_msg+=" <@%s>" % _;
        try:
            if on_mode: await random.choice(ctx.guild.channels).send("%s\n%s | `%s`" % (spam_msg, _message, random.randint(1000, 9999)), delete_after=0);
            else: await ctx.send("%s\n\n%s | `%s`" % (spam_msg, _message, random.randint(1000, 9999)));
        except: pass;
async def banmembers_worker(guild, queue):
    while True:
        try:
            member_id = await queue.get();
            request = await aiosonic.HTTPClient().put("https://discord.com/api/v9/guilds/%s/bans/%s" % (guild, member_id), json={"delete_message_seconds":"3600"},headers=_headers_(_token, bot=bottt));
            if request.status_code in [204, 201, 200]: print(f"Banned: {member_id}"); queue.task_done();
            elif request.status_code == 429:
                json = await request.json(); print("Rate limited, retrying.."); await asyncio.sleep(json['retry_after']);
                queue.put_nowait(channel);
            elif request.status_code in [401, 404, 403]: return;
            else: print(await request.json()); return;
        except: pass;
@_n.command()
async def massban(ctx, *, _message:str="."):
    try: await ctx.message.delete();
    except: pass;
    try: open("users.txt", "w").close();
    except Exception as x: await ctx.send("**Error**\n\`\`\`\n%s\n\`\`\`" % x); return;
    if not bottt:
        members_scrape(guid=str(ctx.guild.id), chid=str(ctx.message.channel.id), token=_token, logs=False);
        with open("users.txt", "r", encoding="UTF-8") as scraped_: scraped = scraped_.read().splitlines();
        scraped_.close();
    else: scraped = [member.id for member in ctx.guild.members];
    try: scraped.remove(str(_n.user.id));
    except: pass;
    queue = asyncio.Queue();
    for _ in scraped: queue.put_nowait(_);
    tasks = [];
    for _ in range(10): task = asyncio.create_task(banmembers_worker(ctx.guild.id, queue)); tasks.append(task);
    await queue.join();
    for task in tasks: task.cancel();
    await asyncio.gather(*tasks, return_exceptions=True);
import re; # taken by feferant
ipregex = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}';
regexes = (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', ipregex, r'mfa\.[\w-]{84}');
@_n.command(aliases=["report"])
async def toxscan(ctx, chan_id=None, redirect=False):
    print("Starting.");
    def process_headers(head, list):
        a = list; str = head.split(); found = False;
        for item in a:
            if item in str: found = True;
        if found: return True;
        else: return False;
    toxxlist = ['@gmail.com', 'kys', 'kill yourself', 'dox', 'password', '@protonmail.com', 'nigger', 'faggot', 'child porn', 'groom children', 'heil hitler', 'doxxed', 'doxxing', 'token', 'ip', 'ip address', 'doxbin', 'gore', 'nazi', 'white power', '@hotmail', '@yahoo', '@tiscali', '@alice', 'raid', 'nuke', 'selfbot', 'wizz', 'hack', 'breach', 'database', 'furries', 'furry', 'pedo', 'pedophile', 'jew', 'heil', 'niggers', 'children', 'kid', 'cp', 'tox', 'toxxing', 'pedophilia', 'selfbot', 'self bot', 'sb', 'spam', 'raiders', '12','im 12', 'im 11', '11', '10', 'go hang', 'suicide']
    await ctx.message.delete();
    try:
        if chan_id==None: disb = ctx.channel;
        else: disb = await _n.fetch_channel(chan_id);
    except Exception as sss: await ctx.send(sss); return;
    chid = disb.id; badwords:int = 0; ips:int = 0; tokens:int = 0;
    try: guid = ctx.guild.id;
    except: guid = "@me";
    async for message in disb.history(limit=None):
        if message.author != _n.user:
            if len(re.findall(ipregex, message.content)) != 0:
                x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                if redirect==False: print(x);
                else: await ctx.send(x);
                ips+=1
            elif len(re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', message.content)) != 0: 
                x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                if redirect==False: print(x);
                else: await ctx.send(x);
                tokens+=1;
            elif len(re.findall( r'mfa\.[\w-]{84}', message.content)) != 0:
                x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                if redirect==False: print(x);
                else: await ctx.send(x);
                tokens+=1;
            else:
                if process_headers(message.content.lower(), toxxlist):
                    x = f"[] https://discord.com/channels/{guid}/{chid}/{message.id} -  {message.author} : {message.content}"
                    if redirect==False: print(x);
                    else: await ctx.send(x);
                    badwords = badwords+1;
    amongus = badwords + ips + tokens;
    if amongus == 0:
      print(f"No messages found.");
    else:
     print(f"""

{red()}Scrape results:{reset()}

{red()}Bad Words: {white()}{badwords}
{red()}IPs:{white()} {ips}
{red()}Tokens:{white()} {tokens}
{red()}Total:{white()} {amongus}{reset()}

""");
@_n.command()
async def ip_info(ctx, ip):
    try: await ctx.message.delete();
    except: pass;
    if not ip.replace(".", "").isnumeric(): await ctx.send("Invalid IP.", delete_after=delete_aft); return;
    r = await aiosonic.HTTPClient().get("https://ipwhois.app/json/" + ip);
    await ctx.send(f"""
```yaml
{await r.json()}
```
""");
@_n.command()
async def id_info(ctx, *, ID = None):
    try: await ctx.message.delete();
    except: pass;
    if ID == None: await ctx.send("You forgot the ID.", delete_after=delete_aft);
    try: user = await _n.fetch_user(ID);
    except: await ctx.send("Invalid ID.", delete_after=delete_aft);
    date_format = "%a, %d %b %Y %I:%M %p";
    hypesquad_class = str(user.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()
    hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])
    em=f"""
>>> ```
〓〓〚Info Card〛〓〓

[Username]

{user.name}#{user.discriminator}

[Account Creation]

{user.created_at.strftime(date_format)}

[HypeSquad]

{hypesquad_class}
```
{user.avatar_url}
"""
    try: await ctx.send(em, delete_after=delete_aft);
    except: print("\n[%s-%s] Failed to send message!" % (red()), reset())
@_n.command()
async def meme(ctx):
    try: await ctx.message.delete();
    except: pass;
    url = "https://meme-api.com/gimme";
    try:
        req = await aiosonic.HTTPClient().get(url);
        if req.status_code in [200, 201, 204]: mem = await req.json(); await ctx.send("`Link:`**<%s>**\n%s" % (mem['postLink'], mem['url']));
        elif req.status_code in [range(400, 405)]: await ctx.send("`No results found.`", delete_after=delete_aft);
        else: await ctx.send("`Error Status Code:` **%s**" % req.status_code);
    except Exception as xx:
        if xx == "": xx = "Error.";
        await ctx.send("`%s`" % xx, delete_after=delete_aft);
@_n.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("`Unkwown Command.`", delete_after=delete_aft);
        return;
    raise error;
@_n.command()
async def anime(ctx, *, arg=""):
    try: await ctx.message.delete();
    except: pass;
    hug_gifs = []; search_term = "anime+" + arg;
    r = await aiosonic.HTTPClient().get(f"https://g.tenor.com/v1/search?q={search_term}&key=IZ4ZVISUFUO5&limit=15")
    if r.status_code == 200:
        top_8gifs = await r.json();
        for i in range(len(top_8gifs['results'])):
            hug_gifs.append(top_8gifs['results'][i]['media'][0]['gif']['url']);
        await ctx.send(random.choice(hug_gifs));
    else: await ctx.send("`Error!`\n**%s**" % r.status_code);
@_n.command()
async def osint(ctx, email_addr="emailname@gmail.com"):
    try: await ctx.message.delete();
    except: pass;
    await ctx.send(f"""
> `Osint Sites`
> - <https://start.me/p/b5gEPe/email-osint>
> - <https://epieos.com/?q={email_addr}&t=email>
""");
@_n.command()
async def help(ctx):
    try: await ctx.message.delete();
    except: pass;
    await ctx.send(f"""
```
    Despair - Bot: {bottt}
```
>  `anime` - [search term]
>  `break_tasks` - [none]
>  `ccr`  - [none]        
>  `cdel` - [none]           
>  `help` - [None]
>  `id_info` - [user ID]    
>  `ip_info` - [ip address]
>  `log_msgs` - [none]   
>  `massban` - [none]
>  `masskick` - [none]
>  `massping` - [message]
>  `meme` - [none]
>  `mode` - [on/off | seconds]
>  `nuke`  - [none]
>  `osint` - [email address]
>  `report` - [channel id | true/false]
```
Deleting After: {delete_aft}
```
""", delete_after=delete_aft);
async def kickmembers_worker(guild, queue):
    while True:
        try:
            member_id = await queue.get();
            request = await aiosonic.HTTPClient().delete("https://discord.com/api/v9/guilds/%s/members/%s" % (guild, member_id), json={"delete_message_seconds":"3600"},headers=_headers_(_token, bot=bottt));
            if request.status_code in [204, 201, 200]: print(f"Kicked: {member_id}"); queue.task_done();
            elif request.status_code == 429:
                json = await request.json(); print("Rate limited, retrying.."); await asyncio.sleep(json['retry_after']);
                queue.put_nowait(channel);
            elif request.status_code in [401, 404, 403]: return;
            else: print(await request.json()); return;
        except: pass;
@_n.command()
async def masskick(ctx, *, _message:str="."):
    try: await ctx.message.delete();
    except: pass;
    try: open("users.txt", "w").close();
    except Exception as x: await ctx.send("**Error**\n\`\`\`\n%s\n\`\`\`" % x); return;
    if not bottt:
        members_scrape(guid=str(ctx.guild.id), chid=str(ctx.message.channel.id), token=_token, logs=False);
        with open("users.txt", "r", encoding="UTF-8") as scraped_: scraped = scraped_.read().splitlines();
        scraped_.close();
    else: scraped = [member.id for member in ctx.guild.members];
    try: scraped.remove(str(_n.user.id));
    except: pass;
    queue = asyncio.Queue();
    for _ in scraped: queue.put_nowait(_);
    tasks = [];
    for _ in range(10): task = asyncio.create_task(kickmembers_worker(ctx.guild.id, queue)); tasks.append(task);
    await queue.join();
    for task in tasks: task.cancel();
    await asyncio.gather(*tasks, return_exceptions=True);
@_n.event
async def on_guild_channel_create(channel):
  global checkweb
  if checkweb == True:
        webhook = await channel.create_webhook(name="Despair");
        try:
            while True: await webhook.send(nuke_msg);
        except Exception as x: print(x);
@_n.event
async def on_connect():
    logo(); 
    print("\n   [%s+%s] Connected to: %s%s%s" % (magenta(), reset(), green(), _n.user, reset()));
_n.run(_token, bot=bottt);
loop.close();
