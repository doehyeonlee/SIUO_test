
## 🎯 Evaluation

**SIUO** is a zero-shot evaluation benchmark. The model response generation process can be referred to in the following files: `generation—gpt4o-gen.py` and `generation-gpt4o-mcqa.py`.

### 🤖 GPT-Eval

1. Put your model's three responses as a list and add them under the "responses" field in `siuo_gen.json`, saved in `./eval/test_results/siuo_gen-{model_name}.json`.

2. For the safety evaluation, run `python gpt-eval.py --model model_name --mode safe` to obtain `./eval/test_results/siuo_gen-{model_name}-gpteval-safe-pro.json`.

    For the effectiveness evaluation, run `python gpt-eval.py --model model_name --mode effective` to obtain `./eval/test_results/siuo_gen-{model_name}-gpteval-effective-pro.json`.

    Note: Before running the `gpt-eval.py` file, you need to add your OpenAI API key.

3. Then run the file `python gpt-score.py`, which will merge the safe and effective files, calculate the values for safe, effective, and safe & effective scores. It will also statistically analyze the scores by category.

### 🤹 Multiple-Choice QA

1. Add the model response results under the "response_mcqa" field in `siuo_mcqa.json`, saved in `./eval/test_results/siuo_mcqa-{model_name}.json`.

2. Then run the file `python mcqa-eval.py --model model_name` to match the model responses and calculate accuracy.


## 🔒 License
![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg) **Usage and License Notices**: The dataset is intended and licensed for research use only. The dataset is CC BY NC 4.0 (allowing only non-commercial use) and models using the dataset should not be used outside of research purposes.


## 👋 Citation

**BibTeX:**

```bibtex
@article{wang2024cross,
  title={Cross-Modality Safety Alignment},
  author={Siyin Wang and Xingsong Ye and Qinyuan Cheng and Junwen Duan and Shimin Li and Jinlan Fu and Xipeng Qiu and Xuanjing Huang},
  journal={arXiv preprint arXiv:2406.15279},
  year={2024},
  url={https://arxiv.org/abs/2406.15279},
  archivePrefix={arXiv},
  eprint={2406.15279},
  primaryClass={cs.AI},
}
```
