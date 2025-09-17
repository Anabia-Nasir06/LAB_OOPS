import random

class BirthdayParadox:
    def __init__(self,trials):
        self.trials = trials

    def has_duplicate(self, birthdays):
        seen = set()
        for b in birthdays:
            if b in seen:
                return True
            seen.add(b)
        return False

    def birthday_paradox(self):
        result = {}
        for n in range(5,101,5):
            count = 0
            for _ in range(self.trials):
                birthdays = [random.randint(1, 365) for _ in range(n)]
                if self.has_duplicate(birthdays):
                    count += 1
            probability = count / self.trials
            result[n] = probability 
        return result
    