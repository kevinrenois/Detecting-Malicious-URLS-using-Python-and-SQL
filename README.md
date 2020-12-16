# Detecting Malicious URLS using Python and SQL

#### Kevin Renois


---
## Problem Statement 

Malicious URLs are one of the biggest categories of threats to cybersecurity for companies and consumers. They can infect or attack in a veriaty of different ways, be it through malware, phishing, command-and-control, etc. For this project, I'd like to determine if machine learning can be used with Natural Language Processing (NLP) and SQL Databses to accurately calssify malicious and benign URLS.

My Goal is to create a model that can make these distinctions and to deploy that model in a Flask app.

## Executive Summary

I successfully created a tool that uses SQL to query a database of labled URLs to determine if a user's input is known to be malicious or benign. If the user's input is not in the database, the tool then uses the predictive model I built in Python to classify the url as probably being malicious or probably being benign. 

the model I created was primarily NLP based and it tested with 98% accuracy score. I wanted to be sure to create a model that minimzes false negatives, and it seems that the model did well in that regard as it scored a 98% in sensitivity (recall).



## Conclusion

The model I created seems to work as intended, and with more data to train on it could perform even better. Machine learning and NLP seem to be useful and powerful tools for classifying malicious and benign URLs.

In the near future I plan to acquire more training data and incorporate more feature vectors into my model to decrease the likely possibilty it being overfit to the particular dataset that I had in hand.

## Sources

[Hidden Fraudulent Dataset](https://machinelearning.inginf.units.it/data-and-tools/hidden-fraudulent-urls-dataset)

[Openphish Dataset](https://www.phishtank.com/developer_info.php)

[Majestic Million Dataset](https://majestic.com/reports/majestic-million?s=999900)

### Papers
[Malicious URL Detection - Chong, Liu](http://cs229.stanford.edu/proj2012/ChongLiu-MaliciousURLDetection.pdf)




