# A SIMPLE TIMER IN PYTHON #
import time

seconds = input ("Number of Seconds: ")

startTime = time.time()

finishTime = startTime + seconds

while time.time() < finishTime:
    print seconds
    seconds = seconds -1
    time.sleep(1)

print "Time is up!" * 4

import sys

sys.stdout.write('\a\a\a\a')
sys.stdout.flush()
