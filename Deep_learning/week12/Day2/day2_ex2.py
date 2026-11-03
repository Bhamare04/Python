from transformers import BertTokenizer, TFBertModel

tokenizer = BertTokenizer.from_pretrained(
    "bert-base-uncased"
)

model = TFBertModel.from_pretrained(
    "bert-base-uncased"
)

text = "Transformers are powerful models for NLP tasks"

inputs = tokenizer(
    text,
    return_tensors='tf'
)

outputs = model(**inputs)

print(
    "Hidden States Shape:",
    outputs.last_hidden_state.shape
)