import time

seconds=input("Time In Seconds")
def countdown_timer(seconds):
    while seconds>0:
        minutes=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{minutes}:{secs}'
        time.sleep(1)
        print(timer)
        seconds=seconds-1
   
    print("Time Up")

countdown_timer(int(seconds))