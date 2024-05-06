from notion.client import NotionClient

# Constants
NOTION_TOKEN = "v02%3Auser_token_or_cookies%3AaB3Rqo_Fqpu0dQdrv8A-_xrDd-8iwdJrBZ6k4DRNNIH4cO-Ul6lb4vMc-F_kBQ64dG8LNTgEgQF4tzzh93CFKEiPwvaJu9YBhFwPqOugX_sZkMB4TqyVXzaKkZtmNcE2P3Xq"

# Authenticate and create Notion client
def authenticate_notion():
    client = NotionClient(token_v2=NOTION_TOKEN)
    notion_client_attributes = dir(client)

    return client
authenticate_notion()