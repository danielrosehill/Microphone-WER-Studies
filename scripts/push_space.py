# /// script
# dependencies = ["huggingface_hub"]
# ///
"""Refresh the bundled fallback CSV and deploy space/ to Hugging Face (uses the local HF login)."""
import pathlib, shutil
from huggingface_hub import HfApi
R = pathlib.Path(__file__).resolve().parent.parent
REPO = "danielrosehill/Microphone-WER-Explorer"
shutil.copy(R / "data/master.csv", R / "space/master.csv")
api = HfApi()
api.create_repo(REPO, repo_type="space", space_sdk="static", private=False, exist_ok=True)
api.upload_folder(repo_id=REPO, repo_type="space", folder_path=str(R / "space"), commit_message="Deploy from GitHub")
