
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for ch in word:
        if ch in punctuation_chars:
            word = word.replace(ch, "")
    return word

def get_neg(text):
    count = 0
    for word in text.split():
        if strip_punctuation(word).lower() in negative_words:
            count += 1
    return count

def get_pos(text):
    count = 0
    for word in text.split():
        if strip_punctuation(word).lower() in positive_words:
            count += 1
    return count

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


            
full_data = []
source = open("project_twitter_data.csv", "r")
lines = source.readlines()[1:]
for row in lines:
    lst = row.strip().split(',')
    tweet_data = {}
    positive_score = get_pos(lst[0])
    negative_score = get_neg(lst[0])
    tweet_data["retweets"] = lst[1]
    tweet_data["replies"] = lst[2]
    tweet_data["positive"] = positive_score
    tweet_data["negative"] = negative_score
    tweet_data["net"] = positive_score - negative_score
    full_data.append(tweet_data)    
source.close()

outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for tweet in full_data:
    row_string = "{},{},{},{},{}".format(tweet["retweets"],tweet["replies"],
                                         tweet["positive"],tweet["negative"],tweet["net"])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
