from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

model = AutoModelForSequenceClassification.from_pretrained(
    "twitter-roberta-base-sentiment-latest_model")
tokenizer = AutoTokenizer.from_pretrained(
    "twitter-roberta-base-sentiment-latest_tokenizer")

async def review_rating(input):
    tokens = tokenizer.encode(input, return_tensors="pt")
    result = model(tokens)
    output_np = result.logits[0].detach().cpu().numpy()
    output = softmax(output_np)

    return output

