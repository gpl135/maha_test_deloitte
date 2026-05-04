from langsmith import Client
from dotenv import load_dotenv
load_dotenv()


client = Client()

# ======================================================
#     Check whether the database is already exist or not
# ======================================================

try:
    dataset = client.read_dataset(dataset_name="chatbot-bot-dataset")
    print("Dataset found")
except Exception as e:
    dataset = client.create_dataset(dataset_name="chatbot-bot-dataset",description="Test dataset for chatbot evaluation")
    print("Dataset not found, creating new one...")

    # Correct format
    client.create_example(
        inputs={"input": "What is AI?"},
        outputs={"output": "Artificial Intelligence"},
        dataset_id=dataset.id
    )

    client.create_example(
        inputs={"input": "Who are you?"},
        outputs={"output": "assistant"},
        dataset_id=dataset.id
    )