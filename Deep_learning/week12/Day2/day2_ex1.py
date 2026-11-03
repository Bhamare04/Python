from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained(
    "bert-base-uncased"
)

model = BertModel.from_pretrained(
    "bert-base-uncased"
)

text = "Transformers are powerful models for NLP tasks"

inputs = tokenizer(
    text,
    return_tensors='pt'
)

outputs = model(**inputs)

print(
    "Hidden States Shape:",
    outputs.last_hidden_state.shape
)