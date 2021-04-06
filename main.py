count = 0
con = 1
import discord
url = "https://discord.com/api/webhooks/828710265586843659/C-kp8q_DVXjJ-3-YOAHr3EykOcpqVeqyME_8uycQrTPLHQQ0zfWF0Tsm0WUR--2XcFl4"
import time
import os
import pythonroblox
import requests
interger = 1
print("To start group scanner, press any key")
os.system("Pause")
while count < 2:
    try:
        groups = pythonroblox.Groups()
        result = groups.search_id(con)
        con = con + int(interger)
        groupmem = result.member_count
        groupname = result.name
        groupid = result.id
        groupown = result.owner_name
        args = "[member_count:", groupmem, ", group_name:", groupname, ", group_id:", groupid, ", group_owner:", groupown, "]"
        print(args)
        r = requests.post(url, data={"content": args})
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        if message.find("HTTP404"):
            print("Connection timed out")
        if message.find("Subscriptable"):
            con = con + int(interger)
            print("Error while loading, timed out for 1 second. The group ID is: ", con-int(1))
        time.sleep(1)
    time.sleep(0.1)
