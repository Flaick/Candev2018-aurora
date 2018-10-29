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
└───Candev         
    ├───class2              
    │   ├───candev_data_2_0               
    │   └───candev_data_2_1           
    └───class6              
        ├───candev_data_6_0              
        ├───candev_data_6_1             
        ├───candev_data_6_2          
        ├───candev_data_6_3          
        ├───candev_data_6_4          
        └───candev_data_6_5             
      
## Examples for each level:  
### class2:       
#### candev_data_2_0:        
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class2/candev_data_2_0/00001.png)       
#### candev_data_2_1:        
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class2/candev_data_2_1/00387.png)        

### class6:           
#### candev_data_6_0:    
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class6/candev_data_6_0/00026.png) 
#### candev_data_6_1:    
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class6/candev_data_6_1/00006.png) 
#### candev_data_6_2:    
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class6/candev_data_6_2/00454.png) 
#### candev_data_6_3:     
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class6/candev_data_6_3/00751.png) 
#### candev_data_6_4:    
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class6/candev_data_6_4/00570.png) 
#### candev_data_6_5:        
![Alt text](https://github.com/Flaick/Candev2018-aurora/blob/master/class6/candev_data_6_5/00207.png) 


## After classifying the images we will combine the value of class2 and class6 to calculate the type of the picture!    
