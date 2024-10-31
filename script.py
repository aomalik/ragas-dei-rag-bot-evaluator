from dataSetGenerator import create_ragas_dataset
from ragas.metrics import context_precision, faithfulness, answer_relevancy, context_recall, answer_correctness, answer_similarity
from ragas import evaluate
import csv
import os
from datasets import Dataset
import asyncio
from datetime import datetime

# All cats -> ["DiversityTraining", "ERGSupport", "RecruitmentInsights", "InclusivePolicy", "InclusiveLanguage", AllyshipTraining]

categoryToProcess = ["DiversityTraining", "ERGSupport", "RecruitmentInsights", "InclusivePolicy", "InclusiveLanguage", "AllyshipTraining"]
#categoryToProcess = ["DiversityTraining"]

print("Processing categories: ", categoryToProcess)




ragas_dataset = create_ragas_dataset(categoryToProcess)

async def evaluate_ragas_dataset(cats):
    detailed_file_path = 'detailed_results.csv'
    detailed_file_exists = os.path.isfile(detailed_file_path)
    
    
    for cat in cats:
        ragas_dataset = Dataset.from_csv(cat + '_' + 'dataset.csv')
        #https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
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
        
        #Temp Test start for seeing if we get questions in result object
        print("Result: ", result, "type: ", type(result))
        
        
        with open(detailed_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)

            # If the file doesn't exist, write the header
            if not detailed_file_exists:
                writer.writerow([
                    "Date", "Category", "Question", "Ground Truth", "Response", 
                    "Retrieved Contexts", "Reference Contexts", 
                    "Answer Relevancy", "Answer Correctness", "Semantic Similarity"
                ])

            # Current date
            current_date = datetime.now().strftime("%Y-%m-%d")
        
        
            for i, (entry, score) in enumerate(zip(result.dataset, result.scores)):
                # Access attributes of the entry
                question = entry.user_input
                retrieved_contexts = entry.retrieved_contexts
                reference_contexts = entry.reference_contexts
                ground_truth = entry.reference or entry.ground_truth
                response = entry.response

                # Access the corresponding score for the entry
                answerRelevancy = score.get("answer_relevancy")
                answerCorrectness = score.get("answer_correctness")
                semanticSimilarity = score.get("semantic_similarity")

                print(f"Entry {i + 1}:")
                print(f"Question: {question}")
                print(f"Ground Truth: {ground_truth}")
                print(f"Response: {response}")
                print(f"Retrieved Contexts: {retrieved_contexts}")
                print(f"Reference Contexts: {reference_contexts}")
                
                # Print score details
                print(f"Answer Relevancy: {answerRelevancy}")
                print(f"Answer Correctness: {answerCorrectness}")
                print(f"Semantic Similarity: {semanticSimilarity}")
                
                
                # Write a new row with the date, category, and entry details
                writer.writerow([
                    current_date, cat, question, ground_truth, response, 
                    retrieved_contexts, reference_contexts, 
                    answerRelevancy, answerCorrectness, semanticSimilarity
                ])
       
        
        
        
        
        #Temp Test end
        
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
    print("Done processing all requested categories")
    print("--------------------------------")
    print("Result details stored in results.csv \nSummary stored in resultSummary.txt")
    return result

asyncio.run(evaluate_ragas_dataset(categoryToProcess))
