import logging
import random
import time
from src.extractors.utils import random_date, random_string

class TwitterParser:
    """Simulates Twitter user profile scraping."""

    def __init__(self, api_endpoint: str, timeout: int):
        self.api_endpoint = api_endpoint
        self.timeout = timeout

    def fetch_user_profile(self, username: str) -> dict:
        """Simulate fetching Twitter profile data."""
        logging.debug(f"Fetching data from {self.api_endpoint} for {username}")
        time.sleep(0.1)  # simulate network latency

        user_id = str(random.randint(1000000000000000000, 9999999999999999999))
        created_at = random_date()
        is_blue_verified = random.choice([True, False])
        followers = random.randint(0, 1000000)
        favourites = random.randint(0, 500)
        media = random.randint(0, 100)
        statuses = random.randint(0, 5000)
        description = f"This is a simulated bio for @{username}. Generated with Fast&Cheapest Scraper 2025."
        profile_img = f"https://pbs.twimg.com/profile_images/{random_string(10)}/normal.png"
        url = f"https://twitter.com/{username}"

        return {
            "userId": user_id,
            "isBlueVerified": is_blue_verified,
            "createdAt": created_at,
            "followersCount": followers,
            "favouritesCount": favourites,
            "mediaCount": media,
            "statusesCount": statuses,
            "username": username,
            "profileImageUrlHttps": profile_img,
            "description": description,
            "url": url,
        }