#!/usr/bin/python

# An implementation of:
# http://xkcd.com/936/

import random
import optparse
import re
import os

re_non_lower = re.compile('[^a-z]')
def read_words(filename, min_len, max_len):
    words = []
    fin = file(filename,'r')
    for line in fin:
        line = line.strip()
        if re_non_lower.search(line):
            # only use lowercase words
            continue
        if min_len is not None and len(line) < min_len:
            continue
        if max_len is not None and len(line) > max_len:
            continue
        words.append(line)
    return words

def parse_options():
    p = optparse.OptionParser()
    p.add_option('-d', '--dictionary', default='/usr/share/dict/words',
                 help='Dictionary for words')
    p.add_option('-l', '--length', default=4, type='int',
                 help='Number of words to pick')
    p.add_option('-n', '--number', default=10, type='int',
                 help='Number of choices to offer')
    p.add_option('-m', '--min', default=None, type='int',
                 help='Minimum word length to use')
    p.add_option('-x', '--max', default=None, type='int',
                 help='Maximum word length to use')
    p.add_option('-g', '--grid', default=False, action='store_true',
                 help='Show as a word grid')
    opts, args = p.parse_args()
    return opts

opts = parse_options()
if not os.path.exists(opts.dictionary):
    raise SystemError, "Couldn't find dictionary, specify --dictionary (default /usr/share/dict/words)"

all_words = read_words(opts.dictionary, opts.min, opts.max)
if not all_words:
    raise SystemError, "Oops, we didn't get any words to pick from - check your dictionary and any length limits (--min, --max)"

if len(all_words) < 1000:
    print "Warning: we didn't find many words: %d" % len(all_words)

max_word_length = max([len(x) for x in all_words])
for i in xrange(0, opts.number):
    password = [ random.choice(all_words) for i in xrange(0, opts.length) ]
    if opts.grid:
        password = [ ('%%-%ds' % max_word_length) % x for x in password ]
    print ' '.join(password)
    
            
    
