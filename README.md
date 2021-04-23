# Political-Polarization
Respository of AI Ethics project, on political polarization in twitter data.

As part of Dr. Malihe Alikhani's CS1699 AI Ethics course, Zhiyi Zhan and I completed a finally project, compiling a data corpus of twitter data consisting of various hashtags that have been present in the news and in popular culture. These will help to train models of Dr. Alikhani's design.

Zhiyi ran a separate examination on Twitter data, using NLP to compare sentiment around the topic of COVID as compared for March of this year to last year.

## How to Run

Clone this repository and run the notebook files described below. The .py file is only for testing purposes and can be disregarded at this time.

## Running AIEthics.ipynb

Run through the import statements and make sure they install correctly. There may be errors with updating Twint. Enter in the phrase you would like to search within the c.Search call, and use c.Limit to get a rough amount. Note, use the example code to return only 100 results- large amounts of results may slow down your computer.

## Running Sentiment.ipynb

The current errors shown is because when I was running them, the file wasn't there. 
The files for processing are COVIDpt1/2/3/4.csv, COVIDMar2021Part1/2/3/4,csv, all located in the folder CSVfiles. They have to be uploaded to the folder sample_data(or other, just change the path). The files get deleted every time the notebook is closed.
