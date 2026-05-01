import logging
import os
from extract import extract
from transform import transform
from load import load

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    try:
        logging.info("Pipeline started")

        raw = extract()
        clean = transform(raw)
        load(clean)

        logging.info("Pipeline completed successfully")
        print("Pipeline executed successfully 🚀")

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    run_pipeline()