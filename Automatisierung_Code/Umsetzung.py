'''
Automatisierung für Testläufe des Anwendungsfalls: Umsetzung
Von:Marcel Bankert
Am: 16.11.2024
'''
import re
from huggingface_hub import login
from dataclasses import dataclass, field
from typing import Optional
import os
from llama_cpp import Llama
import time

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
    
    #Liste der relevanten Projekte
    projects = ["actor_relationship_game", "hone", "hybrid_images", "login_registration", "readtime"]
    res = ""
    
    #Iteration durch die LLM
    for i in data["LLM"][0]["Umsetzung"]:
        #Dateipfad für die Speicherung der Ergebnisse anlegen, sofern noch nicht vorhanden
        "" if os.path.exists("../Results/Umsetzung/" + i["name"]) else subprocess.run(["mkdir", "../Results/Umsetzung/" + i["name"]])

        try:
           
            #Instantiiere Model
            llm = Llama(
            model_path=i["file"],
            n_ctx=16384,  # Genutzte Kontextlänge 
            n_gpu_layers=-1,# Anzahl der Modellayer die auf die GPU ausgelagert werden sollen --> -1 bedeutet, dass alles auf die GPU ausgelagert wird
            verbose=True,
            logits_all=True
            )
            
            #Iteration durch die Projekte
            for project in projects:
               project_implementation_time = 0
                
             #Dateipfad für die Speicherung der Ergebnisse anlegen, sofern noch nicht vorhanden
               "" if os.path.exists("../Results/Umsetzung/" + i["name"] + "/" + project) else subprocess.run(["mkdir", "../Results/Umsetzung/" + i["name"] + "/" + project])
               
               #Lesen der Usecase JSON-Datei für die Eingabesequenz und weitere Informationen
               with open('../JSON_Files/Use_Case.json', 'r') as file:
                               use_cases = json.load(file)

                #Iteration durch die zu implementierenden Dateien des Projekts
               for file_to_implement in use_cases["Use_Cases"][2][f"files_{project}"]:

                   #Laden aller wichtigen Informationen für die Eingabesequenz.

                    #Anforderungsspezifiation
                   with open(use_cases["Use_Cases"][2][f"input_{project}_PRD"], 'r') as file:
                       current_prd_file = file.read()

                    #Entwurf
                   with open(use_cases["Use_Cases"][2][f"input_{project}_Design"], 'r') as file:
                       current_design_file = file.read()

                    #Eingabesequenz
                   task:str = f"You are a nice " + use_cases["Use_Cases"][2][f"language_{project}"] + "developer. This is a software requirement specification:\n" + current_prd_file + "\nThis is a software design:\n" + current_design_file + "\n\n" + use_cases["Use_Cases"][2]["task_text"] + file_to_implement + " file."
                   #Extraktion des Dateinamens
                   filename = str(file_to_implement).rsplit('.', 1)[0]
                   
                    

                    #kwargs für die Generierung
                   generation_kwargs = {
                    "max_tokens":16384,
                    "stop":["</s>"],
                    "echo":False,
                   "top_k":1 #"Greedy decoding"
                   }
                   
                   #Für die Zeitmessung (Start)
                   start = time.time()
                
                    #Inferenz
                   res = llm(task, **generation_kwargs) 
                
                    #Für die Zeitmessung (Ende)
                   end = time.time()
                   project_implementation_time = project_implementation_time + (end - start)
                   
                   #Speichern der Antwort in seperater Datei
                   file_path = Path("../Results/Umsetzung/" + i["name"] +"/" + project + "/" + filename + ".txt")
                   with file_path.open('w') as file:
                       file.write(str(res["choices"][0]["text"]))
                
                   # Wenn alle Dateien für das Projekt generiert wurden kann die Gesamtdauer für die Implementierung in eine gesonderte Datei gespeichert werden
                   if ((use_cases["Use_Cases"][2][f"files_{project}"].index(file_to_implement)+1) == len(use_cases["Use_Cases"][2][f"files_{project}"])):
                       file_path = Path("../Results/Umsetzung/" + i["name"] +"/" + project + "/" + "implementation_time" + ".txt")
                       
                       with file_path.open('w') as file:
                        file.write("It took " + str(project_implementation_time) + f"seconds to implement the entire {project}.")

        except Exception as e:
          print(f"exception {e}")
          exit()
    
    
if __name__ == '__main__':
    
    start()