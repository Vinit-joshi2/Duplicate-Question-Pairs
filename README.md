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



  
