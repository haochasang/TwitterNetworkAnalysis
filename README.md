# TwitterNetworkAnalysis
This project is a Demo project I did to consolidate my knowledge on graph theory and social network analysis. The focus of this project is to study the structure of the data science community on Twitter. The project is consist of two parts, network influencer detection and topic modeling.

The steps taken to identify KOLs are the following.  

- Downloaded 200+ tweets using Twitter API and save the tweets in a json file.
- Extracted the authors of the tweets and used these accounts as seeds to find which accounts they are following.
- Created a graph based on the follower-followee relationships and studied the structure of the network.
- Identify users with high betweenness centrality as network influencers.

The steps taken to detect topics are the following.

- Used the same tweets as the first part and extracted only the text data.
- Built a pipeline to clean the text data.
- Studied the correlation between hashtags and used a heatmap to visualize the results.
- Used topic detection algorithms (LDA & NMF) to find topics that people in data science community are most frequently discussing about.

This project contains the following files:

* The `TweetRead.py` script is used to download tweets containing the keyword "DataScience" via Twitter Search API.
* The `GetFriends.py` script is used to get the authers of the tweets and find their "friends" on Twitter.
* The `TweetText.py` script is used to get only the text part of the tweets and save the results to a csv file.

* The `tweets_DataScience.json` file is the output of `TweetRead.py`. It contains all the tweets downloaded.
* The `userList.txt` file is the output of `GetFriends.py`. It contains all the follower-followee pairs.
* The `TweetText.csv` file is the data output of `TweetText.py`. it contains the raw text of all tweets.

* The `NetworkAnalysis.ipynb` script is the main script for part one. It creates the network using `networkx` library and find the netwrok influencers.
* The `TweetTopicModeling.ipynb` script is the main script for part two. It applies some basic exploratory data analysis on hashtags and uses LDA & NMF algorithms to generate topcis.

This project requires the following libraries:

* re
* nltk
* pandas
* numpy
* scipy
* operator
* json
* sklearn
* matplotlib
* seaborn
* itertools
* networkx

This project is done by Chelsea He.
