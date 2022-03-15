import asyncio
import json

from ..TikTok import TikTok

ins=TikTok(proxies=None, debug=True)
username="something" # accepts username and password both
password="somestrongpassword"
email_username="some@somewhere.com" # only required in case of error code 2033 (forced password reset by tiktok)
email_password="email_inbox_password"
asyncio.run(ins.device_register())
asyncio.run(ins.login(username=username,password=password,email_username=email_username,email_password=email_password))

with open("accounts/{}.json".format(username), "w") as f:
    f.write(json.dumps(ins.device,indent=4,sort_keys=True))
