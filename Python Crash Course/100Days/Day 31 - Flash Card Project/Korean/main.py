import pandas
# Flash Card Program - Time to learn Korean

# Check the wiki for the most frequently used words in other languages - https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800
# Check HermitDave for usable language files - https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
# Language Codes for Google Translate - https://cloud.google.com/translate/docs/languages?hl=en

# Taking a .txt file and converting it to a .csv
# Japanese
ja_to_csv = pandas.read_csv("D:/Work/Crash Course Collection/Python Crash Course/100Days/Day 31 - Flash Card Project/ja_50k.txt", sep=' ')
ja_to_csv.to_csv('output_ja.csv', index=False)

# Korean
ko_to_csv = pandas.read_csv("D:/Work/Crash Course Collection/Python Crash Course/100Days/Day 31 - Flash Card Project/ko_50k.txt", sep=' ')
ko_to_csv.to_csv('output_ko.csv', index=False)
