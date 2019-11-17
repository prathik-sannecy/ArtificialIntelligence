Project: HW3 Heart Anomaly

Class: PSU CS 441/541 - Artificial Intelligence (Fall 2019)

Author: Prathik Sannecy

Email: prathik@pdx.edu

Date: 11/17/19

This project provides a solution to the HW3 Heart Anomaly problem (see HW3_Files/README.md). Basically, it classifies whether a heart is abnormal or normal by comparing its features to other known hearts.

Two different classification algorithms were used: Naive Bayesian, and K-Nearest-Neighbors (KNN). They are trained using the training sets HW3_Files/\*.train.csv. They were then tested using the testing sets HW3_Files/\*.test.csv.

Until the training set was formatted to be binarized for maximized information-theoretical gain, Naive Bayesian classification performed much better than KNN. Furthermore, another thing I noticed is that for these datasets, although Naive Bayesian performed much better with identifying 'normal' hearts, KNN performed noticeably better at identifying 'abnormal' hearts. Thus if you are willing to have many more false positives but be able to identify more abnormal hearts, using the KNN algorithm may be a better choice.

Results on my Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz machine (Ubuntu):
Naive Bayesian Algorithm
spect-itg 145/187(0.7754010695187166) 15/15(1.0) 130/172(0.7558139534883721) 
spect-orig 142/187(0.7593582887700535) 10/15(0.6666666666666666) 132/172(0.7674418604651163) 
spect-resplit 78/90(0.8666666666666667) 17/19(0.8947368421052632) 61/71(0.8591549295774648) 
spect-resplit-itg 63/90(0.7) 17/19(0.8947368421052632) 46/71(0.647887323943662) 

K-Nearest-Neighbor Algorithm
spect-itg 102/187(0.5454545454545454) 15/15(1.0) 87/172(0.5058139534883721) 
spect-orig 98/187(0.5240641711229946) 14/15(0.9333333333333333) 84/172(0.4883720930232558) 
spect-resplit 75/90(0.8333333333333334) 14/19(0.7368421052631579) 61/71(0.8591549295774648) 
spect-resplit-itg 64/90(0.7111111111111111) 18/19(0.9473684210526315) 46/71(0.647887323943662) 


To run this program:
python3 HeartAnomolies.py

By default each algorithm is run on each of the 4 different training/testing set pairs.

The output is sent to stdout, you may redirect it to another file from the terminal.



