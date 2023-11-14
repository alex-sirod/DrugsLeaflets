
def concordance(source, word, context=20):
    """
    Print out a concordance for ``word`` with the specified ``context``.

    :param source: the source text
    :param word: the target word
    :param context: the amount of context on each side of the target word

    """
    for sent in source.sents:
        if word in sent.text:
            pos = sent.text.index(word)
            left = sent.text[:pos].rstrip()
            right = sent.text[pos + len(word):].lstrip()
            print(f'{left[-context:]} {word} {right[:context]}')