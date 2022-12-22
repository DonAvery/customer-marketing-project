# Markeing Promotion Classifier
This repsoitory contains all the necessary information to run a classification model. Using Jupyter Notebooks, python scripts, BentoML and docker allow you to access and test this information.  It is also part of my ML-Zoomcamp Capstone Project.

## Environment
I run my machine learning proejcts on a standalone Ubuntu PC using conda. These instructions are meant for an Ubuntu system and I believe they should work on macOS. I have included items so that you may create them on a Windows machine, but I can't guarntee they will work.

## Data and Inention

The dataset was pulled from Kaggle here: https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign

The target feature in this dataset is the `response` column. This column denotes if a customer responed to the last marketing campaign. We want predict which customers might repsond to a marketing campaign in the future.

Several models were used in this Jupyter Notebook:

- Logistic Regression
- Decision Tree
- Ensemble and Random Forest
- XGBoost

## Model Parameter Tuning
- Decision Tree - tuned `max_depth` and `min_samples_leaf`
- Ensemble and Random Forest - tuned `n_estimators`, `max_depth` and `min_samples_leaf`
- XGBoost - tuned `num_boost_rounds`, `eta`, `max_depth` and `min_child_weight`

## To run the project

Create a folder where you will clone the github repository into

Clone this repository


Run `conda env create -f environment.yml'

Use the requirements.txt to install dependencies

Change directory to the customer-marketing-project folder

Start a jupyter notebook and open "Data-Prep-Clean-EDA.ipynb" to view the data ingestion, data prepe and EDA.

Open the "Model-Training-Tuning-and-Selection.ipynb" to see the tuning and training.

The Best Model & BentoML Save.ipynb is what I created a python script from. You can either run this notebook or run the customer-marketing.py file to create the benmol model.

When ready for deployment run the Best Model & BentoML Save notebook.

After running the BentoML notebook you can start setting up the deployment.

Run bentoml build inside the folder with the files from the files directory.

Run bentoml containerize <tag> the tag will be given to you after the build.

Run docker run -it --rm -p 3000:3000 <tag> serve --production, this line will be given after docker run, copy and paste it.

Copy the json from the locustfile.py and use http://0.0.0.0:8089 to post that json file into the get portion of the page and see the results.
