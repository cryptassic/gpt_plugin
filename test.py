from src.auto_gpt_dexscreener_plugin.dex import DEX

dex = DEX()
token = dex.get_token_data("OSMO")

print(token)
