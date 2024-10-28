import json
import pandas as pd
from datasets import Dataset
from tqdm import tqdm
from deially import ask_deially




def create_ragas_dataset(category, question_data_file='questionData.json'):
    # Load question data from JSON file
    with open(question_data_file, 'r') as file:
        question_data = json.load(file)
    
    # Check if the category exists in the data
    if category not in question_data:
        raise ValueError(f"Category '{category}' not found in question data.")
    
    # Initialize the dataset list
    ragas_dataset = []
    
    # Iterate over each question in the specified category
    for question_item in tqdm(question_data[category]):
        question = question_item['question']
        print("question: ", question)
        ground_truth = question_item['ground_truth']
        print("ground_truth: ", ground_truth)
        
        # Get the answer from DEIAlly
        answer_response = ask_deially(question)
        print("answer_response: ", answer_response)
        answer = answer_response.get('answer', 'No answer provided')
        
        # Append the data to the dataset list
        ragas_dataset.append({
            'question': question,
            'answer': answer,
            'ground_truth': ground_truth
        })
        
    # Convert the list to a DataFrame
    ragas_df = pd.DataFrame(ragas_dataset)
    
    # Convert the DataFrame to a Dataset
    ragas_eval_dataset = Dataset.from_pandas(ragas_df)
    
    return ragas_eval_dataset


