import time
import pigpio

# GPIO pins for the servos
servo_pin_1 = 12
servo_pin_2 = 13

interval = 1

# Connect to the pigpio service
pi = pigpio.pi()

if not pi.connected:
    exit(0)

# Function to set the pulse width of a servo
def set_pulse_width(pin, pulse_width):
    pi.set_servo_pulsewidth(pin, pulse_width)
    time.sleep(.001)  # Adjust the duration as needed

try:
    while True:
        # Sweep servo on GPIO 12
        print("Sweeping servo on GPIO 12:")
        for pulse_width in range(500, 2501, interval):
            set_pulse_width(servo_pin_1, pulse_width)

        time.sleep(.5)

        for pulse_width in range(2500, 499, -interval):
            set_pulse_width(servo_pin_1, pulse_width)

        # Sweep servo on GPIO 13
        print("Sweeping servo on GPIO 13:")
        for pulse_width in range(500, 2501, interval):
            set_pulse_width(servo_pin_2, pulse_width)

        time.sleep(.5)

        for pulse_width in range(2500, 499, -interval):
            set_pulse_width(servo_pin_2, pulse_width)

except KeyboardInterrupt:
    print("\nProgram terminated by user")
finally:
    # Stop the servos
    pi.set_servo_pulsewidth(servo_pin_1, 0)
    pi.set_servo_pulsewidth(servo_pin_2, 0)
    pi.stop()
