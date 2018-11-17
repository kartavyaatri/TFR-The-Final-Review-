import string
#from pyspark import SparkConf,SparkContext
#conf = SparkConf ()
#sc = SparkContext(conf = conf)
#rdd_name = sc.textFile("/user/madhur/dataset")
#data=rdd_name.collect()
table = str.maketrans({key: None for key in string.punctuation})

negative = open(r"negative-words.txt",'r',encoding='utf-8')
nwords = negative.read().split("\n")

positive = open(r"positive-words.txt",'r',encoding='utf-8')
pwords = positive.read().split("\n")

counter = 0
c = 0
data = open(r"Park_Plaza.txt",'r',encoding='utf-8')
l = 0
rating = 0
for lines in data:
    lines = lines.translate(table)
    lines = lines.lower()
    words = lines.strip().split()
    counter = 0
    l += 1
    for word in words:
        if word in pwords:
            counter += 1

        elif word in nwords:
            counter -= 1
    if counter > 0:
        c += 1
    elif counter < 0:
        c -= 1
    if counter >= 3:
        rating += 5
    elif counter > 0:
        rating += 4
    elif counter == 0:
        rating += 3
    elif counter <= -3:
        rating += 1
    elif counter < 0:
        rating += 2

percentage=(c/l)*100
rating=rating/l

print("According to our Sentimental Analysis for park plaza hotl based on trip advisor we come to a conclusion that \n Percentage of Positive Reviews ="+str(percentage)+"\n Percentage of Negative Reviews ="+str(100-percentage)+"\n Rating of the Phone = "+str(rating)+"\n\n Total reviews considered : "+str(l))
