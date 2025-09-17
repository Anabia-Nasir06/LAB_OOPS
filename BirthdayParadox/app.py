from birthdayparadox import BirthdayParadox
class App:
    def run(self):
        bp = BirthdayParadox(trials=1000)
        results = bp.birthday_paradox()
        for n, prob in results.items():
            print(f"n={n}: probability={prob:.3f}")

