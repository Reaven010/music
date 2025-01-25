import time
import vlc

# List of lyrics with timestamps (in seconds) to sync with the song
ajj_din_chadheya_lyrics = [
    ("Ajj din chadheya", 0),
    ("Tere rang warga", 2),
    ("Ajj din chadheya", 6),
    ("Tere rang warga", 10),
    ("", 12),
    ("Phul sa hai khila", 15),
    ("aaj din", 18),
    ("Rabba mere din yeh", 22),
    ("na dhale", 26),
    ("Woh jo mujhe khawab", 30),
    ("mein mile", 34),
    ("", 36),
    ("Use tu lagede abb gale", 40),
    ("Tenu dil da vasta", 44),
    ("Rabba aaya dar de yaar de", 48),
    ("Sara jahan chod chad ke", 52),
    ("Mere sapne sawar de", 56),
    ("Tennu dil da vasta", 60),
    ("", 62),
    ("Ajj din chadheya", 66),
    ("Tere rang warga", 70),
    ("", 74),
    ("Baksha gunaho ko", 78),
    ("Sun ke duwao ko", 82),
    ("Rabba pyaar hai", 86),
    ("Tune sab ko hi de diya", 90),
    ("Meri bhi aahon ko", 94),
    ("Sun le duwao ko", 98),
    ("Mujhko woh dila mene", 102),
    ("jisko hai dil diya", 106),
    ("Hoooo", 110),
    ("", 112),
    ("Baksha gunaho ko", 116),
    ("Sun ke duwao ko", 120),
    ("Rabba pyaar hai", 124),
    ("Tune sab ko hi de diya", 128),
    ("Meri bhi aahon ko", 132),
    ("Sun le duwao ko", 136),
    ("Mujhko woh dila mene", 140),
    ("jisko hai dil diya", 144),
    ("", 148),
    ("Aasmaan pe aasmaan", 152),
    ("uske de itna bata", 156),
    ("Woh jo mujhko dekh", 160),
    ("ke hase", 164),
    ("Pana chahun raat din", 168),
    ("jise", 172),
    ("Rabba mere naam", 176),
    ("kar use", 180),
    ("Tenu dil da vasta", 184),
    ("", 188),
    ("Ajj din chadheya", 192),
    ("Tere rang warga", 196),
    ("", 200),
    ("Manga jo mera hai", 204),
    ("Jata kya tera hai", 208),
    ("Mene kaun si", 212),
    ("Tujhse jannat manga li", 216),
    ("Kaisa khuda hai tu", 220),
    ("Bas naam ka hai tu", 224),
    ("Rabba jo teri itni", 228),
    ("si bhi na chali", 232),
    ("Haaanaaa", 236),
    ("", 240),
    ("Manga jo mera hai", 244),
    ("Jata kya tera hai", 248),
    ("Mene kaun si", 252),
    ("Tujhse jannat manga li", 256),
    ("Kaisa khuda hai tu", 260),
    ("Bas naam ka hai tu", 264),
    ("Rabba jo teri itni", 268),
    ("si bhi na chali", 272),
    ("", 276),
    ("Chahiye jo mujhe", 280),
    ("Kar de tu mujhko ata", 284),
    ("Jeeti rahi saltanat teri", 288),
    ("Jeeti rahe ashiqui meri", 292),
    ("Dede mujhe zindagi meri", 296),
    ("Tenu dil da vasta", 300),
    ("", 304),
    ("Rabba mere din yeh", 308),
    ("na dhale", 312),
    ("Woh jo mujhe khawab", 316),
    ("mein mile", 320),
    ("Use tu lagede abb gale", 324),
    ("Tenu dil da vasta", 328),
    ("", 332),
    ("Rabba aaya dar de yaar de", 336),
    ("Sara jahan chod chad ke", 340),
    ("Mere sapne sawar de", 344),
    ("Tennu dil da vasta", 348),
    ("", 352),
    ("Ajj din chadheya", 356),
    ("Tere rang warga", 360),
    ("Ajj din chadheya", 364),
    ("Tere rang warga", 368),
    ("Ajj din chadheya", 372),
    ("Tere rang warga", 376),
    ("Din chadheya", 380),
    ("Tere rang warga", 384),
    ("Ajj din chadheya", 388)
]

# Function to display the lyrics with timing
def display_lyrics_with_timing(lyrics):
    start_time = time.time()
    for line, timestamp in lyrics:
        while time.time() - start_time < timestamp:
            time.sleep(0.1)  # Wait until the correct timestamp
        print(line)

# Play music using VLC
player = vlc.MediaPlayer("python/spotifydown.com - Ajj Din Chadheya - Rahat Fateh Ali Khan.mp3")
player.play()

print("Playing song... Synchronizing lyrics...")
# Display lyrics synchronized with the song
display_lyrics_with_timing(ajj_din_chadheya_lyrics)

input("Press Enter to stop the music...")
player.stop()
