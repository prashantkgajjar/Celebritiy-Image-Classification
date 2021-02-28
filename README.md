# Celebritiy Image Classification

The objective here is to create the model that would recognize the face of celebrities. For the sake of simplicity, here the program is trained to identify the face of 5 celebrities.(Aysuhmann Khuranna, Leonardo DiCaprio, Rachel Brosnahan, Tapsee Pannu & Will Smith)

# Approach

Here , OpenCV's haarcascade is used for the purpose of facial recognition. The haarcascade algorithm is collected from the https://github.com/opencv/opencv/tree/master/data/haarcascades .
The Support Vector Machine is used for the facial recognition. The output/accuracy is fair in comparison to what a neural network would give.

Below tasks are done accordingly to complete the project:

1. Gather Data through web scrapping (Fatkun).
2. Using OpenCV for image recognition.
3. Identifying & removing irrelevant or inaccurate images.
4. Feature Engineering (convert the image data to a computer language, so it can be used for Machine Learning) using Wavelets
5. Training the dataset through Machine Learning techniques from scikit-learn libraries.
6. Evaluating the best case ML Techniques and Parameters (Support Vector Machine & Logistic Regression had almost similar results. However, SVM provided slightly better results, so it is preferred here).
7. Saving the Model & Json
8. Creating a Python Flask Server("BackEnd" tasks are done in PyCharm)
9. Creating a webpage(UI) using HTML(Visual Studio Code is used for "FrontEnd" tasks)
10. Deployment of model to production using Amazon Web Services(Amazon EC2 Instance)

**Computer Vision**

It involves seeing or sensing a visual stimulus, make sense of what it has seen and also extract complex information that could be used for other machine learning activities.
***USES::***
- Autonomous Vehicles
- Facial Recognition
- Image Seach & Object Recognition
- Robotics 
#### OPENCV It is an opensourced library which has plenty of algorithms for facial recognition.


# Data Extraction

To download the single images can be difficult task. Also, identifying the images through web scrapping url if not relevant, as Google keeps on optimizing its search engine, and the chances of modifying the search results are high. To safe gaurd this, the data has been scrapped from Google Images with help of Fatkun, for training purpose.

Chances are that these images might include the celibirty face, and also that of another person. This will need to be sorted out first.

# Feature Engineering

## PRE REQUISITES

An image can be processed in two forms, 1> spatial domain(i.e., x-y axis) & 2> frequency domain(waveforms).

Here, the image needs to be transformed into frequecy domain, i.e., it would assume the whites & blacks in the image, and store the information in the form of sinusodial waveform. This waveform, represents the image. However, as the image processing is requires the detailed approach, it becomes difficult to utilize the Fourier Transform. The more useful Wavelet Transform will be used to process the image.

In order for machine to understand the image, the image is processed through Wavelet Transform. Wavelet transform is more advance than that of Fourier Transform. The transformation will sepreate out the image wave form, to different frequecnies, which will give back the more truer waveform.

To simplify, the Fourier Transformation will give back more the original frequecny that that of the image. The original frequecy here is (zeros, and ones). The waveform with zero will represent the blacks and ones will represents the whites.

## The Idea of Wavelets

Wavelets comes as a solution to the lack of Fourier Transformation.

Fourier Transformation is the dot product between real signal and various frequency of sine wave.

We get a stats of frequency but we don't know when that "frequecny" happen, we lost the time resolution of the real signal.

To get both the frequency and time resolution we can be dividing the original signal into the several parts and apply Fourier Transformation to each part. This is called Short Term Fourier Transformation. When applied to partial signal, the Frequency it can catch is just n/2 where n is the length of partial signal assuming the duration of partial signal is 1 second.

### Wavelets

In wavelets, the target of the bigger window is a lower frequecny. This is similar to the Fourier Transformation, because we do dot product between the real signal and some wave form.

The Wavelet translation is how far we can "slide" the window from the starting point.

Fourier Transformation can only have 1 type of transformation, but Wavelet Transformation can have many kinds of transformation.(possibilities are infinite)

#### Classes of Wavelet Transform

Continous Wavelet Transformation(CWT):
CwT is a wavelet trasnformation where we can set the scale and translate the aribitory. ex. Morlet Wavelets, Meyer Wavelets, Mexican Hat Wavelets. CWT will often generate a scaleogram
Discrete Wavelet Transformation(DWT):
DWT is a kind of wavelets which restricts the value of scale and aribitory. The restriction is in the increasing power of 2(a=1,2,4,8,..) and translation is the integer (b=1,2,3,4,...) ex. Haar Wavelets, Daubechis Wavelets(it has a FATHER Wavelets, which determines the scaling)

### Simplifying the above:::

So wavelets are a type of “orthogonal transform”. Orthogonal transforms include variants of Fourier transforms and its cousins. They are “orthogonal” because they involve in “infinite summation” of orthogonal functions. In a Fourier transform these are sine, cosine or complex exponential functions.

The feature of orthogonality allows terms of unequal indices to cancel out in the calculation process of finding the transform which radically simplifies the calculation of an “infinite sum” from being horribly and impractically infinite to merely tractably infinite which calculus handles easily.

A wavelet is just a type of orthogonal function. But the nature of a wavelet means there is no one unique function that can be used, unlike trig-based Fourier transforms. Each valid orthogonal function that is “wavelet-like” is called a “mother wavelet”.

For wavelets - there are multiple orthogonal “mother” wavelet functions and each type could have an advantage in some way ranging for representation accuracy/power, economics of use or simplicity of calculation.

# Data Training

As mentoned before, the intention of the model is to not use Deeplearning techniques to identify the Images. And hence, SVM is used here to make sure the classification of the images are done accordingly. The another classification model (Logistic Regression) was also showing good accuracy, but here SVM is preffered.

# Deployment of Server & its UI

## USER INTERFACE
![S1](https://user-images.githubusercontent.com/74737545/109414564-861f6280-79d9-11eb-9827-79f2a5f68b4a.jpg)

## ERROR
![S2](https://user-images.githubusercontent.com/74737545/109414566-8a4b8000-79d9-11eb-90cd-17ac3f21317b.jpg)

## SUCCESS
![S3](https://user-images.githubusercontent.com/74737545/109414569-8ddf0700-79d9-11eb-97fa-4439ee30e8b1.jpg)




