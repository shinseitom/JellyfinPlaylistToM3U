# JellyfinPlaylistToM3U
Quick and dirty python script that converts a hardcoded Jellyfin audio playlist XML into an M3U playlist
Creates an M3U file named according to the playlist name in Jellyfin with an addition "_converted"

I created this because I had a massive 1400+ playlist of songs in Jellyfin I had curated, but I had no way to export it despite Jellyfin having the ability to import playlists.
Seemed like an odd oversight.  So with a half-hour of relearning python and looking up simple XML parsers I finished this tiny script.

Lowest hanging fruit to fix would be making the file be a parameter passed to the script, but I got what I needed so probably no updates.
