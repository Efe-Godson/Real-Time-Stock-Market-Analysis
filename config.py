import logging
import os

frm dotenv import load_dotenv

load_dotenv()

#configure logging
logging.basicConfig(
 level=logging.INFO,
 format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logger.getLogger(_name_)