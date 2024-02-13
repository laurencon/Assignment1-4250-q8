#-------------------------------------------------------------------------
# AUTHOR: Lauren Contreras
# FILENAME: indexing.py
# SPECIFICATION: This program reads the collection.csv file and then
# outputs the tf-idf document term matrix. It conducts stopword removal,
# stemming, finds the index terms, finds TF, finds IDF, and finally
# builds the matrix.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math
documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"i", "she", "her", "and", "they", "their"}
#this is an empty list that stores documents after stopword removal
docStopwords = []
for document in documents:
    #this splits the document into words and checks if there is a match with the list of stopwords provided
    newdoc = ' '.join([word for word in document.split() if word.lower() not in stopWords])
    docStopwords.append(newdoc)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
#a function to remove certain endings
def stemWord(word):
    ends = ['s', 'es', 'ed', 'ing']
    for end in ends:
        if word.endswith(end):
            return word[:-len(end)]
    return word
#this is an empty list that stores documents after stemming removal
stemming = []
for document in docStopwords:
    #this splits the document into words and applies the function above to each word
    stemming1 = ' '.join([stemWord(word) for word in document.split()])
    stemming.append(stemming1)

#Identifying the index terms.
#--> add your Python code here
terms = set()
for document in stemming:
    for term in document.split():
        terms.add(term)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
#this is an empty list to store TF
docTermMatrix = []
#loop to go over each stemmed document in the stemming list
for document in stemming:
    tf = {}
    #splits the current document's words and counting the total number of terms
    totalTerms = len(document.split())
    #loop to go over each term in the current document
    for term in terms:
        #counts the number of times the term was in the document
        termCount = document.split().count(term)
        tf[term] = termCount / totalTerms
      
    docTermMatrix.append(tf)

idf = {}
#total number of documents in the set
docNum = len(documents)
for term in terms:
    #counts the number of documents where the term is
    docCount = sum(1 for document in stemming if term in document.split())
    idf[term] = math.log10(docNum / docCount)
  

tfidfMatrix = []
for doc in docTermMatrix:
    tfidf = {}
    #this loop goes over each term and its TF in the current document
    for term, tf in doc.items():
        tfidf[term] = tf * idf[term]
    tfidfMatrix.append(tfidf)

#Printing the document-term matrix.
#--> add your Python code here
print("Document-term matrix")
print("--------------------")
for i, document in enumerate(tfidfMatrix):
    print(f"Document {i + 1}:", end = " ")
    for term, tfidf in document.items():
        print(f"Term: {term}, {tfidf:.2f}", end="|")
    print("\n")

