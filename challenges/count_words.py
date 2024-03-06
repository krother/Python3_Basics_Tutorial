
import re

# read the file
mobydick = open('moby_dick.txt').read()

# remove crap
mobydick = mobydick.lower()
mobydick = re.sub('[\*\.\!\"\;\?,\d]','',mobydick)
mobydick = re.sub("[\-\(\)\']",' ',mobydick)

# chop it into a list of words.
words = mobydick.split()

out = "Moby Dick contains %8i words."%(len(words))

# count the words in a dictionary
count = {}
for w in words:
    count.setdefault(w,0)
    count[w] += 1

# get a list of sorted word counts
result = []
for w in count:
    result.append( (count[w],w) )
result.sort()
result.reverse()

for count,word in result:
    out += "%5i\t%s\n"%(count,word)
open('words.txt','w').write(out)


