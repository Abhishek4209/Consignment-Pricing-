
# Consignment-Pricing-Prediction-Using-MLOps-DVC

<div style="text-align: center">
  <img src="https://github.com/Abhishek4209/Consignment-Pricing-/blob/main/IMG.jpg" alt="">
</div>

## Project Overview
The Consignment-Price Prediction project aims to develop a machine-learning model that can accurately predict the price of consignment items based on various features and variables. Consignment is a business model in which an individual or business agrees to sell someone else's items on their behalf, typically taking a commission on the final sale price.

This project aims to create a predictive model to help consignment store owners and sellers better understand how to price their items, leading to increased sales and profits. To accomplish this, the project will involve collecting and analyzing data on various features that could impact the sale price of consignment items, such as the item's condition, brand, and rarity, as well as market trends and buyer behaviour.

Once the data is collected, the project will involve cleaning and preprocessing the data, selecting appropriate features, and training and testing various machine learning algorithms to determine which model performs the best. The project will also involve evaluating the accuracy and effectiveness of the final model, and potentially deploying it in a web application or other tool that consignment store owners and sellers can use.

Overall, the Consignment-Price Prediction project has the potential to provide significant value to the consignment industry by helping sellers and store owners make more informed pricing decisions, leading to increased sales and revenue.

## Website
...

## File Structure 
    .
    ├── app_exception           # Custom exception
    ├── application_logging     # custom logger
    ├── data_given              # Given Data
    ├── data                    # raw / processed/ transformed data
    ├── saved_models            # regression model
    ├── report                  # model parameter and pipeline reports.
    ├── notebook                # jupyter notebooks
    ├── src                     # Source files for project implementation
    ├── webapp                  # ml web application
    ├── dvc.yaml                # data version control pipeline.
    ├── app.py                  # Flask backend
    ├── param.yaml              # parameters
    ├── requirements.txt
    └── README.md

## Dataset
The dataset is provided by PW SKILLS: 
[supply-chain-shipment-pricing-data](https://www.kaggle.com/datasets/divyeshardeshana/supply-chain-shipment-pricing-data/code)



## Model information
Experiments:

         Model Name              R2 score 
      1. Linear Regression         92.35        
      2. Lasso Regression          91.41
      3. DecisionTree Regression   95.71
      4.
      
## Results and analysis

After training the model, we achieved an R-squared value of 0.95 (95% accuracy) on the test data, indicating a high level of predictive power.

## Installation
To run the code, first clone this repository and navigate to the project directory:
```
git clone https://github.com/Abhishek4209/Consignment-Pricing-
```
Create a virtual environment
```
conda create -p venv python==3.12 -y
conda activate venv/
```
To run this project, you will need Python packages present in the requirements file
```
pip install -r requirements.txt
```

Then, run the `app.py` file to start the Flask web application:
```
python app.py
```

### Setup
```pip install -e```

### Package building
``` python setup.py sdist bdist_wheel```



Use logging libraries to make logs

### Web Deployment
Streamlit is used to build a website<br>
all the codes are given in app.py

## Contributions
If you have any questions or suggestions regarding the project, please feel free to contact the project maintainer at [gmail](abhishekupadhyay9336@gmail.com
)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Run the Project
- Clone the project
- pip install -r requirements.txt
- python app.py Enjoy the project in a local host
