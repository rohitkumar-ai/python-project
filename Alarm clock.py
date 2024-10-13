import datetime
import time
import os
import platform

def alarm_sound():
    # Check the platform (Windows or others)
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1000 ms
    else:
        # Cross-platform approach (Linux/Mac)
        duration = 1  # seconds
        freq = 440  # Hz (Standard beep sound frequency)
        os.system(f'play -nq -t alsa synth {duration} sine {freq}')

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            alarm_sound()
            break
        time.sleep(1)  # Wait for 1 second before checking again

def main():
    print("Welcome to the Python Alarm Clock!")
    alarm_time = input("Enter the alarm time (HH:MM:SS in 24-hour format): ")

    try:
        # Validate the input time
        valid_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()
        print(f"Alarm is set for {alarm_time}.")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")

if __name__ == "__main__":
    main()
