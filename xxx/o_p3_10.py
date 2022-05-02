from importlib.resources import contents
import json
from urllib import response
import webbrowser
from urllib.request import urlopen

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20200615: ")
url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It shoud appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)