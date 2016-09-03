"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    count = {}
    for word in s.split(' '):
        count[word] = count.get(word,0) + 1
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top_n = count.items()
    top_n = sorted(top_n, key=lambda tup: tup[0])
    top_n = sorted(top_n, key=lambda tup: tup[1], reverse=True)
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n[:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()

