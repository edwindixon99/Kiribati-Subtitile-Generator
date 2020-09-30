import collections
import re
import sys
import time


# Convert a string to lowercase and split into words (w/o punctuation)
def tokenize(string):
    return re.findall(r'\w+', string.lower())


def count_ngrams(lines, min_length=5, max_length=10):
    lengths = range(min_length, max_length + 1)
    ngrams = {length: collections.Counter() for length in lengths}
    queue = collections.deque(maxlen=max_length)

    # Helper function to add n-grams at start of current queue to dict
    def add_queue():
        current = tuple(queue)
        for length in lengths:
            if len(current) >= length:
                ngrams[length][current[:length]] += 1

    # Loop through all lines and words and add n-grams to dict
    for line in lines:
        for word in tokenize(line):
            queue.append(word)
            if len(queue) >= max_length:
                add_queue()

    # Make sure we get the n-grams at the tail end of the queue
    while len(queue) > min_length:
        queue.popleft()
        add_queue()

    return ngrams


def print_most_frequent(ngrams, num=30):
    for n in sorted(ngrams):
        print('----- {} most common {}-grams -----'.format(num, n))
        for gram, count in ngrams[n].most_common(num):
            print('{0}: {1}'.format(' '.join(gram), count))
        print('')


start_time = time.time()
with open('total.txt') as f:
    ngrams = count_ngrams(f)
print_most_frequent(ngrams)
elapsed_time = time.time() - start_time
print('Took {:.03f} seconds'.format(elapsed_time))
