import io
import os

from flask import Flask
import google.auth
from google.cloud import secretmanager


app = Flask(__name__)


def get_google_secret_payload(gcloud_secret_name="beta-env"):
    """
    Load a secret from Google Cloud Secrets Manager
    """
    try:
        _, project_id = google.auth.default()
    except google.auth.exceptions.DefaultCredentialsError:
        project_id = None
    if project_id:
        client = secretmanager.SecretManagerServiceClient()
        secret_label = os.environ.get("GCLOUD_SECRET_NAME", gcloud_secret_name)
        gcloud_secret_name_path = f"projects/{project_id}/secrets/{secret_label}/versions/latest"
        payload = client.access_secret_version(name=gcloud_secret_name_path).payload.data.decode("UTF-8")
        return payload
    return None


@app.route("/")
def index():
    print('get_google_secret_payload', get_google_secret_payload())
    return f'Deploy Test {get_google_secret_payload()}'

