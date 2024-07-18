
#Multiclass Classification using Logistic Regression
'''
Confusion matrix:
    created to know their performance on test data
    created in case of Logistic Regression, SVM, KNN or Random Forest models
'''
#handwritten digit recognition using multiclass logistic regression
#call load_digits() to import sklearn digts data set
from sklearn.datasets import load_digits
digits=load_digits()
#display the names of the cols in bunch object
dir(digits)
# digits.data
# digits.target
#display the no.of rows and cols n the dataset
digits.data.shape #(1797, 64)
 #data[] is represntation of array of the image
 #images[] is the corresponding immage
 #target[] is the actual digit
 
 
#to display 8th image aray
digits.data[8]
 
#to display corresponding image graphic
import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[8])

#let us see the correct numeric digit of the above image
digits.target[8]  #it is 8

# we can use the data and target fot training the model
# let us split the training and testing data
from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test=train_test_split(digits.data, digits.target, test_size=0.3)

#train the model.
#x_train = array of handwritten digits
#y_train = digit

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train, y_train)
#accuracy
model.score(x_train, y_train)


#let us take a random sample for prediction
# this is an image of a digit
plt.matshow([digits.data[67]])

#the corresponding data for this image is data[67]
#let us supply this data for out model -> gives 6
model.predict([digits.data[67]])

#waht is the actual digit?
digits.target[67] #6

#one more prediction: ;et us predict the digits for data [30:35]
#fives array([0, 9, 5, 5, 6])
digits.target[30:35]

#to view the above images
plt.gray()
for i in range(30,35):
    plt.matshow(digits.images[i])

#create confusion matrix
y_predicted=model.predict(x_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_predicted)
cm

#to display the confusion matrix in the form of heatmap
import seaborn as sns 
plt.figure(figsize=(10, 7)) # width and height in inches
sns.heatmap(cm, annot=True)
plt.xlabel('Truth value')
plt.ylabel('Predicted value')



#predict handwritten image:
#import pillow and numpy packages 
from PIL import Image, ImageOps 
import numpy as np

# load image from the folder. L for grayscale image 
img = Image.open(r"C:/test/four-small.png").convert('L')
img

# invert the colors. Black into white and vice versa 
img_inverted = ImageOps.invert(img)
img_inverted
# if needed, display inverted image 
import matplotlib.pyplot as plt 
plt.matshow(img_inverted)

# convert image into an array - gives 2D array 
arr = np.array(img_inverted) 
arr

# convert above 2D array into 1D array for prediction 
arr1 = arr.flatten() 
arr1

# let the model predict which image it is 
model.predict([arr1]) # array([4])

