import time
import pigpio

# GPIO pin for the servo
servo_pin = 12

# Connect to the pigpio service
pi = pigpio.pi()

if not pi.connected:
    exit(0)

# Function to set the pulse width of the servo
def set_pulse_width(pin, pulse_width):
    pi.set_servo_pulsewidth(pin, pulse_width)
    time.sleep(0.1)  # Adjust the duration as needed

try:
    print("Enter pulse width values from 500 to 2500 to control the servo.")
    print("Type 'exit' to end the program.")

    while True:
        user_input = input("Enter pulse width (500-2500): ")

        if user_input.lower() == 'exit':
            break

        try:
            pulse_width = int(user_input)
            if 500 <= pulse_width <= 2500:
                set_pulse_width(servo_pin, pulse_width)
            else:
                print("Invalid input. Pulse width must be between 500 and 2500.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

except KeyboardInterrupt:
    print("\nProgram terminated by user")
finally:
    # Stop the servo
    pi.set_servo_pulsewidth(servo_pin, 0)
    pi.stop()
