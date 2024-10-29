from dataSetGenerator import create_ragas_dataset
from ragas.metrics import context_precision, faithfulness, answer_relevancy, context_recall, answer_correctness, answer_similarity
from ragas import evaluate
import csv
import os


categoryToProcess = "DiversityTraining"


ragas_dataset = create_ragas_dataset(categoryToProcess)

def evaluate_ragas_dataset(ragas_dataset):
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
            categoryToProcess,
            result['answer_relevancy'],
            result['answer_correctness'],
            result['semantic_similarity']
        ])
    return result

evaluate_ragas_dataset(ragas_dataset)