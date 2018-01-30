import unittest
from limerick import LimerickDetector

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.ld = LimerickDetector()

    def test_guess_syllables(self):
        s = []
        
        try: self.assertEqual(self.ld.guess_syllables("kogo"),2)
        except: s.append(1)
        try: self.assertEqual(self.ld.guess_syllables("213"),1)
        except: s.append(2)

        print '\nNumber of failed guess_syllables tests:', str(len(s))
        if len(s)!=0: print 'Failed guess_syllables tests:', ','.join([str(x) for x in s])

    def test_apostrophe(self):
        s = []

        self.assertEqual(self.ld.apstrophe_tokenize("I can't wouldn't isn't won't won;t"), ['I', "can't", "wouldn't", "isn't", "won't", 'won', ';', 't'])
        
        try: self.assertEqual(self.ld.apstrophe_tokenize("I can't wouldn't isn't won't won;t"), ['I', "can't", "wouldn't", "isn't", "won't", 'won', ';', 't'])
        except: s.append(1)

        print '\nNumber of failed apostrophe tests:', str(len(s))
        if len(s)!=0: print 'Failed apostrophe tests:', ','.join([str(x) for x in s])

    def test_rhyme(self):
        s = []

##        self.assertEqual(self.ld.rhymes("awoke", "broke"), False)
        
        try: self.assertEqual(self.ld.rhymes("dog", "bog"), True)
        except: s.append(1)
        try: self.assertEqual(self.ld.rhymes("eleven", "seven"), True)
        except: s.append(2)
        try: self.assertEqual(self.ld.rhymes("nine", "wine"), True)
        except: s.append(3)
        try: self.assertEqual(self.ld.rhymes("dine", "fine"), True)
        except: s.append(4)
        try: self.assertEqual(self.ld.rhymes("wine", "mine"), True)
        except: s.append(5)
        try: self.assertEqual(self.ld.rhymes("dock", "sock"), True)
        except: s.append(6)
        try: self.assertEqual(self.ld.rhymes("weigh", "fey"), True)
        except: s.append(7)
        try: self.assertEqual(self.ld.rhymes("tree", "debris"), True)
        except: s.append(8)
        try: self.assertEqual(self.ld.rhymes("niece", "peace"), True)
        except: s.append(9)
        try: self.assertEqual(self.ld.rhymes("read", "need"), True)
        except: s.append(10)
        try: self.assertEqual(self.ld.rhymes("dog", "cat"), False)
        except: s.append(11)
        try: self.assertEqual(self.ld.rhymes("bagel", "sail"), False)
        except: s.append(12)
        try: self.assertEqual(self.ld.rhymes("wine", "rind"), False)
        except: s.append(13)
        try: self.assertEqual(self.ld.rhymes("failure", "savior"), False)
        except: s.append(14)
        try: self.assertEqual(self.ld.rhymes("cup", "duck"), False)
        except: s.append(15)
        try: self.assertEqual(self.ld.rhymes("og", "bog"), True)
        except: s.append(16)
        try: self.assertEqual(self.ld.rhymes("awoke", "broke"), True)
        except: s.append(17)

        print '\nNumber of failed rhyme tests:', str(len(s))
        if len(s)!=0: print 'Failed rhyme tests:', ','.join([str(x) for x in s])

    def test_syllables(self):
        s = []
        try: self.assertEqual(self.ld.num_syllables("dog"), 1)
        except: s.append(1)
        try: self.assertEqual(self.ld.num_syllables("asdf"), 1)
        except: s.append(2)
        try: self.assertEqual(self.ld.num_syllables("letter"), 2)
        except: s.append(3)
        try: self.assertEqual(self.ld.num_syllables("washington"), 3)
        except: s.append(4)
        try: self.assertEqual(self.ld.num_syllables("dock"), 1)
        except: s.append(5)
        try: self.assertEqual(self.ld.num_syllables("dangle"), 2)
        except: s.append(6)
        try: self.assertEqual(self.ld.num_syllables("thrive"), 1)
        except: s.append(7)
        try: self.assertEqual(self.ld.num_syllables("fly"), 1)
        except: s.append(8)
        try: self.assertEqual(self.ld.num_syllables("placate"), 2)
        except: s.append(9)
        try: self.assertEqual(self.ld.num_syllables("renege"), 2)
        except: s.append(10)
        try: self.assertEqual(self.ld.num_syllables("reluctant"), 3)
        except: s.append(11)

        print '\nNumber of failed syllables tests:', str(len(s))
        if len(s)!=0: print 'Failed syllables tests:', ','.join([str(x) for x in s])

    def test_examples(self):

        a = """
a woman whose friends called a prude
on a lark when bathing all nude
saw a man come along
and unless we are wrong
you expected this line to be lewd
        """

        b = """while it's true all i've done is delay
in defense of myself i must say
today's payoff is great
while the workers all wait
"""

        c = """
this thing is supposed to rhyme
but I simply don't got the time
who cares if i miss,
nobody will read this
i'll end this here poem potato
"""

        d = """There was a young man named Wyatt
whose voice was exceedingly quiet
And then one day
it faded away"""

        e = """An exceedingly fat friend of mine,
When asked at what hour he'd dine,
Replied, "At eleven,     
At three, five, and seven,
And eight and a quarter past nine"""

        f = """A limerick fan from Australia
regarded his work as a failure:
his verses were fine
until the fourth line"""

        g = """There was a young lady one fall
Who wore a newspaper dress to a ball.
The dress caught fire
And burned her entire
Front page, sporting section and all."""

        h = "dog\ndog\ndog\ndog\ndog"

        i = """Technic back in time was so broke
Everyone think computer is just a joke
but machine learning grow
make everybody know
the new time of era has awoke"""

        s = []

##        self.assertEqual(self.ld.is_limerick(a), True)

        try: self.assertEqual(self.ld.is_limerick(a), True)
        except: s.append('a')
        try: self.assertEqual(self.ld.is_limerick(b), False)
        except: s.append('b')
        try: self.assertEqual(self.ld.is_limerick(c), False)
        except: s.append('c')
        try: self.assertEqual(self.ld.is_limerick(d), False)
        except: s.append('d')
        try: self.assertEqual(self.ld.is_limerick(e), True)
        except: s.append('e')
        try: self.assertEqual(self.ld.is_limerick(f), False)
        except: s.append('f')
        try: self.assertEqual(self.ld.is_limerick(g), True)
        except: s.append('g')
        try: self.assertEqual(self.ld.is_limerick(h), False)
        except: s.append('h')
        try: self.assertEqual(self.ld.is_limerick(i), True)
        except: s.append('i')

        print 'Number of failed limerick tests:', str(len(s))
        if len(s)!=0: print 'Failed limerick tests:', ','.join(s)

if __name__ == '__main__':
    unittest.main()