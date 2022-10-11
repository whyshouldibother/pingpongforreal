import random, time
class pos:
    def __init__(self,val,acc):
        self.val=val
        self.acc=acc
    def flip(self):
        self.acc=-self.acc
    def increase(self):
        self.val+=self.acc
class entity:
    def __init__(self):
        self.color=(255,255,255)
    def colour(self):
        random.seed(self.color)
        self.color= (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
def tof():
    random.seed(time.time())
    return random.choice([True,False])
def rec_score(new_score):
    score = open("score.dat", "a")
    score.write(str(new_score)+"\n")
    score.close()
def highscore():
    try:
        score=open("score.dat","r")
        high=0
        for i in score:
            if int(i)>high :
                high=int(i)
        return high
    except:
        return 0