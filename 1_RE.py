import re
text = """
Benicia is learning regular expressions. Her email is benicia@example.com.
She was born on 02/14/2001 and her phone number is +1-234-567-8901.
Her favorite hashtag is #coding and her website is https://benicia.dev.
"""
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print("Emails found:", emails)
date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
dates = re.findall(date_pattern, text)
print("Dates found:", dates)
phone_pattern = r'\+?\d{1,2}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)
hashtag_pattern = r'#\w+'
hashtags = re.findall(hashtag_pattern, text)
print("Hashtags found:", hashtags)
url_pattern = r'https?://[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\S*'
urls = re.findall(url_pattern, text)
print("URLs found:", urls)
