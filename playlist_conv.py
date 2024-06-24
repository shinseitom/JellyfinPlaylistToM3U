import xml.etree.ElementTree as ET

tree = ET.parse("Vocal/playlist.xml")
root = tree.getroot()

if(root.find("PlaylistMediaType").text != "Audio"):
    print("This isn't an audio playlist, skipping!")
    exit()

#we have found an audio playlist

playlistName = root.find("LocalTitle").text

print("Opening " + playlistName + "_converted.m3u for writing")
f = open(playlistName+"_converted.m3u", "w", encoding='utf-8')

for path in root.iter("Path"):
    print(path.text)
    f.write(path.text)
    f.write('\n')


f.close()