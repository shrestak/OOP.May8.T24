class Tap:
    tapMembers = 0
    progress_rate = 2
    cur_prog = 0

    _dept = "Not declared"

    def __init__(self, first, last, progress):
        self.first = first
        self.last = last
        self.progress = progress
        self._dept = _dept
        # print("Initialized")

    def full_name(self):
        return f"{self.first} {(self.last).upper()}"
    
    def set_dep(self,dept):
        self._dept = dept

    def get_dep():
        return self._dept
    
    def __len__(self):
        return len(self.first + self.last)
    
    def __str__(self):
        return f"{self.first} {self.last}: {self.progress} "
    
class Tech(Tap):
    progress = 5


tap1 = Tap("ck", "Smith", 0)
print(tap1)
print(tap1.full_name())
print(tap1.first)
tap1.first = "Charles"
print(tap1.first)
tap1.set_dep("IT")
print(tap1.get_dep)
print(len(tap1))
print(str(tap1))

