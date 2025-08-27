# Duplicate-Question-Pairs
<p>
  The goal of this project is to predict which of the provided pairs of questions contain two questions with the same meaning. The ground truth is the set of labels that have been supplied by human experts. The ground truth labels are inherently subjective, as the true meaning of sentences can never be known with certainty. Human labeling is also a 'noisy' process, and reasonable people will disagree. As a result, the ground truth labels on this dataset should be taken to be 'informed' but not 100% accurate, and may include incorrect labeling. We believe the labels, on the whole, to represent a reasonable consensus, but this may often not be true on a case by case basis for individual items in the dataset.
</p>

# Our Goal
- To predict which of the provided pairs of questions contain two questions with the same meaning
- Applying TF-Idf Teachnique
- Applying BOW Technique
- Advance Feature Engeneering

## Requirements

- **Python Libraries**:
  - `pandas`, `numpy`, `matplotlib`, `seaborn` , `sklearn`
- **Kaggle API Key** (for data downloading)

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Install Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Kaggle API, download the data  and follow the steps to load
   
    - Run this command on any code editor
     ```
     !pip install opendatasets
   ```

   
    - Once you install library then run below command  for loading data into your editor for that you need to pass your kaggle credentials
      
   ```
       import opendatasets as od
       url = "https://www.kaggle.com/c/quora-question-pairs/data
       od.download(url)
   ```

## Exploratory Data Analysis

<p>
  Duplicate questions data
</p>

<img src =  "img1">

<p>
  Null value in datset
</p>

<img src =  "img2">

<p>
  Distribution of Duplicate and Non-duplicate questions
</p>

<img src =  "img3">

<img src =  "img5">

<p>
  Percentage Distribution of Duplicate and Non-duplicate questions
</p>

<img src =  "img4">

<p>
  repeated question
</p>

<img src =  "img6">

<img src =  "img7">

  - As per our histogram unique question are in our datset are 10^5 ~ 5 lakhs
  - There is one question in our dataseyt which is repeated 120 times
  - If we carryfully look at graph,Seems like there is one question which is almost repeated ~156 times
  - Most of the question in our datset are repeated approx 20 or 60 times

## TF-IDF

```
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(
    analyzer = "word" ,
    stop_words = ("english") ,
    ngram_range = (2,2) ,
    max_features = 3000,
    binary = True

)

q1_arr  , q2_arr = np.vsplit(tfidf.fit_transform(question).toarray() , 2)
```

```
print(tfidf.get_feature_names_out())
print(tfidf.idf_)
```

<img src = "img8">

<p>
  Now let's train Random Forest , XGBoost and Decision Tree model
</p>

<img src = "img9">

  - XGBoost achieved the highest accuracy (0.7965), slightly outperforming Random Forest (0.7935), which shows both ensemble methods are effective with TF-IDF features.
  - Decision Tree had the lowest accuracy (71.82%) as a single tree tends to be less robust and more make overfitting or underfitting problem.


## Bag-of-words

<img src = "img10">

```
from sklearn.feature_extraction.text import CountVectorizer
# merge texts
questions = list(ques_df["question1"]) + list(ques_df["question2"])

cv = CountVectorizer(max_features=3000)
q1_arr  , q2_arr = np.vsplit(cv.fit_transform(questions).toarray() , 2)

# 3000 featurename
cv.get_feature_names_out()

```

<img src = "img11">


## BOW - Basic features / Feature Engneering

<img src = "img12">

<p>
  Now this are all the new feature we will create from our existing columns
</p>

<p>
  Let's see the distribution of target column
</p>

<img src = "img13">

  - 63.376667 % data in our dataset is Non-duplicate questions data
  - 36.623333 % data in our dataset is duplicate questions data

<img src = "img14">
<p>
  This all our new feature we created from existing columns
</p>

  
## BOW - BOW Preprocessing and advanced features

<p>
  Let's add few more new feature
</p>

<p>
1. Token Features
  - cwc_min: This is the ratio of the number of common words to the length of the smaller question
  - cwc_max: This is the ratio of the number of common words to the length of the larger question
  - csc_min: This is the ratio of the number of common stop words to the smaller stop word count among the two questions
  - csc_max: This is the ratio of the number of common stop words to the larger stop word count among the two questions
  - ctc_min: This is the ratio of the number of common tokens to the smaller token count among the two questions
  - ctc_max: This is the ratio of the number of common tokens to the larger token count among the two questions
  - last_word_eq: 1 if the last word in the two questions is same, 0 otherwise
  - first_word_eq: 1 if the first word in the two questions is same, 0 otherwise
  
2. Length Based Features
  - mean_len: Mean of the length of the two questions (number of words)
  - abs_len_diff: Absolute difference between the length of the two questions (number of words)
  - longest_substr_ratio: Ratio of the length of the longest substring among the two questions to the length of the smaller question

3. Fuzzy Features
  - fuzz_ratio: fuzz_ratio score from fuzzywuzzy
  - fuzz_partial_ratio: fuzz_partial_ratio from fuzzywuzzy token_sort_ratio: token_sort_ratio from fuzzywuzzy
  - token_set_ratio: token_set_ratio from fuzzywuzzy
</p>

