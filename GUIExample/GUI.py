import dearpygui.dearpygui as dpg
import PyLibBass_Python.bass_library as bass_lib
import PyLibBass_Python.CONSTANTS_BASS as constant_bass
from convert_str_to_bytes import Convert
def SetMusicPlay(value_music : str):
    return dpg.get_value(value_music)
def GetBASS():
    return bass_lib.BASS()
def StopMus():
    if bass_lib.BASS().BASSFree() is False:
        print("Music Is Not Initializated or It's Failed to Free BASS Library!!!")
    else:
        print("Music is Now Stopped Successfully")
def Thread():
    GetBASS().BASS_INIT(device=int(-1), freq=48000, flags=0, win=0, dsguid=0)
    GetBASS().BASS_START()
    handle_stream = GetBASS().BASS_StreamCreateFile(mem=0, filename=Convert(SetMusicPlay("GETVAL_MUSIC")), offset=0, length=0, flags=constant_bass.BASS_SAMPLE_LOOP)
    GetBASS().BASS_ChannelPlay(handle=handle_stream, restart=False)
def SetUI():
    dpg.create_context()
    with dpg.window(tag="WINDOW_PRIM_PYLIBBASS"):
        dpg.add_text("Hello, This Is My First Example to Init BASS Library with DearPyGUI... So Enjoy to use this example!!!")
        dpg.add_input_text(label="Path To Music", tag="GETVAL_MUSIC")
        dpg.add_button(label="Play Music", callback=Thread)
        dpg.add_button(label="Stop Music", callback=StopMus)
    dpg.create_viewport(title='PyLibBass DearPyGui Example by RiritoNinigaya', width=830, height=455)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("WINDOW_PRIM_PYLIBBASS", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
