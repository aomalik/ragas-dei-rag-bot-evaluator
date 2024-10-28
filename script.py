from dataSetGenerator import create_ragas_dataset
from ragas.metrics import context_precision, faithfulness, answer_relevancy, context_recall, answer_correctness, answer_similarity
from ragas import evaluate


categoryToProcess = "DiversityTraining"
ragas_dataset = create_ragas_dataset(categoryToProcess)

def evaluate_ragas_dataset(ragas_dataset):
    result = evaluate(
        ragas_dataset,
        metrics=[
            context_precision,
            faithfulness,
            answer_relevancy,
            context_recall,
            answer_correctness,
            answer_similarity
        ],
    )
    return result

evaluate_ragas_dataset(ragas_dataset)