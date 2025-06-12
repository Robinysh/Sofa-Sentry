import typer
from sofa_sentry.vision import Vision
from sofa_sentry.robot import Robot
import time

app = typer.Typer()

FPS_LIMIT = 2


@app.command()
def main():
    vision = Vision()
    robot = Robot()
    time_last = 0
    while True:
        time_start = time.time()
        time_elasped = time_start - time_last
        if time_elasped < 1 / FPS_LIMIT:
            time.sleep(1 / FPS_LIMIT - time_elasped)

        if position := vision.detected():
            print("Cat detected, moving robot and spraying")
            robot.move_to(position)
            robot.spray()

        time_last = time_start
        # break


if __name__ == "__main__":
    main()
