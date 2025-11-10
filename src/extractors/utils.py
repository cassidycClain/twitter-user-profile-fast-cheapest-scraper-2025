import random
import string
from datetime import datetime, timedelta

def random_date() -> str:
    """Generate a random date string similar to Twitter format."""
    start_date = datetime(2010, 1, 1)
    end_date = datetime.now()
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_time = start_date + timedelta(days=random_days)
    return random_time.strftime("%a %b %d %H:%M:%S +0000 %Y")

def random_string(length: int) -> str:
    """Generate a random alphanumeric string."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))