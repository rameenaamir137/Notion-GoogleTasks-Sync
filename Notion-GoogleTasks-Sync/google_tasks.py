import os 
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Constants
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]

# Authenticate and create Google Tasks service
def authenticate_google_tasks():
    credentials = None

    # Check for saved credentials
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    # If no valid credentials found, authenticate user
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            credentials = flow.run_local_server(port=0)
        # Save credentials for next run
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    # Build Google Tasks service
    service = build("tasks", "v1", credentials=credentials)
    return service
authenticate_google_tasks()