from rpi_hardware_pwm import HardwarePWM
from time import sleep


class Servo:

    def __init__(
        self,
        channel,
        period=20,
        chip=0,
        min_duty_cycle=0.5,
        max_duty_cycle=2.5,
        min_angle=0,
        max_angle=180,
    ):
        self.pwm = HardwarePWM(pwm_channel=0, hz=50, chip=0)
        self.period = period
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.min_duty_cycle = min_duty_cycle
        self.max_duty_cycle = max_duty_cycle
        self.current_angle = None
        self.move(0)

    def move(self, angle):
        angle = min(max(self.min_angle, angle), self.max_angle)
        if angle == self.current_angle:
            return

        target_duty_cycle = self.min_duty_cycle + (angle - self.min_angle) * (
            self.max_duty_cycle - self.min_duty_cycle
        ) / (self.max_angle - self.min_angle)
        self.pwm.start(100 * target_duty_cycle / self.period)
        self.current_angle = angle


class Robot:
    def __init__(self):
        self.spray_servo = Servo(channel=0)
        self.pan_servo = None
        self.tilt_servo = None

    def move_to(self, position):
        print(f"Moving to position: {position}")
        pass

    def spray(self):
        print("Spraying...")
        self.spray_servo.move(180)
        sleep(1)
        self.spray_servo.move(0)
