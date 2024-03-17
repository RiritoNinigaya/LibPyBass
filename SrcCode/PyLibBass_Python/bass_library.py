import ctypes
import os
def ConnectBASS():
        try:
            dllpath = os.path.join(os.path.dirname(__file__), 'x64_bass\\bass.dll')
            bassdll = ctypes.cdll.LoadLibrary(dllpath)
            return bassdll
        except:
            raise RuntimeError("[BASS]: Not Founded BASS.dll or Him Dependencies!!!")
class BASS:
    def BASS_INIT(self, device : int, freq : ctypes.c_int32, flags : ctypes.c_int32, win : int, dsguid : int):
        return ConnectBASS().BASS_Init(self, device, freq, flags, win, dsguid)
    def BASSFree(self):
        return ConnectBASS().BASS_Free()
    def BASSStop(self):
        return ConnectBASS.BASS_Stop()
    def BASS_StreamCreateFile(self, mem : int, filename : str, offset : int, length : int, flags : int):
        return ConnectBASS().BASS_StreamCreateFile(mem, filename, offset, length, flags)
    def BASS_START(self):
        return ConnectBASS().BASS_Start()
    def BASS_ChannelPlay(self, handle, restart : bool):
        return ConnectBASS().BASS_ChannelPlay(handle, restart)