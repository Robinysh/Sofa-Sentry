from gpiozero import AngularServo
from time import sleep
from rpi_hardware_pwm import HardwarePWM

# Device.pin_factory = NativeFactory()

# Device.pin_factory = RPiGPIOFactory()

if False:
    # servo = AngularServo(14, min_angle=-90, max_angle=90, min_pulse_width=0.0006, max_pulse_width=0.0023)
    servo = AngularServo(
        12, min_angle=-90, max_angle=90, min_pulse_width=0.0006, max_pulse_width=0.0023
    )
    # servo = AngularServo(12, min_angle=-90, max_angle=90)
    print(servo.is_active)
    servo.angle = 0
    sleep(1)
    servo.angle = 45
    print(servo.is_active)
    sleep(1)
    servo.angle = 0
    sleep(1)

pwm = HardwarePWM(pwm_channel=0, hz=50, chip=0)

print("1")
pwm.start(100 * 0.5 / 20)

sleep(3)
print("2")
pwm.change_duty_cycle(100 * 2.5 / 20)
sleep(3)
print("3")
pwm.change_duty_cycle(100 * 0.5 / 20)
sleep(3)
print("4")

pwm.stop()
