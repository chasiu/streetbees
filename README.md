# README
## Requirements
All the code was written with Python 3.8.1

To install requirements
```bash
python3 -m pip install requirements.txt
```

To run the service locally a mongo database needs to be set up for the logging and a DB_URI environment variable created. Once that is complete to run the app run the following from a termina/powershell from the app folder. 
```
python3 app.py
```


## Data Exploration
[Notebook](notebooks/data_exploration.ipynb)

The main goal with the explorationw as to try and get an understanding if there was some noticeable difference between the structure of the names that could be exploited and to look for outliers.

There were some noticeable hard to categorise examples such as the album (). 

## Model Exploration
[Notebook](notebooks/model_experiments.ipynb)

In the end I settled for a MultiNomial Naive Bayes model. During all my experiments with different models using a BoW methods it performed well and was much faster at training than any other method I tried. I did also look at K-Nearest Neighbours during my investigation but it failed to scale to such a large dataset as expected. 

If I had more time I would have looked at using another vectorisation method than BoW as can be seen from the results I was not able to see much improvement even with playing with the various parameters during the vectorisation. Word embeddings using a pre-trained model could have been used to maybe give a better understanding of the themes in Names and I think would have likely performed better at dealing with the more "artistic" categories of Album/Film/WrittenWork. On the other hand as a lot of classes are simple people/place names I don't think this would have performed better overall.

As it was not often intutive to tell the differences between the classes I think a Neural Network model may have been the way to go. They tend to be good at spotting relationships in the data that are not as obvious to the human eye. Steps would need to be taken to avoid overfitting as I feel this is a particular task that is very easy to create an overfitted model for. Neural networks also have the disadvantage of being relatively hard to explaint he decision process - often referred to as "black box" models. Whilst I don't think this is a major issue for this particular task it is something to keep in mind when using them.

## Cloud Service
The model is hosted on heroku - https://radiant-brushlands-37405.herokuapp.com

There is a simple UI for querying the model as well as an API - https://radiant-brushlands-37405.herokuapp.com/api/v1/names/classify?name=car 
To query simple change the parameter after ?name= in the URL or call via postman/similar. This hosted version also stores all the queries made to it in a mongo atlas cluster. The goal here would be to investigate how the model is getting queried over time and make changes as required - such as adding a new class.

With more time here I would have liked to add a feedback loop for consumers to confirm the model prediction was correct/wrong. This can then be used to update the training data going forward.
## Unit Tests
There are some unit tests for the text processing scripts [here](text_processing.py)
