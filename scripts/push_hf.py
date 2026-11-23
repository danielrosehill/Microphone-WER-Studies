# /// script
# dependencies = ["huggingface_hub"]
# ///
"""Rebuild, then upload the master table and dataset card to Hugging Face (uses the local HF login)."""
import pathlib, subprocess, sys
from huggingface_hub import CommitOperationAdd, HfApi
R = pathlib.Path(__file__).resolve().parent.parent
REPO = "danielrosehill/Microphone-WER-Studies"
subprocess.run([sys.executable, str(R / "scripts/build.py")], check=True)
api = HfApi()
api.create_repo(REPO, repo_type="dataset", exist_ok=True, private=False)
api.create_commit(REPO, repo_type="dataset", commit_message="Sync from GitHub", operations=[
    CommitOperationAdd("master.csv", str(R / "data/master.csv")),
    CommitOperationAdd("studies.json", str(R / "data/studies.json")),
    CommitOperationAdd("README.md", str(R / "hf/README.md"))])
