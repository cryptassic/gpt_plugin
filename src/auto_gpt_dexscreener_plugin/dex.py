import json
from typing import List

from .dex_client import get_token
from .models import Token


class DEX:
    """
    This is a plugin to use Auto-GPT with DEX Screener.
    """

    def __init__(self):
        self._token_mapping = self._load_mapping(
            "./token_mappings.json"
        )

    def get_token_symbols(self) -> List[str]:
        """This method is called to retrieve all available token symbols.
        Returns:
            List[str]: The list of token symbols.
        """
        return list(self._token_mapping.keys())

    def get_token_data(self, symbol) -> Token:
        """This method is called to retrieve token data.
        Args:
            (str): The token symbol.
        Returns:
            (Token): Token data.
        """
        pool_id = self._symbol_to_pool_id(symbol.upper())

        if pool_id is not None:
            return get_token(pool_id)

        return None

    def _load_mapping(self, filename: str):
        with open(filename, "r") as f:
            data = json.load(f)
            return data

    def _symbol_to_pool_id(self, symbol: str) -> int:
        return self._token_mapping.get(symbol, None)
