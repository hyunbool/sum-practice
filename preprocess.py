#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:53:23 2021

@author: hbae
"""

import json
import os
import re

def preprocessing(text):
    
    splitted_text = list()


    split_sentence = ""

    text = re.sub("[^ ㄱ-ㅣ가-힣0-9a-zA-Z\.|\?|\!]+", "", text)
    sents = re.split(r"[\?|\.|\!|\n]", text)


    for i in range(len(sents)):
        if sents[i] == "f ":
            pass
        elif sents[i] == None:
            pass
        elif sents[i] == "\n":
            pass
        elif sents[i] == "":
            pass
        elif sents[i] == " ":
            pass
        else:
            if sents[i][0] == " ":
                splitted_text.append(sents[i][1:])
            else:
                splitted_text.append(sents[i])
    
    text = " ".join(splitted_text)
    
    return text
         

def main():
    train_path = "./books/Training/train/"
    train_files = os.listdir(train_path)
    train_files.remove(".DS_Store")
    
    val_path = "./books/Validation/valid/"
    val_files = os.listdir(val_path)
    val_files.remove(".DS_Store")
    
    f = open("train.txt", "a")
    for folder in train_files:
        files = os.listdir(train_path + folder)
        for file in files[:2]:
            
            with open(train_path + folder + "/" + file, encoding='utf-8') as json_file:
                json_data = json.load(json_file)
            passage = preprocessing(json_data["passage"])
            summary = preprocessing(json_data["summary"])
            
            f.write(passage + "\t\t" + summary + "\n")
        
    f.close()
    
    f = open("valid.txt", "a")
    for folder in val_files:
        files = os.listdir(val_path + folder)
        for file in files[:2]:
            with open(val_path + folder + "/" + file, encoding='utf-8') as json_file:
                json_data = json.load(json_file)
            passage = preprocessing(json_data["passage"])
            summary = preprocessing(json_data["summary"])
            
            f.write(passage + "\t\t" + summary + "\n")
            
    f.close()
    
    
    
main()