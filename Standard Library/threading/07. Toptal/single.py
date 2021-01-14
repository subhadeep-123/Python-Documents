import logging
import os
from time import time

import key
from download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    ts = time()
    try:
        client_id = key.client_id
    except ImportError:
        logger.error('Cannot Import client_id')
    download_dir = setup_download_dir()
    links = get_links(client_id)
    for link in links:
        download_link(download_dir, link)
    logger.info(f"Took {time() - ts} seconds")


if __name__ == "__main__":
    main()
