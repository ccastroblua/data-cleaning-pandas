import pandas as pd
import seaborn as sns

# This function remove every full null row and only leave in the dataset the columns we want

def first_clean(data, list_columns):
    cleaner_data = data[list_columns].dropna(axis = 0, how = "all")
    return cleaner_data


# Changing every column name into new names (columns new names has to be in order)

def change_column_name(data, new_names):
    
    dic = {}
    lst = list(data.columns)
    i = 0
    
    for name in lst:
        dic[name] = new_names[i]
        i += 1
    
    data.rename(columns = dic, inplace = True)
    
    return data


# Correcting all exact values in one column and change them into a new character previosuly defined

def correcting_values(data, column, list_old_characters, new_characters):
    for char in list_old_characters:
        data[column] = data[column].str.replace(char,new_characters)
    return data


# We eliminate null in the rest of the columns except "Case Number" checking nulls in "Date" column.

def cleaning_date_null(dataset):
    
    dataset_to_eliminate = dataset[dataset["date"].isnull() == True]
    indexes = dataset_to_eliminate.index
    new_dataset = dataset.iloc[0:indexes[0]-1]
    
    return new_dataset


# A new function that uses "correcting_values" function to clean the whole "fatal" column

def cleaning_fatal(dataset):
    list_values = ["y"]
    dataset = correcting_values(dataset, "fatal", list_values, "Y")
    
    list_values_2 = ["n"," N","N ","M"]
    dataset = correcting_values(dataset, "fatal", list_values_2, "N")
    
    list_values_3 = ["2017"]
    dataset = correcting_values(dataset, "fatal", list_values_3, "UNKNOWN")
    
    dataset.fatal.fillna("UNKNOWN", inplace = True)
    
    return dataset