from playsound import playsound
import time

# playsound("mytune.mp3")
CLEAR = "\033[23"
CLEAR_AND_RETURN = "\033[23"


def myfunc(seconds):
    time_passed = 0
    CLEAR = "\033[23"

    while time_passed < seconds:
        time.sleep(1)
        time_passed += 1

        timeleft = seconds - time_passed
        minleft = timeleft // 60
        secleft = timeleft % 60

        print(f"{minleft:02d}:{secleft:02d}")
    playsound("my_alarm\mytune.mp3")


seconds = int(input("enter how many seconds you wait to alarm? : "))
myfunc(seconds)
