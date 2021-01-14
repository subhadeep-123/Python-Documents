import logging
import os
# This is for linux
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
exit(main())
