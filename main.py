average = 0
iterated = 0
import django
from django.conf import settings
from django.template import Template, Context
import http.server
import socketserver
import os
import re
import random
from random import randint
import requests
from bs4 import BeautifulSoup
import json
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import keyboard
from groq import Groq
from datetime import datetime
from keras.models import load_model
htmltext = ""
main_a = ""
main_b = ""
main_c = ""
main_d = ""
main_e = ""
ingred_a = ""
ingred_b = ""
ingred_c = ""
ingred_d = ""
ingred_e = ""
instruc_a = ""
instruc_b = ""
instruc_c = ""
instruc_d = ""
instruc_e = ""
nutr_a = ""
nutr_b = ""
nutr_c = ""
nutr_d = ""
nutr_e = ""
ports = random.randint(1024, 49151)
PORT = ports
# settings.configure(
#     DEBUG=True,
#     INSTALLED_APPS=[],
#     DATABASES={
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': 'mydatabase',
#         }
#     },
#     TEMPLATES=[
#         {
#             'BACKEND': 'django.template.backends.django.DjangoTemplates',
#             'DIRS': [],
#             'APP_DIRS': True,
#             'OPTIONS': {
#                 'context_processors': [
#                     'django.template.context_processors.debug',
#                     'django.template.context_processors.request',
#                     'django.contrib.auth.context_processors.auth',
#                     'django.contrib.messages.context_processors.messages',
#                 ],
#             },
#         },
#     ],
# )
# # django.setup()

# # # Template rendering test
# # template = Template('Hello {{name}}!')
# # context = Context({"name": "Peter & Mary"})

# # # Check if context is valid
# # print("Context:", context)

# # Attempt to render and print the template output
# html_output = template.render(context)
# print("Rendered Template:", html_output)
# print(html_output)
ingredientf = ""
namef = ""
cook_timef = ""
yield_valuef = ""
nutritionf = ""
ingredientsf = ""
instructions = []
jlist = []
jalist = []
rankedl = []
rankedk = []
#the lord is great all the glory goes to our savior#
jcheckej = ""
javerage = ""
approv_da = ""
approv_item = ""
approv = []
approvt = []
dundun = 0
nfacts = [] 
nutchk = ""
irisrec = []
ysure = ""
chk = 0
randostat = 0
ingreci = ""
yes_no = ""
detect_a = ""
detect_b = []
item_list = []
inputed = 0
raw_pred = 0
item_connections = {}
sites = ['https://www.allrecipes.com/recipes/16588/salad/vegetable-salads/caprese-salad/']
#, 'https://www.allrecipes.com/recipes/251/main-dish/sandwiches/', 'https://www.allrecipes.com/recipes/1564/breakfast-and-brunch/eggs/frittata/', 'https://www.allrecipes.com/recipes/15167/everyday-cooking/vegetarian/main-dishes/pizza/', 'https://www.allrecipes.com/recipes/16588/salad/vegetable-salads/caprese-salad/'
jdf = pd.read_csv("required7.txt")
features = jdf.iloc[:, 0]  # Assuming first column contains the text data

# Create a TextVectorization layer
vectorize_layer = tf.keras.layers.TextVectorization(max_tokens=1000, output_mode='int')

# Adapt the layer to the text data
vectorize_layer.adapt(features.values)  # This step builds the lookup table

# Ensure the adapt() function completes before vectorizing the data
# Apply the TextVectorization layer to transform the text into integers
features_vectorized = vectorize_layer(features.values)

# Now you have the vectorized representation as a tensor of numbers
#print(features_vectorized)
#Ingredients: 
# ['Tomato, roma', 
# 'Tomatoes, canned, red, ripe, diced', 
# 'Oil, olive, extra virgin', 
# 'Onions, red, raw', 
# 'Spinach, mature', 
# 'Cheese, mozzarella, low moisture, part-skim', 
# 'Peaches, yellow, raw', 
# 'Garlic, raw', 
# 'Celery, raw', 
# 'Peppers, bell, green, raw']
# Ingredients: 
#['Tomato, roma', 
# 'Tomato Sauce',
# 'Oil, olive, extra virgin', 
# 'Cheese, mozzarella, low moisture, part-skim', 
# 'Cheese, feta',

####### #######

# 'Bread, white, commercially prepared', 
# 'Peppers, bell, red, raw', 
# 'Spinach, mature', 
# 'Flour, raw', 
# 'Egg']
infrac = 0
# Create an iterator from the list
sites_iterator = iter(sites)
ulr = ""
ulr2 = ""
doneso = ""
reciso = ""
detectb = []
# import tensorflow as tf
# import tensorflow_text as text#
#import the lord's will
succe = 0
totae = 0
ratee = 0
title_a = ""
title_b = ""
title_c = ""
title_d = ""
title_e = ""
print("Find Nutritious Recipes from Pantry Items!")
recipefilter = []
fob = []
fod = ""
vari_total = []
ingr_total = []
gob = []
gose = ""
ingredlist = ["Milk", "Sausage", "Beans", "Apple", "Cheese", "Mushroom", "Egg", "Beef", "Tomato", "Chicken", "Oil", "Fish", "Yogurt", "Flour", "Pork", "Potato", "Lettuce", "Nuts", "Cabbage", "Seeds", "Applesauce", "Banana", "Beets", "Blueberries", "Bread", "Broccoli", "Butter", "Carrot", "Cauliflower", "Celery", "Cherries", "Collards", "Cookie", "Crab", "Cream", "Cucumber", "Eggplant", "Fig", "Frankfurter", "Garlic", "Grains", "Grapes", "Ham", "Hummus", "Kale", "Ketchup", "Kiwi", "Lentils", "Melon", "Mustard", "Nectarine", "Oats", "Olive", "Onion", "Orange", "Peach", "Pear", "Peas", "Pepper", "Pickles", "Pineapple", "Raspberries", "Rice", "Salsa", "Salt", "Sauce", "Shrimp", "Spinach", "Squash", "Strawberries", "Sugar", "Turkey"]
inputs = ingredlist
vari1 = ""
vari2 = ""
vari3 = ""
vari4 = ""
vari5 = ""
vari6 = ""
vari7 = ""
vari8 = ""
vari9 = ""
vari10 = ""
vitA = 0.3
vitB1 = 0.4
vitB2 = 0.433
vitB3 = 5.333
vitB5 = 1.667
vitB6 = 0.433
vitB7 = 10
vitB9 = 1.333
vitB12 = 0.8
vitC = 30
vitD = 0.005
vitE = 5
vitK = 40
vitCh = 183.333
minCa = 333.333
minCl = 766.667
minCr = 11.667
minCu = 3
minF = 1.333
minI = 0.05
minFe = 2.667
minMg = 140
minMn = 0.767
minMo = 0.015
minP = 233.333
minK = 1566.667                                               
minSe = 0.018
minNa = 766.667
minS = 283.333
minZn = 3.667
vitA_list = [
    "Vitamin A"
    "Vitamin A, RAE",
    "Vitamin A, RE",
]
vitB1_list = ["Thiamin",
    "Thiamin, intrinsic",
    "Thiamin, added",]
vitB2_list = ["Riboflavin",
    "Riboflavin, intrinsic",
    "Riboflavin, added",]
vitB3_list = ["Niacin",
    "Niacin from tryptophan, determined",
    "Niacin equivalent N406 + N407",
    "Niacin, intrinsic",
    "Niacin, added",]
vitB5_list = ["Pantothenic acid"]
vitB6_list = ["Vitamin B-6",
    "Vitamin B-6, N411 + N412 + N413",]
vitB7_list = ["Biotin",]
vitB9_list = ["Folate, total"]
vitB12_list = []
vitC_list = ["Vitamin B-12",
    "Vitamin B-12, intrinsic",
    "Vitamin B-12, added",]
vitD_list = ["Vitamin D (D2 + D3)"]
vitE_list = ["Vitamin E"]
vitK_list = ["Vitamin K (Menaquinone-4)",
    "Vitamin K (Dihydrophylloquinone)",
    "Vitamin K (phylloquinone)"]#addition for this one ONLY
vitCh_list = ["Choline, total"]
minCa_list = ["Calcium, Ca"]
minCl_list = ["Chlorine, Cl"]
minCr_list = ["Chromium, Cr"]
minCu_list = ["Copper, Cu"]
minF_list = ["Fluoride, F"]
minI_list = ["Iodine, I"]
minFe_list = ["Iron, Fe"]
minMg_list = ["Magnesium, Mg"]
minMn_list = ["Manganese, Mn"]
minMo_list = ["Molybdenum, Mo"]
minP_list = ["Phosphorus, P"]
minK_list = ["Potassium, K"]
minSe_list = ["Selenium, Se"]
minNa_list = ["Sodium, Na"]
minS_list = ["Sulfur, S"]
minZn_list = ["Zinc, Zn"]
calcheck = 0
prtcheck = 0
crbcheck = 0
fatcheck = 0
fibcheck = 0
sarcheck = 0
inicrbcheck = crbcheck
iniprtcheck = prtcheck
inifatcheck = fatcheck
inisarcheck = sarcheck
inifibcheck = fibcheck
inicalcheck = calcheck
checkej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck])
weightsa = np.array([0.2, 0.15, 0.15, 0.1, 0.1, 0.1])
parame = 0
parame2 = 0
#the lord can do all! glory to Him
vitmin = [vitA, vitB1, vitB2, vitB3, vitB5, vitB6, vitB7, vitB9, vitB12, vitC, vitD, vitE, vitK, vitCh, minCa, minCl, minCr, minCu, minF, minI, minFe, minMg, minMn, minMo, minP, minK, minSe, minNa, minS, minZn]
with open('requirements copy.txt', 'r') as file:
    file_contents = file.read()
#PRAISE THE LORD
with open('requirements777.txt', 'r') as file:
    file_contents2 = file.read()
#PRAISE THE LORD
client = Groq(
    api_key="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",
)
#PRAISE THE LORD
df = pd.read_csv("requirements777.txt")
#PRAISE THE LORD
model2_path = r"C:\Users\nickc\Downloads\my_modelsv7.h5"
if os.path.exists(model2_path):
    print("File exists.")
else:
    print("File does not exist.")
model2 = tf.keras.models.load_model(model2_path, compile=False)
model2.compile(optimizer='adam', loss='mean_absolute_error', metrics=tf.keras.metrics.MeanAbsoluteError())
df = df.drop(columns=["data_type", "food_category_id", "publication_date"])
weights = np.array([0.2, 0.15, 0.15, 0.1, 0.1, 0.1])
def carbcheck(calcheck, crbcheck):
    # Scale based on the percentage
    parame = crbcheck/calcheck
    if parame >= 0.7:  # This represents 50% in your original scale
        return 0
    elif parame == 0:  # This represents 70% in your original scale
        return 0
    elif parame == 0.5:  # This represents 70% in your original scale
        return 1
    crbcheck = parame # Mapping from 0.5 to 0
    if crbcheck > 0.5:
        crbcheck = 0.7 - crbcheck
        crbcheck = crbcheck * 5
    else:
        crbcheck = parame * 2
    return crbcheck
def fatfcheck(calcheck, fatcheck):
    parame = fatcheck/calcheck
    if parame >= 0.4:
        return 0
    elif parame == 0:  
        return 0
    elif parame == 0.25:  
        return 1
    fatcheck = parame 
    if fatcheck > 0.25:
        fatcheck = 0.4 - fatcheck
        fatcheck = fatcheck * 7 
    else:
        fatcheck = parame * 2.5
    return fatcheck
def sgarcheck(sarcheck):
    if sarcheck == 10:
        return 1
    if sarcheck == 0 or sarcheck >= 20:
        return 0
    if sarcheck >= 10:
        sarcheck = 20 - sarcheck
        sarcheck = sarcheck/10
        return sarcheck
    elif sarcheck < 10:
        sarcheck = sarcheck/10
        return sarcheck
def protcheck(prtcheck):
    if prtcheck >= 17:
        return 1
    else:
        prtcheck = prtcheck/17
        return prtcheck
def fibecheck(fibcheck):
    if fibcheck >= 10:
        return 1
    else:
        fibcheck = fibcheck/10
        return fibcheck
def calocheck(calcheck):
    if calcheck == 750:
        return 1
    elif calcheck == 0 or calcheck > 1500:
        return 0
    if calcheck < 750:
        calcheck = calcheck/750
        return calcheck
    if calcheck > 750:
        calcheck = 1500 - calcheck 
        calcheck = calcheck/750
        return calcheck

# model = tf.keras.Sequential([
#     tf.keras.layers.Input(shape=(None,), dtype='int32'),  # Input layer for the vectorized text
#     tf.keras.layers.Embedding(input_dim=1000, output_dim=64),  # Embedding layer
#     tf.keras.layers.GlobalAveragePooling1D(),  # Pooling layer
#     tf.keras.layers.Dense(32, activation='relu'),  # Dense hidden layer
#     tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
# ])

# features = "180, 17, 221, 18, 12, 750]" #0.57
# features = eval(features)
# features = np.array(features).reshape(1, -1)
# predictions = model.predict(features)
# print("Scale: ", predictions)
# # features = "[158, 34, 37, 9, 3, 111]" #0.44
# # features = eval(features)
# # features = np.array(features).reshape(1, -1)
# # predictions = model.predict(features)
# # print("Scale: ", predictions)

#For training purposes#[140, 22, 135, 6, 5, 536]
crbcheck = 180
prtcheck = 10
fatcheck = 63
sarcheck = 8
fibcheck = 10
calcheck = 457
dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
jcheckej = str(dcheckej)
crbcheck = (carbcheck(calcheck, crbcheck))
prtcheck = (protcheck(prtcheck))
fatcheck = (fatfcheck(calcheck, fatcheck))
sarcheck = (sgarcheck(sarcheck))
fibcheck = (fibecheck(fibcheck))
calcheck = (calocheck(calcheck))
ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck])
average = np.average(ncheckej, weights=weightsa)
# javerage = str(average)
# jlist.append(javerage)
# jalist.append(jcheckej)
# #print(approv)
print(average)
# approv_da = str(approv)
# approvt.append(approv_da)
# approv.clear()
#print(ncheckej)
#print(average)
jcheckej = f"'{jcheckej}'"
#print(f"{jcheckej}, {javerage}")
# for item in jlist:
#     print(item)
# for item in jalist:
#     print(item)
# n_jlist = np.array(jlist).astype(float)
# print("Max: ", np.max(n_jlist, axis = 0))
# print("Mean: ", np.mean(n_jlist, axis = 0))     
# print("Min: ", np.min(n_jlist, axis = 0))          
# #PRAISE THE LORD
# dafa = []
# df = df["fdc_id"]
# print(df)
###
# for i in range(len(df)):
#     daf = df.values[i]
#     daf = int(daf)
#     dafa.append(daf)

# adf = pd.read_csv("soup3.txt", low_memory=False)
# adf = adf[adf["fdc_id"].isin(dafa)]
# #adf = adf.to_string(index=False)
# #print(adf)

# file_path = r"C:\Users\nickc\Downloads\the_lord_works.csv"
# print(file_path)
# adf.to_csv(path_or_buf=file_path, sep=',', na_rep='', float_format=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', lineterminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)

# # Check if the file exists
# if os.path.exists(file_path):
#     print(f"File saved successfully at: {file_path}")
# else:
#     print("File not found.")

# # #used to help make data more efficient (9/27/2024)/ update database (10/2/2024)
#removed fodd += 1 (when on 5th item)
fodd = 1
#
for i in range(10):
    print(f"Iteration {i}")
    cola = 0
    fod = input("Name a food! Since we want a nutritious meal, pick something healthy from your pantry. ")
    #fod = random.choice(inputs)
    #print(fod)
    fob.append(fod)
    ingr_total.append(fod)
    start_time = datetime.now()
    while True:
        chat_completion = client.chat.completions.create(
        messages=[

            {
                "role": "user",
                "content": "Here's a broad food ingredient. \n" + fod + "\n If the word is misspelled, fix the spelling and write nothing else. Capitalize the first letter if it isn't already, and simplify the item if possible. As an example, if the response was cow's milk, just write milk. Do not write anything else, including the original input. If it's already spelled correctly, only capitalize the first letter if needed and do nothing else. If the word is perfectly spelled and capitalized, don't change anything else. Keep the word as is. If something like Oranges or Blueberries is not in plural form, change it to be so. However, if something like Onion, Pepper, or Apple is in plural form, change it to its singular form. For example: Peppers becomes Pepper and Nut becomes Nuts. Do the least change possible, and don't change an ingredient to a similar one (e.g. Cheese stays Cheese, not Milk). If the food item doesn't work and it seemed to be formatted correctly, change it from plural to non-plural and vice versa."
            }
        ],
        model="llama3-8b-8192",
    )
#
        goe = (chat_completion.choices[0].message.content)
        gose = str(goe)
        # print(gose)
        ndf = df.loc[df["food"] == goe]
        ndf = ndf[ndf['food'] == goe]
        ndf.reset_index(drop=True, inplace=True)
        # print(len(ndf))
        fod_lower = fod.lower()
        # ysure = input("Is this what you were looking for? Lowercase x for no. ")
        # if ysure == "x":
        #     infrac += 1
        #     ndf = ""
        if not ndf.empty:
            infrac = 0
            break
        else:
            infrac += 1
        #     chat_completion = client.chat.completions.create(
        #     messages=[

        #         {
        #             "role": "user",
        #             "content": "I see it didn't work. \n" + fod + "\n If there was an s at the end, try removing it (Peppers to Pepper). If it doesn't work, and if there isn't an s at the end, try adding it. (Blueberry to Blueberries). If there are any spelling issues, apply that first. Do not write anything else but the fixed food item. If the plural doesn't work, always switch to the singular. If the singular doesn't work, always switch to the plural. Do not change it in any other way. For example, do not change Mushrooms to Milk, or Blueberry to Milk.",
        #         }
        #     ],
        #     model="llama3-8b-8192",
        # )
        # #
        #     #print(chat_completion.choices[0].message.content)
        #     goe = (chat_completion.choices[0].message.content)
        #     gose = str(goe)
        #     # print(gose)
        #     ndf = df.loc[df["food"] == goe]
        #     ndf = ndf[ndf['food'] == goe]
        #     ndf.reset_index(drop=True, inplace=True)
        #     # print(len(ndf))
        #     fod_lower = fod.lower()
        #     if not ndf.empty:
        #         infrac = 0
        #         break
            
            # print("Infractions: ")
            # print(infrac)
            if infrac > 7:
                ingr_total.remove(fod)
                fod = input("That food item wasn't in the database. Try a different food. ")
                ingr_total.append(fod)
                infrac = 0
            if fod in inputs:
                print('failed')
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": "This ingredient is in the database, which means it was incorrectly formatted. Try again.",
                        }
                    ],
                    model="llama3-8b-8192",
                )

    # print(fodd)
    print(f"List the column # of {goe} that you have in your pantry.")
    
    print(ndf)
    #print(goe)
#please god i pray to you i have faith amen
    #gog = input("Don't forget to insert the correct number! ")
    #add shortcut to get column
    #needed for AI automation
    inputed = input("Only numbers are allowed. ")
    while True:
        if not re.match("^\d+$", inputed):
            inputed = input("Remember, only list the column. ")
        else:
            break
    while True:
        try:
            inputed = int(inputed)
        except ValueError as ve:
            inputed = input("Remember, only list the column. ")
            inputed = int(inputed)
        else:
            if inputed >= len(ndf) or inputed < 0: 
                inputed = input("The column # was not found. Try again. ")
            else:  
                break
  
    gog = ndf["fdc_id"].values[inputed]
    # for i in range (len(ndf.index)):
    #     goa = ndf["fdc_id"].values[i]
    #     goa = str(goa)
    #     gob.append(goa)
    #     #print(gob)
    # gof = random.choice(gob)
    # gof = int(gof)
    # print(gof)
    #gog = df.loc[df['fdc_id'] == gof, 'fdc_id'].values[0]
    goh = int(gog)
    vari = df.loc[df['fdc_id'] == goh, 'description'].values[0]
    gob.clear()
    #gob.clear()

    if fod in inputs:
        inputs.remove(fod)
    else:
        print(f"Item {fod} not found in the list.")
##
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "Here's some data: \n" + file_contents2 + "\n Using this new data, create a list of the food columns that would be in each row of the database. For example, if the data had four items that seemed to be Squash, then the output would be Squash, Squash, Squash, Squash.There can be duplicates if there are multiple items that fit under the same food item. When making the list with all of the food columns, only take the ingredients from the second file into account.",
    #         }
    #     ],
    #     model="llama3-8b-8192",
    # )
    
    # print(chat_completion.choices[0].message.content)
    df = pd.read_csv("soup3.txt", low_memory=False)
    df = df.drop(columns=["id", "data_points", "derivation_id", "min", "max", "median", "footnote", "min_year_acquired"])
    #print(df.query(f"fdc_id == {goh}"))
    #df = pd.read_csv("almighty.txt")
    df = df.query(f"fdc_id == {goh}")
    atr = len(df['nutrient_id'])
    #print(atr)
    atr = int(atr)
    
    df_f = pd.read_csv("soup3.txt", low_memory=False)
    df_n = pd.read_csv("almighty.txt", low_memory=False)
    df_f = df_f.sort_values(by=['nutrient_id'])
    df_n = df_n.sort_values(by=['nutrient_id'])
    df_merged = pd.merge(df_f, df_n, how="inner")
    df_merged = df_merged.query(f"fdc_id == {goh}")
    df_merged = df_merged.sort_values(by=['nutrient_id'])
    df_merged = df_merged.query("nutrient_id.notna()")
    df_merged = df_merged.query("amount > 0")
    df_merged = df_merged.query("unit_name != 'IU'")
    df_merged = df_merged.drop(columns=["id", "data_points", "derivation_id", "min", "max", "median", "footnote", "min_year_acquired", "nutrient_nbr", "rank"])
    df_merged.loc[df_merged['unit_name'] == 'G', 'amount'] *= 1
    df_merged.loc[df_merged['unit_name'] == 'MG', 'amount'] *= 0.001
    df_merged.loc[df_merged['unit_name'] == 'UG', 'amount'] *= 0.000001
    df_merged.loc[df_merged['unit_name'] == 'KCAL', 'amount'] *= 1
    print(df_merged.columns)
    df_merged = df_merged.drop(columns=["unit_name"])
    print(df_merged[["amount", "name"]])
    print("Food #: ")
    print(fodd)
    print(vari)
    vari_total.append(vari)
    if fodd == 10:
        df_j = df_merged
        frames = [df_a, df_b, df_c, df_d, df_e, df_f, df_g, df_h, df_i, df_j]
        vari10 = vari
        result = pd.concat(frames)
        #print(result)
        dones = [vari1, vari2, vari3, vari4, vari5, vari6, vari7, vari8, vari9, vari10]
        #print(fob)
        #ingr_total.append(fob)
        #fob.clear()
        ulr = sites[0]
        response = requests.get(ulr)
        
        print("FINAL:")
        for x in range(len(dones)):
            print (dones[x]),

# Send a GET request to fetch the data
    

    # Check if the request was successful (status code 200)


    # # Step 1: Fetch the HTML content
    # url = "https://www.bonappetit.com/recipes"
    #response = requests.get(url)   
#
    # Check if the response is successful
    if fodd == 10:
        targ = 1
        ulr = next(sites_iterator)
        while True:
            ulr = ulr  # Ensure 'ulr' contains a valid URL
            print(ulr)
            response = requests.get(ulr)

            if response.status_code == 200:
            # Step 2: Parse the HTML using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Step 3: Find the script tag that contains the JSON-LD data
                json_ld_tag = soup.find('script', type='application/ld+json')
                #
                if json_ld_tag:
                    # Extract the JSON-LD content
                    json_ld_content = json_ld_tag.string
                    
                    # Step 4: Parse the JSON content
                    json_ld_content = json_ld_tag.string.strip()
                    json_data = json.loads(json_ld_content)
                    
                    # Step 5: Now you can work with the extracted JSON data
                    #print(json.dumps(json_data, indent=4))  # Pretty-print the JSON data
                else:
                    print("No JSON-LD script found on the page.")
            else:
                print(f"Failed to fetch the webpage. Status code: {response.status_code}")

                        # Define 'url' properly. For example, use 'ulr' if that's the intended variable

            #print(url)
            print(response.headers['Content-Type'])
            #print("Response content:", response.text)
            if response.status_code == 200:
                try:
                    data = response.json()
                    #print("Parsed JSON data")
                except requests.exceptions.JSONDecodeError:
                    #print("Failed to parse JSON. Response is not valid JSON.")
                    #print("Response content:", response.text)
                    data = None
            else:
                print(f"Request failed with status code: {response.status_code}")
                #print("Response content:", response.text)
                data = None

#                 if data:
#                 # Proceed with processing 'data'
#                     for item in data.get('ListItem', []):
#                         name = item.get('name')
#                         url = item.get('url')
#                         position = item.get('position')
#                         print(f"Recipe {position}: {name}, URL: {url}")
#                 else:
#                     print("No data to process.")
# 
#             # Parse JSON string into a Python dictionary
#             data = json_data

            data = json_data

            # Directly access itemListElement from the JSON data
            item_list = []

            if isinstance(json_data, list):
                for item in json_data:
                    if isinstance(item, dict):  # Check if the item is a dictionary
                        # Safely get 'itemListElement' from the dictionary
                        elements = item.get('itemListElement', [])
                        # Extend item_list with elements found
                        item_list.extend(elements)  # Add all elements to item_list
                        #print(item_list)
            else:
                print("json_data is not a list.")
            # Search for URLs containing 'pumpkin'
            urls_and_positions = [
                (item['url'], item['position'])
                for item in item_list
                if 'url' in item and 'position' in item
            ]

            # Step 2: Define the positions you're interested in
            #target_positions = [targ + 1]  # Example: Select URLs at positions 2, 5, and 10

            # Step 3: Filter URLs based on the target positions
            filtered_urls = [url for url, position in urls_and_positions]

            # Display the filtered URLs
            #print("yeahj")
            #print(filtered_urls)

                    # Print the filtered URLs
            #print(filtered_urls)
            try:
                goo = filtered_urls[targ]
            except IndexError:
                for item in detect_b:
                    print(item)
                try:
                    ulr = next(sites_iterator)
                except StopIteration:
                    break
                print(ulr)
                response = requests.get(ulr)
            if targ > len(item_list):
                targ = 1
                #     print(f"targ: {targ}, len(item_list): {len(item_list)}")
                #     print("yeah")
                #     #ulr = next(sites_iterator)
                #     targ = 1
                #     print(f"targ: {targ}, len(item_list): {len(item_list)}")
                #     print(ulr)
                #     response = requests.get(ulr)
                if response.status_code == 200:
                # Step 2: Parse the HTML using BeautifulSoup
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Step 3: Find the script tag that contains the JSON-LD data
                    json_ld_tag = soup.find('script', type='application/ld+json')
                    #
                    if json_ld_tag:
                        # Extract the JSON-LD content
                        json_ld_content = json_ld_tag.string
                        
                        # Step 4: Parse the JSON content
                        json_ld_content = json_ld_tag.string.strip()
                        json_data = json.loads(json_ld_content)
                        


####### ####### #######


                    else:
                        print("No JSON-LD script found on the page.")
                else:
                    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

                            # Define 'url' properly. For example, use 'ulr' if that's the intended variable

                #print(url)
                print(response.headers['Content-Type'])

####### ####### #######

                if response.status_code == 200:
                    try:
                        data = response.json()
                        #print("Parsed JSON data")
                    except requests.exceptions.JSONDecodeError:
                        #print("Failed to parse JSON. Response is not valid JSON.")
                        #print("Response content:", response.text)
                        data = None
                else:
                    print(f"Request failed with status code: {response.status_code}")
                    #print("Response content:", response.text)
                    data = None

    #                 if data:
    #                 # Proceed with processing 'data'
    #                     for item in data.get('ListItem', []):
    #                         name = item.get('name')
    #                         url = item.get('url')

    #                         position = item.get('position')
    #                         print(f"Recipe {position}: {name}, URL: {url}")
    #                 else:
    #                     print("No data to process.")
    # 
    #             # Parse JSON string into a Python dictionary
     #             data = json_data

                data = json_data

                item_list = []

                if isinstance(json_data, list):
                    for item in json_data:
                        if isinstance(item, dict):  # Check if the item is a dictionary
                            # Safely get 'itemListElement' from the dictionary
                            elements = item.get('itemListElement', [])
                            # Extend item_list with elements found
                            item_list.extend(elements)  # Add all elements to item_list
                            #print(item_list)
                else:
                    print("json_data is not a list.")

                urls_and_positions = [
                    (item['url'], item['position'])
                    for item in item_list
                    if 'url' in item and 'position' in item
                ]

                target_positions = [targ]

                filtered_urls = [url for url, position in urls_and_positions]
                print(filtered_urls)
                            

####### ####### #######


                try:
                    goo = filtered_urls[targ]
                except IndexError:
                    for item in detect_b:
                        print(item)
                    break
                    # Now pass the string to requests.get()
                response = requests.get(goo)
                    
        

#                 if data:
#                 # Proceed with processing 'data'
#                     for item in data.get('ListItem', []):
#                         name = item.get('name')
#                         url = item.get('url')
#                         position = item.get('position')
#                         print(f"Recipe {position}: {name}, URL: {url}")
#                 else:
#                     print("No data to process.")
# #
#             # Parse JSON string into a Python dictionary
#             data = json_data

            data = json_data

            urls_and_positions = [
                (item['url'], item['position'])
                for item in item_list
                if 'url' in item and 'position' in item
            ]

            # Step 2: Define the positions you're interested in
            target_positions = [targ]  # Example: Select URLs at positions 2, 5, and 10

            # Step 3: Filter URLs based on the target positions
            filtered_urls = [
                url
                for url, position in urls_and_positions
                if position in target_positions
            ]

            # Display the filtered URLs
            #print(filtered_urls)

            # Now pass the string to requests.get()
            response = requests.get(goo)

            # Print the status code to verify the request works
            #print(response.status_code)  

            # filtered_urls = str(filtered_urls)
            # goo = filtered_urls ?

            # Extract the first URL (since it's a list with one string element)
            # r = requests.get(goo) ?

            soup = BeautifulSoup(response.content, 'html.parser')
            #print(soup.prettify())
            if response.status_code == 200:
                # Step 2: Parse the HTML using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Step 3: Find the script tag that contains the JSON-LD data
                json_ld_tag = soup.find('script', type='application/ld+json')                
                if json_ld_tag:


####### ####### #######


                    json_ld_content = json_ld_tag.string
                    
                    # Step 4: Parse the JSON content
                    json_data = json.loads(json_ld_content)
                    
####### ####### #######

                else:
                    print("No JSON-LD script found on the page.")
            else:
                print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            if isinstance(json_data, list) and len(json_data) > 0:
                # Access the first item in the list and retrieve recipeIngredient
                ingredients = json_data[0].get('recipeIngredient', [])
            else:
                ingredients = []  # Handle case where json_data is not a list or is empty

            # Now you can work with ingredients safely
            # print(ingredients)
            # try:
            #     ingredients = json_data['recipeIngredient']
            # except KeyError:
            #     print("We couldn't find ingredients for one of them...lol")
#           
            # Display the list of ingredients
            # for ingredient in ingredients: - thaw
            #     print(ingredient)
            doneso = str(dones)
            reciso = str(ingredients)
            detect_a = f"Ingredients: {doneso} Recipe: {reciso}"
#
            print(detect_a)
            detect_b.append(detect_a)
            targ = targ + 1
            # chat_completion = client.chat.completions.create(
            #     messages=[
            #         {
            #             "role": "user",
            #             "content": "Here's a list of ingredients. This is from a recipe. \n" + reciso + "\n Now, here's a list of ingredients someone has: \n" + doneso + "\n Using these two lists, will someone be able to make the recipe using the items listed? If no, just say No. If yes, just say Yes. Name the ingredients that are and are not shared. If not all necessary ingredients are shared, it is no. Assume the viewer already has salt and pepper.",
            #         }
            #     ],
            #     model="llama3-8b-8192",
            #     )
            model_path = r"C:\Users\nickc\Downloads\my_model7.h5"
            if os.path.exists(model_path):
                print("File exists.")
            else:
                print("File does not exist.")
            model = tf.keras.models.load_model(model_path, compile=False)
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
            # model = tf.keras.Sequential([
            #     tf.keras.layers.Input(shape=(None,), dtype='int32'),  # Input layer for the vectorized text
            #     tf.keras.layers.Embedding(input_dim=1000, output_dim=64),  # Embedding layer
            #     tf.keras.layers.GlobalAveragePooling1D(),  # Pooling layer
            #     tf.keras.layers.Dense(32, activation='relu'),  # Dense hidden layer
            #     tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
            # ])
            ingreci = {'connection': [detect_a]}
            aidf = pd.DataFrame(ingreci)
            #aidf['yesorno'] = aidf['yesorno'].astype(int

            features = aidf.iloc[:, 0]
            # print("Features: ")
            # print(features)
            #labels = aidf['yesorno']
            # print("Labels: ")
            # print(labels)

            #print(df)
            # Process the lines into a TensorFlow Dataset
            data = [line.strip() for line in aidf]
            dataset = tf.data.Dataset.from_tensor_slices(data)

            features_vectorized = vectorize_layer(features.values)

            predictions = model.predict(features_vectorized)
            raw_pred = (predictions > 0.5).astype("int32")
            #raw_pred = predictions
            #raw_pred = raw_pred.astype(int)
            #predictions = np.round(predictions)
            #predictions = predictions.astype(int)
  
            print("Prediction: ", raw_pred)
            print("Raw Prediction: ", predictions)
            if raw_pred == 1:
                irisrec.append(filtered_urls)
            #print(doneso)
            #print(reciso)
            # yes_no = (chat_completion.choices[0].message.content)
            # if "1" in predictions:
            #     print("YES")
#
            # if "0" in predictions:
            #     print("NO")
            # print("Uncertainty: ")
            #randostat = predictions - raw_pred
            #randostat = np.abs(randostat)
            #print(randostat)

        #inputs = ingredlist

        #print(irisrec)
        dundun = len(irisrec)
        for item in irisrec:
            nutchk = str(item)
            nutchk = re.sub(r'[\[\]\']', '', nutchk)
            response = requests.get(nutchk)

            soup = BeautifulSoup(response.content, 'html.parser')
            #print(soup.prettify())
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                json_ld_tag = soup.find('script', type='application/ld+json')
                
                if json_ld_tag:
                    json_ld_content = json_ld_tag.string
                    json_data = json.loads(json_ld_content)
                    
                else:
                    print("No JSON-LD script found on the page.")
            else:
                print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            if isinstance(json_data, list) and len(json_data) > 0:
                nfacts = json_data[0].get('nutrition', [])
            else:
                nfacts = [] 
            #print(nfacts)
            #print("Nutrition Facts:  ")
            #for item in nfacts:
                #print(item)
            try:
                nutrition_values = {key: value for key, value in nfacts.items() if key != '@type'}
            except AttributeError:
                print("Uh oh!")
                print(item)
            for nutrient, value in nutrition_values.items():
                approv_item = (f"{nutrient}: {value}")
                approv.append(approv_item)
                if nutrient == "calories":
                    calcheck = re.sub("[^0-9]","",value)
                    calcheck = int(calcheck)
                    #print(calcheck)
                if nutrient == "carbohydrateContent":
                    crbcheck = re.sub("[^0-9]","",value)
                    crbcheck = int(crbcheck)
                    crbcheck = crbcheck * 4
                    #print(crbcheck)
                if nutrient == "proteinContent":
                    prtcheck = re.sub("[^0-9]","",value)
                    prtcheck = int(prtcheck)
                    #prtcheck = prtcheck * 4
                    #print(prtcheck)
                if nutrient == "saturatedFatContent":
                    fatcheck = re.sub("[^0-9]","",value)
                    fatcheck = int(fatcheck)
                    fatcheck = fatcheck * 9
                    #print(fatcheck)
                if nutrient == "fiberContent":
                    fibcheck = re.sub("[^0-9]","",value)
                    fibcheck = int(fibcheck)
                    #print(fibcheck)
                if nutrient == "sugarContent":
                    sarcheck = re.sub("[^0-9]","",value)
                    sarcheck = int(sarcheck)
            inicrbcheck = crbcheck
            iniprtcheck = prtcheck
            inifatcheck = fatcheck
            inisarcheck = sarcheck
            inifibcheck = fibcheck
            inicalcheck = calcheck
            dcheckej = [crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck]
            jcheckej = str(dcheckej)
            crbcheck = (carbcheck(calcheck, crbcheck))
            prtcheck = (protcheck(prtcheck))
            fatcheck = (fatfcheck(calcheck, fatcheck))
            sarcheck = (sgarcheck(sarcheck))
            fibcheck = (fibecheck(fibcheck))
            calcheck = (calocheck(calcheck))
            ncheckej = np.asarray([crbcheck, prtcheck, fatcheck, sarcheck, fibcheck, calcheck])
            average = np.average(ncheckej, weights=weightsa)
            javerage = str(average)
            #print(approv)
            #print(average)
            approv_da = str(approv)
            approvt.append(approv_da)
            approv.clear()
            #print(ncheckej)
            #print(average)
            print(f"{jcheckej}, {javerage}")
            features = jcheckej 
            features = eval(features)
            features = np.array(features).reshape(1, -1)
            predictions = model2.predict(features)
            print(predictions)
            recipefilter.append(predictions)
        if any(isinstance(item, list) for item in irisrec):
            irisrec = [tuple(item) for item in irisrec]
        #print(irisrec)
        item_connections = dict(zip(irisrec, recipefilter))
        #print(item_connections)
        recipefilter = np.asarray(recipefilter, dtype=float)
        recipefilter = recipefilter.flatten()
        recipefilter = np.sort(recipefilter)[::-1]
        ranked = recipefilter[:5]
        print(ranked)
        rankedl = list(ranked)
        for item in ranked:
            for key, value in item_connections.items():
                if value == item:
                    print(key)
                    rankedk.append(key)
        for item in rankedk:
            ulr2 = item[0] 
            ulr2 = ulr2 # Ensure 'ulr' contains a valid URL
            print(ulr2)
            response = requests.get(ulr2)

            if response.status_code == 200:
            # Step 2: Parse the HTML using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Step 3: Find the script tag that contains the JSON-LD data
                json_ld_tag = soup.find('script', type='application/ld+json')
                #
                if json_ld_tag:
                    # Extract the JSON-LD content
                    json_ld_content = json_ld_tag.string
                    
                    # Step 4: Parse the JSON content
                    json_ld_content = json_ld_tag.string.strip()
                    json_data = json.loads(json_ld_content)
                    
                    # Step 5: Now you can work with the extracted JSON data
                    #print(json.dumps(json_data, indent=4))  # Pretty-print the JSON data
                else:
                    print("No JSON-LD script found on the page.")
            else:
                print(f"Failed to fetch the webpage. Status code: {response.status_code}")

                        # Define 'url' properly. For example, use 'ulr' if that's the intended variable

            #print(url)
            print(response.headers['Content-Type'])
            #print("Response content:", response.text)
            if response.status_code == 200:
                try:
                    data = response.json()
                    #print("Parsed JSON data")
                except requests.exceptions.JSONDecodeError:
                    #print("Failed to parse JSON. Response is not valid JSON.")
                    #print("Response content:", response.text)
                    data = None
            else:
                print(f"Request failed with status code: {response.status_code}")
                #print("Response content:", response.text)
                data = None
            data = json_data
            for recipe in data:
                namef = recipe.get("name")
                prep_timef = recipe.get("prepTime")
                cook_timef = recipe.get("cookTime")
                yield_valuef = recipe.get("recipeYield")
                nutritionf = recipe.get("nutrition")
                ingredientsf = recipe.get("recipeIngredient")
                instructions = [step.get("text") for step in recipe.get("recipeInstructions", [])]     
                cook_timef = str(cook_timef)   
                prep_timef = str(prep_timef)   
                yield_valuef = str(yield_valuef)       
                cook_timef = re.sub("[^0-9]","",cook_timef)    
                prep_timef = re.sub("[^0-9]","",prep_timef)   
                yield_valuef = re.sub("[^0-9]","",yield_valuef)   
                print(f"Recipe: {namef}")
                print("")
                print(f"Prep Time: {prep_timef} minutes")
                print(f"Cook Time: {cook_timef} minutes")
                print(f"Yield: {yield_valuef} servings")
                if iterated == 0:
                    main_a += f"Prep Time: {prep_timef} minutes <br>"
                    main_a += f"Cook Time: {cook_timef} minutes <br>"
                    main_a += f"Yield: {yield_valuef} servings <br>"
                if iterated == 1:
                    main_b += f"Prep Time: {prep_timef} minutes <br>"
                    main_b += f"Cook Time: {cook_timef} minutes <br>"
                    main_b += f"Yield: {yield_valuef} servings <br>"
                if iterated == 2:
                    main_c += f"Prep Time: {prep_timef} minutes <br>"
                    main_c += f"Cook Time: {cook_timef} minutes <br>"
                    main_c += f"Yield: {yield_valuef} servings <br>"
                if iterated == 3:
                    main_d += f"Prep Time: {prep_timef} minutes <br>"
                    main_d += f"Cook Time: {cook_timef} minutes <br>"
                    main_d += f"Yield: {yield_valuef} servings <br>"
                if iterated == 4:
                    main_e += f"Prep Time: {prep_timef} minutes <br>"
                    main_e += f"Cook Time: {cook_timef} minutes <br>"
                    main_e += f"Yield: {yield_valuef} servings <br>"
                print("")
                print("Nutrition Facts:")
                for key, value in nutritionf.items():
                    if key != "@type":  # Skip the "@type" key
                        print(f"  {key}: {value}")
                        if iterated == 0:
                            nutr_a += f"{key}: {value} <br>"
                        if iterated == 1:
                            nutr_b += f"{key}: {value} <br>"
                        if iterated == 2:
                            nutr_c += f"{key}: {value} <br>"
                        if iterated == 3:
                            nutr_d += f"{key}: {value} <br>"
                        if iterated == 4:
                            nutr_e += f"{key}: {value} <br>"
                print("Ingredients:")
                for ingredientf in ingredientsf:
                    print(f"  - {ingredientf}")
                    if iterated == 0:
                        ingred_a += f" - {ingredientf} <br>"
                    if iterated == 1:
                        ingred_b += f" - {ingredientf} <br>"
                    if iterated == 2:
                        ingred_c += f" - {ingredientf} <br>"
                    if iterated == 3:
                        ingred_d += f" - {ingredientf} <br>"
                    if iterated == 4:
                        ingred_e += f" - {ingredientf} <br>"
                print("Instructions:")
                for stepno, step in enumerate(instructions, start=1):
                    print("")
                    print(f"  {stepno}. {step}")
                    if iterated == 0:
                        instruc_a += f"{stepno}. {step} <br>"
                    if iterated == 1:
                        instruc_b += f"{stepno}. {step} <br>"
                    if iterated == 2:
                        instruc_c += f"{stepno}. {step} <br>"
                    if iterated == 3:
                        instruc_d += f"{stepno}. {step} <br>"
                    if iterated == 4:
                        instruc_e += f"{stepno}. {step} <br>"
                if iterated == 0:
                    title_a = str(namef)
                if iterated == 1:
                    title_b = str(namef)
                if iterated == 2:
                    title_c = str(namef)
                if iterated == 3:
                    title_d = str(namef)
                if iterated == 4:
                    title_e = str(namef)
                iterated += 1 
        html_output = f"""
        <html>
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width" />
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
            <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400&family=Lobster&display=swap" rel="stylesheet">
            <title>Top 5 Recipe Choices</title>
            <link href="styles.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
            <h1>1. {title_a}</h1>
            <h2>{main_a}</h2>
            <h2>Nutritional Facts:</h2>
            <h3>{nutr_a}</h3>
            <h2>Ingredients:</h2>
            <h3>{ingred_a}</h3>
            <h2>Instructions:</h2>
            <h3>{instruc_a}</h2>
            <h1>2. {title_b}</h1>
            <h2>{main_b}</h2>
            <h2>Nutritional Facts:</h2>
            <h3>{nutr_b}</h3>
            <h2>Ingredients:</h2>
            <h3>{ingred_b}</h3>
            <h2>Instructions:</h2>
            <h3>{instruc_b}</h2>
            <h1>3. {title_c}</h1>
            <h2>{main_c}</h2>
            <h2>Nutritional Facts:</h2>
            <h3>{nutr_c}</h3>
            <h2>Ingredients:</h2>
            <h3>{ingred_c}</h3>
            <h2>Instructions:</h2>
            <h3>{instruc_c}</h2>
            <h1>4. {title_d}</h1>
            <h2>{main_d}</h2>
            <h2>Nutritional Facts:</h2>
            <h3>{nutr_d}</h3>
            <h2>Ingredients:</h2>
            <h3>{ingred_d}</h3>
            <h2>Instructions:</h2>
            <h3>{instruc_d}</h2>
            <h1>5. {title_e}</h1>
            <h2>{main_e}</h2>
            <h2>Nutritional Facts:</h2>
            <h3>{nutr_e}</h3>
            <h2>Ingredients:</h2>
            <h3>{ingred_e}</h3>
            <h2>Instructions:</h2>
            <h3>{instruc_e}</h2>
        </body>
        </html>
        """
        with open("output.html", "w") as file:
            file.write(html_output)

        FILENAME = "output.html"

        class CustomHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/":  # Serve the specific file on root path
                    self.path = FILENAME
                return super().do_GET()

        # Setup server to use the custom handler
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"Serving at http://localhost:{PORT}")
            httpd.serve_forever()
        #print(approvt)
        #did concentation
        #break#
    if fodd == 10:
        fodd = 1
        #looped to 0 at end, fixed 10/6
    if fodd == 9:
        df_i = df_merged
        fodd += 1
        vari9 = vari
    if fodd == 8:
        df_h = df_merged
        fodd += 1
        vari8 = vari
    if fodd == 7:
        df_g = df_merged
        fodd += 1
        vari7 = vari
    if fodd == 6:
        df_f = df_merged
        fodd += 1
        vari6 = vari
    if fodd == 5:
        df_e = df_merged
        fodd += 1
        vari5 = vari
    if fodd == 4:
        df_d = df_merged
        fodd += 1
        vari4 = vari
    if fodd == 3:
        df_c = df_merged
        fodd += 1
        vari3 = vari
    if fodd == 2:
        df_b = df_merged
        fodd += 1
        vari2 = vari
    if fodd == 1:
        df_a = df_merged
        fodd += 1
        vari1 = vari
        #added this part on 9/28 (fodd = 0)
        #print("Yeah")
    #was in oppostite order before, put in logbook for christ's sake
    #realized left side and right side had to be reversed, I had to unindent print
    #used wrong equation sign double
    #after that it worked
    #https://medium.com/@byrda05/building-a-recipe-management-system-api-a-step-by-step-guide-b19ee80d9f2d and learned about flask and https://github.com/hhursev/recipe-scrapers
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "How much \n" + fod + "\n is in this recipe (in grams)? Use the proper conversion rate between units if necessary. If the item is not in the recipe, put 0. https://www.bonappetit.com/recipe/bas-best-bolognese. List only the final amount (as a number) and nothing else.",
    #         }
    #     ],
    #     model="llama3-8b-8192",
    # )

    # print((chat_completion.choices[0].message.content))

    end_time = datetime.now()
    start_time = datetime.strftime(start_time, "%H:%M:%S:%f")
    end_time = datetime.strftime(end_time, "%H:%M:%S:%f")
    start_time = str(start_time)
    end_time = str(end_time)

    t1 = datetime.strptime(start_time, "%H:%M:%S:%f")
    #print('Start time:', t1.time())

    t2 = datetime.strptime(end_time, "%H:%M:%S:%f")
    #print('End time:', t2.time())

    # get difference
    delta = t2 - t1

    # time difference in seconds
    print(f"Time taken: {delta.total_seconds()} seconds")
    df = pd.read_csv("requirements777.txt")

    df = df.drop(columns=["data_type", "food_category_id", "publication_date"])
    #for i in range(atr):
        #goe = ""
    
    # for index, row in df.iterrows():
    #     if [df['amount'] == 0] :
    #         print(f"Row {index} has nutrient_id: {row['nutrient_id']}")
# anfs = len(ingr_total) - thaw
# anfsv = len(vari_total)
# for i in range(anfs):
#     print("Ingredients: ")
#     print(ingr_total[i])
#     ingra = ingr_total[i].lower()
#     ingr_total_low = ingra
#     print("Varities: ")
#     if ingr_total[i] in vari_total[i] or ingr_total_low in vari_total[i]:
#         print("Success!")
#         succe += 1
#     else:
#         print("FAIL")
#     totae += 1
#     print(vari_total[i])
#     ratee = succe/totae * 100
#     print("Success Rate:")
#     print(ratee) - thaw
# ##

       

    