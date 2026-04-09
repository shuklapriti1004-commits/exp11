import logging
# Configure logging
logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Addition operation performed")
    return a + b


# Example usage
if __name__ == "__main__":
    result = add(2, 3)
    print(result)