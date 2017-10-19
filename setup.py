import cx_Freeze
import sys

base=None

if sys.platform=='win32':
         base='Win32GUI'

executables=[cx_Freeze.Executable('brainAudio.py',base=base)]
cx_Freeze.setup(
         name='Foody',
         options={"build_exe":{"packages":["tkinter","PIL.Image","PIL.ImageTk","gtts","pygame"]}},
         version="0.01",
         description="No desc",
         executables=executables
         )
