import pandas as pd
import numpy as np

# Load Dataset

matches = pd.read_csv("Dataset/matches.csv")
deliveries = pd.read_csv("Dataset/deliveries.csv.zip")

print("Matches dataset")
print(matches.head())

print("Deliveries dataset")
print(deliveries.head())

# Dataset size check

print(matches.shape)
print(deliveries.shape)

# Checks columns name

print("Matches columns")
print(matches.columns)

print("\nDeliveries columns")
print(deliveries.columns)

# Checks Data types

print(matches.info())

# Checks Missing Values in the Datasets

print("Missing values in Matches:")
print(matches.isnull().sum())

print("\nMissing values in Deliveries:")
print(deliveries.isnull().sum())

# Fill missing values in matches dataset

matches['city']= matches['city'].fillna("Unknow")

matches['winner']= matches['winner'].fillna("No result")

matches['player_of_match']= matches['player_of_match'].fillna("No award")

print(matches.isnull().sum())

# Save cleaned matches data

matches.to_csv("Dataset/Cleaned_matches.csv",index=False)
print("Cleaned dataset saved sucessfully")