
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions


class Render:
    def __init__(self):
        self.options = RGBMatrixOptions()
        self.options.hardware_mapping = 'adafruit-hat'
        self.options.gpio_slowdown = 3
        self.options.rows = 32
        self.options.cols = 64
        self.options.drop_privileges = False

        self.path = '/home/pi/audio-display/matrixdisplay'

        self.font = graphics.Font()
        self.font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x12.bdf")
        self.font2 = graphics.Font()
        self.font2.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")


    def setVolume(self,volume):
        matrix = RGBMatrix(options=self.options)
        canvas = matrix.CreateFrameCanvas()
        graphics.DrawText(canvas, self.font, 0, 0, graphics.Color(255, 0, 0), str(volume))