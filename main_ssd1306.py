from machine import Pin, SPI
import ssd1306
import time
import framebuf

# Define SPI pins and other control pins
spi_sck = Pin(2) # SPI Clock
spi_mosi = Pin(3) # SPI MOSI
oled_cs = Pin(6, Pin.OUT) # Chip Select
oled_dc = Pin(5, Pin.OUT) # Data/Command
oled_rst = Pin(4, Pin.OUT) # Reset

# Initialize SPI
spi = SPI(0, baudrate=100000, sck=spi_sck, mosi=spi_mosi)

# Initialize SSD1306 OLED
oled = ssd1306.SSD1306_SPI(128, 64, spi, oled_dc, oled_rst, oled_cs) # Adjust width/height for your display

# Clear the display
oled.fill(0)
oled.show()



def Zahabiya():
    # Display text
    oled.text("Happy", 10, 1)
    oled.text("Birthday", 10, 20)
    oled.text("ZAHABIYA", 10, 40)
    oled.show()

def Line():
    oled.hline(0, 10, 128, 1)
    oled.hline(0, 20, 128, 1)
    oled.hline(0, 30, 128, 1)
    oled.hline(0, 40, 128, 1)
    oled.show()

def Clear():
    oled.fill(0)
    oled.show()



Zahabiya()
Clear()
Line()
Clear()

logo = bytearray([
    
])

# Create framebuffer from image
fb = framebuf.FrameBuffer(logo, 128, 64, framebuf.MONO_HLSB)

# Display the image
oled.fill(0)
oled.blit(fb, 0, 0)
oled.show()

Clear()
Zahabiya()
#Clear()

    
