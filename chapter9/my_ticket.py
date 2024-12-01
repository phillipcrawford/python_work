import lottery
import time

my_ticket = lottery.play_lottery()
print(my_ticket)
time.sleep(3)
count = 0

play_again = lottery.play_lottery()
print(play_again)
count += 1
print(count)
while my_ticket != play_again:
    play_again = lottery.play_lottery()
    print(play_again)
    count += 1
    print(count)
