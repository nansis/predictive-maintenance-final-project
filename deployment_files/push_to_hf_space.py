from huggingface_hub import HfApi, create_repo

SPACE_REPO_ID = "nansri/engine-predictive-maintenance-app"

create_repo(
    repo_id=SPACE_REPO_ID,
    repo_type="space",
    space_sdk="docker",
    exist_ok=True
)

api = HfApi()

api.upload_folder(
    folder_path="deployment_files",
    repo_id=SPACE_REPO_ID,
    repo_type="space"
)

print(f"Deployment files uploaded successfully to Hugging Face Space: {SPACE_REPO_ID}")