import os
import cv2
import csv
#5824
#assume list_name
'''for filename in list_name:
    im = cv2.imread(filename)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    save_name = ""
    cv2.imwrite("/home")'''
with open('/home/computer/yk/csv_file/class6,5.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    column1 = [row[1] for row in reader]#check if we have value of the class
    print(column1)
    for num in column1[1:]:
        filename = ""+num
        filename = filename.zfill(5)
        filename = "/home/computer/yk/cropped_scaled/" + filename + ".png"
        print("file name is:"+filename)
        if os.path.exists(filename):
            im = cv2.imread(filename)
            print(im)
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            num = num+""
            num = num.zfill(5)
            save_name = "/home/computer/yk/candev/candev_data_6_5/" + num + ".png"
            print("save name is:"+save_name)
            cv2.imwrite(save_name,gray)
