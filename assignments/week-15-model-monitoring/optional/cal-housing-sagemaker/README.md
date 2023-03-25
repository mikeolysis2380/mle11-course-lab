<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>

# Housing Price Prediction 
This week you will experiment with SageMaker Autopilot that automatically performs feature engineering, model selection, model tuning (hyperparameter optimization) and allows you to directly deploy the best model to an endpoint to serve inference requests.

## Deliverables
- This assignment is *Optional*. 

## ☑️ Learning Objectives
At the end of this session, you will be able to:

- Perform machine learning tasks leveraging Sagemaker (Studio)
- Use SageMaker Autopilot to perform feature engineering, model selection, model tuning (hyperparameter optimization) 
- Deploy the best model to an endpoint to serve inference requests
- Tracking SageMaker Autopilot job progress and results
- Clean up resources


## :hammer_and_wrench: Pre-work
To run the notebook `nb/autopilot_california_housing.ipynb`, there are a few options for you to upload the notebook to SageMaker.
- To use Amazon SageMaker Studio and if it is your first time, you need to complete the [Studio onboarding process](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html). For more information, see **Step 2** in [Build, train, deploy, and monitor a machine learning model
with Amazon SageMaker Studio](https://aws.amazon.com/getting-started/hands-on/build-train-deploy-monitor-machine-learning-model-sagemaker-studio/).

- Alteratively, you can **launch a notebook instance**
	- Navigate to `Notebook` > `Notebook instances` > `Create notebook instance` down in the side panel, using most default values. Choose default instance `ml.t3.medium` (free tier, checking more pricing [here](https://aws.amazon.com/sagemaker/pricing/))
	- Once `Status` turns `InService`, you can launch the notebook instance either by `Open Jupyter | Open JupyterLab`
	- Upload the notebook and run it with kernel `conda_python3`.
	- Or through a Git repository, see details in [Git Repos](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html).

## Instructions
The assignment is rather straightforward. Once the notebook is in sagemaker following one of the options listed in Pre-work, simply run the notebook `nb/autopilot_california_housing.ipynb` and follow the instructions inside the notebook. 

Under the subdirectory `output`, you will find `nb/output/autopilot_california_housing.ipynb` contains cell outputs, adn two notebooks generated from the running the notebook for you review. 

In your SageMaker Studio, the file structure after you finish running the notebook (if you did not uncomment ` # delete_local_files()` in the last cell) should look similar to
```
.
├── automl-housing-20220812-16-18wm1-010-352d0c11
│   ├── analysis.json
│   ├── explanations_shap
│   │   ├── baseline.csv
│   │   └── out.csv
│   │       ├── part-00000-64efe987-b57d-45cf-98e3-27ba3d7b31d0-c000.csv
│   │       └── _SUCCESS
│   ├── report.html
│   ├── report.ipynb
│   └── report.pdf
├── autopilot_california_housing.ipynb
├── cal_housing.tgz
├── CaliforniaHousing
│   ├── cal_housing.data
│   └── cal_housing.domain
├── SageMakerAutopilotCandidateDefinitionNotebook.ipynb
├── SageMakerAutopilotDataExplorationNotebook.ipynb
├── test_data_no_target.csv
└── train_data.csv
```

**Stop the instance** after you are done. Check this out [Automatically shutting down idle resources within Amazon SageMaker Studio](https://aws.amazon.com/blogs/machine-learning/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/)

# Reference
The notebook is taken from [aws/amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples/blob/main/autopilot/autopilot_california_housing.ipynb)

You can explore more SageMaker examples pulling the repo locally. Use `--depth 1` to only pull the latest commit, instead of the entire commit history to save some time.
	
```bash
git clone --depth 1 git@github.com:aws/amazon-sagemaker-examples.git

