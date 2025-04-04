"""
This project utilizes the Rich library for prettifying output and loguru for simpler logging. See readme for more details.
"""


logger.remove() # Removes default logger
logger.add(RichHandler(), level="DEBUG") # Sets Rich as a sink for logging

