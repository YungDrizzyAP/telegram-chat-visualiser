
# Telegram Chat WordCloud Generator


A simple tool to visualise the most used words in a Telegram conversation using a word cloud.

## Chat export:
https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDQ4YTVmNDVhZGRiYjUyYzg4M2JjMjhlOGJiMTA2NGQ3ZDQ1MDNmNiZjdD1n/i1xuotA9kCiWvatubE/giphy.gif
## Installation



```bash
  cd telegram-chat-visualiser
  pip install -r requirements.txt
```
    


## Usage/Examples
To use the script, run it from the command line, passing the input JSON file as a parameter. For example:
```python
python script.py result.json
```
By default, the script will generate a WordCloud with the 150 most common words, with a width of 1280 pixels and a height of 720 pixels. The WordCloud will be saved as a PNG file named 'my_wordcloud.png' in the same directory as the input file.

You can customize the output by using the following optional parameters:

-n or --num_words: The number of most common words to display in the WordCloud (default is 150)

-w or --width: The width of the WordCloud (default is 1280)

-h or --height: The height of the WordCloud (default is 720)

-o or --output_file: The output file name for the WordCloud PNG (default is 'my_wordcloud.png')

## Example
```python
python script.py result.json -n 200 -w 1920 -h 1080 -o my_chat_wordcloud.png

```
