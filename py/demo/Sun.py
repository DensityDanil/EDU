class Sun():
    def __init__( self
                 ,age=10**3
                 ,name='Milky'):
        self.age = age
        self.name = name



s1 = Sun(age=10**15).age
s2 = Sun(age=10**16).age

gt = s1-s2
