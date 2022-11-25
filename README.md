# AWS-ML-Eval

## Background: 

Many cat owners probably have the question of what they should do when their cat hides somewhere in the house. Cats love hiding in small spaces, such as closets, under the bed, and in storage boxes, which make them feel secure and comfortable. Especially when your cat feels nervous or dangerous, it will disappear immediately from your sight. 

In this project, we decide to evaluate whether Amazon Rekognition has the ability to detect cats and help cat lovers find their missing cats in the house. Amazon Rekognition as a cloud based software is able to identify objects, people, text, scenes, and activities in images and videos. Amazon Rekognition has two API sets: Amazon Rekognition Image for image analysis and Amazon Rekognition Video for video analysis. In this project, We are gonna test the Image API. 

Specifically, Amazon Rekognition Image API analyzes source images by assigning labels to varying elements within the picture. A label is defined as an object, scene, action or concept in the image or video based on the content. The Amazon Rekognition Image applies a hierarchical taxonomy of ancestor labels to identify and classify labels. 

## API: 

Nowadays, human-face recognition is pretty well-developed and has a wide variety of use cases. For example, Amazon Rekognition has a strong facial recognition capability, providing facial analysis, face comparison, and face search capabilities with high accuracy. Users can detect, analyze, and compare faces for different uses, including user verification, cataloging, people counting, and public safety. In general, face recognition applies AI algorithms and Machine Learning to search and capture human facial features from the background. Then, the processes require further confirmation to validate it is a human face. The confirmation process uses a large dataset, including both positive and negative images (positive images are normal images; on the other hand, negative images are images where lightest areas are changed to the darkest and the darkest areas appear as the lightest). Beside facial features, the face-recognition process also includes detailed elements and objects such as hats and glasses. However, it is unclear whether object recognition will take various detailed elements into account. Thus, this project uses different pictures of Icy Wang and Jenny Zhang’s cats to evaluate the Amazon Rekognition API. 

Amazon Rekognition Image API is able to detect labels in pictures. A label is defined as an object, scene, action or concept in the image or video based on the content. The Amazon Rekognition Image applies a hierarchical taxonomy of ancestor labels to identify and classify labels. In our process of recognition experiment, we are going to identify the labels in the picture of Icy’s cat. 

## Method: 

The first step is to collect pictures of two cats using the iPhone 12 Pro series. We have selected 76 qualified images to test in the algorithms. The two cats in our data are both 2-year-old domestic shorthair with weights around 10 lb. We curated a dataset of cat pictures which captures two domestic shorthairs in various modes and statuses. There are pictures of them playing, sleeping, hiding, staring, standing posture and et cetera. 

<img src="https://qtm350project.s3.amazonaws.com/1191667592682_.pic.jpg" alt="drawing" width="600"/>

<img src="https://qtm350project.s3.amazonaws.com/1271667592693_.pic.jpg" alt="drawing" width="600"/>

<img src="https://qtm350project.s3.amazonaws.com/IMG_0699.jpg" alt="drawing" width="600"/>

They also vary in the parts of cat shown, such as whole cat, only head, body, tail, or feet. The dataset is further modulated for their qualities where we performed color inversion, rotation (60, 90, and 180 degrees, for more data variation not for differentiation), crop shuffling, and blurring (mean and motion, for more data variation not for differentiation). Through these different methods of image modulation, we intend to compare the recognition confidence across these treatment groups and determine the accuracy of AWS cat Rekognition.

## Metric: 

We will use the original pictures as baseline, and any confidence values which are different from this value of all treatment group will be the indicators of higher or lower ML accuracy. 

## Expectation & Hypotheses: 

We expect our manipulations of these pictures to simulation the distortions of real world picture. Therefore, the mean confidence of the baseline should be the largest. Then, manipulations with less shape change, including inverse and rotate will give us relatively higher confidence, which should be lower than the baseline. In the end, blur and crop&shuffle are expected to give us the least mean confidence because we think shape distortions make it harder for AWS Rekognition to accurately recognize the cat. 

Since labeling API has not been specifically trained to identify cats, we expect a lower efficacy compared to that of human faces. To test the overall efficacy of cat recognition capability, we will build on the original data set and experiment.

The first variable of study is “Coloration”. We performed color inversion on the original dataset, simulating the color shifts of colors. This variable will explore how the different colorations of the same content may lead to difference in the machine’s learning capabilities.

The second variable studies “Rotation” of images. The algorithm rotates all images for 60, 90, and 180 degrees, creating a treatment group of rotated images. This serves to simulate the situation in real world where images are not taken in the upright posture, also replicating times when cats are not in the upright posture or maybe have knocked over the camera taking pictures. With the assumption that the model is trained with more upright figure of cats, the rotation treatment may behave less confident than un-treated control.

For the third variable, we will explore “Cut and shuffle” where the images are cut into four pieces and random reassembled back together. This introduces incomplete parts of cats in the image where a full body may be cropped into tail and feet separately. We hypothesize that this treatment will behave worse than “rotation” or “coloration” treatment groups do for parts are identification of partial cats can be a hard task for human beings.

Lastly, we will test the fourth variable, “blurring”. This treatment group has picture blurred so that the edges of cats are less distinguishable. This simulates the occasions of unclear images taken. Similarly, we expect that AWS Rekognition will perform worse with blurred images since it partially relies on the outline of objects to determine labels. 

Together, we predict that these four treatment groups of image modulation will lead to worse performance. With further testing and experimentation, we will determine the extent to which these variables affect AWS Rekognition’s learning is capable of.

## Structure: 

Here is an architectural map of our model. To construct this model, we create a sagemaker notebook, in which we apply the code uploaded to github repo. The github code involves Amazon SDK for Python (Boto3) with Amazon Rekognition, which helps us detect and display elements in the images. The cat images are uploaded and stored them in the Amazon S3 bucket, a public cloud storage that enables us to store and retrieve the data throughout the project. All of these will be reflected on the notebook as a Machine learning service, and the user will be able to use this machine learning service to further generate outputs. 

![Structure img](./img/resources/structure.jpg)

The notebook is tested to run under AWS Sagemaker using pytorch supported kernal with python version higher than 3.7.
