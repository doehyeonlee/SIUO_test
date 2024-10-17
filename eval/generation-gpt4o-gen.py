import base64
from openai import OpenAI
import unicodedata
import time
import json
import logging

# OpenAI API Key
api_key = "API_KEY"
client = OpenAI(
    api_key=api_key
)

logging.basicConfig(filename='log_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to load data from a JSON file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# Function to encode an image to a base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


# Function to call an API with an image and a text prompt
def api_call(prompt, base64_image, _model_):
    # Assuming client is already initialized and available here
    response = client.chat.completions.create(
    model=_model_,
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ],
        }
    ],
    max_tokens=500,
    n=3
    )
    time.sleep(1)
    return response

forbidden_list = []
# Function to process a range of data items and save results
def process_data(data, start_idx, end_idx, model):
    all_results = []
    for idx in range(start_idx, end_idx + 1):
        item = data[idx]
        if item['question_id'] not in forbidden_list:
            question_id = item['question_id']
            logging.info(question_id)
            
            print(question_id)
            try:
                image_path = "./data/images/" + item["image"]
                base64_image = encode_image(image_path)
                
                response = api_call(item["question"], base64_image, model)
                resp_list = [unicodedata.normalize('NFKC', choice.message.content) for choice in response.choices]
                item["responses"] = resp_list
            
                logging.info(item)
                all_results.append(item)
                print(item)
                with open(f'./eval/{model}/output_{idx}-{question_id}.json', 'w', encoding='utf-8') as outfile:
                    json.dump(item, outfile, ensure_ascii=False, indent=4)

            except Exception as e:
                # Log the error
                print("error_occured", e)
                continue  # Skip to the next item
    
# Main function to manage data processing
def main():
    model="GPT-VLM-MODEL"
    data = load_data('./data/siuo_gen.json')
    start_idx = 0  # Set this to the index from where you need to start or resume
    end_idx = len(data) - 1  # Set this to the last index you want to process
    process_data(data, start_idx, end_idx, model)

if __name__ == "__main__":
    main()

