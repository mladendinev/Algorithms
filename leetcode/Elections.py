import collections

class TimeUnit():
    def __init__(self, key, churki ):
        self.max = key
        self.votes = {}

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.times = times
        self.persons = persons
        self.results = self.calculateResults()

    def calculateResults(self):
        result = collections.defaultdict(TimeUnit)
        result[self.times[0]] = TimeUnit(key = self.persons[0], churki = )
        for idx in range(len(self.times)):
            result[idx] += 1

        return result

    def q(self, t):
        haha = {}
        haha.get(0, 1)
        if t > self.times[-1]:
            return self.results[-1]

        for idx in reversed(range(0, t + 1)):
            if idx in self.results:
                return self.results[idx]

    def countVotes(self, votes):
        person = ""
        max_votes = 0
        hui = {}
        for vote in votes:
            cici = str(vote)
            if not cici in hui:
                hui[cici] = 0
            else:
                hui[cici] += 1
            if hui[cici] >= max_votes:
                person = cici
                max_votes = hui[cici]
        return person


persons = [0, 1, 1, 0, 0, 1, 0]
times = [0, 5, 10, 15, 20, 25, 30]
obj = TopVotedCandidate(persons=persons, times=times)
