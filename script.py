from dataSetGenerator import create_ragas_dataset
from ragas.metrics import context_precision, faithfulness, answer_relevancy, context_recall, answer_correctness, answer_similarity
from ragas import evaluate
import csv
import os
from datasets import Dataset
import asyncio
from datetime import datetime

# All cats -> ["DiversityTraining", "ERGSupport", "RecruitmentInsights", "InclusivePolicy", "InclusiveLanguage"]
#categoryToProcess = ["DiversityTraining", "ERGSupport", "RecruitmentInsights", "InclusivePolicy", "InclusiveLanguage"]

categoryToProcess = ["DiversityTraining", "ERGSupport"]
print("Processing categories: ", categoryToProcess)


ragas_dataset = create_ragas_dataset(categoryToProcess)

async def evaluate_ragas_dataset(cats):
    for cat in cats:
        ragas_dataset = Dataset.from_csv(cat + '_' + 'dataset.csv')
        result = evaluate(
            ragas_dataset,
            metrics=[
                #context_precision,
                #faithfulness,
                answer_relevancy,
                #context_recall,
                answer_correctness,
                answer_similarity

            ],
        )
        

        print("Result: ", result)
        

        results_file = 'resultSummary.txt'
        file_exists = os.path.isfile(results_file)
        
        with open(results_file, mode='a', newline='') as result_file:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result_file.write(f"{current_time} | {cat} | {result}\n")
        #Storing detailed results in csv
        results_file = 'results.csv'
        file_exists = os.path.isfile(results_file)
        
        with open(results_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # If the file does not exist, write the header
            if not file_exists:
                writer.writerow(['category', 'answer_relevancy', 'answer_correctness', 'semantic_similarity'])
                
            writer.writerow([
                cat,
                result['answer_relevancy'],
                result['answer_correctness'],
                result['semantic_similarity'],
            ])
    return result

asyncio.run(evaluate_ragas_dataset(categoryToProcess))
