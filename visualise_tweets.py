# --------------------A L L 	I M P O R T S----------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# --------------------A L L 	M E T H O  D S----------------------------------
def get_pickle_df(file_name):
	"""
		Retreive the data frame from pickle file
	"""
	df = pd.read_pickle(file_name)
	return df

def create_bar_date(count_per_date_df):
	plt.style.use('ggplot')
	dates = list(count_per_date_df.iloc[:, 0])
	tweet_counts = list(count_per_date_df.iloc[:, 1])

	for i in range(len(dates)):
		plt.text(x = dates[i], y = tweet_counts[i] + 1.5, s = tweet_counts[i], size = 8, color='blue')

	plt.bar(dates, tweet_counts, color='#ff4d4d')
	plt.fill(color='red')
	plt.xlabel("Dates")
	plt.ylabel("Counts")
	plt.title(" Tweets per day ")
	plt.savefig("./plots/tweets_per_day.png")
	plt.close()

def create_bar(is_positive, is_negative, is_neutral):
	count_pos = 0
	count_neg = 0
	count_neu = 0

	for pos in is_positive:
		if pos == 1:
			count_pos = count_pos + 1

	for neg in is_negative:
		if neg == 1:
			count_neg = count_neg + 1

	for neu in is_neutral:
		if neu == 1:
			count_neu = count_neu + 1

	sentiments = ['Positive', 'Negative', 'Neutral']
	counts = [count_pos, count_neg, count_neu]

	data = {
		'Sentiment': sentiments,
		'Count': counts
	}

	our_df = pd.DataFrame(data)

	print("our_df: " + str(our_df.shape))
	print(counts)

	for i in range(len(sentiments)):
		plt.text(x = sentiments[i], y = counts[i] + 1.5, s = counts[i], size = 8, color='blue')

	plt.bar(sentiments, counts, color="#99ffeb")
	plt.xlabel("Sentiments")
	plt.ylabel("Counts")
	plt.title(" Tweets Sentiments")
	plt.savefig('./plots/tweets_sentiments.png')
	plt.close()



# -------------------- M A I N ----------------------------------
if __name__ == '__main__':
	tweets_df = get_pickle_df('./tweets_df.pkl')
	create_bar(tweets_df.iloc[:, 5], tweets_df.iloc[:, 6], tweets_df.iloc[:, 7])

	count_per_day_df = get_pickle_df('./count_per_day_df.pkl')

	create_bar_date(count_per_day_df)