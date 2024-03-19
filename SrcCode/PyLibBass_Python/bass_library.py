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
    def BASS_INIT(self, device : ctypes.c_int, freq : ctypes.c_int32, flags : ctypes.c_int32, win : ctypes.c_int, dsguid : ctypes.c_int) -> ctypes.c_bool:
        ConnectBASS().BASS_Init.restype = ctypes.c_bool
        ConnectBASS().BASS_Init.argtypes = [ctypes.c_int, ctypes.c_int32, ctypes.c_int32, ctypes.c_int, ctypes.c_int]
        return ConnectBASS().BASS_Init(device, freq, flags, win, dsguid)
    def BASSFree(self):
        ConnectBASS().BASS_Free.restype = ctypes.c_bool
        return ConnectBASS().BASS_Free()
    def BASSStop(self):
        ConnectBASS().BASS_Stop.restype = ctypes.c_bool
        return ConnectBASS().BASS_Stop()
    def BASS_StreamCreateFile(self, mem : ctypes.c_int, filename : ctypes.c_char, offset : ctypes.c_int, length : ctypes.c_int, flags : ctypes.c_int) -> ctypes.c_ulong:
        ConnectBASS().BASS_StreamCreateFile.restype = ctypes.c_ulong
        ConnectBASS().BASS_StreamCreateFile.argtypes = [ctypes.c_int, ctypes.c_char, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        return ConnectBASS().BASS_StreamCreateFile(mem, filename, offset, length, flags)
    def BASS_START(self):
        return ConnectBASS().BASS_Start()
    def BASS_ChannelPlay(self, handle : int, restart : bool):
        return ConnectBASS().BASS_ChannelPlay(handle, restart)
