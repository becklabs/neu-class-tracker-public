from tracker import Tracker
from tweeter import Tweeter
import time

tweeter = Tweeter()

tracker = Tracker(tweeter)

tracker.add('POLS', '2358')

while True:
    print('Updating...')
    tracker.update()
    time.sleep(30)
