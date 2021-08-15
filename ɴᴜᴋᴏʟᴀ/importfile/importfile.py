from __future__ import unicode_literals
from Cula import *

def videoseeder(command_to_exec):
    process = asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print(e_response)
    filename = t_response.split("Syncing All FetchedFiles")[-1].split('"')[1]
    return filename

def audioseeder(command_to_exec):
    process = asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print("Download error:", e_response)
    return t_response.split("Destination")[-1].split("Deleting")[0].split(":")[-1].strip()