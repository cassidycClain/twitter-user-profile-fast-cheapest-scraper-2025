import json
import logging
from pathlib import Path

class Exporter:
    """Handles exporting scraped data to JSON."""

    def __init__(self, output_file: str):
        self.output_file = Path(output_file)
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

    def export(self, data: list[dict]) -> None:
        """Export data to JSON file."""
        try:
            with open(self.output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logging.info(f"Data successfully written to {self.output_file}")
        except Exception as e:
            logging.error(f"Failed to export data: {e}")
            raise