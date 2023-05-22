# Barrier Free Kiosk Configure
This is part of [Barrier Free Kiosk](https://github.com/devhoodit/barrier-free-kiosk-app)  

# How to use
```powershell
git clone https://github.com/devhoodit/barrier-free-kiosk-configure.git
cd barrier-free-kiosk-configure
pip install -r requirements.txt
python rank.py your_json_file_path output_json_file_path
```
*Maybe you need jvm to run konlpy (nlp library)  

# What is this?
This is part of [Barrier Free Kiosk](https://github.com/devhoodit/barrier-free-kiosk-app) project  
For recommandation system, this project use nlp to rank similarity (cosine similarity with TF-IDF)  
After processing, output.json will hold metadata of ranking (editable!)  

# Additional Setting
Edit default_stop_words in this [file](./config_parser.py)  
If you configure coffee menu kiosk, add "coffee" keyword to avoid misleading recommandation output  
