class KataBowling(object):
    def getScore(self, allScores):
        score = 0
        frames = self.getFrames(allScores)
        for frame in range(len(frames)):
            if frames[frame] == 'X':
                pass
            elif frames[frame] == '/':
                pass
            elif frames[frame] =='-':
                pass
            else:
                score += int(frames[frame])
        return score

    def getFrames(self, allScores):
        pass
                

    
