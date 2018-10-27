from itertools import permutations
import random, urlparse

#TODO: a service that would periodically cache permutations of characters

class Shortener():
    # Shortened URLs should not be guessable
    # a simple iteration across every permutation of the 
    # available characters they have as the URLs come in
    # that would be the best user experience

    def __init__(self):

        self.perms = None
        #self.available_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789"
        # combos not having the same characters will ensure two
        # permutations are not same
        self.char_combos = ["aDgjM", "bEhkN", "cFilP"] 
    
    def genPermutations(self):
        self.perms = []
        for i in range(0, len(self.char_combos)):
            self.perms.append([''.join(p) for p in permutations(self.char_combos[i])])

    def getURLToken(self):
        start = random.randint(0, len(self.char_combos)-1)
        end = random.randint(0, 120-1)
        value = self.perms[start][end]
        #pop once assigned
        self.perms[start].remove(value)
        return value

    def checkIfValid(self, url):
        try:
            result = urlparse.urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    # Custom URL can be at max 12 characters
    # and min 3 chars
    def customShortURL(self, url, custom):
        #check custom for certain constraints
        if len(str(custom)) < 3:
            return "Select a URL with atleast 3 characters"
        if len(str(custom)) > 12:
            return "Select a URL with less than 12 characters"
        return custom