import sys, os
if os.name == "nt":
    import msvcrt, ctypes
    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]
class functions:
    def hide_cursor():
        if os.name == "nt":
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = False
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == "posix":
            sys.stdout.write("[?25l")
            sys.stdout.flush()
    def show_cursor():
        if os.name == "nt":
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = True
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == "posix":
            sys.stdout.write("[?25h")
            sys.stdout.flush()
def show():
    """Shows the cursor."""
    functions.show_cursor()
def hide():
    """Hides the cursor."""
    functions.hide_cursor()
def pos(x, y):
    """Returns a code to set the cursor position."""
    return "[" + str(y) + ";" + str(x) + "H"
def move(x, y):
    """Moves the cursor to the given coordinates."""
    print(pos(x, y), end="")