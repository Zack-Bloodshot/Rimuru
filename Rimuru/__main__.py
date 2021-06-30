from Rimuru import rimuru 
import logging  
import Rimuru.modules 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger("__name__")

print("Starting....")
rimuru.start()
rimuru.run_until_disconnected()
