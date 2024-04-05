import json
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"
data_path = "/workspaces/Hollow-Technique-Purple/chat_x/context.json" # Path to your JSON file

# Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a question-answering pipeline
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

# Load context from JSON file
with open(data_path, "r") as f:
    context_data = json.load(f)
    context = context_data["context"]

while True:
    user_input = input("Ask a question (or press 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    QA_input = {
        'question': user_input,
        'context': context
    }

    res = nlp(QA_input)
    print(res)

    print(f"Answer: {res['answer']}")
