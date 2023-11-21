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
    time.sleep(0.0005)  # Adjust the duration as needed

# Initial sweep to find zeroed positions

for pulse_width in range(2500, 499, -interval):
    set_pulse_width(servo_pin_1, pulse_width)

time.sleep(1)

for pulse_width in range(2500, 499, -interval):
    set_pulse_width(servo_pin_2, pulse_width)

time.sleep(1)

print("Servos initialized to zeroed positions.")

# Function to move the servo to a new position gradually
def move_to_position(pin, current_position, target_position):
    step = 1 if target_position > current_position else -1

    for pulse_width in range(current_position, target_position, step):
        set_pulse_width(pin, pulse_width)

try:
    while True:
        # Get user input for servo 1
        user_input_1 = input("Enter position for Servo 1 (500-2500): ")

        if user_input_1.lower() == 'exit':
            break

        try:
            target_position_1 = int(user_input_1)
            if 500 <= target_position_1 <= 2500:
                move_to_position(servo_pin_1, pi.get_servo_pulsewidth(servo_pin_1), target_position_1)
            else:
                print("Invalid input. Position must be between 500 and 2500.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Get user input for servo 2
        user_input_2 = input("Enter position for Servo 2 (500-2500): ")

        if user_input_2.lower() == 'exit':
            break

        try:
            target_position_2 = int(user_input_2)
            if 500 <= target_position_2 <= 2500:
                move_to_position(servo_pin_2, pi.get_servo_pulsewidth(servo_pin_2), target_position_2)
            else:
                print("Invalid input. Position must be between 500 and 2500.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

except KeyboardInterrupt:
    print("\nProgram terminated by user")
finally:
    # Stop the servos
    pi.set_servo_pulsewidth(servo_pin_1, 0)
    pi.set_servo_pulsewidth(servo_pin_2, 0)
    pi.stop()
