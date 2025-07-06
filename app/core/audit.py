import logging

logging.basicConfig(filename="audit.log", level=logging.INFO)

def log_action(action: str, actor: str):
    logging.info(f"[AUDIT] {actor} -> {action}")
