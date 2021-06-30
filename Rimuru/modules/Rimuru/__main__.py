from Rimuru import rimuru, rafael
import logging  
import Rimuru.modules 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger("__name__")

print("Starting....")
rimuru.parse_mode = 'md'
rafel.parse_mode = 'md'
rimuru.start()
rimuru.run_until_disconnected()
