from logger import logger
from system import bot
import messages


def main():
    try:
        logger.info("bot starting")
        bot.polling(none_stop=True)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logger.info("bot stopped")
        logger.critical(e)
    

if __name__ == "__main__":
    main()
