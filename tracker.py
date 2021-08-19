import pickle
import nubanner
import tweeter


class Tracker:
    def __init__(self, tweeter):
        self.tweeter = tweeter
        try:
            infile = open('trackedClasses', 'rb')
            self.TrackedClasses = pickle.load(infile)
            infile.close()
        except FileNotFoundError:
            self.TrackedClasses = {}

    def save(self):
        outfile = open('trackedClasses', 'wb')
        pickle.dump(self.TrackedClasses, outfile)
        outfile.close()

    def add(self, subject, courseNumber):
        self.TrackedClasses[(subject, courseNumber)] = nubanner.getClassData(
            subject, courseNumber)

    def update(self):
        self.oldTrackedClasses = self.TrackedClasses
        for classInfo in self.TrackedClasses:
            self.TrackedClasses[classInfo] = nubanner.getClassData(
                classInfo[0], classInfo[1])
            for CRN in self.TrackedClasses[classInfo]:
                if self.oldTrackedClasses[classInfo][CRN] == False and self.TrackedClasses[classInfo][CRN] == True:
                    self.tweeter.tweet(
                        f'A seat in {classInfo[0]} {classInfo[1]} CRN:{CRN} is now available')
                if self.oldTrackedClasses[classInfo][CRN] == True and self.TrackedClasses[classInfo][CRN] == False:
                    self.tweeter.tweet(
                        f'There are now no seats available in {classInfo[0]} {classInfo[1]} CRN:{CRN}')
