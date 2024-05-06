
import subprocess
import json
import requests
import schedule 
import time
from google_tasks import authenticate_google_tasks
from notion_api import authenticate_notion
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the NOTION_TOKEN and database_id from the environment
notion_token = os.getenv("notion_token")
database_id = os.getenv("DATABASE_ID")


def sync_tasks():
    # Get existing pages from Notion database
    notion_pages = []

    # Make a cURL command to query the Notion database
    curl_command = [
        "curl",
        "-X",
        "POST",
        f"https://api.notion.com/v1/databases/{database_id}/query",
        "-H",
        f"Authorization: Bearer {notion_token}",
        "-H",
        "Content-Type: application/json",
        "-H",
        "Notion-Version: 2022-06-28",
        "--data",
        ' {}'
    ]
    # Execute the cURL command and get the response
    curl_output = subprocess.check_output(curl_command).decode("utf-8")
    response = json.loads(curl_output)
    notion_results = response.get("results", [])

    # Iterate over the Notion results and extract page information
    for result in notion_results:
        page_title = result["properties"]["Title"]["title"][0]["text"]["content"]
        page_description = result["properties"]["Description"]["rich_text"][0]["text"]["content"]
        notion_pages.append({"title": page_title, "description": page_description})

    # Authenticate with Google Tasks API
    google_tasks_service = authenticate_google_tasks()

    # Get all Google Tasks
    tasks_result = google_tasks_service.tasks().list(tasklist="@default").execute()
    tasks = tasks_result.get("items", [])

    # Sync tasks to Notion
    for task in tasks:
        task_title = task["title"]
        task_description = task.get("notes", "")

        # Check if task is already in Notion
        is_duplicate = False
        for page in notion_pages:
            if page["title"] == task_title and page["description"] == task_description:
                is_duplicate = True
                break

        if is_duplicate:
            continue

        # Create a new page in the Notion database
        data = {
            "parent": {"database_id": database_id},
            "properties": {
                "Title": {"title": [{"text": {"content": task_title}}]},
                "Description": {"rich_text": [{"text": {"content": task_description}}]}
            }
        }
        response = requests.post(
            "https://api.notion.com/v1/pages",
            headers={
                "Authorization": f"Bearer {notion_token}",
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28"
            },
            json=data
        )
        print(response.status_code)
        print(response.json())

# Schedule the task synchronization every 10 seconds
schedule.every(10).seconds.do(sync_tasks)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)

