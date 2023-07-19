import numpy as np
import win32gui, win32ui
import dxcam
from PIL import Image

class WindowCapture:
    #Properties
    w = 0
    h = 0
    hwnd = None
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=None):
        if window_name is None:
            raise Exception("Window name not specified")

        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception("Window not found: {}".format(window_name))

        rect = win32gui.GetWindowRect(self.hwnd)
        self.w = rect[2] 
        self.h = rect[3] 
        self.camera = dxcam.create(region=(0, 0, self.w, self.h))

    def get_screenshot(self) -> np.ndarray:
        return self.camera.grab()  # numpy.ndarray of size (640x640x3) -> (HXWXC)

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)

    def get_cursor(self):
        hcursor = win32gui.GetCursorInfo()[1]
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 36, 36)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0,0), hcursor)

        bmpinfo = hbmp.GetInfo()
        bmpstr = hbmp.GetBitmapBits(True)
        cursor = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1).convert("RGBA")

        # win32gui.DestroyIcon(hcursor)    
        win32gui.DeleteObject(hbmp.GetHandle())
        hdc.DeleteDC()
        pixdata = cursor.load()

        width, height = cursor.size
        for y in range(height):
            for x in range(width):

                if pixdata[x, y] == (0, 0, 0, 255):
                    pixdata[x, y] = (0, 0, 0, 0)

        hotspot = win32gui.GetIconInfo(hcursor)[1:3]

        return (cursor, hotspot)