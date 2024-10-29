# RAGAS Evaluation for RAG Chat Applications

This project is designed to evaluate the performance of API based RAG Chatbots's AI in answering questions related to various categories such as Diversity Training, ERG Support, Recruitment Insights, Inclusive Policy, and Inclusive Language.

The tool includes a set of questions related to DEI with ground truths.


## Setup

1. Clone the repository:
    ```sh
    git clone this repo
    ```
2. Navigate to the project directory:
    ```sh
    cd yourproject
    ```
3. Install the required dependencies, ideally in a new environment:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up your environment variables by creating a `.env` file and adding your DEIAlly API key:
    ```sh
    DEIALLY_API_KEY=your_api_key
    OPENAI_API_KEY=your_api_key
    DEIALLY_API_URL=https://app.deially.ai for production
    ```

## Usage
Step 1: Make sure questionData.json has the category and questions you want to evaluate for that category.
Step 2: If you want to run ask_llm in DEIAlly, make sure to delete all .csv files in project root directory.
Otherwise, RAGAS evaluator will use the old data from .csv files to save API calls.
Step 3: Select the categories you want to evaluate for by changing the categoryToProcess list in script.py.
Step 4: Run the script.
```sh
python script.py
```
Step 4: Check the results in results.csv file.


## Notes/ToDos
- Once DEIAlly api is updated to provide context, update script.py to run more metrics.
- We need to improve the quality of ground truths in questionData.json.
- We need to add more questions to questionData.json.
- If we can access the files on production, we may be able to automate the process of creating the questions and ground truths using RAGAS.
