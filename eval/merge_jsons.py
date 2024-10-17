import json, glob, os
def merge_json_files(input_folder, output_file):
    all_data = []
    json_files = glob.glob(os.path.join(input_folder, '*.json'))
    
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_data.append(data)
    
    sorted_data = sorted(all_data, key=lambda x: x['question_id'])

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(sorted_data, outfile, ensure_ascii=False, indent=4)

MODEL = "gpt4o"
inputname = f'./eval/test_results/siuo_gen-{MODEL}.json'
merge_json_files(f'./eval/{MODEL}', inputname)
