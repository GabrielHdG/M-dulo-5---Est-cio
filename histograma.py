from faker import Faker
import pandas as pd
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

fake = Faker()

texto = open("Hirogram.txt", "w+")


def create_rows(num=1):
    output = [{"Nome": fake.name(),
               "Pontuação": random.randint(1, 10)} for x in range(num)]
    return output


data = pd.DataFrame(create_rows(20))
data.to_csv(texto, header=None, index=None, sep=' ', mode='a')
hist = data.hist(bins=3)  # transforma em histograma
plt.show()

wordcloud = WordCloud(width=800, height=800,
                      background_color='white', stopwords=STOPWORDS, min_font_size=10).generate(str(data))

plt.imshow(wordcloud)
plt.axis("off")
plt.show()  # mostra o histograma
