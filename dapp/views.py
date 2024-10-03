from django.shortcuts import render
from nltk.corpus import wordnet

def index(request):
    md = {}
    if request.method == "POST":
        word = request.POST.get('search')

        synonyms = set()
        antonyms = set()

        synsets = wordnet.synsets(word)
        if synsets:
            meaning = synsets[0].definition()

            for x in synsets:
                for lemma in x.lemmas():
                    synonyms.add(lemma.name())
                    if lemma.antonyms():
                        antonyms.add(lemma.antonyms()[0].name())
        else:
            meaning = "No meaning found"

        limited_synonyms = list(synonyms)[:10]
        limited_antonyms = list(antonyms)[:10]

        md = {
            'word': word,
            'meaning': meaning,
            'synonyms': ", ".join(limited_synonyms) if limited_synonyms else "No synonyms found",
            'antonyms': ", ".join(limited_antonyms) if limited_antonyms else "No antonyms found",
        }

    return render(request, 'indx.html', md)
