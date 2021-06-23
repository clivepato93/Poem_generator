from random import choice
def make_poem():
    nouns=["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
    verbs=["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adjectives=["furry", "balding", "incredulous", "fragrant", "exu-berant", "glistening"]
    prepositions=["against", "after", "into", "beneath", "upon", "for", "in", "like", "over","within"]
    adverbs= ["curiously", "extravagantly", "tantalizingly","furiously", "sensuously"]
    n_nouns=[]
    n_verbs=[]
    n_adjectives=[]
    n_prepositions=[]
    n_adverbs= [choice(adverbs)]
    while len(n_prepositions)!=2:
        d=choice(prepositions)
        if d not in n_prepositions:
            n_prepositions.append(d)
    while len(n_nouns) !=3:
        a=choice(nouns)
        b=choice(verbs)
        c=choice(adjectives)
        if a not in n_nouns and b not in n_verbs and c not in n_adjectives:
            n_nouns.append(a)
            n_verbs.append(b)
            n_adjectives.append(c)
    first_word=["A","An"][n_adjectives[0][0] in "aeiou"]
    first_sentence=f"{first_word} {n_adjectives[0]} {n_nouns[0]}"
    sencond_sentece=f"""{first_sentence} {n_verbs[0]} {n_prepositions[0]} the {n_adjectives[1]} {n_nouns[1]}
{n_adverbs[0]} the {n_nouns[0]} {n_verbs[1]}"""
    third_sentece=f"the {n_nouns[1]} {n_verbs[2]} {n_prepositions[1]} a {n_adjectives[2]} {n_nouns[2]}"
    print(first_sentence)
    print("\n")
    print(sencond_sentece)
    print(third_sentece)

make_poem()
