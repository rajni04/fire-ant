from newspaper import Article
from news import table as news_table

WORD_COUNT = "word_count"


def read_article(url):
    a = Article(url)
    a.download()
    a.parse()
    a.nlp()
    print("\n", a.title, "\n")
    print(a.text)
    word_count = 0
    i = input("Is reading complete?")
    if i == "y":
        a_word_count = len(a.text.split())
        try:
            news_table.insert(url, a.text, a_word_count)
            with open(WORD_COUNT, "r") as f:
                try:
                    word_count = int(f.readline())
                except ValueError:
                    word_count = 0

            word_count = word_count + a_word_count
            with open(WORD_COUNT, "w") as f:
                print("Article:", a_word_count, "Total:", word_count)
                f.write(str(word_count))
        except Exception as e:
            print(e)
