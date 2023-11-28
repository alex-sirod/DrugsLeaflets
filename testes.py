import jellyfish

s1 = 'gigant'
s2 = 'gigant'

if len(s1) > len(s2):
    v = len(s1)
else:
    v = len(s2)

l = jellyfish.levenshtein_distance(s1, s2)


print(f"Maior Valor: {v}")
print(f"TAMANHO 1 \'{s1}\' ", len(s1))
print(f"TAMANHO 2 \'{s2}\' ", len(s2))
print("LEVENSHTEIN", jellyfish.levenshtein_distance(s1, s2))

print(((100/v) * l)/100)


# print("HAMMING", jellyfish.hamming_distance(s1, s2))
# print("JARO", jellyfish.jaro_winkler_similarity(s1, s2))
# print("DAMERAU", jellyfish.damerau_levenshtein_distance(s1, s2))
# print("METAPHONE", jellyfish.metaphone(s1))
# print("SOUNDEX", jellyfish.soundex(s1))
# print("NYSIIS", jellyfish.nysiis(s1))
# print("MATCH RATING CODEX", jellyfish.match_rating_codex(s1))

#
# jellyfish.metaphone('Jellyfish')
#
# jellyfish.soundex('Jellyfish')
#
# jellyfish.nysiis('Jellyfish')
#
# jellyfish.match_rating_codex('Jellyfish')
