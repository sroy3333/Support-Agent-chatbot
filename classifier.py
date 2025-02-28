from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def is_relevant_question(question):
    labels = ["CDP-related", "Irrelevant"]
    result = classifier(question, labels)
    return result["labels"][0] == "CDP-related"

# Test
if __name__ == "__main__":
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
