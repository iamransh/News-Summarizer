import tkinter as tk

# Natural Language Toolkit
import nltk

# library for processing textual data
from textblob import TextBlob

# module used for extracting and parsing newspaper articles
from newspaper import Article


def summarize():
    url = utext.get('1.0', "end").strip()

    # downloading Punkt Sentence Tokenizer
    # nltk.download('punkt')

    # url = 'https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html'

    article = Article(url)

    # downloading the news article we passed into url variable
    article.download()

    # (.parse) is used to study or read the article
    article.parse()

    # nlp is used to perform natual language processing
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert(
        '1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disable')
    author.config(state='disable')
    publication.config(state='disable')
    summary.config(state='disable')
    sentiment.config(state='disable')


# for gui
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

# for title
tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disable', bg='#dddddd')
title.pack()

# for author
alabel = tk.Label(root, text="Author/Authors")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disable', bg='#dddddd')
author.pack()

# for publishing date
plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disable', bg='#dddddd')
publication.pack()

# for summary
slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disable', bg='#dddddd')
summary.pack()

# for sentiment analysis
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disable', bg='#dddddd')
sentiment.pack()

# for url
ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# for button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
