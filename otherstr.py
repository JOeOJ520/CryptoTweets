def user_name(tweets):
  from simple_tokenize import simple_tokenize
  from nltk.stem import PorterStemmer
  st = PorterStemmer()

  commonfile = open("CS431FP/CommonEnglishWord.txt", 'r')
  commonword = [line.strip() for line in commonfile .readlines()][20]

  return tweets.select("user_name").rdd.flatMap(lambda x: simple_tokenize(x[0])).\
  map(lambda x: st.stem(x)).filter(lambda x: x not in commonword).\
  map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).\
  sortBy(lambda x: x[1],ascending = False)

def user_location(tweets):
  import pycountry
  def get_country(x):
    for country in pycountry.countries:
      if country.name in x:
        return country.name
    return "others"
  return tweets.select("user_location").rdd.map(lambda x: (get_country(x[0]),1))\
  .reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], ascending = False)

def user_verified(tweets):
  def cleaning(x):
    if x not in ["True","False"]:
      return "Others"
    else: return x
  return tweets.select("user_verified").rdd.map(lambda x: cleaning(x[0])).map(lambda x: (x,1)).\
  reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], ascending = False)

def hashtags(tweets):
  from simple_tokenize import simple_tokenize
  from nltk.stem import PorterStemmer
  st = PorterStemmer()

  commonfile = open("CS431FP/CommonEnglishWord.txt", 'r')
  commonword = [line.strip() for line in commonfile .readlines()][20]

  def cleaning(x):
    if "dog" in x:
      return 'dogecoin'
    elif "bit" in x or "btc" in x:
      return 'bitcoin'
    elif "ntf" in x:
      return "ntf"
    elif "cov" in x:
      return "covid"
    elif "crypto" in x:
      return "cryptocurrency"
    elif "eth" in x:
      return "etherenum"
    elif "bnb" in x:
      return "binanc"
    else: return x

  return tweets.select("hashtags").rdd.flatMap(lambda x: simple_tokenize(x[0])).\
  map(lambda x: st.stem(x)).filter(lambda x: x not in commonword).\
  map(lambda x: (cleaning(x),1)).reduceByKey(lambda x,y: x+y).\
  sortBy(lambda x: x[1],ascending = False)

def source(tweets):
  from simple_tokenize import simple_tokenize

  def cleaning(x):
    if x not in ["Twitter for Android","Twitter Web App","Twitter for iPhone"]:
      return "Others"
    else: return x
  return tweets.select("source").rdd.map(lambda x: cleaning(x[0])).map(lambda x: (x,1)).\
  reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], ascending = False)

def is_retweet(tweets):
  def cleaning(x):
    if x not in ["True","False"]:
      return "Others"
    else: return x
  return tweets.select("is_retweet").rdd.map(lambda x: cleaning(x[0])).map(lambda x: (x,1)).\
  reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], ascending = False)
