import PyLibBass_Python.bass_library as bass
import PyLibBass_Python.CONSTANTS_BASS as const
import time
FALSE = int(0)
TRUE = int(1)
false = bool(0)
tr = bool(1)
def Main():
    bass.BASS().BASS_INIT(device=int(-1), freq=48000, flags=0, win=0, dsguid=0)
    bass.BASS().BASS_START()
    handle_stream = bass.BASS().BASS_StreamCreateFile(FALSE, b"BUSSIN.mp3", 0, 0, const.BASS_SAMPLE_LOOP)
    bass.BASS().BASS_ChannelPlay(handle=handle_stream, restart=False)
    while True:
        time.sleep(4)

if __name__ == "__main__":
    Main()