# Gaussian-Mixture-Modeling for Iris & Car Evaluation Datasets

DL 3

**Part 1**

This first part of the project (IanSpetnagelGMMIrisDataset) uses the Iris Dataset I have used previously where K = 3. It contains 150 data points for Sepal width and length and pedal width and length. The three types of flowers are Setosa, Versicolor, Virginica. In programming the Gaussian Mixture model we are trying to differentiate the data into the three flower categories through clustering and density estimation.


*From scikit-learn.org*

*"A Gaussian mixture model is a probabilistic model that assumes all the data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters. One can think of mixture models as generalizing k-means clustering to incorporate information about the covariance structure of the data as well as the centers of the latent Gaussians."*


<img width="657" alt="dm31" src="https://github.com/ianspetnagel/Gaussian-Mixture-Modeling/assets/62821052/e0e35908-94da-43c9-b210-3ab2bd6a68e6">
<img width="650" alt="dm32" src="https://github.com/ianspetnagel/Gaussian-Mixture-Modeling/assets/62821052/e6b05662-5665-4dd1-8772-3fba5956594d">

This GMM produced an accuracy of 96.66 (97%). Each color is a different flower and has clustered them appropriately. I then added another file to compare the above output with the GMM in the Sklearn library to compare the two accuracies.. as you can see it produced the exact same output. Thus the initial output was correct.

<img width="612" alt="dm33" src="https://github.com/ianspetnagel/Gaussian-Mixture-Modeling/assets/62821052/9db2e158-88a1-47b4-bb74-b8370883df71">


**Part 2**

The second part of this project (IanSpetnagelGMMcardataset) uses the Car Evaluation Dataset. I again will compute the Gaussian Mixture Model. To do this I imported the text file into Excel to transform it into a .csv format. I then adjusted the data to be entirely numerical. Previously the data contained text attributes but I adjusted each category to have numerical rankings as listed in the parentheses below. Our “species” are the classes.

<pre>
buying:   vhigh(4), high (3), med(2), low(1).
maint:     vhigh(4), high (3), med(2), low(1).
doors:    2, 3, 4, 5more (considered as 5).
persons:  2, 4, more (considered as 5).
lug_boot: small(1), med(2), big(3).
safety:   low(1), med(2), high(3).
</pre>

*The classes were changed to unacc(0), acc(1), good(2), vgood(3)*

This problem posed several challenges. Due to the dataset being different, the replacement of values took time as did altering lines in the GMM code. Additionally, the system I used for numerically assigning values to text data was not perfect since each category has a different meaning and purpose. Moreover, there are more variables and the data is more scattered than the Iris Dataset, thus the completed GMM has a much lower accuracy percentage of just 51%.


<img width="604" alt="dm34" src="https://github.com/ianspetnagel/Gaussian-Mixture-Modeling/assets/62821052/396cc332-0eec-4109-a1f7-4bb7f7cbdf81">





