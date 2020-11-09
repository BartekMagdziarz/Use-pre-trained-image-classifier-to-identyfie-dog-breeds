#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Bartek Magdziarz
# DATE CREATED: 5/11/2020                   
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for keys (image files names) and values (extracted and formatted pet labels)
    pet_labels_dict = {}
    
    
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for i in range(0, len(in_files)):
                   
    # Skips file if starts with . (like .DS_Store of Mac OSX) because it isn't an pet image file
        if in_files[i][0] != ".":
             
    # Uses split to extract words of filename into list image_name 
            image_name = in_files[i].split("_")

    # Creates empty string for pet label to be extracted and formatted from image_name               
            pet_label = ""
                   
    # Processes each of the character strings(words) split by '_' in 
    # list image_name by processing each word - only adding to pet_label
    # if word is all letters - then process by putting blanks between 
    # these words and putting them in all lowercase letters  
            for word in image_name:
     
    # Only add to pet_label if word is all letters add blank at end
                if word.isalpha():
                    pet_label += word + " "
    
    # strips off trailing whitespace                   
            pet_label = pet_label.strip().lower()
            print(pet_label)
    # If filename doesn't already exist in dictionary add it and it's
    # pet label - otherwise print an error message because indicates 
    # duplicate files (filenames)
            if in_files[i] not in pet_labels_dict:
                pet_labels_dict[in_files[i]] = [pet_label]
            else:
                print("Warning, duplicate files exists in the directory", in_files[i])
        
        
              
    # Replace None with the results_dic dictionary that you created with this
    # function
    return pet_labels_dict
