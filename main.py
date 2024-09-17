import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if current_time == alarm_time:
            print("Time to wake up")
            pygame.mixer.init() 
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
    pass

if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 2, 2048)

    alarm = input("Enter the time to set alarm: HH:MM:SS :")
    set_alarm(alarm)
