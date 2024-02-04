# WriteRight

<p align="center">
    <img src="assets/logo.png" alt="Project logo">
</p>

## Table of Contents

- [WriteRight](#WriteRight)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about)
  - [Demo](#demo)
  - [Flowchart](#flowchart)
  - [Documentation](#documentation)
  - [File Structure](#file-structure)
  - [Getting started](#Getting-Started)
  - [Future Goals](#future-goals)
  - [References](#references)
  - [License](#license)
  

## About

The computerized grading of essays by machine learning and natural language processing is known as Automated Essay Scoring (AES). The project's primary goal is to rate an essay from 1 to 10 based on a variety of criteria. The algorithm considers three primary factors: the quality of word and phrase usage (Statistical), the correctness of the grammar (Syntax), and the essay's coherence and depth (Semantics). This makes essay evaluations more interpretable and accurate, while also saving time for educational institutions and tests like the GRE.

## Demo

## Flowchart

<p align="center">
    <img src="assets/flowchart.png" alt="Flowchart">
</p>


## Documentation

Please refer ```/documentation``` or click <a href="https://github.com/PritK99/WriteRight/blob/main/documentation/README.md">here</a> for complete documentation of the project.

## File Structure
```
👨‍💻WriteRight
 ┣ 📂assets                            // Contains all the reference gifs, images
 ┣ 📂data                              // Datasets for training and Testing
 ┃ ┣ 📄train.csv  
 ┃ ┣ 📄test.csv 
 ┣ 📂Documentation                     // Complete Documentation and Project Workflow
 ┃ ┣ 📄README.md
 ┣ 📂model                             // Standalone model         
 ┃ ┣ 📄main.py    
 ┃ ┣ 📄statistics.py
 ┃ ┣ 📄syntax.py                
 ┃ ┣ 📄semantics.py 
 ┣ 📂test                              // Testing       
 ┃ ┣ 📄test.py   
 ┣ 📂client                            // Frontend        
 ┃ ┃ ┣ 📂src                                      
 ┃ ┃ ┃ ┣ 📂components  
 ┃ ┃ ┃ ┃ ┣ 📄RunButton.js  
 ┃ ┃ ┃ ┃ ┣ 📄ScoreReport.js 
 ┃ ┃ ┃ ┃ ┣ 📄TextInput.js
 ┃ ┃ ┃ ┣ 📂styles
 ┃ ┃ ┃ ┃ ┣ 📄App.css
 ┃ ┃ ┃ ┣ 📄index.js
 ┃ ┃ ┣ 📂public 
 ┃ ┃ ┃ ┣ 📄index.html
 ┣ 📂server                            // Backend 
 ┃ ┣ 📄app.py   
 ┣ 📄README.md
``` 

## Getting Started

### Prerequisites
To download and use this code, the minimum requirements are:

* Windows 7 or later (64-bit), Ubuntu 20.04 or later
* [Microsoft VS Code](https://code.visualstudio.com/download) or any other IDE 
* Please install all the neccesary Python libraries using pip if required.

### Installation

Clone the project by typing the following command in your Terminal/CommandPrompt

```
git clone https://github.com/PritK99/WriteRight
```
Navigate to the WriteRight folder

```
cd WriteRight
```

### Usage

Once the requirements are satisfied, you can easily use the project. There are two ways to use the project, one is through the Web Application and other is through command line.

<b>Note:</b> The model requires approximately ```1.5 minutes``` to complete the evaluation of the essay. Thus, please wait for the model to evaluate results and print for some time after clicking run on web application or pressing enter twice on command line.

#### Method I: Using Web Application

  * To start the client, run these commands
  ```
  cd client
  ```
  ```
  npm i
  ```
  ```
  npm start
  ```

  * To start the server, run these commands on new terminal

  ```
  cd server
  ```
  ```
  python app.py
  ```
#### Method II: Using Command Line

  Navigate to standalone model folder
  ```
  cd model
  ```

  Run the driver file using python or the IDE of your choice.
  ```
  python main.py
  ```

## References
* Unsupervised learning during the statistical phase was conducted using a dataset from Kaggle's Feedback Prize – English Language Learning competition. The dataset can be accessed <a href="https://www.kaggle.com/competitions/feedback-prize-english-language-learning/data?select=train.csv.">here</a>.
* Hewlett Foundation's <a href="https://www.kaggle.com/competitions/asap-aes/overview">Automated Essay Scoring Competition</a>, held in 2012.
<a href="The Hewlett Foundation: Automated Essay Scoring">Automated Essay Scoring</a> competion by Hewlett Foundation.
* Reference was made to the following <a href="https://github.com/ZhuoyueWang/AutomatedEssayScoring">GitHub repository</a> for Automated Essay Scoring.

## Future Goals

- [ ] Considering more features such as number of Short Words, number of Long Words, Sentence Formation, Capitalization, Proper use of articles etc.
- [ ] Improving the Web Application by adding better UI and Features.
- [ ] Using Deep Learning Techniques such as LSTMs and CNNs to improve the performance of the algorithm.

## License
[MIT License](https://opensource.org/licenses/MIT)