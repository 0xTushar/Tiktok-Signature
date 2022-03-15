import asyncio

from ..TikTok import TikTok

ins=TikTok(proxies=None, debug=True)
username="something"
aweme_id="XXXX" # video id
ins.userFromJSON(username=username) # load user session json


response=asyncio.run(ins.api.aweme_stats(aweme_id=aweme_id))
print(response)
