# Gaussian-Mixture-Modeling for Iris & Car Evaluation Datasets

This project used the Iris Dataset I have used previously where K = 3. It contains 150 data points for Sepal width and length and pedal width and length. The three types of flowers are Setosa, Versicolor, Virginica. In programming the Gaussian Mixture model we are trying to differentiate the data into the three flower categories through clustering and density estimation.


*From scikit-learn.org*

*"A Gaussian mixture model is a probabilistic model that assumes all the data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters. One can think of mixture models as generalizing k-means clustering to incorporate information about the covariance structure of the data as well as the centers of the latent Gaussians."*


<img width="657" alt="dm31" src="https://github.com/ianspetnagel/Gaussian-Mixture-Modeling/assets/62821052/e0e35908-94da-43c9-b210-3ab2bd6a68e6">
<img width="650" alt="dm32" src="https://github.com/ianspetnagel/Gaussian-Mixture-Modeling/assets/62821052/e6b05662-5665-4dd1-8772-3fba5956594d">

This GMM produced an accuracy of 96.66 (97%). Each color is a different flower and has clustered them appropriately. I then added another file to compare the above output with the GMM in the Sklearn library to compare the two accuracies.. as you can see it produced the exact same output. Thus the initial output was correct.

<img width="612" alt="dm33" src="https://github.com/ianspetnagel/Gaussian-Mixture-Modeling/assets/62821052/9db2e158-88a1-47b4-bb74-b8370883df71">



