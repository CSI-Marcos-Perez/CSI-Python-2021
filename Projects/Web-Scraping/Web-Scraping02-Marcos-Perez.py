import requests
req = requests.get("https://www.gutenberg.org/cache/epub/67635/pg67635.txt")
req.raise_for_status()
playFile = open("Koning Hendrik de Vijfde.text", "wb")
for chunk in req.iter_content(759):
    playFile.write(chunk)
playFile.close()