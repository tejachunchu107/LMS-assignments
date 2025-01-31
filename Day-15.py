#Day 15
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  
    plt.show()
    
    
    wordcloud.to_file('wordcloud_image.png')


text = 'data science machine learning artificial intelligence'
generate_wordcloud(text)
