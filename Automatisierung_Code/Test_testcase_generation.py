'''
Automatisierung für Testläufe des Anwendungsfalls: Testfall-Generierung
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
#import llama_cpp_python

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
    #Liste der Funktionen und Dateien für die Testfälle generiert werden sollen
    test_functions = ["testAddActor", "test_nest_small_csv", "test_mean_filter_RGB", "RegisterPage.vue", "test_plain_text_empty"]
    res = ""
    

    #Iteration durch die LLM
    for i in data["LLM"][0]["Test"]:
        #Dateipfad für die Speicherung der Ergebnisse anlegen, sofern noch nicht vorhanden
        "" if os.path.exists("../Results/Test/Testcases/" + i["name"]) else subprocess.run(["mkdir", "../Results/Test/Testcases/" + i["name"]])

        try:
            llm = None
            ## Instantiate model
            
            if i["GGUF"]:
                # Instantiiere Model
                llm = Llama(
                model_path=i["file"],
                n_ctx=30000, # Genutzte Kontextlänge 
                n_gpu_layers=-1,# Anzahl der Modellayer die auf die GPU ausgelagert werden sollen --> -1 bedeutet, dass alles auf die GPU ausgelagert wird
                verbose=True,
                logits_all=True,
                device = device
                )
            else:
                 pass
                #Keine '.bin' und '.safetensor' Modelle für diesen Anwendungsfall selektiert.

            # Iteration durch Projekte
            for project in projects:
               project_implementation_time = 0
                 #Dateipfad für die Speicherung der Ergebnisse anlegen, sofern noch nicht vorhanden
               "" if os.path.exists("../Results/Test/Testcases/" + i["name"] + "/" + project) else subprocess.run(["mkdir", "../Results/Test/Testcases/" + i["name"] + "/" + project])
               
               #Lesen der Usecase JSON-Datei für die Eingabesequenz und weitere Informationen
               with open('../JSON_Files/Use_Case.json', 'r') as file:
                               use_cases = json.load(file)


               #Lesen der relevanten Datei mit dem Test zu dem Testfälle implementiert werden sollen.
               with open(use_cases["Use_Cases"][3][f"input_{project}_Sourcecode_test_implementation"], 'r') as file:
                   current_testimplementation_file = file.read()
                

               index = projects.index(project)

               task:str = f"You are a nice " + use_cases["Use_Cases"][3][f"language_{project}"] + "developer. This is a test implementation:\n" + current_testimplementation_file + "\n This is an example for a test case: "  + use_cases["Use_Cases"][3][f"input_{project}_Sourcecode_test_case_examples"] + "\n" + use_cases["Use_Cases"][3]["task_generate_test_cases"] + f"{test_functions[index]} function."
              

               if i["GGUF"]:

                #kwargs für die Generierung
                generation_kwargs = {
                "max_tokens":30000,
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
                project_implementation_time = end - start
                
                #Speichern der Antwort in seperater Datei
                file_path = Path("../Results/Test/Testcases/" + i["name"] +"/" + project + "/" + project + ".txt")
                with file_path.open('w') as file:
                # Write content to the file
                   file.write(str(res["choices"][0]["text"]))
                
               else:
                pass
                #Keine '.bin' und '.safetensor' Modelle für diesen Anwendungsfall selektiert.
                   

        except Exception as e:
          print(f"exception {e}")
          exit()
    
    
if __name__ == '__main__':
    
    start()