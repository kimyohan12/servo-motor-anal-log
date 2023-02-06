import spidev
import time

# Constants for the trigger and echo pins
TRIGGER_PIN = 0
ECHO_PIN = 1

# Create an instance of the SpiDev class
spi = spidev.SpiDev()

# Open a connection to the ADC
spi.open(0,0)

# Set the maximum speed (in Hz) of the communication
spi.max_speed_hz = 1000000

def distance_read():
    # Trigger the sensor by setting the trigger pin high for 10 us
    spi.xfer2([1, (8+TRIGGER_PIN)<<4, 0])
    time.sleep(10e-6)
    spi.xfer2([1, (8+TRIGGER_PIN)<<4, 0])

    # Wait for 