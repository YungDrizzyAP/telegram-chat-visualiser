import argparse
import json
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# parse command line arguments
parser = argparse.ArgumentParser(description='Generate a WordCloud from Telegram chat data JSON file')
parser.add_argument('input_file', type=str, help='the input JSON file')
parser.add_argument('--num_words', type=int, default=150, help='number of most common words to display in the WordCloud')
parser.add_argument('--width', type=int, default=1280, help='width of the WordCloud')
parser.add_argument('--height', type=int, default=720, help='height of the WordCloud')
parser.add_argument('--output_file', type=str, default='my_wordcloud.png', help='output file name for the WordCloud PNG')
args = parser.parse_args()

# read the JSON data and extract the messages
with open(args.input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

messages = []
for message in data['messages']:
    if 'text' in message:
        text = message['text']
        if isinstance(text, str):
            text = re.sub(r'[^\w\s]+|[\d]+|<[^>]+>', '', text)
            messages.append(text.strip()) # Strip leading/trailing whitespace

# Remove the 'from' field from each message
for i in range(len(messages)):
    if ': ' in messages[i]:
        message_parts = messages[i].split(': ', 1)
        if len(message_parts) > 1:
            messages[i] = message_parts[1]
        else:
            messages[i] = message_parts[0]

# convert the list of messages to a single string
text = ' '.join(messages)

# read the stopword lists for both English and Russian languages
en_stopwords = set(stopwords.words('english'))
ru_stopwords = set(stopwords.words('russian'))

# tokenize the text into words
words = nltk.word_tokenize(text)

# remove stopwords from both English and Russian languages
filtered_words = [word.lower() for word in words if word.lower() not in en_stopwords and word.lower() not in ru_stopwords]

# calculate word frequency distribution
fdist = nltk.FreqDist(filtered_words)

# get the most common words
most_common_words = fdist.most_common(args.num_words)

# create a WordCloud object
wordcloud = WordCloud(width=args.width, height=args.height, background_color='black')

# generate the word cloud using the most common words
wordcloud.generate_from_frequencies(dict(most_common_words))

# plot the word cloud using Matplotlib
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)

# save the plot as a PNG file with the provided name
output_file = args.output_file if args.output_file else 'my_wordcloud.png'
wordcloud.to_file(output_file)