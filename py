diff --git a/.pre-commit-config.yaml b/.pre-commit-config.yaml
index f12c8b8..37b2203 100644
--- a/.pre-commit-config.yaml
+++ b/.pre-commit-config.yaml
@@ -1,18 +1,18 @@
 repos:
-  - repo: https://github.com/PyCQA/flake8
-    rev: 3.8.3
+  - repo: https://gitee.com/openmmlab/mirrors-flake8
+    rev: 5.0.4
     hooks:
       - id: flake8
-  - repo: https://github.com/PyCQA/isort
-    rev: 5.10.1
+  - repo: https://gitee.com/openmmlab/mirrors-isort
+    rev: 5.11.5
     hooks:
       - id: isort
-  - repo: https://github.com/pre-commit/mirrors-yapf
-    rev: v0.30.0
+  - repo: https://gitee.com/openmmlab/mirrors-yapf
+    rev: v0.32.0
     hooks:
       - id: yapf
-  - repo: https://github.com/pre-commit/pre-commit-hooks
-    rev: v4.1.0
+  - repo: https://gitee.com/openmmlab/mirrors-pre-commit-hooks
+    rev: v4.3.0
     hooks:
       - id: trailing-whitespace
       - id: check-yaml
@@ -23,4 +23,4 @@ repos:
       - id: fix-encoding-pragma
         args: ["--remove"]
       - id: mixed-line-ending
-        args: ["--fix=lf"]
+        args: ["--fix=lf"]
\ No newline at end of file
diff --git a/README.md b/README.md
index 65d5e07..735a27e 100644
--- a/README.md
+++ b/README.md
@@ -10,25 +10,24 @@
 [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 
-
 <div align="center">
 
 👋🤗🤗👋 Join our [WeChat](assets/wechat.jpg).
+
 </div>
 
 # Efficient Finetuning of Quantized LLMs  --- 低资源的大语言模型量化训练/部署方案
 
-
 <div align="center">
 
 [中文](README_zh.md) | English
+
 </div>
 
 This is the repo for the `Efficient Finetuning of Quantized LLMs` project, which aims to build and share instruction-following Chinese `baichuan-7b/LLaMA/Pythia/GLM` model tuning methods which can be trained on **a single Nvidia RTX-2080TI**, multi-round chatbot which can be trained on **a single Nvidia RTX-3090** with the context len 2048.
 
 We uses [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) for quantization and is integrated with Huggingface's [PEFT](https://github.com/huggingface/peft) and [transformers](https://github.com/huggingface/transformers/) libraries.
 
-
 ## News
 
 - [23/07/20] Now we support training the **LLaMA-2** models in this repo. Try `--model_name_or_path Llama-2-7b-hf` argument to use the LLaMA-2 model.
@@ -67,6 +66,7 @@ We uses [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) for quantiza
 As of now, we support the following datasets, most of which are all available in the [Hugging Face datasets library](https://huggingface.co/datasets/).
 
 - For supervised fine-tuning:
+
   - [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca)
   - [Stanford Alpaca (Chinese)](https://github.com/ymcui/Chinese-LLaMA-Alpaca)
   - [Hello-SimpleAI/HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3)
@@ -88,6 +88,7 @@ As of now, we support the following datasets, most of which are all available in
   - [Evol-Instruct](https://huggingface.co/datasets/victor123/evol_instruct_70k)
 
 - For reward model training:
+
   - [HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf)
   - [Open Assistant](https://huggingface.co/datasets/OpenAssistant/oasst1)
   - [GPT-4 Generated Data](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
@@ -109,7 +110,6 @@ We provide a number of data preprocessing tools in the [data](./chatllms/data) f
 - [sft_dataset.py](./chatllms/data/sft_dataset.py) :  Supervised fine-tuning dataset class and collator
 - [conv_dataset.py](./chatllms/data/conv_dataset.py) :  Conversation dataset class and collator
 
-
 ## Model Zoo
 
 We provide a number of models in the [Hugging Face model hub](https://huggingface.co/decapoda-research). These models are trained with QLoRA and can be used for inference and finetuning. We provide the following models:
@@ -129,13 +129,17 @@ We provide a number of models in the [Hugging Face model hub](https://huggingfac
 - CUDA >= 11.0
 
 - Python 3.8+ and PyTorch 1.13.1+
+
 - 🤗Transformers, Datasets, Accelerate, PEFT and bitsandbytes
+
 - jieba, rouge_chinese and nltk (used at evaluation)
+
 - gradio (used in gradio_webserver.py)
 
 ### Install required packages
 
 To load models in 4bits with transformers and bitsandbytes, you have to install accelerate and transformers from source and make sure you have the latest version of the bitsandbytes library (0.39.0). You can achieve the above with the following commands:
+
 ```bash
 pip install -q -U bitsandbytes
 pip install -q -U git+https://github.com/huggingface/transformers.git
@@ -154,11 +158,11 @@ cd Efficient-Tuning-LLMs
 
 ## Getting Started
 
-| main function                            | Useage                                                                               | Scripts                                    |
-| ---------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------ |
-| [train.py](./train.py)                   | Full finetune LLMs on  SFT datasets                                                  | [full_finetune](./scripts/full_finetune)   |
-| [train_lora.py](./train_lora.py)         | Finetune LLMs by using Lora  (Low-Rank Adaptation of Large Language Models finetune) | [lora_finetune](./scripts/lora_finetune)   |
-| [train_qlora.py](train_qlora.py)         | Finetune LLMs by using QLora (QLoRA: Efficient Finetuning of Quantized LLMs)         | [qlora_finetune](./scripts/qlora_finetune) |
+| main function                    | Useage                                                                               | Scripts                                    |
+| -------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------ |
+| [train.py](./train.py)           | Full finetune LLMs on  SFT datasets                                                  | [full_finetune](./scripts/full_finetune)   |
+| [train_lora.py](./train_lora.py) | Finetune LLMs by using Lora  (Low-Rank Adaptation of Large Language Models finetune) | [lora_finetune](./scripts/lora_finetune)   |
+| [train_qlora.py](train_qlora.py) | Finetune LLMs by using QLora (QLoRA: Efficient Finetuning of Quantized LLMs)         | [qlora_finetune](./scripts/qlora_finetune) |
 
 ### QLora int4 Finetune
 
@@ -170,6 +174,7 @@ python train_qlora.py --model_name_or_path <path_or_name>
 ```
 
 For models larger than 13B, we recommend adjusting the learning rate:
+
 ```bash
 python train_qlora.py –learning_rate 0.0001 --model_name_or_path <path_or_name>
 ```
@@ -220,7 +225,9 @@ python train_qlora.py \
 To find more scripts for finetuning and inference, please refer to the `scripts` folder.
 
 ## Quantization
+
 Quantization parameters are controlled from the `BitsandbytesConfig` ([see HF documenation](https://huggingface.co/docs/transformers/main_classes/quantization#transformers.BitsAndBytesConfig)) as follows:
+
 - Loading in 4 bits is activated through `load_in_4bit`
 - The datatype used for the linear layer computations with `bnb_4bit_compute_dtype`
 - Nested quantization is activated through `bnb_4bit_use_double_quant`
@@ -245,20 +252,25 @@ Quantization parameters are controlled from the `BitsandbytesConfig` ([see HF do
 ## Tutorials and Demonstrations
 
 We provide two Google Colab notebooks to demonstrate the use of 4bit models in inference and fine-tuning. These notebooks are intended to be a starting point for further research and development.
+
 - [Basic usage Google Colab notebook](https://colab.research.google.com/drive/1ge2F1QSK8Q7h0hn3YKuBCOAS0bK8E0wf?usp=sharing) - This notebook shows how to use 4bit models in inference with all their variants, and how to run GPT-neo-X (a 20B parameter model) on a free Google Colab instance 🤯
 - [Fine tuning Google Colab notebook](https://colab.research.google.com/drive/1VoYNfYDKcKRQRor98Zbf2-9VQTtGJ24k?usp=sharing) - This notebook shows how to fine-tune a 4bit model on a downstream task using the Hugging Face ecosystem. We show that it is possible to fine tune GPT-neo-X 20B on a Google Colab instance!
 
 Other examples are found under the examples/ folder.
+
 - Finetune LLama-7B (ex1)
 - Finetune GPT-neo-X 20B (ex2)
 
 ## Using Local Datasets
+
 You can specify the path to your dataset using the --dataset argument. If the --dataset_format argument is not set, it will default to the Alpaca format. Here are a few examples:
 
 - Training with an alpaca format dataset:
+
 ```python
 python train_qlora.py --dataset="path/to/your/dataset"
 ```
+
 - Training with a self-instruct format dataset:
 
 ```python
@@ -266,9 +278,11 @@ python train_qlora.py --dataset="path/to/your/dataset" --dataset_format="self-in
 ```
 
 ## Multi GPU
+
 Multi GPU training and inference work out-of-the-box with Hugging Face's Accelerate. Note that the per_device_train_batch_size and per_device_eval_batch_size arguments are global batch sizes unlike what their name suggest.
 
 When loading a model for training or inference on multiple GPUs you should pass something like the following to AutoModelForCausalLM.from_pretrained():
+
 ```python
 device_map = "auto"
 max_memory = {i: '46000MB' for i in range(torch.cuda.device_count())}
@@ -303,15 +317,15 @@ python gradio_webserver.py \
     --lora_model_name_or_path  `path/to/your/model_dir`
 ```
 
-
 ## Sample Outputs
+
 We provide generations for the models described in the paper for both OA and Vicuna queries in the `eval/generations` folder. These are intended to foster further research on model evaluation and analysis.
 
 Can you distinguish ChatGPT from Guanaco? Give it a try!
 You can access [the model response Colab here](https://colab.research.google.com/drive/1kK6xasHiav9nhiRUJjPMZb4fAED4qRHb?usp=sharing) comparing ChatGPT and Guanaco 65B on Vicuna prompts.
 
-
 ## Known Issues and Limitations
+
 Here a list of known issues and bugs. If your issue is not reported here, please open a new issue and describe the problem.
 
 1. 4-bit inference is slow. Currently, our 4-bit inference implementation is not yet integrated with the 4-bit matrix multiplication
@@ -319,13 +333,12 @@ Here a list of known issues and bugs. If your issue is not reported here, please
 3. Currently, using `bnb_4bit_compute_type='fp16'` can lead to instabilities. For 7B LLaMA, only 80% of finetuning runs complete without error. We have solutions, but they are not integrated yet into bitsandbytes.
 4. Make sure that `tokenizer.bos_token_id = 1` to avoid generation issues.
 
-
 ## License
 
 `Efficient Finetuning of Quantized LLMs` is released under the Apache 2.0 license.
 
-
 ## Acknowledgements
+
 We thank the Huggingface team, in particular Younes Belkada, for their support integrating QLoRA with PEFT and transformers libraries.
 
 We appreciate the work by many open-source contributors, especially:
@@ -338,7 +351,6 @@ We appreciate the work by many open-source contributors, especially:
 - [Vicuna](https://github.com/lm-sys/FastChat/)
 - [xTuring](https://github.com/stochasticai/xTuring)
 
-
 ## Citation
 
 Please cite the repo if you use the data or code in this repo.
diff --git a/README_zh.md b/README_zh.md
index 00b7078..3b2d883 100644
--- a/README_zh.md
+++ b/README_zh.md
@@ -13,22 +13,22 @@
 <div align="center">
 
 👋🤗🤗👋 加入我们 [WeChat](assets/wechat.jpg).
-</div>
 
+</div>
 
 # Efficient Finetuning of Quantized LLMs --- 低资源的大语言模型量化训练/部署方案
 
-
 <div align="center">
 
 [English](README.md) | 中文
+
 </div>
 
 这里是`Efficient Finetuning of Quantized LLMs`项目的存储库，旨在构建和开源 遵循指令的`baichuan/LLaMA/Pythia/GLM`中文大模型微调训练方法，该方法可以在**单个 Nvidia RTX-2080TI**上进行训练，多轮聊天机器人可以在**单个 Nvidia RTX-3090**上进行上下文长度 2048的模型训练。
 
 我们使用[bitsandbytes](https://github.com/TimDettmers/bitsandbytes)进行量化，并与Huggingface的[PEFT](https://github.com/huggingface/peft)和 [transformers](https://github.com/huggingface/transformers/)库集成。
 
- 本项目主要内容如下：
+本项目主要内容如下：
 
 - 📗 支持全量参数指令微调、LoRA指令微调(后续将会提供支持)， QLoRA低成本高效指令微调。
 - 📗 支持绝大部分主流的开源大模型，如百川 baichuan、Ziya、Bloom、LLaMA、Pythia、OPT等。
@@ -88,6 +88,7 @@ QLora 引入了多种创新，旨在在不牺牲性能的情况下减少内存
 截至目前，我们支持以下数据集，这些数据集都可以在 [Hugging Face Datasets](https://huggingface.co/datasets) 上找到。我们将在未来添加更多数据集。
 
 - For supervised fine-tuning:
+
   - [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca)
   - [Stanford Alpaca (Chinese)](https://github.com/ymcui/Chinese-LLaMA-Alpaca)
   - [Hello-SimpleAI/HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3)
@@ -103,16 +104,16 @@ QLora 引入了多种创新，旨在在不牺牲性能的情况下减少内存
   - [Evol-Instruct](https://huggingface.co/datasets/victor123/evol_instruct_70k)
 
 - For reward model training:
+
   - [HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf)
   - [Open Assistant](https://huggingface.co/datasets/OpenAssistant/oasst1)
   - [GPT-4 Generated Data](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
   - [GPT-4 Generated Data (Chinese)](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
 
-
 请参考 [data/README.md](data/README.md) 了解如何使用这些数据集训练自己的 ChatGPT。如果您想探索更多数据集，请参考 [awesome-instruction-datasets](https://github.com/jianzhnie/awesome-instruction-datasets). 默认情况下，我们使用 [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) 数据集进行训练和微调。
 
-
 部分数据集需要 huggingface 的账号认证确认才能使用，我们建议使用以下命令登录您的 Hugging Face 账户。
+
 ```bash
 pip install --upgrade huggingface_hub
 huggingface-cli login
@@ -126,7 +127,6 @@ huggingface-cli login
 - sft_dataset.py：有监督的对话数据集类
 - conv_dataset.py：多轮对话数据集类
 
-
 ## 模型仓库
 
 我们在 [Hugging Face ](https://huggingface.co/GaussianTech/)提供了许多模型。这些模型经过Self- Instruct 数据集的训练，可用于推理和微调：
diff --git a/assets/guanaco.svg b/assets/guanaco.svg
index 64e341f..c126704 100644
--- a/assets/guanaco.svg
+++ b/assets/guanaco.svg
@@ -1,98 +1,98 @@
-<?xml version="1.0" encoding="utf-8"?>
-<!-- Generator: Moho 12.5 build 22438 -->
-<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
-<svg version="1.1" id="Frame_0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280px" height="720px">
-<g id="Layer_6">
-<path fill="#e7e1cb" fill-rule="evenodd" stroke="none" d="M 575.641 397.169 C 571.045 395.618 564.453 395.465 559.658 394.735 C 559.658 394.728 561.135 347.274 561.767 326.934 C 561.778 326.933 639.181 322.293 672.359 320.304 C 672.363 320.299 706.382 287.200 713.768 268.802 C 718.782 256.311 716.988 237.559 718.634 224.200 C 721.710 199.227 726.725 166.050 730.193 141.129 C 730.196 141.131 749.293 156.200 757.479 162.659 C 757.446 165.866 757.282 170.142 757.370 173.348 C 757.492 177.800 757.854 183.735 758.370 188.159 C 759.284 195.991 761.099 206.369 762.836 214.061 C 764.483 221.351 767.704 230.808 769.551 238.050 C 770.795 242.927 772.504 249.431 773.349 254.394 C 774.264 259.769 774.983 267.021 775.306 272.464 C 775.828 281.268 775.939 293.054 775.476 301.860 C 775.073 309.515 774.056 319.717 772.688 327.260 C 769.614 344.214 763.885 366.603 757.862 382.746 C 754.884 390.730 750.769 401.554 745.742 408.434 C 741.967 413.601 735.899 420.061 730.287 423.134 C 710.197 434.133 677.960 435.107 655.088 436.310 C 651.693 436.489 647.134 436.327 643.762 435.891 C 639.247 435.307 633.259 434.026 628.971 432.494 C 625.455 431.238 620.978 428.969 617.796 427.016 C 612.282 423.633 605.772 417.890 600.705 413.869 C 599.091 412.589 596.988 410.822 595.379 409.536 C 593.330 407.896 590.687 405.580 588.500 404.130 C 584.843 401.707 579.797 398.571 575.641 397.169 M 757.479 162.659 C 757.479 162.659 757.479 162.659 757.479 162.659 Z"/>
-<path fill="none" stroke="#e7e1cb" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 559.658 394.735 C 559.658 394.735 559.658 394.735 559.658 394.735 C 564.453 395.465 571.045 395.618 575.641 397.169 C 579.797 398.571 584.843 401.707 588.500 404.130 C 590.687 405.580 593.330 407.896 595.379 409.536 C 596.988 410.822 599.091 412.589 600.705 413.869 C 605.772 417.890 612.282 423.633 617.796 427.016 C 620.978 428.969 625.455 431.238 628.971 432.494 C 633.259 434.026 639.247 435.307 643.762 435.891 C 647.134 436.327 651.693 436.489 655.088 436.310 C 677.960 435.107 710.197 434.133 730.287 423.134 C 735.899 420.061 741.967 413.601 745.742 408.434 C 750.769 401.554 754.884 390.730 757.862 382.746 C 763.885 366.603 769.614 344.214 772.688 327.260 C 774.056 319.717 775.073 309.515 775.476 301.860 C 775.939 293.054 775.828 281.268 775.306 272.464 C 774.983 267.021 774.264 259.769 773.349 254.394 C 772.504 249.431 770.795 242.927 769.551 238.050 C 767.704 230.808 764.483 221.351 762.836 214.061 C 761.099 206.369 759.284 195.991 758.370 188.159 C 757.854 183.735 757.492 177.800 757.370 173.348 C 757.282 170.142 757.446 165.866 757.479 162.659 C 757.479 162.659 757.479 162.659 757.479 162.659 C 749.293 156.200 730.196 141.131 730.193 141.129 C 730.193 141.129 730.193 141.129 730.193 141.129 C 726.725 166.050 721.710 199.227 718.634 224.200 C 716.988 237.559 718.782 256.311 713.768 268.802 C 706.382 287.200 672.363 320.299 672.359 320.304 C 672.359 320.304 672.359 320.304 672.359 320.304 C 639.181 322.293 561.778 326.933 561.767 326.934 C 561.767 326.934 561.767 326.934 561.767 326.934 C 561.135 347.274 559.658 394.728 559.658 394.735 "/>
-<path fill="#5f524a" fill-rule="evenodd" stroke="#5f524a" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 747.648 113.356 C 744.021 115.471 737.946 114.709 733.789 115.289 C 733.789 115.289 733.789 115.289 733.789 115.289 C 735.113 112.385 736.646 108.394 738.203 105.607 C 741.734 99.287 746.889 90.956 751.928 85.757 C 755.456 82.116 761.237 78.447 765.406 75.563 C 768.524 73.407 772.673 70.464 776.076 68.797 C 778.100 67.805 780.930 66.727 783.114 66.175 C 784.317 65.871 785.963 65.496 787.203 65.555 C 788.177 65.602 789.479 65.903 790.363 66.315 C 791.095 66.655 792.272 67.133 792.541 67.894 C 792.872 68.830 792.068 70.195 791.585 71.063 C 790.804 72.466 789.094 73.865 787.958 75.000 C 786.271 76.684 783.884 78.787 782.090 80.357 C 779.570 82.562 776.045 85.310 773.528 87.519 C 769.580 90.982 764.450 95.753 760.674 99.402 C 758.141 101.849 754.774 105.129 752.400 107.730 C 750.910 109.361 749.557 112.244 747.648 113.356 Z"/>
-<path fill="#6d6057" fill-rule="evenodd" stroke="#6d6057" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 741.736 111.321 C 738.370 114.076 732.141 114.631 728.029 116.050 C 728.029 116.050 728.029 116.050 728.029 116.050 C 729.040 112.678 730.097 108.080 731.400 104.809 C 734.080 98.083 738.520 89.421 742.544 83.403 C 745.424 79.096 749.784 73.649 753.562 70.102 C 756.459 67.382 760.768 64.202 764.225 62.243 C 766.038 61.215 768.580 59.999 770.596 59.472 C 771.891 59.134 773.689 58.962 775.027 58.964 C 776.002 58.966 777.329 59.026 778.258 59.324 C 779.026 59.570 780.253 59.898 780.615 60.620 C 781.060 61.507 780.432 62.962 780.061 63.883 C 779.461 65.372 777.991 67.016 776.953 68.241 C 775.458 70.005 773.101 72.019 771.465 73.653 C 769.039 76.079 765.726 79.241 763.436 81.795 C 759.956 85.676 755.628 91.130 752.517 95.312 C 750.379 98.185 747.740 102.168 745.750 105.146 C 744.523 106.983 743.446 109.922 741.736 111.321 Z"/>
-<path fill="#a89984" fill-rule="evenodd" stroke="none" d="M 703.345 591.533 C 703.084 591.940 702.744 592.488 702.487 592.897 C 702.488 592.898 708.174 594.324 710.670 594.456 C 712.426 594.549 714.772 594.257 716.515 594.027 C 719.978 593.571 724.639 592.909 727.935 591.750 C 729.735 591.117 731.917 589.759 733.624 588.906 C 733.624 588.906 729.281 588.297 727.461 587.839 C 725.607 587.373 723.095 586.739 721.416 585.824 C 720.348 585.242 718.902 584.339 718.216 583.335 C 718.045 583.085 717.914 582.687 717.864 582.389 C 717.727 581.575 717.818 580.441 718.035 579.645 C 718.316 578.615 719.407 577.522 719.681 576.490 C 719.940 575.514 719.788 574.137 719.819 573.129 C 719.854 571.964 719.966 570.408 719.894 569.245 C 719.846 568.475 719.711 567.449 719.541 566.696 C 719.251 565.414 718.677 563.748 718.178 562.532 C 717.751 561.492 716.768 560.270 716.512 559.175 C 716.406 558.722 716.470 558.089 716.459 557.624 C 716.401 555.110 716.376 551.756 716.387 549.241 C 716.417 542.834 716.700 534.294 716.823 527.888 C 716.930 522.340 717.025 514.941 717.158 509.394 C 717.171 508.838 717.194 508.097 717.210 507.541 C 717.208 507.541 702.211 507.631 695.783 507.670 C 696.484 516.039 697.398 527.200 698.119 535.568 C 698.411 538.963 698.908 543.482 699.117 546.884 C 699.406 551.582 699.823 557.862 699.637 562.565 C 699.624 562.903 699.638 563.365 699.535 563.687 C 699.260 564.553 698.267 565.405 697.903 566.237 C 697.397 567.393 696.997 569.061 696.883 570.317 C 696.789 571.355 696.851 572.770 697.087 573.785 C 697.360 574.959 697.941 576.515 698.661 577.481 C 699.727 578.910 701.750 580.320 703.313 581.179 C 704.029 581.573 705.241 581.606 705.867 582.133 C 706.319 582.513 706.780 583.231 706.896 583.810 C 707.093 584.793 706.618 586.157 706.248 587.089 C 705.660 588.569 704.203 590.192 703.345 591.533 M 695.783 507.670 C 695.783 507.670 695.783 507.670 695.783 507.670 Z"/>
-<path fill="none" stroke="#978e71" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 702.487 592.897 C 702.487 592.897 702.487 592.897 702.487 592.897 C 702.744 592.488 703.084 591.940 703.345 591.533 C 704.203 590.192 705.660 588.569 706.248 587.089 C 706.618 586.157 707.093 584.793 706.896 583.810 C 706.780 583.231 706.319 582.513 705.867 582.133 C 705.241 581.606 704.029 581.573 703.313 581.179 C 701.750 580.320 699.727 578.910 698.661 577.481 C 697.941 576.515 697.360 574.959 697.087 573.785 C 696.851 572.770 696.789 571.355 696.883 570.317 C 696.997 569.061 697.397 567.393 697.903 566.237 C 698.267 565.405 699.260 564.553 699.535 563.687 C 699.638 563.365 699.624 562.903 699.637 562.565 C 699.823 557.862 699.406 551.582 699.117 546.884 C 698.908 543.482 698.411 538.963 698.119 535.568 C 697.398 527.200 696.484 516.039 695.783 507.670 C 695.783 507.670 695.783 507.670 695.783 507.670 C 702.211 507.631 717.208 507.541 717.210 507.541 C 717.210 507.541 717.210 507.541 717.210 507.541 C 717.194 508.097 717.171 508.838 717.158 509.394 C 717.025 514.941 716.930 522.340 716.823 527.888 C 716.700 534.294 716.417 542.834 716.387 549.241 C 716.376 551.756 716.401 555.110 716.459 557.624 C 716.470 558.089 716.406 558.722 716.512 559.175 C 716.768 560.270 717.751 561.492 718.178 562.532 C 718.677 563.748 719.251 565.414 719.541 566.696 C 719.711 567.449 719.846 568.475 719.894 569.245 C 719.966 570.408 719.854 571.964 719.819 573.129 C 719.788 574.137 719.940 575.514 719.681 576.490 C 719.407 577.522 718.316 578.615 718.035 579.645 C 717.818 580.441 717.727 581.575 717.864 582.389 C 717.914 582.687 718.045 583.085 718.216 583.335 C 718.902 584.339 720.348 585.242 721.416 585.824 C 723.095 586.739 725.607 587.373 727.461 587.839 C 729.281 588.297 733.624 588.906 733.624 588.906 C 733.624 588.906 733.624 588.906 733.624 588.906 C 731.917 589.759 729.735 591.117 727.935 591.750 C 724.639 592.909 719.978 593.571 716.515 594.027 C 714.772 594.257 712.426 594.549 710.670 594.456 C 708.174 594.324 702.488 592.898 702.487 592.897 "/>
-<path fill="#a89984" fill-rule="evenodd" stroke="none" d="M 516.067 588.955 C 515.802 590.088 515.291 591.556 514.959 592.670 C 514.960 592.671 521.683 595.626 524.768 595.984 C 526.745 596.213 529.406 595.707 531.382 595.474 C 534.782 595.072 539.589 595.173 542.643 593.625 C 543.848 593.014 545.002 591.532 546.013 590.635 C 546.012 590.635 541.506 588.937 539.696 587.956 C 538.386 587.246 536.595 586.279 535.559 585.208 C 534.626 584.244 533.755 582.632 533.193 581.414 C 532.947 580.880 532.641 580.141 532.567 579.558 C 532.463 578.722 532.699 577.595 532.822 576.761 C 532.969 575.765 533.304 574.461 533.503 573.473 C 533.702 572.485 534.045 571.178 534.147 570.174 C 534.253 569.132 534.244 567.728 534.179 566.682 C 534.125 565.819 533.939 564.679 533.803 563.825 C 533.605 562.588 533.389 560.921 533.025 559.723 C 532.739 558.782 532.116 557.616 531.758 556.700 C 531.404 555.795 530.895 554.595 530.650 553.654 C 530.099 551.542 529.791 548.629 529.593 546.455 C 529.010 540.074 529.326 531.505 529.072 525.102 C 528.694 515.568 527.597 502.883 527.289 493.346 C 527.271 492.790 527.269 492.049 527.260 491.493 C 527.258 491.493 510.812 492.222 503.762 492.534 C 505.308 504.845 507.243 521.277 508.914 533.572 C 509.374 536.955 510.209 541.437 510.538 544.835 C 510.978 549.377 511.708 555.488 511.252 560.029 C 511.202 560.520 511.038 561.162 510.915 561.640 C 510.713 562.426 510.323 563.439 510.112 564.223 C 509.782 565.446 509.317 567.083 509.184 568.343 C 508.991 570.165 509.012 572.640 509.304 574.449 C 509.430 575.228 509.566 576.339 510.030 576.976 C 511.133 578.492 514.033 578.870 515.432 580.117 C 515.940 580.570 516.501 581.303 516.851 581.887 C 517.171 582.420 517.817 583.185 517.672 583.789 C 517.588 584.140 516.987 584.311 516.806 584.623 C 516.146 585.764 516.368 587.672 516.067 588.955 M 503.762 492.534 C 503.762 492.534 503.762 492.534 503.762 492.534 Z"/>
-<path fill="none" stroke="#978e71" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 514.959 592.670 C 514.959 592.670 514.959 592.670 514.959 592.670 C 515.291 591.556 515.802 590.088 516.067 588.955 C 516.368 587.672 516.146 585.764 516.806 584.623 C 516.987 584.311 517.588 584.140 517.672 583.789 C 517.817 583.185 517.171 582.420 516.851 581.887 C 516.501 581.303 515.940 580.570 515.432 580.117 C 514.033 578.870 511.133 578.492 510.030 576.976 C 509.566 576.339 509.430 575.228 509.304 574.449 C 509.012 572.640 508.991 570.165 509.184 568.343 C 509.317 567.083 509.782 565.446 510.112 564.223 C 510.323 563.439 510.713 562.426 510.915 561.640 C 511.038 561.162 511.202 560.520 511.252 560.029 C 511.708 555.488 510.978 549.377 510.538 544.835 C 510.209 541.437 509.374 536.955 508.914 533.572 C 507.243 521.277 505.308 504.845 503.762 492.534 C 503.762 492.534 503.762 492.534 503.762 492.534 C 510.812 492.222 527.258 491.493 527.260 491.493 C 527.260 491.493 527.260 491.493 527.260 491.493 C 527.269 492.049 527.271 492.790 527.289 493.346 C 527.597 502.883 528.694 515.568 529.072 525.102 C 529.326 531.505 529.010 540.074 529.593 546.455 C 529.791 548.629 530.099 551.542 530.650 553.654 C 530.895 554.595 531.404 555.795 531.758 556.700 C 532.116 557.616 532.739 558.782 533.025 559.723 C 533.389 560.921 533.605 562.588 533.803 563.825 C 533.939 564.679 534.125 565.819 534.179 566.682 C 534.244 567.728 534.253 569.132 534.147 570.174 C 534.045 571.178 533.702 572.485 533.503 573.473 C 533.304 574.461 532.969 575.765 532.822 576.761 C 532.699 577.595 532.463 578.722 532.567 579.558 C 532.641 580.141 532.947 580.880 533.193 581.414 C 533.755 582.632 534.626 584.244 535.559 585.208 C 536.595 586.279 538.386 587.246 539.696 587.956 C 541.506 588.937 546.012 590.635 546.013 590.635 C 546.013 590.635 546.013 590.635 546.013 590.635 C 545.002 591.532 543.848 593.014 542.643 593.625 C 539.589 595.173 534.782 595.072 531.382 595.474 C 529.406 595.707 526.745 596.213 524.768 595.984 C 521.683 595.626 514.960 592.671 514.959 592.670 "/>
-<path fill="#9d4c0b" fill-rule="evenodd" stroke="#9d4c0b" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 518.617 276.432 C 516.417 274.744 513.065 273.094 510.562 271.901 C 508.274 270.810 505.192 269.291 502.709 268.780 C 498.331 267.879 492.191 267.795 487.809 268.679 C 484.279 269.392 479.845 271.496 476.734 273.311 C 473.258 275.338 469.138 278.857 466.163 281.566 C 463.335 284.141 459.805 287.852 457.404 290.829 C 455.551 293.126 453.264 296.353 451.818 298.925 C 450.392 301.460 448.760 305.010 447.856 307.775 C 446.956 310.529 446.190 314.342 445.833 317.216 C 445.424 320.517 445.081 324.994 445.467 328.298 C 445.764 330.842 446.696 334.175 447.644 336.555 C 448.610 338.977 450.326 342.039 451.818 344.177 C 453.877 347.127 457.141 350.696 459.769 353.152 C 463.465 356.606 469.159 360.303 473.184 363.367 C 473.184 363.367 473.184 363.367 473.184 363.367 C 480.937 358.346 492.927 353.564 499.029 346.630 C 505.247 339.563 506.103 325.166 512.567 318.323 C 516.475 314.185 526.270 313.724 528.907 308.680 C 532.304 302.184 527.089 291.672 526.310 284.383 C 526.310 284.383 526.310 284.383 526.310 284.383 C 526.328 284.354 521.250 278.452 518.617 276.432 Z"/>
-<path fill="#8a7b66" fill-rule="evenodd" stroke="none" d="M 713.483 592.015 C 716.741 591.871 721.117 591.756 724.318 591.135 C 726.527 590.706 729.267 589.266 731.495 588.958 C 733.037 588.746 735.140 588.796 736.681 589.005 C 738.231 589.215 740.333 589.624 741.719 590.350 C 742.938 590.988 744.621 592.065 745.232 593.298 C 745.745 594.331 745.808 596.030 745.474 597.134 C 745.056 598.522 743.623 600.031 742.486 600.930 C 740.439 602.550 737.015 603.700 734.490 604.363 C 731.205 605.225 726.615 605.304 723.224 605.493 C 720.441 605.648 716.717 605.784 713.936 605.615 C 712.458 605.524 710.475 605.355 709.039 604.993 C 707.546 604.617 705.485 604.066 704.252 603.144 C 703.223 602.375 702.089 600.968 701.610 599.776 C 701.201 598.759 701.163 597.239 701.214 596.144 C 701.248 595.409 701.453 594.436 701.676 593.734 C 701.806 593.325 702.019 592.784 702.253 592.424 C 702.329 592.305 702.538 592.086 702.545 592.092 C 702.553 592.100 710.205 592.159 713.483 592.015 Z"/>
-<path fill="#77674e" d="M 713.479 591.905 C 716.738 591.761 721.106 591.646 724.297 591.027 L 724.339 591.243 C 721.128 591.865 716.745 591.981 713.488 592.124 L 713.479 591.905 Z"/>
-<path fill="#77674e" d="M 724.297 591.027 C 726.488 590.603 729.230 589.162 731.480 588.850 L 731.510 589.067 C 729.303 589.370 726.566 590.809 724.339 591.243 L 724.297 591.027 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 724.297 591.027 L 724.339 591.243 "/>
-<path fill="#77674e" d="M 731.480 588.850 C 733.032 588.636 735.147 588.686 736.696 588.896 L 736.667 589.114 C 735.132 588.905 733.042 588.856 731.510 589.067 L 731.480 588.850 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 731.480 588.850 L 731.510 589.067 "/>
-<path fill="#77674e" d="M 736.696 588.896 C 738.250 589.107 740.367 589.520 741.770 590.252 L 741.668 590.447 C 740.299 589.729 738.213 589.323 736.667 589.114 L 736.696 588.896 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 736.696 588.896 L 736.667 589.114 "/>
-<path fill="#77674e" d="M 741.770 590.252 C 742.994 590.893 744.699 591.988 745.331 593.249 L 745.134 593.347 C 744.543 592.143 742.882 591.083 741.668 590.447 L 741.770 590.252 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 741.770 590.252 L 741.668 590.447 "/>
-<path fill="#77674e" d="M 745.331 593.249 C 745.852 594.308 745.917 596.041 745.580 597.166 L 745.369 597.102 C 745.698 596.020 745.637 594.354 745.134 593.347 L 745.331 593.249 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 745.331 593.249 L 745.134 593.347 "/>
-<path fill="#77674e" d="M 745.580 597.166 C 745.148 598.581 743.698 600.111 742.554 601.016 L 742.418 600.844 C 743.548 599.951 744.963 598.462 745.369 597.102 L 745.580 597.166 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 745.580 597.166 L 745.369 597.102 "/>
-<path fill="#77674e" d="M 742.554 601.016 C 740.489 602.648 737.047 603.805 734.518 604.469 L 734.462 604.256 C 736.983 603.595 740.389 602.452 742.418 600.844 L 742.554 601.016 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 742.554 601.016 L 742.418 600.844 "/>
-<path fill="#77674e" d="M 734.518 604.469 C 731.218 605.335 726.619 605.414 723.230 605.603 L 723.218 605.384 C 726.612 605.195 731.192 605.116 734.462 604.256 L 734.518 604.469 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 734.518 604.469 L 734.462 604.256 "/>
-<path fill="#77674e" d="M 723.230 605.603 C 720.446 605.758 716.717 605.894 713.929 605.724 L 713.942 605.505 C 716.718 605.674 720.436 605.539 723.218 605.384 L 723.230 605.603 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 723.230 605.603 L 723.218 605.384 "/>
-<path fill="#77674e" d="M 713.929 605.724 C 712.449 605.634 710.458 605.464 709.012 605.100 L 709.066 604.886 C 710.492 605.246 712.466 605.415 713.942 605.505 L 713.929 605.724 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 713.929 605.724 L 713.942 605.505 "/>
-<path fill="#77674e" d="M 709.012 605.100 C 707.518 604.723 705.440 604.167 704.186 603.232 L 704.317 603.056 C 705.529 603.966 707.574 604.510 709.066 604.886 L 709.012 605.100 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 709.012 605.100 L 709.066 604.886 "/>
-<path fill="#77674e" d="M 704.186 603.232 C 703.145 602.453 701.996 601.026 701.508 599.818 L 701.712 599.735 C 702.183 600.910 703.301 602.298 704.317 603.056 L 704.186 603.232 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 704.186 603.232 L 704.317 603.056 "/>
-<path fill="#77674e" d="M 701.508 599.818 C 701.093 598.779 701.053 597.239 701.104 596.139 L 701.324 596.149 C 701.273 597.240 701.310 598.740 701.712 599.735 L 701.508 599.818 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 701.508 599.818 L 701.712 599.735 "/>
-<path fill="#77674e" d="M 701.104 596.139 C 701.139 595.394 701.346 594.409 701.571 593.701 L 701.781 593.767 C 701.560 594.463 701.357 595.424 701.324 596.150 L 701.104 596.139 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 701.104 596.139 L 701.324 596.150 "/>
-<path fill="#77674e" d="M 701.571 593.701 C 701.703 593.287 701.921 592.735 702.160 592.364 L 702.345 592.483 C 702.118 592.833 701.910 593.362 701.781 593.767 L 701.571 593.701 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 701.571 593.701 L 701.781 593.767 "/>
-<path fill="#77674e" d="M 702.160 592.364 C 702.245 592.234 702.489 592.036 702.595 592.043 L 702.494 592.141 C 702.588 592.135 702.413 592.376 702.345 592.483 L 702.160 592.364 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 702.160 592.364 L 702.345 592.483 "/>
-<path fill="#77674e" d="M 702.595 592.043 C 702.553 592.030 710.204 592.049 713.479 591.905 L 713.488 592.124 C 710.206 592.269 702.552 592.170 702.495 592.141 L 702.595 592.043 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 702.595 592.043 L 702.495 592.141 "/>
-<path fill="#8a7b66" fill-rule="evenodd" stroke="none" d="M 525.681 591.775 C 528.779 591.875 532.932 592.081 536.013 591.740 C 538.135 591.505 540.843 590.382 542.974 590.259 C 544.450 590.174 546.438 590.368 547.885 590.670 C 549.335 590.972 551.294 591.490 552.559 592.259 C 553.658 592.927 555.182 594.018 555.672 595.207 C 556.074 596.186 556.010 597.751 555.619 598.735 C 555.119 599.991 553.640 601.257 552.507 601.996 C 550.436 603.346 547.113 604.142 544.678 604.569 C 541.498 605.126 537.146 604.870 533.918 604.802 C 531.271 604.746 527.733 604.606 525.108 604.253 C 523.715 604.065 521.850 603.771 520.514 603.336 C 519.131 602.886 517.221 602.246 516.113 601.303 C 515.206 600.531 514.225 599.167 513.858 598.033 C 513.549 597.076 513.622 595.680 513.751 594.682 C 513.837 594.010 514.104 593.134 514.366 592.509 C 514.520 592.142 514.762 591.662 515.009 591.351 C 515.091 591.247 515.305 591.061 515.310 591.068 C 515.317 591.076 522.564 591.674 525.681 591.775 Z"/>
-<path fill="#77674e" d="M 525.684 591.665 C 528.784 591.765 532.930 591.971 536.001 591.631 L 536.025 591.850 C 532.934 592.191 528.774 591.985 525.677 591.885 L 525.684 591.665 Z"/>
-<path fill="#77674e" d="M 536.001 591.631 C 538.105 591.399 540.815 590.276 542.968 590.149 L 542.981 590.369 C 540.870 590.489 538.165 591.611 536.025 591.850 L 536.001 591.631 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 536.001 591.631 L 536.025 591.850 "/>
-<path fill="#77674e" d="M 542.968 590.149 C 544.454 590.064 546.453 590.259 547.907 590.562 L 547.862 590.778 C 546.422 590.477 544.447 590.284 542.981 590.369 L 542.968 590.149 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 542.968 590.149 L 542.981 590.369 "/>
-<path fill="#77674e" d="M 547.907 590.562 C 549.361 590.865 551.334 591.388 552.616 592.165 L 552.502 592.353 C 551.253 591.592 549.309 591.079 547.862 590.778 L 547.907 590.562 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 547.907 590.562 L 547.862 590.778 "/>
-<path fill="#77674e" d="M 552.616 592.165 C 553.720 592.836 555.265 593.945 555.773 595.165 L 555.570 595.249 C 555.100 594.091 553.597 593.019 552.502 592.353 L 552.616 592.165 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 552.616 592.165 L 552.502 592.353 "/>
-<path fill="#77674e" d="M 555.773 595.165 C 556.183 596.171 556.119 597.771 555.721 598.776 L 555.517 598.694 C 555.902 597.732 555.965 596.200 555.570 595.249 L 555.773 595.165 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 555.773 595.165 L 555.570 595.249 "/>
-<path fill="#77674e" d="M 555.721 598.776 C 555.205 600.059 553.707 601.345 552.568 602.088 L 552.447 601.904 C 553.573 601.170 555.032 599.923 555.517 598.694 L 555.721 598.776 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 555.721 598.776 L 555.517 598.694 "/>
-<path fill="#77674e" d="M 552.568 602.088 C 550.477 603.449 547.136 604.249 544.697 604.677 L 544.659 604.460 C 547.090 604.034 550.396 603.244 552.447 601.904 L 552.568 602.088 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 552.568 602.088 L 552.447 601.904 "/>
-<path fill="#77674e" d="M 544.697 604.677 C 541.502 605.236 537.142 604.980 533.916 604.912 L 533.921 604.692 C 537.151 604.760 541.493 605.016 544.659 604.460 L 544.697 604.677 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 544.697 604.677 L 544.659 604.460 "/>
-<path fill="#77674e" d="M 533.916 604.912 C 531.267 604.856 527.724 604.716 525.094 604.362 L 525.123 604.144 C 527.742 604.496 531.274 604.636 533.921 604.692 L 533.916 604.912 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 533.916 604.912 L 533.921 604.692 "/>
-<path fill="#77674e" d="M 525.094 604.362 C 523.699 604.174 521.826 603.878 520.480 603.441 L 520.548 603.231 C 521.875 603.663 523.731 603.957 525.123 604.144 L 525.094 604.362 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 525.094 604.362 L 525.123 604.144 "/>
-<path fill="#77674e" d="M 520.480 603.441 C 519.096 602.991 517.169 602.343 516.042 601.387 L 516.185 601.219 C 517.272 602.148 519.165 602.782 520.548 603.231 L 520.480 603.441 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 520.480 603.441 L 520.548 603.231 "/>
-<path fill="#77674e" d="M 516.042 601.387 C 515.124 600.604 514.128 599.219 513.754 598.067 L 513.963 598.000 C 514.322 599.115 515.288 600.458 516.185 601.219 L 516.042 601.387 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 516.042 601.387 L 516.185 601.219 "/>
-<path fill="#77674e" d="M 513.754 598.067 C 513.439 597.087 513.513 595.670 513.641 594.668 L 513.860 594.696 C 513.732 595.689 513.658 597.065 513.963 598.000 L 513.754 598.067 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 513.754 598.067 L 513.963 598.000 "/>
-<path fill="#77674e" d="M 513.641 594.668 C 513.730 593.985 514.000 593.097 514.265 592.466 L 514.468 592.551 C 514.208 593.170 513.944 594.034 513.860 594.696 L 513.641 594.668 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 513.641 594.668 L 513.860 594.696 "/>
-<path fill="#77674e" d="M 514.265 592.466 C 514.420 592.096 514.669 591.605 514.922 591.282 L 515.095 591.419 C 514.856 591.720 514.620 592.189 514.468 592.551 L 514.265 592.466 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 514.265 592.466 L 514.468 592.551 "/>
-<path fill="#77674e" d="M 514.922 591.282 C 515.014 591.168 515.260 591.007 515.364 591.024 L 515.255 591.112 C 515.349 591.116 515.167 591.326 515.095 591.419 L 514.922 591.282 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 514.922 591.282 L 515.095 591.419 "/>
-<path fill="#77674e" d="M 515.364 591.023 C 515.323 591.007 522.571 591.564 525.684 591.665 L 525.677 591.885 C 522.557 591.784 515.311 591.146 515.256 591.112 L 515.364 591.023 Z"/>
-<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 515.364 591.023 L 515.256 591.112 "/>
-<path fill="#bb5e21" fill-rule="evenodd" stroke="none" d="M 574.703 359.609 C 573.834 356.357 573.509 351.846 572.997 348.519 C 572.997 348.518 572.327 342.534 572.618 339.989 C 572.818 338.234 573.260 335.836 574.134 334.302 C 574.750 333.222 575.864 331.833 576.984 331.294 C 577.754 330.923 578.969 330.862 579.817 330.974 C 581.024 331.133 582.556 331.848 583.566 332.528 C 585.900 334.100 588.147 337.244 589.919 339.430 C 592.292 342.357 594.888 346.686 597.162 349.690 C 599.459 352.723 602.347 356.968 605.151 359.540 C 607.674 361.855 611.587 364.307 614.581 365.967 C 617.513 367.593 621.589 369.537 624.809 370.470 C 628.467 371.530 633.572 372.601 637.370 372.317 C 639.348 372.169 641.906 371.307 643.744 370.562 C 645.916 369.681 648.524 367.904 650.579 366.775 C 651.796 366.106 653.285 364.852 654.643 364.558 C 655.864 364.294 657.688 364.265 658.799 364.836 C 659.797 365.348 660.768 366.665 661.201 367.699 C 662.122 369.899 661.693 373.260 661.570 375.642 C 661.446 378.049 660.696 381.198 660.370 383.586 C 660.124 385.384 659.666 387.775 659.630 389.589 C 659.555 393.495 660.172 398.713 660.933 402.544 C 662.482 410.340 666.078 420.382 668.916 427.806 C 670.357 431.576 672.965 436.322 674.362 440.108 C 676.082 444.767 677.793 451.180 679.056 455.983 C 680.705 462.252 682.432 470.726 683.883 477.043 C 684.639 480.334 685.521 484.753 686.406 488.012 C 687.669 492.664 689.505 498.840 691.262 503.330 C 691.830 504.783 692.492 506.806 693.414 508.065 C 694.658 509.763 696.841 511.682 698.687 512.693 C 700.399 513.630 702.986 514.349 704.929 514.522 C 707.195 514.724 710.315 514.412 712.463 513.661 C 714.104 513.088 716.085 511.770 717.413 510.648 C 718.847 509.437 720.512 507.507 721.503 505.913 C 723.193 503.193 724.493 499.055 725.485 496.011 C 726.989 491.395 728.413 485.060 729.359 480.299 C 730.639 473.858 731.676 465.152 732.584 458.649 C 733.327 453.325 734.101 446.198 734.903 440.883 C 736.436 430.715 738.913 417.226 740.776 407.113 C 742.350 398.566 744.775 387.231 746.295 378.674 C 747.467 372.081 749.099 363.293 749.868 356.641 C 750.044 355.124 750.697 353.033 750.274 351.565 C 749.986 350.561 749.078 349.379 748.270 348.717 C 747.520 348.102 746.226 347.736 745.316 347.398 C 744.495 347.093 743.195 347.114 742.521 346.554 C 741.954 346.084 741.545 345.104 741.360 344.392 C 741.033 343.129 741.211 341.332 741.421 340.045 C 741.865 337.324 743.366 333.905 744.424 331.358 C 745.442 328.908 747.330 325.878 748.306 323.411 C 749.410 320.617 750.650 316.781 751.235 313.833 C 751.970 310.129 752.211 305.068 752.367 301.295 C 752.571 296.372 752.235 289.800 752.206 284.873 C 752.154 276.232 752.551 264.701 752.157 256.069 C 751.788 247.985 750.879 237.215 749.759 229.200 C 748.843 222.641 747.069 213.978 745.662 207.506 C 744.454 201.948 742.691 194.565 741.143 189.091 C 740.108 185.430 738.611 180.576 737.302 177.003 C 736.594 175.070 735.257 172.636 734.697 170.656 C 733.861 167.703 733.308 163.611 733.141 160.547 C 732.945 156.943 733.371 152.123 733.707 148.529 C 733.915 146.311 734.409 143.378 734.710 141.170 C 733.610 132.812 732.143 121.668 731.043 113.310 C 728.919 114.612 725.909 116.096 723.962 117.650 C 721.664 119.483 718.981 122.392 717.144 124.687 C 715.598 126.621 713.775 129.398 712.599 131.578 C 710.850 134.821 709.055 139.421 707.829 142.896 C 706.489 146.693 705.021 151.872 704.139 155.800 C 703.257 159.725 702.468 165.041 701.958 169.031 C 701.010 176.454 700.145 186.406 699.813 193.881 C 699.398 203.217 699.265 215.700 699.787 225.031 C 699.924 227.476 700.428 230.710 700.608 233.153 C 700.923 237.432 701.270 243.151 701.225 247.441 C 701.193 250.401 701.060 254.362 700.628 257.291 C 700.189 260.261 699.485 264.262 698.319 267.029 C 697.167 269.758 694.961 273.122 693.031 275.370 C 691.195 277.508 688.372 280.099 685.956 281.551 C 683.270 283.165 679.258 284.638 676.181 285.232 C 671.852 286.067 665.885 285.637 661.484 285.366 C 657.772 285.137 652.859 284.377 649.191 283.762 C 640.422 282.292 628.926 279.310 620.197 277.616 C 612.046 276.034 601.155 274.014 592.940 272.806 C 586.083 271.798 576.908 270.641 570.000 270.080 C 565.629 269.725 559.784 269.438 555.399 269.394 C 552.870 269.369 549.492 269.389 546.971 269.590 C 544.782 269.765 541.863 270.100 539.719 270.570 C 534.793 271.650 528.366 273.763 523.717 275.717 C 519.477 277.499 514.050 280.417 510.140 282.839 C 506.075 285.357 500.788 288.991 497.231 292.187 C 493.722 295.339 489.612 300.152 486.701 303.863 C 484.074 307.213 480.866 311.918 478.714 315.591 C 476.687 319.052 474.094 323.778 472.744 327.556 C 471.309 331.574 470.332 337.225 469.616 341.432 C 469.339 343.053 469.091 345.235 468.935 346.873 C 468.688 349.478 468.222 352.968 468.391 355.579 C 468.699 360.324 470.084 366.600 471.656 371.087 C 473.574 376.562 477.566 383.275 480.443 388.313 C 483.643 393.915 488.604 400.964 491.997 406.451 C 494.059 409.785 496.878 414.194 498.734 417.647 C 500.232 420.434 502.105 424.225 503.292 427.158 C 504.636 430.480 506.383 434.974 507.057 438.494 C 507.676 441.728 507.749 446.157 507.713 449.450 C 507.667 453.646 507.290 459.262 506.520 463.387 C 506.007 466.140 504.815 469.695 503.978 472.367 C 503.080 475.230 501.321 478.883 500.720 481.823 C 500.302 483.864 500.114 486.662 500.158 488.745 C 500.196 490.512 500.434 492.879 500.862 494.593 C 501.173 495.840 501.725 497.493 502.378 498.599 C 503.433 500.386 505.342 502.477 506.949 503.789 C 508.944 505.418 511.971 507.232 514.428 508.005 C 516.521 508.663 519.513 508.880 521.704 508.753 C 523.917 508.624 526.899 508.068 528.915 507.146 C 531.432 505.995 534.369 503.586 536.269 501.573 C 538.316 499.403 540.274 495.872 541.784 493.300 C 544.539 488.610 547.524 481.981 549.945 477.111 C 552.609 471.750 556.119 464.582 558.723 459.193 C 562.118 452.166 566.998 442.948 569.905 435.706 C 572.600 428.993 575.595 419.799 577.492 412.819 C 578.856 407.798 580.486 401.029 581.174 395.872 C 581.735 391.662 582.215 385.975 581.943 381.737 C 581.810 379.664 581.363 376.907 580.789 374.911 C 580.167 372.748 578.739 370.077 577.904 367.987 C 576.906 365.489 575.398 362.208 574.703 359.609 M 731.043 113.310 C 731.043 113.310 731.043 113.310 731.043 113.310 Z"/>
-<path fill="none" stroke="#aa5115" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 572.997 348.519 C 572.997 348.519 572.997 348.519 572.997 348.519 C 573.509 351.846 573.834 356.357 574.703 359.609 C 575.398 362.208 576.906 365.489 577.904 367.987 C 578.739 370.077 580.167 372.748 580.789 374.911 C 581.363 376.907 581.810 379.664 581.943 381.737 C 582.215 385.975 581.735 391.662 581.174 395.872 C 580.486 401.029 578.856 407.798 577.492 412.819 C 575.595 419.799 572.600 428.993 569.905 435.706 C 566.998 442.948 562.118 452.166 558.723 459.193 C 556.119 464.582 552.609 471.750 549.945 477.111 C 547.524 481.981 544.539 488.610 541.784 493.300 C 540.274 495.872 538.316 499.403 536.269 501.573 C 534.369 503.586 531.432 505.995 528.915 507.146 C 526.899 508.068 523.917 508.624 521.704 508.753 C 519.513 508.880 516.521 508.663 514.428 508.005 C 511.971 507.232 508.944 505.418 506.949 503.789 C 505.342 502.477 503.433 500.386 502.378 498.599 C 501.725 497.493 501.173 495.840 500.862 494.593 C 500.434 492.879 500.196 490.512 500.158 488.745 C 500.114 486.662 500.302 483.864 500.720 481.823 C 501.321 478.883 503.080 475.230 503.978 472.367 C 504.815 469.695 506.007 466.140 506.520 463.387 C 507.290 459.262 507.667 453.646 507.713 449.450 C 507.749 446.157 507.676 441.728 507.057 438.494 C 506.383 434.974 504.636 430.480 503.292 427.158 C 502.105 424.225 500.232 420.434 498.734 417.647 C 496.878 414.194 494.059 409.785 491.997 406.451 C 488.604 400.964 483.643 393.915 480.443 388.313 C 477.566 383.275 473.574 376.562 471.656 371.087 C 470.084 366.600 468.699 360.324 468.391 355.579 C 468.222 352.968 468.688 349.478 468.935 346.873 C 469.091 345.235 469.339 343.053 469.616 341.432 C 470.332 337.225 471.309 331.574 472.744 327.556 C 474.094 323.778 476.687 319.052 478.714 315.591 C 480.866 311.918 484.074 307.213 486.701 303.863 C 489.612 300.152 493.722 295.339 497.231 292.187 C 500.788 288.991 506.075 285.357 510.140 282.839 C 514.050 280.417 519.477 277.499 523.717 275.717 C 528.366 273.763 534.793 271.650 539.719 270.570 C 541.863 270.100 544.782 269.765 546.971 269.590 C 549.492 269.389 552.870 269.369 555.399 269.394 C 559.784 269.438 565.629 269.725 570.000 270.080 C 576.908 270.641 586.083 271.798 592.940 272.806 C 601.155 274.014 612.046 276.034 620.197 277.616 C 628.926 279.310 640.422 282.292 649.191 283.762 C 652.859 284.377 657.772 285.137 661.484 285.366 C 665.885 285.637 671.852 286.067 676.181 285.232 C 679.258 284.638 683.270 283.165 685.956 281.551 C 688.372 280.099 691.195 277.508 693.031 275.370 C 694.961 273.122 697.167 269.758 698.319 267.029 C 699.485 264.262 700.189 260.261 700.628 257.291 C 701.060 254.362 701.193 250.401 701.225 247.441 C 701.270 243.151 700.923 237.432 700.608 233.153 C 700.428 230.710 699.924 227.476 699.787 225.031 C 699.265 215.700 699.398 203.217 699.813 193.881 C 700.145 186.406 701.010 176.454 701.958 169.031 C 702.468 165.041 703.257 159.725 704.139 155.800 C 705.021 151.872 706.489 146.693 707.829 142.896 C 709.055 139.421 710.850 134.821 712.599 131.578 C 713.775 129.398 715.598 126.621 717.144 124.687 C 718.981 122.392 721.664 119.483 723.962 117.650 C 725.909 116.096 728.919 114.612 731.043 113.310 C 731.043 113.310 731.043 113.310 731.043 113.310 C 732.143 121.668 733.610 132.812 734.710 141.170 C 734.710 141.170 734.710 141.170 734.710 141.170 C 734.710 141.170 734.710 141.170 734.710 141.170 C 734.409 143.378 733.915 146.311 733.707 148.529 C 733.371 152.123 732.945 156.943 733.141 160.547 C 733.308 163.611 733.861 167.703 734.697 170.656 C 735.257 172.636 736.594 175.070 737.302 177.003 C 738.611 180.576 740.108 185.430 741.143 189.091 C 742.691 194.565 744.454 201.948 745.662 207.506 C 747.069 213.978 748.843 222.641 749.759 229.200 C 750.879 237.215 751.788 247.985 752.157 256.069 C 752.551 264.701 752.154 276.232 752.206 284.873 C 752.235 289.800 752.571 296.372 752.367 301.295 C 752.211 305.068 751.970 310.129 751.235 313.833 C 750.650 316.781 749.410 320.617 748.306 323.411 C 747.330 325.878 745.442 328.908 744.424 331.358 C 743.366 333.905 741.865 337.324 741.421 340.045 C 741.211 341.332 741.033 343.129 741.360 344.392 C 741.545 345.104 741.954 346.084 742.521 346.554 C 743.195 347.114 744.495 347.093 745.316 347.398 C 746.226 347.736 747.520 348.102 748.270 348.717 C 749.078 349.379 749.986 350.561 750.274 351.565 C 750.697 353.033 750.044 355.124 749.868 356.641 C 749.099 363.293 747.467 372.081 746.295 378.674 C 744.775 387.231 742.350 398.566 740.776 407.113 C 738.913 417.226 736.436 430.715 734.903 440.883 C 734.101 446.198 733.327 453.325 732.584 458.649 C 731.676 465.152 730.639 473.858 729.359 480.299 C 728.413 485.060 726.989 491.395 725.485 496.011 C 724.493 499.055 723.193 503.193 721.503 505.913 C 720.512 507.507 718.847 509.437 717.413 510.648 C 716.085 511.770 714.104 513.088 712.463 513.661 C 710.315 514.412 707.195 514.724 704.929 514.522 C 702.986 514.349 700.399 513.630 698.687 512.693 C 696.841 511.682 694.658 509.763 693.414 508.065 C 692.492 506.806 691.830 504.783 691.262 503.330 C 689.505 498.840 687.669 492.664 686.406 488.012 C 685.521 484.753 684.639 480.334 683.883 477.043 C 682.432 470.726 680.705 462.252 679.056 455.983 C 677.793 451.180 676.082 444.767 674.362 440.108 C 672.965 436.322 670.357 431.576 668.916 427.806 C 666.078 420.382 662.482 410.340 660.933 402.544 C 660.172 398.713 659.555 393.495 659.630 389.589 C 659.666 387.775 660.124 385.384 660.370 383.586 C 660.696 381.198 661.446 378.049 661.570 375.642 C 661.693 373.260 662.122 369.899 661.201 367.699 C 660.768 366.665 659.797 365.348 658.799 364.836 C 657.688 364.265 655.864 364.294 654.643 364.558 C 653.285 364.852 651.796 366.106 650.579 366.775 C 648.524 367.904 645.916 369.681 643.744 370.562 C 641.906 371.307 639.348 372.169 637.370 372.317 C 633.572 372.601 628.467 371.530 624.809 370.470 C 621.589 369.537 617.513 367.593 614.581 365.967 C 611.587 364.307 607.674 361.855 605.151 359.540 C 602.347 356.968 599.459 352.723 597.162 349.690 C 594.888 346.686 592.292 342.357 589.919 339.430 C 588.147 337.244 585.900 334.100 583.566 332.528 C 582.556 331.848 581.024 331.133 579.817 330.974 C 578.969 330.862 577.754 330.923 576.984 331.294 C 575.864 331.833 574.750 333.222 574.134 334.302 C 573.260 335.836 572.818 338.234 572.618 339.989 C 572.327 342.534 572.997 348.518 572.997 348.519 "/>
-<path fill="#ac9783" fill-rule="evenodd" stroke="#9b8d73" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 735.004 111.393 C 736.851 110.687 739.410 109.979 741.357 109.635 C 743.197 109.310 745.700 109.226 747.566 109.132 C 749.857 109.017 752.923 108.827 755.211 108.989 C 759.320 109.278 764.746 110.324 768.745 111.317 C 771.083 111.898 774.141 112.911 776.395 113.763 C 782.226 115.966 789.898 119.256 795.339 122.298 C 798.575 124.108 802.650 126.936 805.622 129.154 C 810.031 132.445 815.664 137.175 819.666 140.952 C 821.191 142.391 823.434 144.190 824.512 145.988 C 824.802 146.472 825.074 147.192 825.178 147.746 C 825.309 148.447 825.260 149.414 825.178 150.122 C 824.784 153.485 823.451 157.864 822.187 161.005 C 821.864 161.808 821.448 162.926 820.875 163.574 C 819.595 165.019 817.193 166.243 815.395 166.942 C 813.316 167.750 810.311 168.138 808.088 168.312 C 805.457 168.519 801.900 168.457 799.297 168.027 C 797.890 167.795 796.131 166.976 794.730 166.714 C 792.147 166.230 788.624 166.076 785.997 166.029 C 783.220 165.979 779.525 166.342 776.749 166.428 C 774.253 166.506 770.922 166.701 768.428 166.587 C 764.314 166.400 758.758 166.108 754.796 164.987 C 750.586 163.797 745.079 161.449 741.579 158.824 C 738.739 156.693 735.724 152.909 733.697 149.993 C 732.238 147.894 730.636 144.852 729.656 142.491 C 728.476 139.647 727.225 135.694 726.732 132.655 C 726.263 129.760 726.345 125.818 726.400 122.886 C 726.426 121.523 726.447 119.692 726.692 118.351 C 726.851 117.480 727.057 116.271 727.527 115.521 C 727.659 115.311 727.916 115.093 728.105 114.933 C 728.244 114.815 728.451 114.687 728.599 114.582 C 728.599 114.582 728.599 114.582 728.599 114.582 C 728.604 114.583 732.999 112.160 735.004 111.393 Z"/>
-<path fill="#4b4642" fill-rule="evenodd" stroke="none" d="M 805.784 147.146 C 805.476 146.807 805.186 146.259 804.930 145.880 C 804.930 145.880 809.052 145.930 810.818 145.975 C 812.765 146.023 815.359 146.167 817.307 146.196 C 819.605 146.232 822.669 146.174 824.968 146.165 C 824.968 146.165 825.795 146.553 826.012 146.861 C 826.474 147.518 826.460 148.693 826.496 149.496 C 826.549 150.730 826.351 152.390 826.058 153.590 C 825.521 155.794 824.329 158.623 823.196 160.587 C 822.804 161.267 822.110 162.062 821.645 162.694 C 821.645 162.694 821.545 161.809 821.248 161.661 C 820.900 161.488 820.362 161.884 820.015 162.058 C 819.323 162.407 818.630 163.240 817.948 163.609 C 816.301 164.500 813.842 165.123 812.026 165.581 C 810.154 166.052 807.611 166.545 805.685 166.679 C 804.101 166.790 801.967 166.738 800.393 166.529 C 799.402 166.398 797.988 166.321 797.148 165.780 C 796.799 165.556 796.519 165.046 796.249 164.732 C 796.249 164.732 798.156 165.249 798.995 165.331 C 801.951 165.618 805.946 165.286 808.881 164.832 C 810.238 164.622 812.044 164.229 813.324 163.733 C 814.837 163.147 816.875 162.237 818.067 161.137 C 818.620 160.627 819.240 159.790 819.515 159.090 C 820.193 157.369 820.017 154.798 820.064 152.949 C 820.079 152.380 820.029 151.621 820.014 151.052 C 820.014 151.052 819.237 151.133 818.904 151.168 C 817.751 151.110 816.201 151.149 815.059 150.976 C 813.007 150.664 810.223 150.126 808.380 149.172 C 807.503 148.718 806.450 147.876 805.784 147.146 M 818.904 151.168 C 818.904 151.168 818.904 151.168 818.904 151.168 Z"/>
-<path fill="none" stroke="#4b4642" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 804.930 145.880 C 804.930 145.880 804.930 145.880 804.930 145.880 C 805.186 146.259 805.476 146.807 805.784 147.146 C 806.450 147.876 807.503 148.718 808.380 149.172 C 810.223 150.126 813.007 150.664 815.059 150.976 C 816.201 151.149 817.751 151.110 818.904 151.168 C 818.904 151.168 818.904 151.168 818.904 151.168 C 819.237 151.133 820.014 151.052 820.014 151.052 C 820.014 151.052 820.014 151.052 820.014 151.052 C 820.029 151.621 820.079 152.380 820.064 152.949 C 820.017 154.798 820.193 157.369 819.515 159.090 C 819.240 159.790 818.620 160.627 818.067 161.137 C 816.875 162.237 814.837 163.147 813.324 163.733 C 812.044 164.229 810.238 164.622 808.881 164.832 C 805.946 165.286 801.951 165.618 798.995 165.331 C 798.156 165.249 796.249 164.732 796.249 164.732 C 796.249 164.732 796.249 164.732 796.249 164.732 C 796.519 165.046 796.799 165.556 797.148 165.780 C 797.988 166.321 799.402 166.398 800.393 166.529 C 801.967 166.738 804.101 166.790 805.685 166.679 C 807.611 166.545 810.154 166.052 812.026 165.581 C 813.842 165.123 816.301 164.500 817.948 163.609 C 818.630 163.240 819.323 162.407 820.015 162.058 C 820.362 161.884 820.900 161.488 821.248 161.661 C 821.545 161.809 821.645 162.694 821.645 162.694 C 821.645 162.694 821.645 162.694 821.645 162.694 C 822.110 162.062 822.804 161.267 823.196 160.587 C 824.329 158.623 825.521 155.794 826.058 153.590 C 826.351 152.390 826.549 150.730 826.496 149.496 C 826.460 148.693 826.474 147.518 826.012 146.861 C 825.795 146.553 824.968 146.165 824.968 146.165 C 824.968 146.165 824.968 146.165 824.968 146.165 C 822.669 146.174 819.605 146.232 817.307 146.196 C 815.359 146.167 812.765 146.023 810.818 145.975 C 809.052 145.930 804.930 145.880 804.930 145.880 "/>
-<path fill="#333132" fill-rule="evenodd" stroke="#2c2924" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 773.415 137.847 C 773.415 137.847 773.415 137.847 773.415 137.847 C 773.291 138.033 773.157 138.306 773.002 138.466 C 772.347 139.144 771.227 139.796 770.358 140.160 C 769.234 140.631 767.607 140.949 766.391 141.028 C 765.012 141.118 763.128 141.013 761.805 140.615 C 760.690 140.280 759.299 139.505 758.375 138.797 C 757.422 138.066 756.322 136.858 755.648 135.863 C 754.964 134.853 754.204 133.370 753.913 132.186 C 753.655 131.137 753.797 129.669 753.747 128.591 C 753.747 128.591 753.747 128.591 753.747 128.591 C 754.318 128.517 755.074 128.375 755.648 128.343 C 757.456 128.241 759.911 128.166 761.681 128.550 C 762.801 128.792 764.225 129.411 765.234 129.955 C 766.860 130.831 768.921 132.249 770.234 133.549 C 771.373 134.678 773.415 137.846 773.415 137.847 C 773.415 137.847 773.415 137.847 773.415 137.847 Z"/>
-<path fill="#e5e3e4" fill-rule="evenodd" stroke="#e5e3e4" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 757.590 129.293 C 758.724 129.293 759.697 130.253 759.697 131.525 C 759.697 132.796 758.724 133.756 757.590 133.756 C 756.456 133.756 755.483 132.796 755.483 131.525 C 755.483 130.253 756.456 129.293 757.590 129.293 Z"/>
-<path fill="#3e3633" d="M 740.081 132.203 C 750.402 126.042 765.773 123.366 773.614 135.733 L 771.050 137.290 C 764.604 126.129 751.417 128.866 741.625 134.775 L 740.081 132.203 Z"/>
-<path fill="#3e3633" d="M 773.614 135.733 C 774.762 137.623 775.394 140.844 775.410 143.259 L 774.810 143.259 C 774.825 141.034 772.220 139.217 771.050 137.290 L 773.614 135.733 Z"/>
-<path fill="none" stroke="#3e3633" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 773.614 135.733 L 771.050 137.290 "/>
-</g>
-</svg>
+<?xml version="1.0" encoding="utf-8"?>
+<!-- Generator: Moho 12.5 build 22438 -->
+<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
+<svg version="1.1" id="Frame_0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280px" height="720px">
+<g id="Layer_6">
+<path fill="#e7e1cb" fill-rule="evenodd" stroke="none" d="M 575.641 397.169 C 571.045 395.618 564.453 395.465 559.658 394.735 C 559.658 394.728 561.135 347.274 561.767 326.934 C 561.778 326.933 639.181 322.293 672.359 320.304 C 672.363 320.299 706.382 287.200 713.768 268.802 C 718.782 256.311 716.988 237.559 718.634 224.200 C 721.710 199.227 726.725 166.050 730.193 141.129 C 730.196 141.131 749.293 156.200 757.479 162.659 C 757.446 165.866 757.282 170.142 757.370 173.348 C 757.492 177.800 757.854 183.735 758.370 188.159 C 759.284 195.991 761.099 206.369 762.836 214.061 C 764.483 221.351 767.704 230.808 769.551 238.050 C 770.795 242.927 772.504 249.431 773.349 254.394 C 774.264 259.769 774.983 267.021 775.306 272.464 C 775.828 281.268 775.939 293.054 775.476 301.860 C 775.073 309.515 774.056 319.717 772.688 327.260 C 769.614 344.214 763.885 366.603 757.862 382.746 C 754.884 390.730 750.769 401.554 745.742 408.434 C 741.967 413.601 735.899 420.061 730.287 423.134 C 710.197 434.133 677.960 435.107 655.088 436.310 C 651.693 436.489 647.134 436.327 643.762 435.891 C 639.247 435.307 633.259 434.026 628.971 432.494 C 625.455 431.238 620.978 428.969 617.796 427.016 C 612.282 423.633 605.772 417.890 600.705 413.869 C 599.091 412.589 596.988 410.822 595.379 409.536 C 593.330 407.896 590.687 405.580 588.500 404.130 C 584.843 401.707 579.797 398.571 575.641 397.169 M 757.479 162.659 C 757.479 162.659 757.479 162.659 757.479 162.659 Z"/>
+<path fill="none" stroke="#e7e1cb" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 559.658 394.735 C 559.658 394.735 559.658 394.735 559.658 394.735 C 564.453 395.465 571.045 395.618 575.641 397.169 C 579.797 398.571 584.843 401.707 588.500 404.130 C 590.687 405.580 593.330 407.896 595.379 409.536 C 596.988 410.822 599.091 412.589 600.705 413.869 C 605.772 417.890 612.282 423.633 617.796 427.016 C 620.978 428.969 625.455 431.238 628.971 432.494 C 633.259 434.026 639.247 435.307 643.762 435.891 C 647.134 436.327 651.693 436.489 655.088 436.310 C 677.960 435.107 710.197 434.133 730.287 423.134 C 735.899 420.061 741.967 413.601 745.742 408.434 C 750.769 401.554 754.884 390.730 757.862 382.746 C 763.885 366.603 769.614 344.214 772.688 327.260 C 774.056 319.717 775.073 309.515 775.476 301.860 C 775.939 293.054 775.828 281.268 775.306 272.464 C 774.983 267.021 774.264 259.769 773.349 254.394 C 772.504 249.431 770.795 242.927 769.551 238.050 C 767.704 230.808 764.483 221.351 762.836 214.061 C 761.099 206.369 759.284 195.991 758.370 188.159 C 757.854 183.735 757.492 177.800 757.370 173.348 C 757.282 170.142 757.446 165.866 757.479 162.659 C 757.479 162.659 757.479 162.659 757.479 162.659 C 749.293 156.200 730.196 141.131 730.193 141.129 C 730.193 141.129 730.193 141.129 730.193 141.129 C 726.725 166.050 721.710 199.227 718.634 224.200 C 716.988 237.559 718.782 256.311 713.768 268.802 C 706.382 287.200 672.363 320.299 672.359 320.304 C 672.359 320.304 672.359 320.304 672.359 320.304 C 639.181 322.293 561.778 326.933 561.767 326.934 C 561.767 326.934 561.767 326.934 561.767 326.934 C 561.135 347.274 559.658 394.728 559.658 394.735 "/>
+<path fill="#5f524a" fill-rule="evenodd" stroke="#5f524a" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 747.648 113.356 C 744.021 115.471 737.946 114.709 733.789 115.289 C 733.789 115.289 733.789 115.289 733.789 115.289 C 735.113 112.385 736.646 108.394 738.203 105.607 C 741.734 99.287 746.889 90.956 751.928 85.757 C 755.456 82.116 761.237 78.447 765.406 75.563 C 768.524 73.407 772.673 70.464 776.076 68.797 C 778.100 67.805 780.930 66.727 783.114 66.175 C 784.317 65.871 785.963 65.496 787.203 65.555 C 788.177 65.602 789.479 65.903 790.363 66.315 C 791.095 66.655 792.272 67.133 792.541 67.894 C 792.872 68.830 792.068 70.195 791.585 71.063 C 790.804 72.466 789.094 73.865 787.958 75.000 C 786.271 76.684 783.884 78.787 782.090 80.357 C 779.570 82.562 776.045 85.310 773.528 87.519 C 769.580 90.982 764.450 95.753 760.674 99.402 C 758.141 101.849 754.774 105.129 752.400 107.730 C 750.910 109.361 749.557 112.244 747.648 113.356 Z"/>
+<path fill="#6d6057" fill-rule="evenodd" stroke="#6d6057" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 741.736 111.321 C 738.370 114.076 732.141 114.631 728.029 116.050 C 728.029 116.050 728.029 116.050 728.029 116.050 C 729.040 112.678 730.097 108.080 731.400 104.809 C 734.080 98.083 738.520 89.421 742.544 83.403 C 745.424 79.096 749.784 73.649 753.562 70.102 C 756.459 67.382 760.768 64.202 764.225 62.243 C 766.038 61.215 768.580 59.999 770.596 59.472 C 771.891 59.134 773.689 58.962 775.027 58.964 C 776.002 58.966 777.329 59.026 778.258 59.324 C 779.026 59.570 780.253 59.898 780.615 60.620 C 781.060 61.507 780.432 62.962 780.061 63.883 C 779.461 65.372 777.991 67.016 776.953 68.241 C 775.458 70.005 773.101 72.019 771.465 73.653 C 769.039 76.079 765.726 79.241 763.436 81.795 C 759.956 85.676 755.628 91.130 752.517 95.312 C 750.379 98.185 747.740 102.168 745.750 105.146 C 744.523 106.983 743.446 109.922 741.736 111.321 Z"/>
+<path fill="#a89984" fill-rule="evenodd" stroke="none" d="M 703.345 591.533 C 703.084 591.940 702.744 592.488 702.487 592.897 C 702.488 592.898 708.174 594.324 710.670 594.456 C 712.426 594.549 714.772 594.257 716.515 594.027 C 719.978 593.571 724.639 592.909 727.935 591.750 C 729.735 591.117 731.917 589.759 733.624 588.906 C 733.624 588.906 729.281 588.297 727.461 587.839 C 725.607 587.373 723.095 586.739 721.416 585.824 C 720.348 585.242 718.902 584.339 718.216 583.335 C 718.045 583.085 717.914 582.687 717.864 582.389 C 717.727 581.575 717.818 580.441 718.035 579.645 C 718.316 578.615 719.407 577.522 719.681 576.490 C 719.940 575.514 719.788 574.137 719.819 573.129 C 719.854 571.964 719.966 570.408 719.894 569.245 C 719.846 568.475 719.711 567.449 719.541 566.696 C 719.251 565.414 718.677 563.748 718.178 562.532 C 717.751 561.492 716.768 560.270 716.512 559.175 C 716.406 558.722 716.470 558.089 716.459 557.624 C 716.401 555.110 716.376 551.756 716.387 549.241 C 716.417 542.834 716.700 534.294 716.823 527.888 C 716.930 522.340 717.025 514.941 717.158 509.394 C 717.171 508.838 717.194 508.097 717.210 507.541 C 717.208 507.541 702.211 507.631 695.783 507.670 C 696.484 516.039 697.398 527.200 698.119 535.568 C 698.411 538.963 698.908 543.482 699.117 546.884 C 699.406 551.582 699.823 557.862 699.637 562.565 C 699.624 562.903 699.638 563.365 699.535 563.687 C 699.260 564.553 698.267 565.405 697.903 566.237 C 697.397 567.393 696.997 569.061 696.883 570.317 C 696.789 571.355 696.851 572.770 697.087 573.785 C 697.360 574.959 697.941 576.515 698.661 577.481 C 699.727 578.910 701.750 580.320 703.313 581.179 C 704.029 581.573 705.241 581.606 705.867 582.133 C 706.319 582.513 706.780 583.231 706.896 583.810 C 707.093 584.793 706.618 586.157 706.248 587.089 C 705.660 588.569 704.203 590.192 703.345 591.533 M 695.783 507.670 C 695.783 507.670 695.783 507.670 695.783 507.670 Z"/>
+<path fill="none" stroke="#978e71" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 702.487 592.897 C 702.487 592.897 702.487 592.897 702.487 592.897 C 702.744 592.488 703.084 591.940 703.345 591.533 C 704.203 590.192 705.660 588.569 706.248 587.089 C 706.618 586.157 707.093 584.793 706.896 583.810 C 706.780 583.231 706.319 582.513 705.867 582.133 C 705.241 581.606 704.029 581.573 703.313 581.179 C 701.750 580.320 699.727 578.910 698.661 577.481 C 697.941 576.515 697.360 574.959 697.087 573.785 C 696.851 572.770 696.789 571.355 696.883 570.317 C 696.997 569.061 697.397 567.393 697.903 566.237 C 698.267 565.405 699.260 564.553 699.535 563.687 C 699.638 563.365 699.624 562.903 699.637 562.565 C 699.823 557.862 699.406 551.582 699.117 546.884 C 698.908 543.482 698.411 538.963 698.119 535.568 C 697.398 527.200 696.484 516.039 695.783 507.670 C 695.783 507.670 695.783 507.670 695.783 507.670 C 702.211 507.631 717.208 507.541 717.210 507.541 C 717.210 507.541 717.210 507.541 717.210 507.541 C 717.194 508.097 717.171 508.838 717.158 509.394 C 717.025 514.941 716.930 522.340 716.823 527.888 C 716.700 534.294 716.417 542.834 716.387 549.241 C 716.376 551.756 716.401 555.110 716.459 557.624 C 716.470 558.089 716.406 558.722 716.512 559.175 C 716.768 560.270 717.751 561.492 718.178 562.532 C 718.677 563.748 719.251 565.414 719.541 566.696 C 719.711 567.449 719.846 568.475 719.894 569.245 C 719.966 570.408 719.854 571.964 719.819 573.129 C 719.788 574.137 719.940 575.514 719.681 576.490 C 719.407 577.522 718.316 578.615 718.035 579.645 C 717.818 580.441 717.727 581.575 717.864 582.389 C 717.914 582.687 718.045 583.085 718.216 583.335 C 718.902 584.339 720.348 585.242 721.416 585.824 C 723.095 586.739 725.607 587.373 727.461 587.839 C 729.281 588.297 733.624 588.906 733.624 588.906 C 733.624 588.906 733.624 588.906 733.624 588.906 C 731.917 589.759 729.735 591.117 727.935 591.750 C 724.639 592.909 719.978 593.571 716.515 594.027 C 714.772 594.257 712.426 594.549 710.670 594.456 C 708.174 594.324 702.488 592.898 702.487 592.897 "/>
+<path fill="#a89984" fill-rule="evenodd" stroke="none" d="M 516.067 588.955 C 515.802 590.088 515.291 591.556 514.959 592.670 C 514.960 592.671 521.683 595.626 524.768 595.984 C 526.745 596.213 529.406 595.707 531.382 595.474 C 534.782 595.072 539.589 595.173 542.643 593.625 C 543.848 593.014 545.002 591.532 546.013 590.635 C 546.012 590.635 541.506 588.937 539.696 587.956 C 538.386 587.246 536.595 586.279 535.559 585.208 C 534.626 584.244 533.755 582.632 533.193 581.414 C 532.947 580.880 532.641 580.141 532.567 579.558 C 532.463 578.722 532.699 577.595 532.822 576.761 C 532.969 575.765 533.304 574.461 533.503 573.473 C 533.702 572.485 534.045 571.178 534.147 570.174 C 534.253 569.132 534.244 567.728 534.179 566.682 C 534.125 565.819 533.939 564.679 533.803 563.825 C 533.605 562.588 533.389 560.921 533.025 559.723 C 532.739 558.782 532.116 557.616 531.758 556.700 C 531.404 555.795 530.895 554.595 530.650 553.654 C 530.099 551.542 529.791 548.629 529.593 546.455 C 529.010 540.074 529.326 531.505 529.072 525.102 C 528.694 515.568 527.597 502.883 527.289 493.346 C 527.271 492.790 527.269 492.049 527.260 491.493 C 527.258 491.493 510.812 492.222 503.762 492.534 C 505.308 504.845 507.243 521.277 508.914 533.572 C 509.374 536.955 510.209 541.437 510.538 544.835 C 510.978 549.377 511.708 555.488 511.252 560.029 C 511.202 560.520 511.038 561.162 510.915 561.640 C 510.713 562.426 510.323 563.439 510.112 564.223 C 509.782 565.446 509.317 567.083 509.184 568.343 C 508.991 570.165 509.012 572.640 509.304 574.449 C 509.430 575.228 509.566 576.339 510.030 576.976 C 511.133 578.492 514.033 578.870 515.432 580.117 C 515.940 580.570 516.501 581.303 516.851 581.887 C 517.171 582.420 517.817 583.185 517.672 583.789 C 517.588 584.140 516.987 584.311 516.806 584.623 C 516.146 585.764 516.368 587.672 516.067 588.955 M 503.762 492.534 C 503.762 492.534 503.762 492.534 503.762 492.534 Z"/>
+<path fill="none" stroke="#978e71" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 514.959 592.670 C 514.959 592.670 514.959 592.670 514.959 592.670 C 515.291 591.556 515.802 590.088 516.067 588.955 C 516.368 587.672 516.146 585.764 516.806 584.623 C 516.987 584.311 517.588 584.140 517.672 583.789 C 517.817 583.185 517.171 582.420 516.851 581.887 C 516.501 581.303 515.940 580.570 515.432 580.117 C 514.033 578.870 511.133 578.492 510.030 576.976 C 509.566 576.339 509.430 575.228 509.304 574.449 C 509.012 572.640 508.991 570.165 509.184 568.343 C 509.317 567.083 509.782 565.446 510.112 564.223 C 510.323 563.439 510.713 562.426 510.915 561.640 C 511.038 561.162 511.202 560.520 511.252 560.029 C 511.708 555.488 510.978 549.377 510.538 544.835 C 510.209 541.437 509.374 536.955 508.914 533.572 C 507.243 521.277 505.308 504.845 503.762 492.534 C 503.762 492.534 503.762 492.534 503.762 492.534 C 510.812 492.222 527.258 491.493 527.260 491.493 C 527.260 491.493 527.260 491.493 527.260 491.493 C 527.269 492.049 527.271 492.790 527.289 493.346 C 527.597 502.883 528.694 515.568 529.072 525.102 C 529.326 531.505 529.010 540.074 529.593 546.455 C 529.791 548.629 530.099 551.542 530.650 553.654 C 530.895 554.595 531.404 555.795 531.758 556.700 C 532.116 557.616 532.739 558.782 533.025 559.723 C 533.389 560.921 533.605 562.588 533.803 563.825 C 533.939 564.679 534.125 565.819 534.179 566.682 C 534.244 567.728 534.253 569.132 534.147 570.174 C 534.045 571.178 533.702 572.485 533.503 573.473 C 533.304 574.461 532.969 575.765 532.822 576.761 C 532.699 577.595 532.463 578.722 532.567 579.558 C 532.641 580.141 532.947 580.880 533.193 581.414 C 533.755 582.632 534.626 584.244 535.559 585.208 C 536.595 586.279 538.386 587.246 539.696 587.956 C 541.506 588.937 546.012 590.635 546.013 590.635 C 546.013 590.635 546.013 590.635 546.013 590.635 C 545.002 591.532 543.848 593.014 542.643 593.625 C 539.589 595.173 534.782 595.072 531.382 595.474 C 529.406 595.707 526.745 596.213 524.768 595.984 C 521.683 595.626 514.960 592.671 514.959 592.670 "/>
+<path fill="#9d4c0b" fill-rule="evenodd" stroke="#9d4c0b" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 518.617 276.432 C 516.417 274.744 513.065 273.094 510.562 271.901 C 508.274 270.810 505.192 269.291 502.709 268.780 C 498.331 267.879 492.191 267.795 487.809 268.679 C 484.279 269.392 479.845 271.496 476.734 273.311 C 473.258 275.338 469.138 278.857 466.163 281.566 C 463.335 284.141 459.805 287.852 457.404 290.829 C 455.551 293.126 453.264 296.353 451.818 298.925 C 450.392 301.460 448.760 305.010 447.856 307.775 C 446.956 310.529 446.190 314.342 445.833 317.216 C 445.424 320.517 445.081 324.994 445.467 328.298 C 445.764 330.842 446.696 334.175 447.644 336.555 C 448.610 338.977 450.326 342.039 451.818 344.177 C 453.877 347.127 457.141 350.696 459.769 353.152 C 463.465 356.606 469.159 360.303 473.184 363.367 C 473.184 363.367 473.184 363.367 473.184 363.367 C 480.937 358.346 492.927 353.564 499.029 346.630 C 505.247 339.563 506.103 325.166 512.567 318.323 C 516.475 314.185 526.270 313.724 528.907 308.680 C 532.304 302.184 527.089 291.672 526.310 284.383 C 526.310 284.383 526.310 284.383 526.310 284.383 C 526.328 284.354 521.250 278.452 518.617 276.432 Z"/>
+<path fill="#8a7b66" fill-rule="evenodd" stroke="none" d="M 713.483 592.015 C 716.741 591.871 721.117 591.756 724.318 591.135 C 726.527 590.706 729.267 589.266 731.495 588.958 C 733.037 588.746 735.140 588.796 736.681 589.005 C 738.231 589.215 740.333 589.624 741.719 590.350 C 742.938 590.988 744.621 592.065 745.232 593.298 C 745.745 594.331 745.808 596.030 745.474 597.134 C 745.056 598.522 743.623 600.031 742.486 600.930 C 740.439 602.550 737.015 603.700 734.490 604.363 C 731.205 605.225 726.615 605.304 723.224 605.493 C 720.441 605.648 716.717 605.784 713.936 605.615 C 712.458 605.524 710.475 605.355 709.039 604.993 C 707.546 604.617 705.485 604.066 704.252 603.144 C 703.223 602.375 702.089 600.968 701.610 599.776 C 701.201 598.759 701.163 597.239 701.214 596.144 C 701.248 595.409 701.453 594.436 701.676 593.734 C 701.806 593.325 702.019 592.784 702.253 592.424 C 702.329 592.305 702.538 592.086 702.545 592.092 C 702.553 592.100 710.205 592.159 713.483 592.015 Z"/>
+<path fill="#77674e" d="M 713.479 591.905 C 716.738 591.761 721.106 591.646 724.297 591.027 L 724.339 591.243 C 721.128 591.865 716.745 591.981 713.488 592.124 L 713.479 591.905 Z"/>
+<path fill="#77674e" d="M 724.297 591.027 C 726.488 590.603 729.230 589.162 731.480 588.850 L 731.510 589.067 C 729.303 589.370 726.566 590.809 724.339 591.243 L 724.297 591.027 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 724.297 591.027 L 724.339 591.243 "/>
+<path fill="#77674e" d="M 731.480 588.850 C 733.032 588.636 735.147 588.686 736.696 588.896 L 736.667 589.114 C 735.132 588.905 733.042 588.856 731.510 589.067 L 731.480 588.850 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 731.480 588.850 L 731.510 589.067 "/>
+<path fill="#77674e" d="M 736.696 588.896 C 738.250 589.107 740.367 589.520 741.770 590.252 L 741.668 590.447 C 740.299 589.729 738.213 589.323 736.667 589.114 L 736.696 588.896 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 736.696 588.896 L 736.667 589.114 "/>
+<path fill="#77674e" d="M 741.770 590.252 C 742.994 590.893 744.699 591.988 745.331 593.249 L 745.134 593.347 C 744.543 592.143 742.882 591.083 741.668 590.447 L 741.770 590.252 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 741.770 590.252 L 741.668 590.447 "/>
+<path fill="#77674e" d="M 745.331 593.249 C 745.852 594.308 745.917 596.041 745.580 597.166 L 745.369 597.102 C 745.698 596.020 745.637 594.354 745.134 593.347 L 745.331 593.249 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 745.331 593.249 L 745.134 593.347 "/>
+<path fill="#77674e" d="M 745.580 597.166 C 745.148 598.581 743.698 600.111 742.554 601.016 L 742.418 600.844 C 743.548 599.951 744.963 598.462 745.369 597.102 L 745.580 597.166 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 745.580 597.166 L 745.369 597.102 "/>
+<path fill="#77674e" d="M 742.554 601.016 C 740.489 602.648 737.047 603.805 734.518 604.469 L 734.462 604.256 C 736.983 603.595 740.389 602.452 742.418 600.844 L 742.554 601.016 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 742.554 601.016 L 742.418 600.844 "/>
+<path fill="#77674e" d="M 734.518 604.469 C 731.218 605.335 726.619 605.414 723.230 605.603 L 723.218 605.384 C 726.612 605.195 731.192 605.116 734.462 604.256 L 734.518 604.469 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 734.518 604.469 L 734.462 604.256 "/>
+<path fill="#77674e" d="M 723.230 605.603 C 720.446 605.758 716.717 605.894 713.929 605.724 L 713.942 605.505 C 716.718 605.674 720.436 605.539 723.218 605.384 L 723.230 605.603 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 723.230 605.603 L 723.218 605.384 "/>
+<path fill="#77674e" d="M 713.929 605.724 C 712.449 605.634 710.458 605.464 709.012 605.100 L 709.066 604.886 C 710.492 605.246 712.466 605.415 713.942 605.505 L 713.929 605.724 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 713.929 605.724 L 713.942 605.505 "/>
+<path fill="#77674e" d="M 709.012 605.100 C 707.518 604.723 705.440 604.167 704.186 603.232 L 704.317 603.056 C 705.529 603.966 707.574 604.510 709.066 604.886 L 709.012 605.100 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 709.012 605.100 L 709.066 604.886 "/>
+<path fill="#77674e" d="M 704.186 603.232 C 703.145 602.453 701.996 601.026 701.508 599.818 L 701.712 599.735 C 702.183 600.910 703.301 602.298 704.317 603.056 L 704.186 603.232 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 704.186 603.232 L 704.317 603.056 "/>
+<path fill="#77674e" d="M 701.508 599.818 C 701.093 598.779 701.053 597.239 701.104 596.139 L 701.324 596.149 C 701.273 597.240 701.310 598.740 701.712 599.735 L 701.508 599.818 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 701.508 599.818 L 701.712 599.735 "/>
+<path fill="#77674e" d="M 701.104 596.139 C 701.139 595.394 701.346 594.409 701.571 593.701 L 701.781 593.767 C 701.560 594.463 701.357 595.424 701.324 596.150 L 701.104 596.139 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 701.104 596.139 L 701.324 596.150 "/>
+<path fill="#77674e" d="M 701.571 593.701 C 701.703 593.287 701.921 592.735 702.160 592.364 L 702.345 592.483 C 702.118 592.833 701.910 593.362 701.781 593.767 L 701.571 593.701 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 701.571 593.701 L 701.781 593.767 "/>
+<path fill="#77674e" d="M 702.160 592.364 C 702.245 592.234 702.489 592.036 702.595 592.043 L 702.494 592.141 C 702.588 592.135 702.413 592.376 702.345 592.483 L 702.160 592.364 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 702.160 592.364 L 702.345 592.483 "/>
+<path fill="#77674e" d="M 702.595 592.043 C 702.553 592.030 710.204 592.049 713.479 591.905 L 713.488 592.124 C 710.206 592.269 702.552 592.170 702.495 592.141 L 702.595 592.043 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 702.595 592.043 L 702.495 592.141 "/>
+<path fill="#8a7b66" fill-rule="evenodd" stroke="none" d="M 525.681 591.775 C 528.779 591.875 532.932 592.081 536.013 591.740 C 538.135 591.505 540.843 590.382 542.974 590.259 C 544.450 590.174 546.438 590.368 547.885 590.670 C 549.335 590.972 551.294 591.490 552.559 592.259 C 553.658 592.927 555.182 594.018 555.672 595.207 C 556.074 596.186 556.010 597.751 555.619 598.735 C 555.119 599.991 553.640 601.257 552.507 601.996 C 550.436 603.346 547.113 604.142 544.678 604.569 C 541.498 605.126 537.146 604.870 533.918 604.802 C 531.271 604.746 527.733 604.606 525.108 604.253 C 523.715 604.065 521.850 603.771 520.514 603.336 C 519.131 602.886 517.221 602.246 516.113 601.303 C 515.206 600.531 514.225 599.167 513.858 598.033 C 513.549 597.076 513.622 595.680 513.751 594.682 C 513.837 594.010 514.104 593.134 514.366 592.509 C 514.520 592.142 514.762 591.662 515.009 591.351 C 515.091 591.247 515.305 591.061 515.310 591.068 C 515.317 591.076 522.564 591.674 525.681 591.775 Z"/>
+<path fill="#77674e" d="M 525.684 591.665 C 528.784 591.765 532.930 591.971 536.001 591.631 L 536.025 591.850 C 532.934 592.191 528.774 591.985 525.677 591.885 L 525.684 591.665 Z"/>
+<path fill="#77674e" d="M 536.001 591.631 C 538.105 591.399 540.815 590.276 542.968 590.149 L 542.981 590.369 C 540.870 590.489 538.165 591.611 536.025 591.850 L 536.001 591.631 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 536.001 591.631 L 536.025 591.850 "/>
+<path fill="#77674e" d="M 542.968 590.149 C 544.454 590.064 546.453 590.259 547.907 590.562 L 547.862 590.778 C 546.422 590.477 544.447 590.284 542.981 590.369 L 542.968 590.149 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 542.968 590.149 L 542.981 590.369 "/>
+<path fill="#77674e" d="M 547.907 590.562 C 549.361 590.865 551.334 591.388 552.616 592.165 L 552.502 592.353 C 551.253 591.592 549.309 591.079 547.862 590.778 L 547.907 590.562 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 547.907 590.562 L 547.862 590.778 "/>
+<path fill="#77674e" d="M 552.616 592.165 C 553.720 592.836 555.265 593.945 555.773 595.165 L 555.570 595.249 C 555.100 594.091 553.597 593.019 552.502 592.353 L 552.616 592.165 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 552.616 592.165 L 552.502 592.353 "/>
+<path fill="#77674e" d="M 555.773 595.165 C 556.183 596.171 556.119 597.771 555.721 598.776 L 555.517 598.694 C 555.902 597.732 555.965 596.200 555.570 595.249 L 555.773 595.165 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 555.773 595.165 L 555.570 595.249 "/>
+<path fill="#77674e" d="M 555.721 598.776 C 555.205 600.059 553.707 601.345 552.568 602.088 L 552.447 601.904 C 553.573 601.170 555.032 599.923 555.517 598.694 L 555.721 598.776 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 555.721 598.776 L 555.517 598.694 "/>
+<path fill="#77674e" d="M 552.568 602.088 C 550.477 603.449 547.136 604.249 544.697 604.677 L 544.659 604.460 C 547.090 604.034 550.396 603.244 552.447 601.904 L 552.568 602.088 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 552.568 602.088 L 552.447 601.904 "/>
+<path fill="#77674e" d="M 544.697 604.677 C 541.502 605.236 537.142 604.980 533.916 604.912 L 533.921 604.692 C 537.151 604.760 541.493 605.016 544.659 604.460 L 544.697 604.677 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 544.697 604.677 L 544.659 604.460 "/>
+<path fill="#77674e" d="M 533.916 604.912 C 531.267 604.856 527.724 604.716 525.094 604.362 L 525.123 604.144 C 527.742 604.496 531.274 604.636 533.921 604.692 L 533.916 604.912 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 533.916 604.912 L 533.921 604.692 "/>
+<path fill="#77674e" d="M 525.094 604.362 C 523.699 604.174 521.826 603.878 520.480 603.441 L 520.548 603.231 C 521.875 603.663 523.731 603.957 525.123 604.144 L 525.094 604.362 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 525.094 604.362 L 525.123 604.144 "/>
+<path fill="#77674e" d="M 520.480 603.441 C 519.096 602.991 517.169 602.343 516.042 601.387 L 516.185 601.219 C 517.272 602.148 519.165 602.782 520.548 603.231 L 520.480 603.441 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 520.480 603.441 L 520.548 603.231 "/>
+<path fill="#77674e" d="M 516.042 601.387 C 515.124 600.604 514.128 599.219 513.754 598.067 L 513.963 598.000 C 514.322 599.115 515.288 600.458 516.185 601.219 L 516.042 601.387 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 516.042 601.387 L 516.185 601.219 "/>
+<path fill="#77674e" d="M 513.754 598.067 C 513.439 597.087 513.513 595.670 513.641 594.668 L 513.860 594.696 C 513.732 595.689 513.658 597.065 513.963 598.000 L 513.754 598.067 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 513.754 598.067 L 513.963 598.000 "/>
+<path fill="#77674e" d="M 513.641 594.668 C 513.730 593.985 514.000 593.097 514.265 592.466 L 514.468 592.551 C 514.208 593.170 513.944 594.034 513.860 594.696 L 513.641 594.668 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 513.641 594.668 L 513.860 594.696 "/>
+<path fill="#77674e" d="M 514.265 592.466 C 514.420 592.096 514.669 591.605 514.922 591.282 L 515.095 591.419 C 514.856 591.720 514.620 592.189 514.468 592.551 L 514.265 592.466 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 514.265 592.466 L 514.468 592.551 "/>
+<path fill="#77674e" d="M 514.922 591.282 C 515.014 591.168 515.260 591.007 515.364 591.024 L 515.255 591.112 C 515.349 591.116 515.167 591.326 515.095 591.419 L 514.922 591.282 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 514.922 591.282 L 515.095 591.419 "/>
+<path fill="#77674e" d="M 515.364 591.023 C 515.323 591.007 522.571 591.564 525.684 591.665 L 525.677 591.885 C 522.557 591.784 515.311 591.146 515.256 591.112 L 515.364 591.023 Z"/>
+<path fill="none" stroke="#77674e" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 515.364 591.023 L 515.256 591.112 "/>
+<path fill="#bb5e21" fill-rule="evenodd" stroke="none" d="M 574.703 359.609 C 573.834 356.357 573.509 351.846 572.997 348.519 C 572.997 348.518 572.327 342.534 572.618 339.989 C 572.818 338.234 573.260 335.836 574.134 334.302 C 574.750 333.222 575.864 331.833 576.984 331.294 C 577.754 330.923 578.969 330.862 579.817 330.974 C 581.024 331.133 582.556 331.848 583.566 332.528 C 585.900 334.100 588.147 337.244 589.919 339.430 C 592.292 342.357 594.888 346.686 597.162 349.690 C 599.459 352.723 602.347 356.968 605.151 359.540 C 607.674 361.855 611.587 364.307 614.581 365.967 C 617.513 367.593 621.589 369.537 624.809 370.470 C 628.467 371.530 633.572 372.601 637.370 372.317 C 639.348 372.169 641.906 371.307 643.744 370.562 C 645.916 369.681 648.524 367.904 650.579 366.775 C 651.796 366.106 653.285 364.852 654.643 364.558 C 655.864 364.294 657.688 364.265 658.799 364.836 C 659.797 365.348 660.768 366.665 661.201 367.699 C 662.122 369.899 661.693 373.260 661.570 375.642 C 661.446 378.049 660.696 381.198 660.370 383.586 C 660.124 385.384 659.666 387.775 659.630 389.589 C 659.555 393.495 660.172 398.713 660.933 402.544 C 662.482 410.340 666.078 420.382 668.916 427.806 C 670.357 431.576 672.965 436.322 674.362 440.108 C 676.082 444.767 677.793 451.180 679.056 455.983 C 680.705 462.252 682.432 470.726 683.883 477.043 C 684.639 480.334 685.521 484.753 686.406 488.012 C 687.669 492.664 689.505 498.840 691.262 503.330 C 691.830 504.783 692.492 506.806 693.414 508.065 C 694.658 509.763 696.841 511.682 698.687 512.693 C 700.399 513.630 702.986 514.349 704.929 514.522 C 707.195 514.724 710.315 514.412 712.463 513.661 C 714.104 513.088 716.085 511.770 717.413 510.648 C 718.847 509.437 720.512 507.507 721.503 505.913 C 723.193 503.193 724.493 499.055 725.485 496.011 C 726.989 491.395 728.413 485.060 729.359 480.299 C 730.639 473.858 731.676 465.152 732.584 458.649 C 733.327 453.325 734.101 446.198 734.903 440.883 C 736.436 430.715 738.913 417.226 740.776 407.113 C 742.350 398.566 744.775 387.231 746.295 378.674 C 747.467 372.081 749.099 363.293 749.868 356.641 C 750.044 355.124 750.697 353.033 750.274 351.565 C 749.986 350.561 749.078 349.379 748.270 348.717 C 747.520 348.102 746.226 347.736 745.316 347.398 C 744.495 347.093 743.195 347.114 742.521 346.554 C 741.954 346.084 741.545 345.104 741.360 344.392 C 741.033 343.129 741.211 341.332 741.421 340.045 C 741.865 337.324 743.366 333.905 744.424 331.358 C 745.442 328.908 747.330 325.878 748.306 323.411 C 749.410 320.617 750.650 316.781 751.235 313.833 C 751.970 310.129 752.211 305.068 752.367 301.295 C 752.571 296.372 752.235 289.800 752.206 284.873 C 752.154 276.232 752.551 264.701 752.157 256.069 C 751.788 247.985 750.879 237.215 749.759 229.200 C 748.843 222.641 747.069 213.978 745.662 207.506 C 744.454 201.948 742.691 194.565 741.143 189.091 C 740.108 185.430 738.611 180.576 737.302 177.003 C 736.594 175.070 735.257 172.636 734.697 170.656 C 733.861 167.703 733.308 163.611 733.141 160.547 C 732.945 156.943 733.371 152.123 733.707 148.529 C 733.915 146.311 734.409 143.378 734.710 141.170 C 733.610 132.812 732.143 121.668 731.043 113.310 C 728.919 114.612 725.909 116.096 723.962 117.650 C 721.664 119.483 718.981 122.392 717.144 124.687 C 715.598 126.621 713.775 129.398 712.599 131.578 C 710.850 134.821 709.055 139.421 707.829 142.896 C 706.489 146.693 705.021 151.872 704.139 155.800 C 703.257 159.725 702.468 165.041 701.958 169.031 C 701.010 176.454 700.145 186.406 699.813 193.881 C 699.398 203.217 699.265 215.700 699.787 225.031 C 699.924 227.476 700.428 230.710 700.608 233.153 C 700.923 237.432 701.270 243.151 701.225 247.441 C 701.193 250.401 701.060 254.362 700.628 257.291 C 700.189 260.261 699.485 264.262 698.319 267.029 C 697.167 269.758 694.961 273.122 693.031 275.370 C 691.195 277.508 688.372 280.099 685.956 281.551 C 683.270 283.165 679.258 284.638 676.181 285.232 C 671.852 286.067 665.885 285.637 661.484 285.366 C 657.772 285.137 652.859 284.377 649.191 283.762 C 640.422 282.292 628.926 279.310 620.197 277.616 C 612.046 276.034 601.155 274.014 592.940 272.806 C 586.083 271.798 576.908 270.641 570.000 270.080 C 565.629 269.725 559.784 269.438 555.399 269.394 C 552.870 269.369 549.492 269.389 546.971 269.590 C 544.782 269.765 541.863 270.100 539.719 270.570 C 534.793 271.650 528.366 273.763 523.717 275.717 C 519.477 277.499 514.050 280.417 510.140 282.839 C 506.075 285.357 500.788 288.991 497.231 292.187 C 493.722 295.339 489.612 300.152 486.701 303.863 C 484.074 307.213 480.866 311.918 478.714 315.591 C 476.687 319.052 474.094 323.778 472.744 327.556 C 471.309 331.574 470.332 337.225 469.616 341.432 C 469.339 343.053 469.091 345.235 468.935 346.873 C 468.688 349.478 468.222 352.968 468.391 355.579 C 468.699 360.324 470.084 366.600 471.656 371.087 C 473.574 376.562 477.566 383.275 480.443 388.313 C 483.643 393.915 488.604 400.964 491.997 406.451 C 494.059 409.785 496.878 414.194 498.734 417.647 C 500.232 420.434 502.105 424.225 503.292 427.158 C 504.636 430.480 506.383 434.974 507.057 438.494 C 507.676 441.728 507.749 446.157 507.713 449.450 C 507.667 453.646 507.290 459.262 506.520 463.387 C 506.007 466.140 504.815 469.695 503.978 472.367 C 503.080 475.230 501.321 478.883 500.720 481.823 C 500.302 483.864 500.114 486.662 500.158 488.745 C 500.196 490.512 500.434 492.879 500.862 494.593 C 501.173 495.840 501.725 497.493 502.378 498.599 C 503.433 500.386 505.342 502.477 506.949 503.789 C 508.944 505.418 511.971 507.232 514.428 508.005 C 516.521 508.663 519.513 508.880 521.704 508.753 C 523.917 508.624 526.899 508.068 528.915 507.146 C 531.432 505.995 534.369 503.586 536.269 501.573 C 538.316 499.403 540.274 495.872 541.784 493.300 C 544.539 488.610 547.524 481.981 549.945 477.111 C 552.609 471.750 556.119 464.582 558.723 459.193 C 562.118 452.166 566.998 442.948 569.905 435.706 C 572.600 428.993 575.595 419.799 577.492 412.819 C 578.856 407.798 580.486 401.029 581.174 395.872 C 581.735 391.662 582.215 385.975 581.943 381.737 C 581.810 379.664 581.363 376.907 580.789 374.911 C 580.167 372.748 578.739 370.077 577.904 367.987 C 576.906 365.489 575.398 362.208 574.703 359.609 M 731.043 113.310 C 731.043 113.310 731.043 113.310 731.043 113.310 Z"/>
+<path fill="none" stroke="#aa5115" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 572.997 348.519 C 572.997 348.519 572.997 348.519 572.997 348.519 C 573.509 351.846 573.834 356.357 574.703 359.609 C 575.398 362.208 576.906 365.489 577.904 367.987 C 578.739 370.077 580.167 372.748 580.789 374.911 C 581.363 376.907 581.810 379.664 581.943 381.737 C 582.215 385.975 581.735 391.662 581.174 395.872 C 580.486 401.029 578.856 407.798 577.492 412.819 C 575.595 419.799 572.600 428.993 569.905 435.706 C 566.998 442.948 562.118 452.166 558.723 459.193 C 556.119 464.582 552.609 471.750 549.945 477.111 C 547.524 481.981 544.539 488.610 541.784 493.300 C 540.274 495.872 538.316 499.403 536.269 501.573 C 534.369 503.586 531.432 505.995 528.915 507.146 C 526.899 508.068 523.917 508.624 521.704 508.753 C 519.513 508.880 516.521 508.663 514.428 508.005 C 511.971 507.232 508.944 505.418 506.949 503.789 C 505.342 502.477 503.433 500.386 502.378 498.599 C 501.725 497.493 501.173 495.840 500.862 494.593 C 500.434 492.879 500.196 490.512 500.158 488.745 C 500.114 486.662 500.302 483.864 500.720 481.823 C 501.321 478.883 503.080 475.230 503.978 472.367 C 504.815 469.695 506.007 466.140 506.520 463.387 C 507.290 459.262 507.667 453.646 507.713 449.450 C 507.749 446.157 507.676 441.728 507.057 438.494 C 506.383 434.974 504.636 430.480 503.292 427.158 C 502.105 424.225 500.232 420.434 498.734 417.647 C 496.878 414.194 494.059 409.785 491.997 406.451 C 488.604 400.964 483.643 393.915 480.443 388.313 C 477.566 383.275 473.574 376.562 471.656 371.087 C 470.084 366.600 468.699 360.324 468.391 355.579 C 468.222 352.968 468.688 349.478 468.935 346.873 C 469.091 345.235 469.339 343.053 469.616 341.432 C 470.332 337.225 471.309 331.574 472.744 327.556 C 474.094 323.778 476.687 319.052 478.714 315.591 C 480.866 311.918 484.074 307.213 486.701 303.863 C 489.612 300.152 493.722 295.339 497.231 292.187 C 500.788 288.991 506.075 285.357 510.140 282.839 C 514.050 280.417 519.477 277.499 523.717 275.717 C 528.366 273.763 534.793 271.650 539.719 270.570 C 541.863 270.100 544.782 269.765 546.971 269.590 C 549.492 269.389 552.870 269.369 555.399 269.394 C 559.784 269.438 565.629 269.725 570.000 270.080 C 576.908 270.641 586.083 271.798 592.940 272.806 C 601.155 274.014 612.046 276.034 620.197 277.616 C 628.926 279.310 640.422 282.292 649.191 283.762 C 652.859 284.377 657.772 285.137 661.484 285.366 C 665.885 285.637 671.852 286.067 676.181 285.232 C 679.258 284.638 683.270 283.165 685.956 281.551 C 688.372 280.099 691.195 277.508 693.031 275.370 C 694.961 273.122 697.167 269.758 698.319 267.029 C 699.485 264.262 700.189 260.261 700.628 257.291 C 701.060 254.362 701.193 250.401 701.225 247.441 C 701.270 243.151 700.923 237.432 700.608 233.153 C 700.428 230.710 699.924 227.476 699.787 225.031 C 699.265 215.700 699.398 203.217 699.813 193.881 C 700.145 186.406 701.010 176.454 701.958 169.031 C 702.468 165.041 703.257 159.725 704.139 155.800 C 705.021 151.872 706.489 146.693 707.829 142.896 C 709.055 139.421 710.850 134.821 712.599 131.578 C 713.775 129.398 715.598 126.621 717.144 124.687 C 718.981 122.392 721.664 119.483 723.962 117.650 C 725.909 116.096 728.919 114.612 731.043 113.310 C 731.043 113.310 731.043 113.310 731.043 113.310 C 732.143 121.668 733.610 132.812 734.710 141.170 C 734.710 141.170 734.710 141.170 734.710 141.170 C 734.710 141.170 734.710 141.170 734.710 141.170 C 734.409 143.378 733.915 146.311 733.707 148.529 C 733.371 152.123 732.945 156.943 733.141 160.547 C 733.308 163.611 733.861 167.703 734.697 170.656 C 735.257 172.636 736.594 175.070 737.302 177.003 C 738.611 180.576 740.108 185.430 741.143 189.091 C 742.691 194.565 744.454 201.948 745.662 207.506 C 747.069 213.978 748.843 222.641 749.759 229.200 C 750.879 237.215 751.788 247.985 752.157 256.069 C 752.551 264.701 752.154 276.232 752.206 284.873 C 752.235 289.800 752.571 296.372 752.367 301.295 C 752.211 305.068 751.970 310.129 751.235 313.833 C 750.650 316.781 749.410 320.617 748.306 323.411 C 747.330 325.878 745.442 328.908 744.424 331.358 C 743.366 333.905 741.865 337.324 741.421 340.045 C 741.211 341.332 741.033 343.129 741.360 344.392 C 741.545 345.104 741.954 346.084 742.521 346.554 C 743.195 347.114 744.495 347.093 745.316 347.398 C 746.226 347.736 747.520 348.102 748.270 348.717 C 749.078 349.379 749.986 350.561 750.274 351.565 C 750.697 353.033 750.044 355.124 749.868 356.641 C 749.099 363.293 747.467 372.081 746.295 378.674 C 744.775 387.231 742.350 398.566 740.776 407.113 C 738.913 417.226 736.436 430.715 734.903 440.883 C 734.101 446.198 733.327 453.325 732.584 458.649 C 731.676 465.152 730.639 473.858 729.359 480.299 C 728.413 485.060 726.989 491.395 725.485 496.011 C 724.493 499.055 723.193 503.193 721.503 505.913 C 720.512 507.507 718.847 509.437 717.413 510.648 C 716.085 511.770 714.104 513.088 712.463 513.661 C 710.315 514.412 707.195 514.724 704.929 514.522 C 702.986 514.349 700.399 513.630 698.687 512.693 C 696.841 511.682 694.658 509.763 693.414 508.065 C 692.492 506.806 691.830 504.783 691.262 503.330 C 689.505 498.840 687.669 492.664 686.406 488.012 C 685.521 484.753 684.639 480.334 683.883 477.043 C 682.432 470.726 680.705 462.252 679.056 455.983 C 677.793 451.180 676.082 444.767 674.362 440.108 C 672.965 436.322 670.357 431.576 668.916 427.806 C 666.078 420.382 662.482 410.340 660.933 402.544 C 660.172 398.713 659.555 393.495 659.630 389.589 C 659.666 387.775 660.124 385.384 660.370 383.586 C 660.696 381.198 661.446 378.049 661.570 375.642 C 661.693 373.260 662.122 369.899 661.201 367.699 C 660.768 366.665 659.797 365.348 658.799 364.836 C 657.688 364.265 655.864 364.294 654.643 364.558 C 653.285 364.852 651.796 366.106 650.579 366.775 C 648.524 367.904 645.916 369.681 643.744 370.562 C 641.906 371.307 639.348 372.169 637.370 372.317 C 633.572 372.601 628.467 371.530 624.809 370.470 C 621.589 369.537 617.513 367.593 614.581 365.967 C 611.587 364.307 607.674 361.855 605.151 359.540 C 602.347 356.968 599.459 352.723 597.162 349.690 C 594.888 346.686 592.292 342.357 589.919 339.430 C 588.147 337.244 585.900 334.100 583.566 332.528 C 582.556 331.848 581.024 331.133 579.817 330.974 C 578.969 330.862 577.754 330.923 576.984 331.294 C 575.864 331.833 574.750 333.222 574.134 334.302 C 573.260 335.836 572.818 338.234 572.618 339.989 C 572.327 342.534 572.997 348.518 572.997 348.519 "/>
+<path fill="#ac9783" fill-rule="evenodd" stroke="#9b8d73" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 735.004 111.393 C 736.851 110.687 739.410 109.979 741.357 109.635 C 743.197 109.310 745.700 109.226 747.566 109.132 C 749.857 109.017 752.923 108.827 755.211 108.989 C 759.320 109.278 764.746 110.324 768.745 111.317 C 771.083 111.898 774.141 112.911 776.395 113.763 C 782.226 115.966 789.898 119.256 795.339 122.298 C 798.575 124.108 802.650 126.936 805.622 129.154 C 810.031 132.445 815.664 137.175 819.666 140.952 C 821.191 142.391 823.434 144.190 824.512 145.988 C 824.802 146.472 825.074 147.192 825.178 147.746 C 825.309 148.447 825.260 149.414 825.178 150.122 C 824.784 153.485 823.451 157.864 822.187 161.005 C 821.864 161.808 821.448 162.926 820.875 163.574 C 819.595 165.019 817.193 166.243 815.395 166.942 C 813.316 167.750 810.311 168.138 808.088 168.312 C 805.457 168.519 801.900 168.457 799.297 168.027 C 797.890 167.795 796.131 166.976 794.730 166.714 C 792.147 166.230 788.624 166.076 785.997 166.029 C 783.220 165.979 779.525 166.342 776.749 166.428 C 774.253 166.506 770.922 166.701 768.428 166.587 C 764.314 166.400 758.758 166.108 754.796 164.987 C 750.586 163.797 745.079 161.449 741.579 158.824 C 738.739 156.693 735.724 152.909 733.697 149.993 C 732.238 147.894 730.636 144.852 729.656 142.491 C 728.476 139.647 727.225 135.694 726.732 132.655 C 726.263 129.760 726.345 125.818 726.400 122.886 C 726.426 121.523 726.447 119.692 726.692 118.351 C 726.851 117.480 727.057 116.271 727.527 115.521 C 727.659 115.311 727.916 115.093 728.105 114.933 C 728.244 114.815 728.451 114.687 728.599 114.582 C 728.599 114.582 728.599 114.582 728.599 114.582 C 728.604 114.583 732.999 112.160 735.004 111.393 Z"/>
+<path fill="#4b4642" fill-rule="evenodd" stroke="none" d="M 805.784 147.146 C 805.476 146.807 805.186 146.259 804.930 145.880 C 804.930 145.880 809.052 145.930 810.818 145.975 C 812.765 146.023 815.359 146.167 817.307 146.196 C 819.605 146.232 822.669 146.174 824.968 146.165 C 824.968 146.165 825.795 146.553 826.012 146.861 C 826.474 147.518 826.460 148.693 826.496 149.496 C 826.549 150.730 826.351 152.390 826.058 153.590 C 825.521 155.794 824.329 158.623 823.196 160.587 C 822.804 161.267 822.110 162.062 821.645 162.694 C 821.645 162.694 821.545 161.809 821.248 161.661 C 820.900 161.488 820.362 161.884 820.015 162.058 C 819.323 162.407 818.630 163.240 817.948 163.609 C 816.301 164.500 813.842 165.123 812.026 165.581 C 810.154 166.052 807.611 166.545 805.685 166.679 C 804.101 166.790 801.967 166.738 800.393 166.529 C 799.402 166.398 797.988 166.321 797.148 165.780 C 796.799 165.556 796.519 165.046 796.249 164.732 C 796.249 164.732 798.156 165.249 798.995 165.331 C 801.951 165.618 805.946 165.286 808.881 164.832 C 810.238 164.622 812.044 164.229 813.324 163.733 C 814.837 163.147 816.875 162.237 818.067 161.137 C 818.620 160.627 819.240 159.790 819.515 159.090 C 820.193 157.369 820.017 154.798 820.064 152.949 C 820.079 152.380 820.029 151.621 820.014 151.052 C 820.014 151.052 819.237 151.133 818.904 151.168 C 817.751 151.110 816.201 151.149 815.059 150.976 C 813.007 150.664 810.223 150.126 808.380 149.172 C 807.503 148.718 806.450 147.876 805.784 147.146 M 818.904 151.168 C 818.904 151.168 818.904 151.168 818.904 151.168 Z"/>
+<path fill="none" stroke="#4b4642" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 804.930 145.880 C 804.930 145.880 804.930 145.880 804.930 145.880 C 805.186 146.259 805.476 146.807 805.784 147.146 C 806.450 147.876 807.503 148.718 808.380 149.172 C 810.223 150.126 813.007 150.664 815.059 150.976 C 816.201 151.149 817.751 151.110 818.904 151.168 C 818.904 151.168 818.904 151.168 818.904 151.168 C 819.237 151.133 820.014 151.052 820.014 151.052 C 820.014 151.052 820.014 151.052 820.014 151.052 C 820.029 151.621 820.079 152.380 820.064 152.949 C 820.017 154.798 820.193 157.369 819.515 159.090 C 819.240 159.790 818.620 160.627 818.067 161.137 C 816.875 162.237 814.837 163.147 813.324 163.733 C 812.044 164.229 810.238 164.622 808.881 164.832 C 805.946 165.286 801.951 165.618 798.995 165.331 C 798.156 165.249 796.249 164.732 796.249 164.732 C 796.249 164.732 796.249 164.732 796.249 164.732 C 796.519 165.046 796.799 165.556 797.148 165.780 C 797.988 166.321 799.402 166.398 800.393 166.529 C 801.967 166.738 804.101 166.790 805.685 166.679 C 807.611 166.545 810.154 166.052 812.026 165.581 C 813.842 165.123 816.301 164.500 817.948 163.609 C 818.630 163.240 819.323 162.407 820.015 162.058 C 820.362 161.884 820.900 161.488 821.248 161.661 C 821.545 161.809 821.645 162.694 821.645 162.694 C 821.645 162.694 821.645 162.694 821.645 162.694 C 822.110 162.062 822.804 161.267 823.196 160.587 C 824.329 158.623 825.521 155.794 826.058 153.590 C 826.351 152.390 826.549 150.730 826.496 149.496 C 826.460 148.693 826.474 147.518 826.012 146.861 C 825.795 146.553 824.968 146.165 824.968 146.165 C 824.968 146.165 824.968 146.165 824.968 146.165 C 822.669 146.174 819.605 146.232 817.307 146.196 C 815.359 146.167 812.765 146.023 810.818 145.975 C 809.052 145.930 804.930 145.880 804.930 145.880 "/>
+<path fill="#333132" fill-rule="evenodd" stroke="#2c2924" stroke-width="0" stroke-linecap="round" stroke-linejoin="round" d="M 773.415 137.847 C 773.415 137.847 773.415 137.847 773.415 137.847 C 773.291 138.033 773.157 138.306 773.002 138.466 C 772.347 139.144 771.227 139.796 770.358 140.160 C 769.234 140.631 767.607 140.949 766.391 141.028 C 765.012 141.118 763.128 141.013 761.805 140.615 C 760.690 140.280 759.299 139.505 758.375 138.797 C 757.422 138.066 756.322 136.858 755.648 135.863 C 754.964 134.853 754.204 133.370 753.913 132.186 C 753.655 131.137 753.797 129.669 753.747 128.591 C 753.747 128.591 753.747 128.591 753.747 128.591 C 754.318 128.517 755.074 128.375 755.648 128.343 C 757.456 128.241 759.911 128.166 761.681 128.550 C 762.801 128.792 764.225 129.411 765.234 129.955 C 766.860 130.831 768.921 132.249 770.234 133.549 C 771.373 134.678 773.415 137.846 773.415 137.847 C 773.415 137.847 773.415 137.847 773.415 137.847 Z"/>
+<path fill="#e5e3e4" fill-rule="evenodd" stroke="#e5e3e4" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" d="M 757.590 129.293 C 758.724 129.293 759.697 130.253 759.697 131.525 C 759.697 132.796 758.724 133.756 757.590 133.756 C 756.456 133.756 755.483 132.796 755.483 131.525 C 755.483 130.253 756.456 129.293 757.590 129.293 Z"/>
+<path fill="#3e3633" d="M 740.081 132.203 C 750.402 126.042 765.773 123.366 773.614 135.733 L 771.050 137.290 C 764.604 126.129 751.417 128.866 741.625 134.775 L 740.081 132.203 Z"/>
+<path fill="#3e3633" d="M 773.614 135.733 C 774.762 137.623 775.394 140.844 775.410 143.259 L 774.810 143.259 C 774.825 141.034 772.220 139.217 771.050 137.290 L 773.614 135.733 Z"/>
+<path fill="none" stroke="#3e3633" stroke-width="1" stroke-linecap="butt" stroke-linejoin="round" d="M 773.614 135.733 L 771.050 137.290 "/>
+</g>
+</svg>
diff --git a/chatbot.py b/chatbot.py
index 31021c0..fa44857 100644
--- a/chatbot.py
+++ b/chatbot.py
@@ -1,27 +1,31 @@
-import openai
 import gradio as gr
+import openai
 
-
-if __name__ == "__main__":
-    openai.api_key = "Your API key"
+if __name__ == '__main__':
+    openai.api_key = 'Your API key'
 
     messages = [
-        {"role": "system", "content": "You are a helpful and kind AI Assistant."},
+        {
+            'role': 'system',
+            'content': 'You are a helpful and kind AI Assistant.'
+        },
     ]
 
     def chatbot(input):
         if input:
-            messages.append({"role": "user", "content": input})
-            chat = openai.ChatCompletion.create(
-                model="gpt-3.5-turbo", messages=messages
-            )
+            messages.append({'role': 'user', 'content': input})
+            chat = openai.ChatCompletion.create(model='gpt-3.5-turbo',
+                                                messages=messages)
             reply = chat.choices[0].message.content
-            messages.append({"role": "assistant", "content": reply})
+            messages.append({'role': 'assistant', 'content': reply})
             return reply
 
-    inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
-    outputs = gr.outputs.Textbox(label="Reply")
+    inputs = gr.inputs.Textbox(lines=7, label='Chat with AI')
+    outputs = gr.outputs.Textbox(label='Reply')
 
-    gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
-                description="Ask anything you want",
-                theme="compact").launch(share=True)
\ No newline at end of file
+    gr.Interface(fn=chatbot,
+                 inputs=inputs,
+                 outputs=outputs,
+                 title='AI Chatbot',
+                 description='Ask anything you want',
+                 theme='compact').launch(share=True)
diff --git a/chatllms/configs/gen_args.py b/chatllms/configs/gen_args.py
index ca5df19..8ed84fd 100644
--- a/chatllms/configs/gen_args.py
+++ b/chatllms/configs/gen_args.py
@@ -4,9 +4,7 @@ from typing import Any, Dict, Optional
 
 @dataclass
 class GenerationArguments:
-    """
-    Arguments pertaining to specify the model generation parameters.
-    """
+    """Arguments pertaining to specify the model generation parameters."""
     # generation parameters
     # 是否使用cache
     use_cache: Optional[bool] = field(default=True)
diff --git a/chatllms/data/conv_dataset.py b/chatllms/data/conv_dataset.py
index 4e885f3..5f9f3e9 100644
--- a/chatllms/data/conv_dataset.py
+++ b/chatllms/data/conv_dataset.py
@@ -13,22 +13,22 @@ from chatllms.data.sft_dataset import DataCollatorForSupervisedDataset
 
 @dataclass
 class VicunaDataset(Dataset):
-    """
-    Dataset for multi-turn conversations using a Transformer model.
+    """Dataset for multi-turn conversations using a Transformer model.
 
     Attributes:
         raw_data: The preprocessed dataset dict to load
         tokenizer: Pretrained tokenizer to encode text
         max_seq_length: Maximum sequence length for model inputs
     """
+
     def __init__(
         self,
         raw_data: datasets.DatasetDict,
         tokenizer: PreTrainedTokenizer,
         max_seq_length: int = 1024,
     ):
-        """
-        Initialize the dataset with conversations, tokenizer, and max sequence length.
+        """Initialize the dataset with conversations, tokenizer, and max
+        sequence length.
 
         Args:
             raw_data: The preprocessed dataset dict to load
@@ -51,8 +51,7 @@ class VicunaDataset(Dataset):
     def tokenize_conversation(
             self,
             conversation: List[Dict]) -> Tuple[torch.Tensor, torch.Tensor]:
-        """
-        Tokenize a single conversation into input IDs and labels.
+        """Tokenize a single conversation into input IDs and labels.
 
         Args:
             conversation: List of turns in the conversation
@@ -105,8 +104,7 @@ class VicunaDataset(Dataset):
         return torch.tensor(input_ids), torch.tensor(labels)
 
     def _get_human_prefix(self, turn_id: int, role: str) -> str:
-        """
-        Get the prefix for a human turn.
+        """Get the prefix for a human turn.
 
         Args:
             turn_id: Index of the current turn
@@ -126,8 +124,7 @@ class VicunaDataset(Dataset):
         return len(self.raw_data)
 
     def __getitem__(self, index: int) -> Dict:
-        """
-        Get the input IDs and labels for a specific conversation.
+        """Get the input IDs and labels for a specific conversation.
 
         Args:
             index: Index of the conversation
@@ -147,23 +144,22 @@ class VicunaDataset(Dataset):
 
 @dataclass
 class ConversationDataset(Dataset):
-    """
-    Dataset for multi-turn conversations using Transformer model.
+    """Dataset for multi-turn conversations using Transformer model.
 
     Attributes:
         raw_data: The preprocessed dataset dict to load
         tokenizer: Pretrained tokenizer
         max_seq_length: Maximum length of sequence
     """
+
     def __init__(
         self,
         raw_data: datasets.DatasetDict,
         tokenizer: PreTrainedTokenizer,
         max_seq_length: int = 1024,
     ):
-        """
-        Initialize the dataset with conversations, tokenizer and max sequence length.
-        """
+        """Initialize the dataset with conversations, tokenizer and max
+        sequence length."""
         self.raw_data = raw_data
         self.tokenizer = tokenizer
         self.max_seq_length = max_seq_length
@@ -174,8 +170,7 @@ class ConversationDataset(Dataset):
         self,
         conversation: List[Dict],
     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
-        """
-        Tokenize a single conversation into input IDs and labels.
+        """Tokenize a single conversation into input IDs and labels.
 
         Args:
             conversation: List of turns in the conversation
@@ -218,8 +213,7 @@ class ConversationDataset(Dataset):
         return len(self.raw_data)
 
     def __getitem__(self, index: int) -> Dict[str, torch.Tensor]:
-        """
-        Get the input IDs and labels for a specific conversation.
+        """Get the input IDs and labels for a specific conversation.
 
         Args:
             index: Index of the conversation
@@ -248,9 +242,9 @@ class ConversationDataset(Dataset):
 
 @dataclass
 class ConversationDataCollator(object):
-    """
-    Collate and pad a batch of conversation examples to prepare for training.
-    """
+    """Collate and pad a batch of conversation examples to prepare for
+    training."""
+
     def __init__(
         self,
         tokenizer: PreTrainedTokenizer,
@@ -300,8 +294,7 @@ class ConversationDataCollator(object):
 
 def make_conversation_data_module(tokenizer: PreTrainedTokenizer,
                                   args) -> Dict[str, Dataset]:
-    """
-    Create dataset and collator for conversation modeling.
+    """Create dataset and collator for conversation modeling.
 
     Args:
         tokenizer (PreTrainedTokenizer): The tokenizer object.
@@ -310,7 +303,6 @@ def make_conversation_data_module(tokenizer: PreTrainedTokenizer,
 
     Returns:
         dict: A dictionary containing the train_dataset and eval_dataset.
-
     """
     # Determine the appropriate dataset class based on dataset_type flag
     dataset_cls = (VicunaDataset if args.conversation_template == 'vicuna' else
diff --git a/chatllms/data/data_utils.py b/chatllms/data/data_utils.py
index 01e96a2..7c03cfa 100644
--- a/chatllms/data/data_utils.py
+++ b/chatllms/data/data_utils.py
@@ -87,8 +87,7 @@ def extract_default_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
 
 
 def extract_alpaca_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
-    """
-    Extracts input from an example in the Alpaca dataset.
+    """Extracts input from an example in the Alpaca dataset.
 
     Args:
         example: A dictionary containing a single example from the Alpaca dataset.
@@ -100,7 +99,6 @@ def extract_alpaca_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
         >>> example = {'input': 'example input', 'output': 'example output'}
         >>> extract_alpaca_dataset(example)
         {'input': 'example input'}
-
     """
     if example.get('input', '') != '':
         prompt_format = ALPACA_PROMPT_DICT['prompt_input']
@@ -110,8 +108,8 @@ def extract_alpaca_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
 
 
 def extract_vicuna_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
-    """
-    Extracts the input and output portions of a single conversation example from the Vicuña format.
+    """Extracts the input and output portions of a single conversation example
+    from the Vicuña format.
 
     Args:
         example (Dict[str, Any]): A single conversation example in the Vicuña format.
@@ -184,8 +182,8 @@ def extract_random_prompt_dataset(example: Dict[str, Any]) -> Dict[str, str]:
 
 def local_dataset(dataset_path: str,
                   eval_dataset_size: float = 0.1) -> Tuple[Dataset, Dataset]:
-    """
-    Reads in a dataset from a file and returns it as a split train-test dataset.
+    """Reads in a dataset from a file and returns it as a split train-test
+    dataset.
 
     Args:
         dataset_path (str): The name of the dataset file to read in. \
@@ -195,7 +193,6 @@ def local_dataset(dataset_path: str,
         A tuple containing two datasets - the training subset and the testing subset.
     Raises:
         ValueError: If the specified file format is unsupported.
-
     """
 
     # Read in the full dataset from file based on the file format
@@ -221,8 +218,7 @@ def local_dataset(dataset_path: str,
 def load_data(
         dataset_path: str,
         eval_dataset_size: float = 0.1) -> Union[Dict[str, Dataset], None]:
-    """
-    Load a dataset based on its name.
+    """Load a dataset based on its name.
 
     Args:
         dataset_path: A string representing the path to the dataset to be loaded.
@@ -238,7 +234,6 @@ def load_data(
     Examples:
         >>> load_data('alpaca')
         {'train': Dataset(...), 'validation': Dataset(...), 'test': Dataset(...)}
-
     """
     if not os.path.exists(dataset_path):
         # Download dataset from HuggingFace Datasets
@@ -263,9 +258,7 @@ def formate_instruction_dataset(
         dataset_name: str,
         dataset_format: str,
         instruction_template: str = 'default') -> Optional[Dict[str, Dataset]]:
-    """
-    Formats a given dataset based on its name and format.
-
+    """Formats a given dataset based on its name and format.
 
     Removes unused columns, renames columns to 'input' and 'output',
     and applies dataset-specific formatting based on the dataset_name.
@@ -283,6 +276,7 @@ def formate_instruction_dataset(
         specified format.
         None if the dataset does not exist or if the format is not recognized.
     """
+
     def _format_dolly15k(dataset: Dataset) -> Dataset:
         """Format Dolly-15k dataset."""
         dataset = dataset.rename_column('context', 'input')
@@ -376,8 +370,8 @@ def split_train_eval(
     do_train: bool = True,
     max_train_samples: int = None,
 ) -> Dict[str, Dataset]:
-    """
-    Prepare the training and evaluation datasets for a machine learning model.
+    """Prepare the training and evaluation datasets for a machine learning
+    model.
 
     Args:
         dataset (DatasetDict): The complete dataset containing train, validation, and test splits.
@@ -435,9 +429,8 @@ def split_train_eval(
 
 
 def make_data_module(args):
-    """
-    Make dataset and collator for supervised fine-tuning.
-    Datasets are expected to have the following columns: { `input`, `output` }
+    """Make dataset and collator for supervised fine-tuning. Datasets are
+    expected to have the following columns: { `input`, `output` }
 
     Available datasets to be selected with `dataset` argument:
         - alpaca, 52002 examples
@@ -456,7 +449,6 @@ def make_data_module(args):
         - supernatural-instructions, 69624 examples (same as paper with 100 ex/task more can be used)
         - flan (FLAN v2), up to 20M examples available
         - vicuna
-
     """
     train_datasets: List[Dataset] = []
     eval_datasets: List[Dataset] = []
diff --git a/chatllms/data/sft_dataset.py b/chatllms/data/sft_dataset.py
index 71383dd..a4c0177 100644
--- a/chatllms/data/sft_dataset.py
+++ b/chatllms/data/sft_dataset.py
@@ -16,8 +16,7 @@ logger = logging.getLogger(__name__)
 
 
 class SFTInstructionDataset(Dataset):
-    """
-    Dataset for supervised fine-tuning of instruction following models.
+    """Dataset for supervised fine-tuning of instruction following models.
 
     Converts raw dataset containing source/target instructions
     into tokenized input/target pairs with truncation and padding.
@@ -26,14 +25,13 @@ class SFTInstructionDataset(Dataset):
         dataset: The raw dataset containing source/target examples
         tokenizer: Tokenizer to use for encoding text
         max_seq_len: Maximum sequence length for truncation
-
     """
+
     def __init__(self,
                  raw_data: DatasetDict,
                  tokenizer: PreTrainedTokenizer,
                  max_seq_len: int = 1024):
-        """
-        Initialize the dataset with the raw data and tokenizer.
+        """Initialize the dataset with the raw data and tokenizer.
 
         Args:
             raw_data: Raw dataset containing source/target examples
@@ -45,12 +43,11 @@ class SFTInstructionDataset(Dataset):
         self.max_seq_len = max_seq_len
 
     def __len__(self) -> int:
-        """Return number of examples in dataset"""
+        """Return number of examples in dataset."""
         return len(self.dataset)
 
     def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
-        """
-        Convert an raw example into tokenized input/target pair.
+        """Convert an raw example into tokenized input/target pair.
 
         Args:
             idx: Index of the example in the dataset
@@ -107,14 +104,15 @@ class SFTInstructionDataset(Dataset):
 class SupervisedDataset(Dataset):
     """Dataset for supervised fine-tuning.
 
-        Args:
-            hf_dataset (dataset): The preprocesed dataset to load.
-            tokenizer (PreTrainedTokenizer): The tokenizer to use when tokenizing the data.
-            source_max_len (int): The maximum length allowed for the source text.
-            target_max_len (int): The maximum length allowed for the target text.
-            train_on_source (bool): If True, the model will be trained on the source text as well as the target text.
-            predict_with_generate (bool): If True, the model will generate predictions instead of training.
+    Args:
+        hf_dataset (dataset): The preprocesed dataset to load.
+        tokenizer (PreTrainedTokenizer): The tokenizer to use when tokenizing the data.
+        source_max_len (int): The maximum length allowed for the source text.
+        target_max_len (int): The maximum length allowed for the target text.
+        train_on_source (bool): If True, the model will be trained on the source text as well as the target text.
+        predict_with_generate (bool): If True, the model will generate predictions instead of training.
     """
+
     def __init__(
         self,
         hf_dataset: datasets.DatasetDict,
@@ -185,9 +183,7 @@ class SupervisedDataset(Dataset):
 
 @dataclass
 class DataCollatorForSupervisedDataset:
-    """
-    Collate and pad examples for supervised training.
-    """
+    """Collate and pad examples for supervised training."""
 
     tokenizer: PreTrainedTokenizer
     predict_with_generate: bool = False
@@ -196,8 +192,7 @@ class DataCollatorForSupervisedDataset:
             self,
             examples: List[Dict[str,
                                 torch.Tensor]]) -> Dict[str, torch.Tensor]:
-        """
-        Collate examples into dictionary for supervised training.
+        """Collate examples into dictionary for supervised training.
 
         Args:
             examples: List of examples, each containing 'input_ids' and 'labels'
diff --git a/chatllms/data/utils/conversation.py b/chatllms/data/utils/conversation.py
index 1ef229a..bcbf4ea 100644
--- a/chatllms/data/utils/conversation.py
+++ b/chatllms/data/utils/conversation.py
@@ -1,6 +1,4 @@
-"""
-Conversation prompt templates.
-"""
+"""Conversation prompt templates."""
 
 import dataclasses
 from enum import Enum, auto
@@ -25,7 +23,8 @@ class SeparatorStyle(Enum):
 
 @dataclasses.dataclass
 class Conversation:
-    """A class that manages prompt templates and keeps all conversation history."""
+    """A class that manages prompt templates and keeps all conversation
+    history."""
 
     # The name of this template
     name: str
@@ -163,8 +162,9 @@ class Conversation:
     def update_last_message(self, message: str):
         """Update the last output.
 
-        The last message is typically set to be None when constructing the prompt,
-        so we need to update it in-place after getting the response from a model.
+        The last message is typically set to be None when constructing the
+        prompt, so we need to update it in-place after getting the response
+        from a model.
         """
         self.messages[-1][1] = message
 
diff --git a/chatllms/data/utils/convert_alpaca.py b/chatllms/data/utils/convert_alpaca.py
index 8af5520..4513072 100644
--- a/chatllms/data/utils/convert_alpaca.py
+++ b/chatllms/data/utils/convert_alpaca.py
@@ -1,5 +1,4 @@
-"""
-Convert alpaca dataset into sharegpt format.
+"""Convert alpaca dataset into sharegpt format.
 
 Usage: python3 -m chatllms.data.convert_alpaca --in alpaca_data.json
 """
diff --git a/chatllms/data/utils/convert_oasst1.py b/chatllms/data/utils/convert_oasst1.py
index a6f06ae..35a538d 100644
--- a/chatllms/data/utils/convert_oasst1.py
+++ b/chatllms/data/utils/convert_oasst1.py
@@ -167,9 +167,9 @@ def test_add_open_assistant(fixup_personality,
                             only_personality,
                             deberta_grading,
                             save_json=True):
-    """
-    Flatten tree structure into one row per path from root to leaf
-    Also turn into human_bot prompting format:
+    """Flatten tree structure into one row per path from root to leaf Also turn
+    into human_bot prompting format:
+
         <human>: question\n<bot>: answer <human>: question2\n<bot>: answer2 Etc.
     Also saves a .json locally as side-effect
     returns list of dicts, containing intput, prompt_type and source
diff --git a/chatllms/data/vicuna_dataset.py b/chatllms/data/vicuna_dataset.py
index 392d6fe..f5fcbf1 100644
--- a/chatllms/data/vicuna_dataset.py
+++ b/chatllms/data/vicuna_dataset.py
@@ -49,8 +49,7 @@ def tokenize_conversations(
     conversations: List[str],
     tokenizer: PreTrainedTokenizer,
 ) -> torch.Tensor:
-    """Tokenize conversations
-    """
+    """Tokenize conversations."""
 
     input_ids = tokenizer(
         conversations,
@@ -70,7 +69,9 @@ def mask_targets(
     tokenizer: PreTrainedTokenizer,
     conv: Conversation,
 ) -> None:
-    """Mask targets. Only compute loss on the assistant outputs.
+    """Mask targets.
+
+    Only compute loss on the assistant outputs.
     """
 
     # Mask targets
@@ -108,8 +109,7 @@ def mask_targets(
 
 def preprocess(sources: Sequence[Dict[str, str]],
                tokenizer: PreTrainedTokenizer) -> Dict[str, List[int]]:
-    """
-    Preprocesses the data by tokenizing it.
+    """Preprocesses the data by tokenizing it.
 
     Args:
         sources (Sequence[Dict[str, str]]): List of conversation sources.
@@ -131,13 +131,13 @@ def preprocess(sources: Sequence[Dict[str, str]],
 
 
 class SupervisedDataset(Dataset):
-    """
-    Dataset for supervised fine-tuning.
+    """Dataset for supervised fine-tuning.
 
     Args:
         raw_data (List[Dict]): Raw input data.
         tokenizer (PreTrainedTokenizer): Tokenizer for preprocessing the data.
     """
+
     def __init__(self, raw_data: List[Dict[str, List[str]]],
                  tokenizer: PreTrainedTokenizer) -> None:
         super().__init__()
@@ -160,8 +160,7 @@ class SupervisedDataset(Dataset):
         return len(self.input_ids)
 
     def __getitem__(self, index: int) -> Dict[str, torch.Tensor]:
-        """
-        Get an example from the dataset at the specified index.
+        """Get an example from the dataset at the specified index.
 
         Args:
             index (int): Index of the example to retrieve.
@@ -177,16 +176,14 @@ class SupervisedDataset(Dataset):
 
 
 class LazySupervisedDataset(Dataset):
-    """
-    Dataset for supervised fine-tuning.
-    """
+    """Dataset for supervised fine-tuning."""
+
     def __init__(
         self,
         raw_data: List[Dict[str, str]],
         tokenizer: PreTrainedTokenizer,
     ):
-        """
-        Initialize the LazySupervisedDataset.
+        """Initialize the LazySupervisedDataset.
 
         Args:
             raw_data (List[Dict[str, str]]): The raw input data for the dataset.
@@ -198,8 +195,7 @@ class LazySupervisedDataset(Dataset):
         self.cached_data_dict: Dict[int, Dict[str, torch.Tensor]] = {}
 
     def __len__(self) -> int:
-        """
-        Get the length of the dataset.
+        """Get the length of the dataset.
 
         Returns:
             int: The length of the dataset.
@@ -207,8 +203,7 @@ class LazySupervisedDataset(Dataset):
         return len(self.raw_data)
 
     def __getitem__(self, i: int) -> Dict[str, torch.Tensor]:
-        """
-        Get an item from the dataset at the given index.
+        """Get an item from the dataset at the given index.
 
         Args:
             i (int): The index of the item to retrieve.
@@ -240,8 +235,7 @@ def make_conversation_data_module(
     lazy_preprocess: bool,
     data_path: str,
 ) -> Dict[str, Dataset]:
-    """
-    Make dataset and collator for supervised fine-tuning.
+    """Make dataset and collator for supervised fine-tuning.
 
     Args:
         tokenizer (PreTrainedTokenizer): The tokenizer object.
@@ -250,7 +244,6 @@ def make_conversation_data_module(
 
     Returns:
         dict: A dictionary containing the train_dataset and eval_dataset.
-
     """
     # Determine the appropriate dataset class based on lazy_preprocess flag
 
diff --git a/chatllms/evaluation/evaluate_zh.py b/chatllms/evaluation/evaluate_zh.py
index f23d611..ca2c26e 100644
--- a/chatllms/evaluation/evaluate_zh.py
+++ b/chatllms/evaluation/evaluate_zh.py
@@ -95,8 +95,7 @@ class CEval(object):
         data_path: str = 'ceval/ceval-exam',
         output_dir: str = 'ceval_output',
     ) -> None:
-        """
-        Initialize the CEval object.
+        """Initialize the CEval object.
 
         Args:
             model (PreTrainedModel): Pre-trained model for question answering.
@@ -112,8 +111,7 @@ class CEval(object):
         self.output_dir = output_dir
 
     def run(self, shot: int, split: str) -> None:
-        """
-        Run the evaluation for all tasks.
+        """Run the evaluation for all tasks.
 
         Args:
             shot (int): Number of additional examples to include in the prompt.
@@ -144,8 +142,7 @@ class CEval(object):
 
     def run_single_task(self, task_name: str, shot: int,
                         split: str) -> Tuple[List[Dict[str, str]], float]:
-        """
-        Run the evaluation for a single task.
+        """Run the evaluation for a single task.
 
         Args:
             task_name (str): Name of the task.
@@ -198,8 +195,7 @@ class CEval(object):
     def build_example(self,
                       data: Dict[str, str],
                       with_answer: bool = True) -> str:
-        """
-        Builds an example string based on the given data.
+        """Builds an example string based on the given data.
 
         Args:
             data (Dict[str, str]): A dictionary containing the question, choices, and answer.
diff --git a/chatllms/model/compute_metrics.py b/chatllms/model/compute_metrics.py
index 6488c39..2b311d0 100644
--- a/chatllms/model/compute_metrics.py
+++ b/chatllms/model/compute_metrics.py
@@ -10,14 +10,14 @@ from transformers import PreTrainedTokenizer
 
 @dataclass
 class ComputeMetrics:
-    """
-    Wraps the tokenizer into metric functions, used in Seq2SeqPeftTrainer.
-    Borrowed from: https://github.com/THUDM/ChatGLM-6B/blob/0c2806fea82683349194e21996dd6b3acc3c265b/ptuning/main.py#L307
+    """Wraps the tokenizer into metric functions, used in Seq2SeqPeftTrainer.
 
+    Borrowed from: https://github.com/THUDM/ChatGLM-6B/blob/0c2806fea82683349194e21996dd6b3acc3c265b/ptuning/main.py#L307
     """
+
     def __init__(self, tokenizer: PreTrainedTokenizer) -> None:
-        """
-        Initialize the ComputeMetrics class with a pre-trained tokenizer object.
+        """Initialize the ComputeMetrics class with a pre-trained tokenizer
+        object.
 
         Args:
             tokenizer (PreTrainedTokenizer): A pre-trained tokenizer object to be used for decoding tokenized sequences.
@@ -27,8 +27,7 @@ class ComputeMetrics:
     def __call__(
         self, eval_preds: List[Union[np.ndarray, Tuple[np.ndarray]]]
     ) -> Dict[str, float]:
-        """
-        Computes evaluation metrics for model predictions.
+        """Computes evaluation metrics for model predictions.
 
         Args:
             eval_preds (List[Union[np.ndarray, Tuple[np.ndarray]]]): List of tuples containing prediction and label arrays.
diff --git a/chatllms/model/llm_perplexity.py b/chatllms/model/llm_perplexity.py
index 2da2fe7..30a1c79 100644
--- a/chatllms/model/llm_perplexity.py
+++ b/chatllms/model/llm_perplexity.py
@@ -18,8 +18,7 @@ from chatllms.utils.model_utils import add_special_tokens_if_missing
 
 
 class LLMPerplexity:
-    """
-    Language model to compute perplexity.
+    """Language model to compute perplexity.
 
     Args:
         cache_dir (str): Directory to cache models.
@@ -31,6 +30,7 @@ class LLMPerplexity:
         fp16 (bool): Whether to use 16-bit precision.
         device (str): Device to load model to.
     """
+
     def __init__(
         self,
         cache_dir: str = None,
@@ -93,8 +93,7 @@ class LLMPerplexity:
     def get_perplexity(self,
                        input_texts: Union[str, List[str]],
                        batch_size: int = None) -> Union[float, List[float]]:
-        """
-        Compute perplexity on input text(s).
+        """Compute perplexity on input text(s).
 
         Args:
             input_texts (Union[str, List[str]]): Input text(s) to compute perplexity for.
diff --git a/chatllms/model/load_pretrain_model.py b/chatllms/model/load_pretrain_model.py
index b917bad..a8e5c38 100644
--- a/chatllms/model/load_pretrain_model.py
+++ b/chatllms/model/load_pretrain_model.py
@@ -27,9 +27,8 @@ def load_model_tokenizer(
     is_trainable: Optional[bool] = True,
     logger=None,
 ) -> Tuple[PreTrainedModel, PreTrainedTokenizer]:
-    """
-    Returns a language model and tokenizer for text generation that can be trained with mixed precision.
-    Support both training and inference.
+    """Returns a language model and tokenizer for text generation that can be
+    trained with mixed precision. Support both training and inference.
 
     Args:
         args: A dictionary containing various hyperparameters.
diff --git a/chatllms/model/mmlueval_callback.py b/chatllms/model/mmlueval_callback.py
index 839b5b1..2e6e9c2 100644
--- a/chatllms/model/mmlueval_callback.py
+++ b/chatllms/model/mmlueval_callback.py
@@ -17,10 +17,9 @@ from chatllms.data.sft_dataset import SupervisedDataset
 
 @dataclass
 class MMLUEvalCallback(TrainerCallback):
-    """
-    A callback function called after each evaluation step during training to evaluate \
-        the performance of a model on an
-    MMLU (Mean Length of Utterance) dataset.
+    """A callback function called after each evaluation step during training to
+    evaluate the performance of a model on an MMLU (Mean Length of Utterance)
+    dataset.
 
     Args:
         trainer (Trainer): The trainer instance to be used.
@@ -28,6 +27,7 @@ class MMLUEvalCallback(TrainerCallback):
         data_dir (str): The directory where the MMLU dataset is stored.
         args (argparse.Namespace): The command line arguments for the current run.
     """
+
     def __init__(
         self,
         trainer: 'Trainer',
@@ -98,8 +98,8 @@ class MMLUEvalCallback(TrainerCallback):
         model: PreTrainedModel,
         **kwargs: Any,
     ) -> None:
-        """
-        Iterate over the batches of the evaluation dataset and make predictions for MMLU.
+        """Iterate over the batches of the evaluation dataset and make
+        predictions for MMLU.
 
         Args:
             args (Dict[str, Any]): Dictionary containing the evaluation arguments.
diff --git a/chatllms/model/sample_generate_callback.py b/chatllms/model/sample_generate_callback.py
index 6c453fa..10a2788 100644
--- a/chatllms/model/sample_generate_callback.py
+++ b/chatllms/model/sample_generate_callback.py
@@ -7,13 +7,14 @@ from transformers import PreTrainedTokenizer, TrainerCallback
 
 @dataclass
 class SampleGenerateCallback(TrainerCallback):
-    """
-    A callback that generates text samples from a pre-trained language model during training.
+    """A callback that generates text samples from a pre-trained language model
+    during training.
 
     Args:
         tokenizer (PreTrainedTokenizer): The tokenizer used to preprocess inputs.
         max_new_tokens (int): The maximum number of tokens to generate in response to each input.
     """
+
     def __init__(self, tokenizer: PreTrainedTokenizer,
                  generation_config: argparse.Namespace, logger: None):
         self.tokenizer = tokenizer
@@ -49,8 +50,7 @@ class SampleGenerateCallback(TrainerCallback):
 
     def on_evaluate(self, args: Any, state: Dict[str, Any], control: Any,
                     **kwargs: Any) -> None:
-        """
-        Generates text samples from the language model during evaluation.
+        """Generates text samples from the language model during evaluation.
 
         Args:
             args (Any): Trainer arguments, not used in this method.
diff --git a/chatllms/model/save_peft_model_callback.py b/chatllms/model/save_peft_model_callback.py
index 2c93e8c..fb37f12 100644
--- a/chatllms/model/save_peft_model_callback.py
+++ b/chatllms/model/save_peft_model_callback.py
@@ -7,16 +7,15 @@ from transformers.trainer_utils import PREFIX_CHECKPOINT_DIR
 
 
 class SavePeftModelCallback(TrainerCallback):
-    """
-    Callback to save PEFT model checkpoints during training.
+    """Callback to save PEFT model checkpoints during training.
 
     Saves both the full model and the adapter model to separate directories
     within the checkpoint directory.
     """
+
     def save_model(self, args: Any, state: TrainingArguments,
                    kwargs: Dict[str, Any]) -> None:
-        """
-        Saves the PEFT model checkpoint.
+        """Saves the PEFT model checkpoint.
 
         Args:
             args (Any): The command line arguments passed to the script.
@@ -52,8 +51,8 @@ class SavePeftModelCallback(TrainerCallback):
     def on_save(self, args: Any, state: TrainingArguments,
                 control: TrainerControl,
                 **kwargs: Dict[str, Any]) -> TrainerControl:
-        """
-        Callback method that calls save_model() and returns `control` argument.
+        """Callback method that calls save_model() and returns `control`
+        argument.
 
         Args:
             args (Any): The command line arguments passed to the script.
@@ -74,8 +73,8 @@ class SavePeftModelCallback(TrainerCallback):
     def on_train_end(self, args: Any, state: TrainingArguments,
                      control: TrainerControl, **kwargs: Dict[str,
                                                              Any]) -> None:
-        """
-        Callback method that saves the model checkpoint and creates a 'completed' file in the output directory.
+        """Callback method that saves the model checkpoint and creates a
+        'completed' file in the output directory.
 
         Args:
             args (Any): The command line arguments passed to the script.
diff --git a/chatllms/train/training.py b/chatllms/train/training.py
index 0a2a2c8..c473969 100644
--- a/chatllms/train/training.py
+++ b/chatllms/train/training.py
@@ -11,8 +11,7 @@ from torch.utils.data import Dataset
 
 def train_and_evaluate(trainer: transformers.Trainer, args: argparse.Namespace,
                        logger: None) -> None:
-    """
-    Trains and evaluates a machine learning model.
+    """Trains and evaluates a machine learning model.
 
     Args:
         trainer (Trainer): The training object to use for training and evaluation.
@@ -75,10 +74,8 @@ def predict_and_save(trainer: transformers.Trainer,
                      tokenizer: transformers.PreTrainedTokenizer,
                      predict_dataset: Dataset, args: argparse.Namespace,
                      logger: None) -> None:
-    """
-    Make predictions on new data, save them to a file along with input examples,
-    and update the overall metrics.
-    """
+    """Make predictions on new data, save them to a file along with input
+    examples, and update the overall metrics."""
     logger.info('=' * 80)
     logger.info('*** Predict ***')
     logger.info('=' * 80)
diff --git a/chatllms/utils/apply_lora.py b/chatllms/utils/apply_lora.py
index b46639e..0291f4e 100644
--- a/chatllms/utils/apply_lora.py
+++ b/chatllms/utils/apply_lora.py
@@ -1,5 +1,4 @@
-"""
-Apply the LoRA weights on top of a base model.
+"""Apply the LoRA weights on top of a base model.
 
 Usage:
 python3 apply_lora.py --base_model_path ~/model_weights/llama-7b --target_model_path ~/model_weights/baize-7b \
@@ -24,7 +23,8 @@ def apply_lora(
     use_auth_token: str = True,
     trust_remote_code: bool = True,
 ) -> Tuple[AutoModelForCausalLM, AutoTokenizer]:
-    """Applies the LoRA adapter to a base model and saves the resulting target model (optional).
+    """Applies the LoRA adapter to a base model and saves the resulting target
+    model (optional).
 
     Args:
         base_model_path (str): The path to the base model to which the LoRA adapter will be applied.
@@ -36,7 +36,6 @@ def apply_lora(
 
     Returns:
         Tuple[AutoModelForCausalLM, AutoTokenizer]: A tuple containing the target model and its tokenizer.
-
     """
     # Load the base model and tokenizer
     print(f'Loading the base model from {base_model_path}')
diff --git a/chatllms/utils/model_utils.py b/chatllms/utils/model_utils.py
index a053f5d..af4b092 100644
--- a/chatllms/utils/model_utils.py
+++ b/chatllms/utils/model_utils.py
@@ -9,19 +9,18 @@ from transformers import PreTrainedModel, PreTrainedTokenizer, Trainer
 from transformers.generation.logits_process import LogitsProcessor
 from transformers.generation.utils import LogitsProcessorList
 from transformers.trainer_utils import get_last_checkpoint
-from transformers.generation.logits_process import LogitsProcessor
-from transformers.generation.utils import LogitsProcessorList
+
 from chatllms.data.data_utils import (DEFAULT_BOS_TOKEN, DEFAULT_EOS_TOKEN,
                                       DEFAULT_PAD_TOKEN, DEFAULT_UNK_TOKEN)
 
 
 def add_special_tokens_if_missing(tokenizer: PreTrainedTokenizer,
                                   model: PreTrainedModel) -> None:
-    """
-    If 'llama' or 'baichuan' is in the model name or path, check if the special tokens are set correctly.
-    Add any missing special tokens to prevent them from being parsed into different tokens.
-    Note that these special tokens are present in the vocabulary.
-    Note also that `model.config.pad_token_id` is 0 which corresponds to `<unk>` token.
+    """If 'llama' or 'baichuan' is in the model name or path, check if the
+    special tokens are set correctly. Add any missing special tokens to prevent
+    them from being parsed into different tokens. Note that these special
+    tokens are present in the vocabulary. Note also that
+    `model.config.pad_token_id` is 0 which corresponds to `<unk>` token.
 
     Args:
         tokenizer: The pre-trained tokenizer.
@@ -54,8 +53,7 @@ def smart_tokenizer_and_embedding_resize(special_tokens_dict: Dict[str, str],
                                          tokenizer: PreTrainedTokenizer,
                                          model: PreTrainedModel) -> None:
     """Resize tokenizer and embedding to accommodate new special tokens.
-    改变tokenizer和embedding的尺寸。
-    一般需要将tokenizer和embedding的尺寸设置为64的倍数，方便GPU加速。
+    改变tokenizer和embedding的尺寸。 一般需要将tokenizer和embedding的尺寸设置为64的倍数，方便GPU加速。
 
     Args:
         special_tokens_dict (Dict[str, str]): A dictionary of special tokens to be added to the tokenizer.
@@ -99,11 +97,9 @@ def smart_tokenizer_and_embedding_resize(special_tokens_dict: Dict[str, str],
 
 def find_all_linear_names(args: argparse.Namespace,
                           model: torch.nn.Module) -> List[str]:
-    """
-    Returns a list of names of all linear layers present in the given model.
+    """Returns a list of names of all linear layers present in the given model.
     如果args.bits是4，使用bitsandbytes库中的bnb.nn.Linear4bit层；
-    如果args.bits是8，使用bitsandbytes库中的bnb.nn.Linear8bitLt层；
-    否则，使用torch.nn.Linear层；
+    如果args.bits是8，使用bitsandbytes库中的bnb.nn.Linear8bitLt层； 否则，使用torch.nn.Linear层；
     并记录下这些层的名称，保存在lora_module_names集合中。
 
     Args:
@@ -154,8 +150,7 @@ def find_all_linear_names(args: argparse.Namespace,
 
 def print_trainable_parameters(args: argparse.Namespace,
                                model: torch.nn.Module) -> None:
-    """
-    Prints the number of trainable parameters in the given model.
+    """Prints the number of trainable parameters in the given model.
 
     Args:
         args (argparse.Namespace): A namespace containing arguments of the script. Must contain the 'bits' argument.
@@ -198,8 +193,7 @@ def print_trainable_parameters(args: argparse.Namespace,
 
 
 def verify_dtypes(model: torch.nn.Module) -> None:
-    """
-    检查模型参数的数据类型，并输出各个数据类型在这些张量中所占的比例.
+    """检查模型参数的数据类型，并输出各个数据类型在这些张量中所占的比例.
 
     :param model: 待检查的模型.
     :return: 无返回值.
@@ -225,9 +219,9 @@ def verify_dtypes(model: torch.nn.Module) -> None:
 
 def check_training_finished(args: argparse.Namespace,
                             logger=None) -> Tuple[str, bool]:
-    """
-    Given a directory containing previous saved checkpoints, returns the path to the last checkpoint
-    if available along with a boolean flag indicating whether training has already been completed.
+    """Given a directory containing previous saved checkpoints, returns the
+    path to the last checkpoint if available along with a boolean flag
+    indicating whether training has already been completed.
 
     Args:
         checkpoint_dir (str): Path to the directory containing the saved checkpoints.
@@ -276,24 +270,10 @@ def find_last_checkpoint(checkpoint_dir):
         last_checkpoint = join(checkpoint_dir, f'checkpoint-{max_step}')
     return last_checkpoint
 
-# Avoid runtime error in model.generate(do_sample=True).
-class InvalidScoreLogitsProcessor(LogitsProcessor):
-    def __call__(self, input_ids: torch.LongTensor,
-                 scores: torch.FloatTensor) -> torch.FloatTensor:
-        if torch.isnan(scores).any() or torch.isinf(scores).any():
-            scores.zero_()
-            scores[..., 0] = 1.0
-        return scores
-
-
-def get_logits_processor() -> LogitsProcessorList:
-    logits_processor = LogitsProcessorList()
-    logits_processor.append(InvalidScoreLogitsProcessor())
-    return logits_processor
-
 
 # Avoid runtime error in model.generate(do_sample=True).
 class InvalidScoreLogitsProcessor(LogitsProcessor):
+
     def __call__(self, input_ids: torch.LongTensor,
                  scores: torch.FloatTensor) -> torch.FloatTensor:
         if torch.isnan(scores).any() or torch.isinf(scores).any():
diff --git a/chatllms/utils/stream_server.py b/chatllms/utils/stream_server.py
index 66bf42f..93288b3 100644
--- a/chatllms/utils/stream_server.py
+++ b/chatllms/utils/stream_server.py
@@ -1,5 +1,5 @@
-"""
-Helpers to support streaming generate output.
+"""Helpers to support streaming generate output.
+
 Borrowed from https://github.com/oobabooga/text-generation-webui/blob/ad37f396fc8bcbab90e11ecf17c56c97bfbd4a9c/modules/callbacks.py
 """
 import traceback
@@ -10,6 +10,7 @@ import transformers
 
 
 class Stream(transformers.StoppingCriteria):
+
     def __init__(self, callback_func=None):
         self.callback_func = callback_func
 
@@ -20,10 +21,9 @@ class Stream(transformers.StoppingCriteria):
 
 
 class Iteratorize:
-    """
-    Transforms a function that takes a callback
-    into a lazy iterator (generator).
-    """
+    """Transforms a function that takes a callback into a lazy iterator
+    (generator)."""
+
     def __init__(self, func, kwargs={}, callback=None):
         self.mfunc = func
         self.c_callback = callback
diff --git a/chatllms/utils/template.py b/chatllms/utils/template.py
index a96b8fa..e865331 100644
--- a/chatllms/utils/template.py
+++ b/chatllms/utils/template.py
@@ -7,8 +7,7 @@ logger = logging.getLogger(__name__)
 
 @dataclass
 class PromptTemplate(object):
-    """
-    A template for formatting a conversation prompt.
+    """A template for formatting a conversation prompt.
 
     Args:
         name: Name of template
@@ -16,7 +15,6 @@ class PromptTemplate(object):
         prompt: Prompt text
         sep: Separator between prompts
         use_history: Whether to use conversation history
-
     """
 
     name: str
@@ -31,8 +29,7 @@ class PromptTemplate(object):
         history: Optional[List[Tuple[str, str]]] = None,
         prefix: Optional[str] = None,
     ) -> str:
-        """
-        Returns a string containing prompt without response.
+        """Returns a string containing prompt without response.
 
         Args:
             query (str): The input query text.
@@ -67,8 +64,7 @@ class PromptTemplate(object):
                        query: str,
                        history: Optional[List[Tuple[str, str]]] = None,
                        prefix: Optional[str] = None) -> List[str]:
-        """
-        Formats the conversation example.
+        """Formats the conversation example.
 
         Args:
             query (str): The input query text.
@@ -100,8 +96,7 @@ class PromptTemplate(object):
         sep: str,
         use_history: Optional[bool] = True,
     ) -> None:
-        """
-        Registers a new conversation template.
+        """Registers a new conversation template.
 
         Args:
             prefix (str): The prefix text for the prompt.
@@ -116,13 +111,9 @@ class PromptTemplate(object):
         self.use_history = use_history
 
     def __post_init__(self):
-        """
-        Initializes the instance of the class.
-        """
+        """Initializes the instance of the class."""
         if self.name == 'default':
-            """
-            Supports language model inference without histories.
-            """
+            """Supports language model inference without histories."""
             self.register_template(name='vanilla',
                                    prefix='',
                                    prompt='<s>{query}</s>',
diff --git a/cli_demo.py b/cli_demo.py
index 959be76..85e34f0 100644
--- a/cli_demo.py
+++ b/cli_demo.py
@@ -22,8 +22,8 @@ def generate_response(
     model: PreTrainedModel,
     generation_args: dict,
 ) -> List[str]:
-    """
-    Generates a response to the given query using GPT-3.5 model and prints it to the console.
+    """Generates a response to the given query using GPT-3.5 model and prints
+    it to the console.
 
     Args:
         query (str): The input query for which a response is to be generated.
diff --git a/data/README.md b/data/README.md
index 5612380..eff7c4f 100644
--- a/data/README.md
+++ b/data/README.md
@@ -1,4 +1,3 @@
-
 # How to use the data
 
 ## Datasets Supported by the Framework
@@ -44,7 +43,6 @@ We provide the following datasets for the experiments in this framework.
   数据集说明：开源了数据规模为145k的价值对齐数据集，该数据集对于每个prompt包括了拒绝&正向建议,(safe and reponsibility) > 拒绝为主(safe) > 风险回复(unsafe)三种类型，可用于增强SFT模型的安全性或用于训练reward模型。
 - [CValues-Comparison中文大模型价值观比较数据集](https://modelscope.cn/datasets/damo/CValues-Comparison/summary)
 
-
 ## Dataset formation
 
 The `dataset_info.yaml` file contains all the datasets can be used in the experiments. The following is the format of the datasets, main including the following fields.
diff --git a/data/alpaca_zh_pcyn.yaml b/data/alpaca_zh_pcyn.yaml
deleted file mode 100644
index 84b6a01..0000000
--- a/data/alpaca_zh_pcyn.yaml
+++ /dev/null
@@ -1,42 +0,0 @@
-# The dataset_info.yaml file contains the information of the datasets used in the experiments.
-coig:
-  hf_hub_url: BAAI/COIG
-  local_path: /userhome/jianzhnie/prompt_data/COIG/train_alpaca.json
-  dataset_format: alpaca
-  multi_turn: False
-
-cvalues_comparison_train:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/CValues-Comparison/train_alpaca.json
-  dataset_format: alpaca
-  multi_turn: False
-
-cvalues_comparison_test:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/CValues-Comparison/test_alpaca.json
-  dataset_format: alpaca
-  multi_turn: False
-
-olcc:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/olcc/olcc_alpaca.json
-  dataset_format: alpaca
-  multi_turn: False
-
-100PoisonMpts:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/100PoisonMpts/train_alpaca.json
-  dataset_format: alpaca
-  multi_turn: False
-
-safety_prompt_part1:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/Safety-Prompts/attack_scenarios_alpaca.json
-  dataset_format: alpaca
-  multi_turn: False
-
-safety_prompt_part2:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/Safety-Prompts/safety_scenarios_alpaca.json
-  dataset_format: alpaca
-  multi_turn: False
diff --git a/data/dataset_info.py b/data/dataset_info.py
index 7f38e6c..62c96f5 100644
--- a/data/dataset_info.py
+++ b/data/dataset_info.py
@@ -2,9 +2,9 @@ from os.path import join
 
 
 def get_dataset_info(dataset_dir):
-    """
-    Returns the datasets info to a dataset based on a pre-defined map of dataset names to their corresponding URLs on the internet
-    or local file paths.
+    """Returns the datasets info to a dataset based on a pre-defined map of
+    dataset names to their corresponding URLs on the internet or local file
+    paths.
 
     Args:
         dataset_dir (str): The local directory where the dataset is stored; this is used for datasets that are stored locally.
diff --git a/data/vicuna_zh_pcyn.yaml b/data/vicuna_zh_pcyn.yaml
deleted file mode 100644
index 610d8e1..0000000
--- a/data/vicuna_zh_pcyn.yaml
+++ /dev/null
@@ -1,42 +0,0 @@
-# The dataset_info.yaml file contains the information of the datasets used in the experiments.
-coig:
-  hf_hub_url: BAAI/COIG
-  local_path: /userhome/jianzhnie/prompt_data/COIG/train_vicuna.json
-  dataset_format: sharegpt
-  multi_turn: True
-
-cvalues_comparison_train:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/CValues-Comparison/train_vicuna.json
-  dataset_format: sharegpt
-  multi_turn: True
-
-cvalues_comparison_test:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/CValues-Comparison/test_vicuna.json
-  dataset_format: sharegpt
-  multi_turn: True
-
-olcc:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/olcc/olcc_vicuna.json
-  dataset_format: sharegpt
-  multi_turn: True
-
-100PoisonMpts:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/100PoisonMpts/train_vicuna.json
-  dataset_format: sharegpt
-  multi_turn: True
-
-safety_prompt_part1:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/Safety-Prompts/attack_scenarios_vicuna.json
-  dataset_format: sharegpt
-  multi_turn: True
-
-safety_prompt_part2:
-  hf_hub_url: ''
-  local_path: /userhome/jianzhnie/prompt_data/Safety-Prompts/safety_scenarios_vicuna.json
-  dataset_format: sharegpt
-  multi_turn: True
diff --git a/examples/clean_sharegpt/clean_sharegpt.py b/examples/clean_sharegpt/clean_sharegpt.py
index 017fecb..ed4fab7 100644
--- a/examples/clean_sharegpt/clean_sharegpt.py
+++ b/examples/clean_sharegpt/clean_sharegpt.py
@@ -99,8 +99,8 @@ def format_roles(
 def filter_invalid_roles(
         raw_data: List[Dict[str,
                             any]]) -> List[Dict[str, List[Dict[str, any]]]]:
-    """
-    Filter out invalid contents based on the roles assigned to each conversation.
+    """Filter out invalid contents based on the roles assigned to each
+    conversation.
 
     Args:
         raw_data: A list of dictionaries containing conversation data.
diff --git a/examples/clean_sharegpt/hardcoded_questions.py b/examples/clean_sharegpt/hardcoded_questions.py
index cb89c63..abafaf2 100644
--- a/examples/clean_sharegpt/hardcoded_questions.py
+++ b/examples/clean_sharegpt/hardcoded_questions.py
@@ -2,9 +2,8 @@ import json
 
 
 def identity_questions():
-    """ "
-    Adopted from https://github.com/young-geng/koala_data_pipeline/blob/main/process_hard_coded_data.py
-    """
+    """" Adopted from https://github.com/young-
+    geng/koala_data_pipeline/blob/main/process_hard_coded_data.py."""
     content = []
 
     name = 'Vicuna'
diff --git a/examples/clean_sharegpt/merge.py b/examples/clean_sharegpt/merge.py
index bdf2b40..727b9a8 100644
--- a/examples/clean_sharegpt/merge.py
+++ b/examples/clean_sharegpt/merge.py
@@ -1,5 +1,4 @@
-"""
-Merge two conversation files into one
+"""Merge two conversation files into one.
 
 Usage: python3 -m fastchat.data.merge --in file1.json file2.json --out merged.json
 """
diff --git a/examples/clean_sharegpt/split_long_conversation.py b/examples/clean_sharegpt/split_long_conversation.py
index e14b952..1e551c6 100644
--- a/examples/clean_sharegpt/split_long_conversation.py
+++ b/examples/clean_sharegpt/split_long_conversation.py
@@ -1,5 +1,4 @@
-"""
-Split long conversations based on certain max length.
+"""Split long conversations based on certain max length.
 
 Usage: python3 -m split_long_conversation.py \
     --in sharegpt_clean.json \
@@ -23,8 +22,8 @@ from tqdm import tqdm
 
 def make_sample(sample: Dict[str, any], start_idx: int,
                 end_idx: int) -> Dict[str, any]:
-    """
-    Create a new sample dictionary by selecting conversations from the given sample.
+    """Create a new sample dictionary by selecting conversations from the given
+    sample.
 
     Args:
         sample (Dict[str, any]): The original sample dictionary.
@@ -43,8 +42,8 @@ def make_sample(sample: Dict[str, any], start_idx: int,
 
 
 def split_one_sample(sample: Dict[str, any]) -> List[Dict[str, any]]:
-    """
-    Split a single sample into multiple samples based on conversation lengths.
+    """Split a single sample into multiple samples based on conversation
+    lengths.
 
     Args:
         sample (Dict[str, any]): The original sample dictionary.
@@ -94,8 +93,8 @@ def worker(input_data: List[Dict[str, Any]]):
 def split_all(raw_data: List[Dict[str, Any]],
               tokenizer_: transformers.PreTrainedTokenizer,
               max_length_: int) -> List[Dict[str, Any]]:
-    """
-    Split the content into smaller parts based on the max token length constraint.
+    """Split the content into smaller parts based on the max token length
+    constraint.
 
     Args:
         raw_data (List[Dict[str, Any]]): The list of samples to split.
diff --git a/examples/finetune_llm/baichuan7b_demo.py b/examples/finetune_llm/baichuan7b_demo.py
index 73169e0..cfdca1b 100644
--- a/examples/finetune_llm/baichuan7b_demo.py
+++ b/examples/finetune_llm/baichuan7b_demo.py
@@ -19,5 +19,5 @@ def main(load_in_8bit=True, model_path=''):
 
 if __name__ == '__main__':
     load_in_8bit = True
-    model_path = '/home/robin/work_dir/llm/llm_pretrain_model/baichuan'
+    model_path = 'baichuan'
     main(load_in_8bit, model_path)
diff --git a/examples/finetune_llm/finetune_llama_with_qlora.py b/examples/finetune_llm/finetune_llama_with_qlora.py
index d9dd3f2..a7bc1ee 100644
--- a/examples/finetune_llm/finetune_llama_with_qlora.py
+++ b/examples/finetune_llm/finetune_llama_with_qlora.py
@@ -15,9 +15,7 @@ DEFAULT_UNK_TOKEN = '<unk>'
 
 
 def print_trainable_parameters(model: AutoModelForCausalLM) -> None:
-    """
-    Prints the number of trainable parameters in the model.
-    """
+    """Prints the number of trainable parameters in the model."""
     trainable_params, all_param = 0, 0
     for _, param in model.named_parameters():
         all_param += param.numel()
diff --git a/examples/finetune_llm/qlora_int4_finetune.py b/examples/finetune_llm/qlora_int4_finetune.py
index 123029c..3e7d46a 100644
--- a/examples/finetune_llm/qlora_int4_finetune.py
+++ b/examples/finetune_llm/qlora_int4_finetune.py
@@ -284,6 +284,7 @@ def find_all_linear_names(args, model):
 
 
 class SavePeftModelCallback(transformers.TrainerCallback):
+
     def save_model(self, args, state, kwargs):
         logger.info('Saving PEFT checkpoint...')
         if state.best_model_checkpoint is not None:
@@ -307,6 +308,7 @@ class SavePeftModelCallback(transformers.TrainerCallback):
         return control
 
     def on_train_end(self, args, state, control, **kwargs):
+
         def touch(fname, times=None):
             with open(fname, 'a'):
                 os.utime(fname, times)
@@ -408,9 +410,7 @@ def get_accelerate_model(args, checkpoint_dir):
 
 
 def print_trainable_parameters(args, model):
-    """
-    Prints the number of trainable parameters in the model.
-    """
+    """Prints the number of trainable parameters in the model."""
     trainable_params = 0
     all_param = 0
     for _, param in model.named_parameters():
@@ -576,9 +576,8 @@ def local_dataset(dataset_name):
 
 def make_data_module(tokenizer: transformers.PreTrainedTokenizer,
                      args) -> Dict:
-    """
-    Make dataset and collator for supervised fine-tuning.
-    Datasets are expected to have the following columns: { `input`, `output` }
+    """Make dataset and collator for supervised fine-tuning. Datasets are
+    expected to have the following columns: { `input`, `output` }
 
     Available datasets to be selected with `dataset` argument:
         - alpaca, 52002 examples
@@ -597,8 +596,8 @@ def make_data_module(tokenizer: transformers.PreTrainedTokenizer,
         - supernatural-instructions, 69624 examples (same as paper with 100 ex/task more can be used)
         - flan (FLAN v2), up to 20M examples available
         - vicuna
-
     """
+
     def load_data(dataset_name):
         if dataset_name == 'alpaca':
             return load_dataset('tatsu-lab/alpaca')
@@ -832,6 +831,7 @@ def train():
         accuracy = evaluate.load('accuracy')
 
         class MMLUEvalCallback(transformers.TrainerCallback):
+
             def on_evaluate(self, args, state, control, model, **kwargs):
                 data_loader = trainer.get_eval_dataloader(mmlu_dataset)
                 source_max_len = trainer.data_collator.source_max_len
diff --git a/examples/format_data/convert_oasst1.py b/examples/format_data/convert_oasst1.py
index 31a29e8..ac965dc 100644
--- a/examples/format_data/convert_oasst1.py
+++ b/examples/format_data/convert_oasst1.py
@@ -16,12 +16,14 @@ def json_load(in_file):
 
 
 def convert_oasst1_data(data_dir, output_dir):
-    '''
-    For OASST1, because it's in a tree structure, where every user input might get multiple replies,
-    we have to save every path from the root node to the assistant reply (including both leaf node and intemediate node).
-    This results in some of the messages being duplicated among different paths (instances).
-    Be careful when using this dataset for training. Ideally, you should only minimize the loss of the last message in each path.
-    '''
+    """For OASST1, because it's in a tree structure, where every user input
+    might get multiple replies, we have to save every path from the root node
+    to the assistant reply (including both leaf node and intemediate node).
+
+    This results in some of the messages being duplicated among different paths
+    (instances). Be careful when using this dataset for training. Ideally, you
+    should only minimize the loss of the last message in each path.
+    """
     conversations = []
     with open(os.path.join(data_dir, '2023-04-12_oasst_ready.trees.jsonl'),
               'r') as fin:
diff --git a/examples/format_data/merge.py b/examples/format_data/merge.py
index 8da9846..84324e7 100644
--- a/examples/format_data/merge.py
+++ b/examples/format_data/merge.py
@@ -1,5 +1,4 @@
-"""
-Merge two conversation files into one
+"""Merge two conversation files into one.
 
 Usage: python3 -m fastchat.data.merge --in file1.json file2.json --out merged.json
 """
diff --git a/examples/vllm/apil_chient.py b/examples/vllm/apil_chient.py
deleted file mode 100644
index d3ba848..0000000
--- a/examples/vllm/apil_chient.py
+++ /dev/null
@@ -1,77 +0,0 @@
-"""Example Python client for vllm.entrypoints.api_server"""
-
-import argparse
-import json
-from typing import Iterable, List
-
-import requests
-
-
-def clear_line(n: int = 1) -> None:
-    LINE_UP = '\033[1A'
-    LINE_CLEAR = '\x1b[2K'
-    for _ in range(n):
-        print(LINE_UP, end=LINE_CLEAR, flush=True)
-
-
-def post_http_request(prompt: str,
-                      api_url: str,
-                      n: int = 1,
-                      stream: bool = False) -> requests.Response:
-    headers = {'User-Agent': 'Test Client'}
-    pload = {
-        'prompt': prompt,
-        'n': n,
-        'use_beam_search': True,
-        'temperature': 0.0,
-        'max_tokens': 16,
-        'stream': stream,
-    }
-    response = requests.post(api_url, headers=headers, json=pload, stream=True)
-    return response
-
-
-def get_streaming_response(response: requests.Response) -> Iterable[List[str]]:
-    for chunk in response.iter_lines(chunk_size=8192,
-                                     decode_unicode=False,
-                                     delimiter=b'\0'):
-        if chunk:
-            data = json.loads(chunk.decode('utf-8'))
-            output = data['text']
-            yield output
-
-
-def get_response(response: requests.Response) -> List[str]:
-    data = json.loads(response.content)
-    output = data['text']
-    return output
-
-
-if __name__ == '__main__':
-    parser = argparse.ArgumentParser()
-    parser.add_argument('--host', type=str, default='localhost')
-    parser.add_argument('--port', type=int, default=8000)
-    parser.add_argument('--n', type=int, default=4)
-    parser.add_argument('--prompt', type=str, default='San Francisco is a')
-    parser.add_argument('--stream', action='store_true')
-    args = parser.parse_args()
-    prompt = args.prompt
-    api_url = f'http://{args.host}:{args.port}/generate'
-    n = args.n
-    stream = args.stream
-
-    print(f'Prompt: {prompt!r}\n', flush=True)
-    response = post_http_request(prompt, api_url, n, stream)
-
-    if stream:
-        num_printed_lines = 0
-        for h in get_streaming_response(response):
-            clear_line(num_printed_lines)
-            num_printed_lines = 0
-            for i, line in enumerate(h):
-                num_printed_lines += 1
-                print(f'Beam candidate {i}: {line!r}', flush=True)
-    else:
-        output = get_response(response)
-        for i, line in enumerate(output):
-            print(f'Beam candidate {i}: {line!r}', flush=True)
diff --git a/examples/vllm/vllm_demo.py b/examples/vllm/vllm_demo.py
deleted file mode 100644
index f23be9b..0000000
--- a/examples/vllm/vllm_demo.py
+++ /dev/null
@@ -1,19 +0,0 @@
-from vllm import LLM, SamplingParams
-
-prompts = [
-    'Hello, my name is',
-    'The president of the United States is',
-    'The capital of France is',
-    'The future of AI is',
-]
-sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
-
-llm = LLM(model='decapoda-research/llama-7b-hf', gpu_memory_utilization=0.9)
-
-# Print the outputs.
-for i in range(10):
-    outputs = llm.generate(prompts, sampling_params)
-    for output in outputs:
-        prompt = output.prompt
-        generated_text = output.outputs[0].text
-        print(f'Prompt: {prompt!r}, Generated text: {generated_text!r}')
diff --git a/scripts/server/apply_lora_to_base_model.sh b/scripts/server/apply_lora_to_base_model.sh
index d4a21f5..040f901 100644
--- a/scripts/server/apply_lora_to_base_model.sh
+++ b/scripts/server/apply_lora_to_base_model.sh
@@ -1,4 +1,4 @@
 CUDA_VISIBLE_DEVICES=0 python chatllms/utils/apply_lora.py \
         --base-model-path ~/checkpoints/baichuan7b/ \
         --lora-model-path ./work_dir/vicuna_merge_vicuna-baichuan-7b-1gpu/checkpoint-15000 \
-        --target-model-path ./work_dir/vicuna_merge_vicuna-baichuan-7b-1gpu/merged_model
\ No newline at end of file
+        --target-model-path ./work_dir/vicuna_merge_vicuna-baichuan-7b-1gpu/merged_model
diff --git a/scripts/server/run_inference.sh b/scripts/server/run_inference.sh
index e316b23..ff65545 100755
--- a/scripts/server/run_inference.sh
+++ b/scripts/server/run_inference.sh
@@ -1,3 +1,3 @@
 # generated_chat_vicuna
 CUDA_VISIBLE_DEVICES=0 python single_chat.py \
-    --model_name_or_path ./work_dir/vicuna_merge_vicuna-baichuan-7b-1gpu/merged_model
\ No newline at end of file
+    --model_name_or_path ./work_dir/vicuna_merge_vicuna-baichuan-7b-1gpu/merged_model
diff --git a/server/gradio_qlora_webserver.py b/server/gradio_qlora_webserver.py
index 3493495..9e6eb16 100644
--- a/server/gradio_qlora_webserver.py
+++ b/server/gradio_qlora_webserver.py
@@ -32,12 +32,11 @@ logger = logging.getLogger(__name__)
 
 
 class Prompter:
-    """
-    A class for generating prompts and extracting responses from generated text.
-    """
+    """A class for generating prompts and extracting responses from generated
+    text."""
+
     def __init__(self, prompt_template: str = None):
-        """
-        Initializes a new instance of the Prompter class.
+        """Initializes a new instance of the Prompter class.
 
         Args:
             prompt_template (str): The name of the prompt template to use. Default is None.
@@ -50,8 +49,7 @@ class Prompter:
                         instruction: str,
                         input: Union[str, None] = None,
                         response: Union[str, None] = None) -> str:
-        """
-        Generates a prompt based on the specified inputs.
+        """Generates a prompt based on the specified inputs.
 
         Args:
             instruction (str): The instruction to include in the prompt.
@@ -76,8 +74,7 @@ class Prompter:
         return prompt_text
 
     def get_response(self, output: str) -> str:
-        """
-        Extracts the response from the generated text.
+        """Extracts the response from the generated text.
 
         Args:
             output (str): The generated text to extract the response from.
diff --git a/server/gradio_webserver.py b/server/gradio_webserver.py
index 795ba54..0592fcd 100644
--- a/server/gradio_webserver.py
+++ b/server/gradio_webserver.py
@@ -11,6 +11,7 @@ from chatllms.utils.stream_server import Iteratorize, Stream
 
 
 class Prompter(object):
+
     def __init__(self) -> None:
         self.PROMPT_DICT = {
             'prompt_input':
diff --git a/server/multi_chat.py b/server/multi_chat.py
index f368aaa..18b927e 100644
--- a/server/multi_chat.py
+++ b/server/multi_chat.py
@@ -12,9 +12,7 @@ from chatllms.utils.model_utils import get_logits_processor
 
 
 def main(model_server_args, generation_args):
-    """
-    多轮对话，不具有对话历史的记忆功能
-    """
+    """多轮对话，不具有对话历史的记忆功能."""
     device = 'cuda' if torch.cuda.is_available() else 'cpu'
     model = AutoModelForCausalLM.from_pretrained(
         model_server_args.model_name_or_path,
diff --git a/server/single_chat.py b/server/single_chat.py
index a85c270..ef679a4 100644
--- a/server/single_chat.py
+++ b/server/single_chat.py
@@ -17,8 +17,8 @@ from chatllms.utils.model_utils import get_logits_processor
 def generate_response(query: str, tokenizer: PreTrainedTokenizer,
                       model: PreTrainedModel,
                       generation_args: dict) -> List[str]:
-    """
-    Generates a response to the given query using GPT-3.5 model and prints it to the console.
+    """Generates a response to the given query using GPT-3.5 model and prints
+    it to the console.
 
     Args:
         query (str): The input query for which a response is to be generated.
@@ -63,9 +63,7 @@ def generate_response(query: str, tokenizer: PreTrainedTokenizer,
 
 
 def main():
-    """
-    单轮对话，不具有对话历史的记忆功能
-    Run conversational agent loop with input/output.
+    """单轮对话，不具有对话历史的记忆功能 Run conversational agent loop with input/output.
 
     Args:
         model_args: Arguments for loading model
diff --git a/train.py b/train.py
index 3606ef4..8519c83 100644
--- a/train.py
+++ b/train.py
@@ -15,8 +15,8 @@ from chatllms.utils.model_utils import (add_special_tokens_if_missing,
 
 
 def load_model_tokenizer(args) -> Tuple[PreTrainedModel, PreTrainedTokenizer]:
-    """
-    Load a pre-trained model and tokenizer for natural language processing tasks.
+    """Load a pre-trained model and tokenizer for natural language processing
+    tasks.
 
     Args:
         args: An object containing the input arguments.
@@ -66,8 +66,7 @@ def load_model_tokenizer(args) -> Tuple[PreTrainedModel, PreTrainedTokenizer]:
 
 
 def train() -> None:
-    """
-    Trains a language model using Hugging Face's Transformers library.
+    """Trains a language model using Hugging Face's Transformers library.
 
     Args:
         model_args (ModelArguments): The arguments for the model configuration.
@@ -76,7 +75,6 @@ def train() -> None:
 
     Returns:
         None
-
     """
     parser = HfArgumentParser(
         (ModelArguments, DataArguments, TrainingArguments))
diff --git a/train_lora.py b/train_lora.py
index e497cfc..81560e7 100644
--- a/train_lora.py
+++ b/train_lora.py
@@ -32,9 +32,9 @@ class LoraArguments:
 
 
 def maybe_zero_3(param: Union[torch.Tensor, object]) -> torch.Tensor:
-    """
-    Applies zero.GatheredParameters to gather the parameter if it has ds_id attribute,
-    and clones and detaches the tensor data if ds_status is ZeroParamStatus.NOT_AVAILABLE.
+    """Applies zero.GatheredParameters to gather the parameter if it has ds_id
+    attribute, and clones and detaches the tensor data if ds_status is
+    ZeroParamStatus.NOT_AVAILABLE.
 
     Args:
         param: The parameter to be processed.
@@ -58,8 +58,7 @@ def maybe_zero_3(param: Union[torch.Tensor, object]) -> torch.Tensor:
 # Borrowed from peft.utils.get_peft_model_state_dict
 def get_peft_state_maybe_zero_3(named_params: List[Tuple[str, torch.Tensor]],
                                 bias: str) -> Dict[str, torch.Tensor]:
-    """
-    Filters and processes named parameters based on the specified bias.
+    """Filters and processes named parameters based on the specified bias.
 
     Args:
         named_params: An iterable containing tuples of parameter names and their corresponding values.
@@ -107,8 +106,8 @@ def get_peft_state_maybe_zero_3(named_params: List[Tuple[str, torch.Tensor]],
 def load_model_tokenizer(
         args: argparse.Namespace
 ) -> Tuple[PreTrainedModel, PreTrainedTokenizer]:
-    """
-    Load a pre-trained model and tokenizer for natural language processing tasks.
+    """Load a pre-trained model and tokenizer for natural language processing
+    tasks.
 
     Args:
         args: An object containing the input arguments.
