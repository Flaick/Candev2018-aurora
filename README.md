# Candev2018-aurora
Candev Contest 2018. Classification model.         

This project implements on the Pytorch framework.

'class2' and 'class6' folders contain the dataset used for training two different models.

'model' folder contains the final model for the class2 classification.

class2new.py file contains the procedure of building a model and training the model with dataset.

convert.py file contains the procedure of making our own dataset.

Depends on the time and memory of GPU, we only train one model for 'class2' which is saved in the 'model' folder

The model is built on the Resnet-18

Structure of training data:
'''
+-- class2
|    +--candev_data_2_0
|       +-- data1
|       +-- data2
|    +--candev_data_2_1
'''

'''
+-- class6
|    +--candev_data_6_0
|        +--data1
|        +--data2
|    +--candev_data_6_1
|    +--candev_data_6_2
|    +--candev_data_6_3
|    +--candev_data_6_4
|    +--candev_data_6_5
'''
