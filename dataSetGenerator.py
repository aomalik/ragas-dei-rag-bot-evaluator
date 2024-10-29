import json
import os
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
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
            
            # Function to fetch answer for each question concurrently
            def fetch_answer(question_item):
                question = question_item['question']
                ground_truth = question_item['ground_truth']
                answer_response = ask_deially(question)
                answer = answer_response.get('message', 'No answer provided') if answer_response else 'No answer provided'
                return {
                    'question': question,
                    'answer': answer,
                    'ground_truth': ground_truth,
                    'category': cat
                }

            # Use ThreadPoolExecutor to fetch answers concurrently
            with ThreadPoolExecutor(max_workers=5) as executor:
                results = list(tqdm(executor.map(fetch_answer, question_data[cat]), total=len(question_data[cat])))
            

            ragas_dataset.extend(results)
            ragas_df = pd.DataFrame(ragas_dataset)
            ragas_df.to_csv(cat + '_' + dataset_file, index=False)
    
    return 0
