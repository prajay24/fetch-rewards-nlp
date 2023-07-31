**Fetch Rewards - NLP Take Home 
Prajay Sachdev (prajay9924@gmail.com)**

Steps to run the assignment in a new conda environment

- Create a new conda environment. Use the conda terminal and run the command: 'conda create --name fetch-prajay python=3.8.8'
- Activate 'fetch-prajay' environment
- Launch VSCODE
- Launch Terminal from VSCode, ensure that your conda envirnment is 'fetch-prajay'
- Run the command in the terminal 'pip install -r requirements.txt'. This shall install all the packages required for the project. This may take a few minutes to install
- To activate the server, run, 'uvicorn main:app --reload'
- Ensure there are no other local servers previous running on the same port. Open in an incognito browser window to open 'http://127.0.0.1:8000/docs' This will launch the Swagger Document with the 6 GET APIs.
  - 3 APIs each starting with /cosine for cosine similarities to give results for user searches by - brand, retailer, and category
  - 3 APIs each starting with /dot for dot scores to give results for user searches by - brand, retailer, and category
