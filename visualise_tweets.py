# --------------------A L L 	I M P O R T S----------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# --------------------A L L 	M E T H O  D S----------------------------------
def get_tweets(file_name):
	"""
		Retreive the data frame from pickle file
	"""
	tweets_df = pd.read_pickle(file_name)
	return tweets_df


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

	plt.bar(sentiments, counts)
	plt.xlabel("Sentiments")
	plt.ylabel("Counts")
	plt.show()



# -------------------- M A I N ----------------------------------
if __name__ == '__main__':
	tweets_df = get_tweets('./tweets_df.pkl')
	print("shape: " + str(tweets_df.shape))

	create_bar(tweets_df.iloc[:, 5], tweets_df.iloc[:, 6], tweets_df.iloc[:, 7])