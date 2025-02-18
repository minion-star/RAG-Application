import os, openai
from dotenv import load_dotenv
from article_generation import *
from make_vectordb import *
from audio_generation import *


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def main(topic, context):
    
    
    vectordb = load_vectordb()

    article = generate_article(topic, context, vectordb)
    # print(article)
    save_audio(article)

if __name__ == "__main__":
    topic = "Management of preeclampsia with severe features at 34 weeks gestation"
    context = "I saw this while on service with Dr. Jones"
    main(topic, context)