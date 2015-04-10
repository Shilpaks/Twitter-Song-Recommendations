import pytest
import keyword_extracting_algorithms
import twitter_data 

# content of test_sample.py

def test_correct_output(): 
	correct_output = ['This is a tweet about me being excited!', "I'm so excited!", 'Just signed up for Twitter!']
	td = twitter_data.twitter_data('testuser242')
	actual_output = td.twitter_data_wrapper()
	assert correct_output==actual_output