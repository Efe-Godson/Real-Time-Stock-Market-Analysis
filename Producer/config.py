import logging
import os

from dotenv import load_dotenv

load_dotenv()

#configure logging
logging.basicConfig(
 level=logging.INFO,
 format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

BASEURL = "alpha-vantage.p.rapidapi.com"
url = f"https://{BASEURL}/query"

api_key = os.getenv('API_KEY')

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": BASEURL
}


