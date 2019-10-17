import logging

logging.basicConfig(level=logging.DEBUG)


def pay_developer(hours):
    logging.debug(f"We get {hours} hours of work")

    if hours < 120:
        logging.warning(f"Too less hours {hours}")

    if not isinstance(hours, int):
        logging.error(f"Wrong type of hours {type(hours)}")
        return None

    result = hours * 50
    logging.info(f"We pay {result} money")
    return result


if __name__ == "__main__":
    pay_developer(100)
