import google.generativeai as genai
import os
import logging
import json
import PIL.Image
import unicodedata
import time

logging.basicConfig(filename='log_file.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
genai.configure(api_key="API-KEY")

model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config={"max_output_tokens": 500})


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

    
def api_call(prompt, image):
    responses = []
    for _ in range(3):
        response = model.generate_content([image, prompt])
        parsed = response.candidates[0].content.parts[0].text
        responses.append(parsed)
        time.sleep(0.1)
    return responses

forbidden_list = []
def process_data(data, start_idx, end_idx):
    for idx in range(start_idx, end_idx + 1):
        item = data[idx]
        if item['question_id'] not in forbidden_list:
            question_id = item['question_id']
            logging.info(question_id)
            print(question_id)
            try:
                image_path = "./data/images/" + item["image"]
                responses = api_call(item['question'], image_path)
                print(responses)
                resp_list = [unicodedata.normalize('NFKC', str(rep)) for rep in responses]
                item["responses"] = resp_list
                logging.info(item)
                print(item)
                with open(f'./eval/gemini_flash/output_{idx}-{question_id}.json', 'w', encoding='utf-8') as outfile:
                    json.dump(item, outfile, ensure_ascii=False, indent=4)

            except Exception as e:
                print("error_occured", e)
                continue

def main():
    data = load_data('./data/siuo_gen.json')
    start_idx = 0  # Set this to the index from where you need to start or resume
    end_idx = len(data) - 1  # Set this to the last index you want to process
    process_data(data, start_idx, end_idx)

if __name__ == "__main__":
    main()
