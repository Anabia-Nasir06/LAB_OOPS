import random

class BirthdayParadox:
    def __init__(self, trials):
        self._trials = trials     
        self._results = []         

    def __has_duplicate(self, birthdays):  
        seen = set()
        for b in birthdays:
            if b in seen:
                return True
            seen.add(b)
        return False

    def birthday_paradox(self):
        for n in range(5, 101, 5):
            count = 0
            for _ in range(self._trials):
                birthdays = [random.randint(1, 365) for _ in range(n)]
                if self.__has_duplicate(birthdays):
                    count += 1
            probability = count / self._trials
            self._results.append((n, probability))
        return self._results

    @property
    def trials(self):
        return self._trials

    @trials.setter
    def trials(self, value):
        if value <= 0:
            raise ValueError("Number of trials must be positive")
        self._trials = value

    @property
    def results(self):
        return self._results

    def __str__(self):
        if not self._results:
            return "No experiments run yet."
        output = "Birthday Paradox Results:\n"
        for n, prob in self._results:
            output += f"Group size {n}: Probability {prob:.3f}\n"
        return output
    