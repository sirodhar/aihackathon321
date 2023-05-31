@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

rem Set variables
set prediction_url="https://language-aihackathon321.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=QnA-AIHackathon321&api-version=2021-10-01&deploymentName=production"
set key="ae07177ad7254524a6b104ac487aefaf"

curl -X POST !prediction_url! -H "Ocp-Apim-Subscription-Key: !key!" -H "Content-Type: application/json" -d "{'question': 'What is a learning Path?' }"