'''
Automatisierung für Testläufe des Anwendungsfalls: Anforderungsanalyse
Von:Marcel Bankert
Am: 16.11.2024
'''

from huggingface_hub import login
from dataclasses import dataclass, field
from typing import Optional
import os
from llama_cpp import Llama

import peft
import torch
from peft import PeftConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel
from transformers import pipeline
from huggingface_hub import hf_hub_download
import json
import subprocess
from pathlib import Path

#Definition der globalen Variable in dem die Modelle mit den Dateiendungen ".bin" und ".safetensors" gesichert werden.
os.environ['HF_HOME'] = './model_cache'

# Eigens generierter API key aus dem Huggingface Account
login(token="API key")


def start():
    #Lesen der JSON Datei in der die Informationen zu den relevanten LLMs zu finden sind.
    with open('../JSON_Files/LLM.json', 'r') as file:
        data = json.load(file)
    #Für die Nutzung auf die GPU relevant
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    #Liste der relevanten Projekte
    projects = ["actor_relationship_game", "hone", "hybrid_images", "login_registration", "readtime"]
    res = ""

  #Iteration durch die LLM
    for i in data["LLM"][0]["Anforderungsanalyse"]:

        #Dateipfad für die Speicherung der Ergebnisse anlegen, sofern noch nicht vorhanden
         "" if os.path.exists("../Results/Anforderungsanalyse/" + i["name"]) else subprocess.run(["mkdir", "../Results/Anforderungsanalyse/" + i["name"]])
         
         if i["GGUF"]:

             try:
                 llm = None
                 # Instantiiere Model
                 llm = Llama(
                 model_path=i["file"],
                 n_gpu_layers=-1,# Anzahl der Modellayer die auf die GPU ausgelagert werden sollen --> -1 bedeutet, dass alles auf die GPU ausgelagert wird
                 n_ctx=4096,# Genutzte Kontextlänge 
                 verbose=True,
                 logits_all=True
                 )

                 #kwargs für die Generierung
                 generation_kwargs = {
                     "max_tokens":4096,
                     "stop":["</s>"],
                     "echo":False,
                     "top_k":1 #"Greedy decoding"
                 }
                 
                 #Iteration durch die Projekte
                 for project in projects:
                     #Öffnen der Usecase JSON-Datei welche alle Infos zu den Aufgabenstellungen enthält.
                        with open('../JSON_Files/Use_Case.json', 'r') as file:
                                    use_cases = json.load(file)

                        task:str = use_cases["Use_Cases"][0]["task_text_" + project] + " " + use_cases["Use_Cases"][0]["input_" + project]

                        ## Inferenz
                        res = llm(task, **generation_kwargs)
                        #Speichern der Antwort in seperater Datei
                        file_path = Path("../Results/Anforderungsanalyse/" + i["name"]+"/" + i["name"] + "_" + project + ".txt")
                        with file_path.open('w') as file:
                            file.write(str(res["choices"][0]["text"]))
             except Exception as e:
               print(f"exception {e}")
               exit()

        


            

         else:
             tokenizer:any = ""
             model:any = ""

             #Sofern dieses Modell einen Adapter benötigt
             if i["adapter"]:
                 tokenizer = AutoTokenizer.from_pretrained(str(i["model"]))
                 model = AutoModelForCausalLM.from_pretrained(i["model"], load_in_4bit=False)

                 inputs = tokenizer(task, return_tensors="pt").to("cuda")
                 generated_ids = model.generate(
                     **inputs, max_new_tokens=2048)

                 model.load_adapter(i["adapter_link"])

                #Inferenz
                 res = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)



                 #Speichern der Antwort
                 with file_path.open('w') as file:
                     file.write(str(res))
             else:
                 #Tokenizer und Model Auswählen
                 tokenizer = AutoTokenizer.from_pretrained(str(i["model"]))
                 model = AutoModel.from_pretrained(i["model"], load_in_4bit=False)

             with open('../JSON_Files/Use_Case.json', 'r') as file:
                 use_cases = json.load(file)

                 messages = [
                 {"role": "user", "content": task},]
                 pipe = pipeline("text-generation", model=i["model"], device=device, max_new_tokens=2048) if not i["adapter"] else pipeline("text-generation", model=i["model"], max_new_tokens=2048)

                #Inferenz
                 res = pipe(messages)

                 #Datei speichern
                 with file_path.open('w') as file:
                     # Write content to the file
                     file.write(str(res[0]["generated_text"][1]))
    
    
if __name__ == '__main__':
    
    start()