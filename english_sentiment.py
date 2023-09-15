from transformers import AutoTokenizer, AutoModelForSequenceClassification


model = AutoModelForSequenceClassification.from_pretrained(
    "C:/Users/EmilJohansson/PycharmProjects/Rating_API/model/cardiffnlp/twitter-roberta-base-sentiment-latest")
tokenizer = AutoTokenizer.from_pretrained(
    "C:/Users/EmilJohansson/PycharmProjects/Rating_API/model/cardiffnlp/twitter-roberta-base-sentiment-latest")

# model med 1-3 rating: cardiffnlp/twitter-roberta-base-sentiment-latest
# model med 1-5 rating: nlptown/bert-base-multilingual-uncased-sentiment

async def review_rating(input):
    tokens = tokenizer.encode(input, return_tensors="pt")
    result = model(tokens)
    output_np = result.logits[0].detach().cpu().numpy()

    return output_np

