'''
Automatisierung für Testläufe des Anwendungsfalls: Inbetriebnahme
Von:Marcel Bankert
Am: 16.11.2024
'''

import re
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
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)


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
    res = ""

    #Iteration durch die LLM
    for i in data["LLM"][0]["Inbetriebnahme"]:
        #Dateipfad für die Speicherung der Ergebnisse anlegen, sofern noch nicht vorhanden
         "" if os.path.exists("../Results/Inbetriebnahme/" + i["name"]) else subprocess.run(["mkdir", "../Results/Inbetriebnahme/" + i["name"]])
         if i["GGUF"]:

             try:
                # Instantiiere Model
                 llm = Llama(
                 model_path=i["file"],
                 n_ctx=4096,  # Genutzte Kontextlänge
                 n_gpu_layers=-1,# Anzahl der Modellayer die auf die GPU ausgelagert werden sollen --> -1 bedeutet, dass alles auf die GPU ausgelagert wird
                 verbose=True,
                 logits_all=True
                 )
                 
                 #Iteration durch die zu klassifizierenden Logs
                 for j in range(1,101):
                     
                    #Öffnen des relevanten Pfads für die Infos zu der Eingabesquenz
                    with open('../JSON_Files/Use_Case.json', 'r') as file:
                                    use_cases = json.load(file)
                    
                    #Lesen des jeweiligen Logs den es zu klassifizieren gilt
                    with open(use_cases["Use_Cases"][4][f"path_to_logs"] + "/Log" + str(j) + ".txt", 'r') as file:
                        current_log_file = file.read()
                                
                    #Preprocessing
                    current_log_file = current_log_file.replace("\"","")
                    current_log_file = current_log_file.replace("@", "")
                    current_log_file = current_log_file.replace('\n', ' ').replace('\r', '')
                    current_log_file = ' '.join(current_log_file.split())
                    current_log_file = re.sub(r'^https?:\/\/.*[\r\n]*', '', current_log_file, flags=re.MULTILINE)
                    
                    task:str = "This is a log: " + current_log_file + " " + use_cases["Use_Cases"][4]["task_text"]
                   
                     #kwargs für die Generierung
                    generation_kwargs = {
                     "max_tokens":4096,
                     "stop":["</s>"],
                     "echo":False,
                    "top_k":1 #"Greedy decoding"
                    }
                    
                    #Inferenz
                    res = llm(task, **generation_kwargs)
                    
                    #Speichern des Ergebnisses für den betrachteten Log
                    file_path = Path("../Results/Inbetriebnahme/" + i["name"] +"/" + f"Log{str(j)}" + ".txt")
                    with file_path.open('w') as file:
                        file.write(str(res["choices"][0]["text"]))

             except Exception as e:
               print(f"exception {e}")
               exit()
         else:
             pass
             #Keine '.bin' und '.safetensor' Modelle für diesen Anwendungsfall selektiert.
              
if __name__ == '__main__':
    
    start()