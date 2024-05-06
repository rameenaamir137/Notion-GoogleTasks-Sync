from notion.client import NotionClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Read the NOTION_TOKEN from the environment
NOTION_TOKEN = os.getenv("NOTION_TOKEN")

# Authenticate and create Notion client
def authenticate_notion():
    client = NotionClient(token_v2=NOTION_TOKEN)
    notion_client_attributes = dir(client)

    return client
authenticate_notion()
