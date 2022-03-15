import asyncio
import json

from ..TikTok import TikTok

ins=TikTok(proxies=None, debug=True)
email="something"
password="somestrongpassword"
email_username="some@somewhere.com"
email_password="email_inbox_password"
asyncio.run(ins.device_register())
asyncio.run(ins.register(username=email,password=password,email_username=email_username,email_password=email_password))

with open("accounts/{}.json".format(email), "w") as f:
    f.write(json.dumps(ins.device,indent=4,sort_keys=True))
