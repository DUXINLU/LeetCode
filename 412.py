class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                l.append("FizzBuzz")
                continue
            if not i % 3:
                l.append("Fizz")
                continue
            if not i % 5:
                l.append("Buzz")
                continue
            l.append(str(i))
        return l
