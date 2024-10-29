# RAGAS Evaluation for RAG Chat Applications

This project aims to evaluate the performance of API-based RAG Chatbots' AI in answering questions related to various categories, including Diversity Training, ERG Support, Recruitment Insights, Inclusive Policy, and Inclusive Language.

The tool includes a set of questions related to DEI (Diversity, Equity, and Inclusion) with corresponding ground truths.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project_directory>
    ```
3. Install the required dependencies, ideally in a new environment named 'deially-evaluator':
    ```sh
    pip install -r requirements.txt
    ```
4. Set up your environment variables by creating a `.env` file and adding your DEIAlly API key:
    ```sh
    DEIALLY_API_KEY=your_api_key
    OPENAI_API_KEY=your_api_key
    DEIALLY_API_URL=https://app.deially.ai
    ```

## Usage

1. Ensure `questionData.json` contains the categories and questions you want to evaluate.
2. If you want to run `ask_llm` in DEIAlly, delete all `.csv` files in the project root directory. Otherwise, the RAGAS evaluator will use the existing data from the `.csv` files to save API calls.
3. Select the categories you want to evaluate by modifying the `categoryToProcess` list in `script.py`.
4. Run the script:
    ```sh
    python script.py
    ```
5. Check the results in the `results.csv` file.

## Notes/ToDos

- Once the DEIAlly API is updated to provide context, update `script.py` to run additional metrics.
- Improve the quality of ground truths in `questionData.json`.
- Add more questions to `questionData.json`.
- If we can access the files in production, we may be able to automate the process of creating the questions and ground truths using RAGAS.
