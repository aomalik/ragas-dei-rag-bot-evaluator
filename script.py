from dataSetGenerator import create_ragas_dataset
from ragas.metrics import context_precision, faithfulness, answer_relevancy, context_recall, answer_correctness, answer_similarity
from ragas import evaluate
import csv
import os
from datasets import Dataset
import asyncio

#All cats -> ["DiversityTraining", "ERGSupport", "RecruitmentInsights", "InclusivePolicy", "InclusiveLanguage"]

categoryToProcess = ["DiversityTraining", "ERGSupport", "RecruitmentInsights", "InclusivePolicy", "InclusiveLanguage"]


ragas_dataset = create_ragas_dataset(categoryToProcess)

async def evaluate_ragas_dataset(cats):
    for cat in cats:
        #ragas_dataset = pd.read_csv(cat + '_' + 'dataset.csv')
        ragas_dataset = Dataset.from_csv(cat + '_' + 'dataset.csv')
        result = await evaluate(
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
        await asyncio.sleep(0)
        

        print(result)

        # Define the results file
        results_file = 'results.csv'

        # Check if the file exists
        file_exists = os.path.isfile(results_file)

        # Open the file in append mode
        with open(results_file, mode='a', newline='') as file:
            writer = csv.writer(file)

            # If the file does not exist, write the header
            if not file_exists:
                writer.writerow(['category', 'answer_relevancy', 'answer_correctness', 'semantic_similarity'])

            # Write the result row
            writer.writerow([
                cat,
                result['answer_relevancy'],
                result['answer_correctness'],
                result['semantic_similarity'],
            ])
    return result

asyncio.run(evaluate_ragas_dataset(categoryToProcess))
