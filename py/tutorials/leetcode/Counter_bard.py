def createCounter(init):
  """
  Creates a counter object with an initial value of init.

  Args:
    init: The initial value of the counter.

  Returns:
    A counter object with three functions: increment(), decrement(), and reset().
  """

  class Counter:
    def __init__(self, init):
      self.value = init

    def increment(self):
      self.value += 1
      return self.value

    def decrement(self):
      self.value -= 1
      return self.value

    def reset(self):
      self.value = init
      return self.value

  return Counter(init)

n = 5
c = createCounter(n)

r1 = c.decrement()
r2 = c.reset()
print(r1,r2)
