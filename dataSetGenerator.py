import json
import os
import pandas as pd
#from datasets import Dataset
from tqdm import tqdm
from deially import ask_deially



def create_ragas_dataset(category, question_data_file='questionData.json', dataset_file='dataset.csv'):
    # Check if the dataset file already exists
    
    for cat in category:
        if os.path.exists(cat + '_' + dataset_file):
            print("Loading existing dataset for category: ", cat)
            # Load the dataset from the CSV file
            ragas_df = pd.read_csv(cat + '_' + dataset_file)
            
        else:
            print("Creating new dataset for category: ", cat)
            
            with open(question_data_file, 'r') as file:
                question_data = json.load(file)
            
            # Check if the category exists in the data
            if cat not in question_data:
                raise ValueError(f"Category '{cat}' not found in question data.")
            
            # Initialize the dataset list
            ragas_dataset = []
            
            # Iterate over each question in the specified category
            for question_item in tqdm(question_data[cat]):
                question = question_item['question']
                ground_truth = question_item['ground_truth']

                # Get the answer from DEIAlly
                #print("Question for asking DEIAlly: ", question)
                answer_response = ask_deially(question)
                answer = answer_response.get('message', 'No answer provided')
            
                # Append the data to the dataset list
                ragas_dataset.append({
                    'question': question,
                    'answer': answer,
                    'ground_truth': ground_truth,
                    'category': cat
                })
        
            # Convert the list to a DataFrame
            ragas_df = pd.DataFrame(ragas_dataset)
        
            # Save the DataFrame to a CSV file for reuse
            ragas_df.to_csv(cat + '_' + dataset_file, index=False)
    
    return 0