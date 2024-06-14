from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")

def qa_model(question):
    with open('context.txt', 'r') as file:
        context = file.read().replace('\n', '')

        inputs = tokenizer(question, context, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)

        answer_start_index = outputs.start_logits.argmax()
        answer_end_index = outputs.end_logits.argmax()

        answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]

        result = tokenizer.decode(answer_tokens)

        print(" ".join([question, result]))

        return result