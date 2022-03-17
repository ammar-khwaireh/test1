if __name__ == '__main__':
    try:
        logger.info('ETL Process Initialized for main_fix1')
        main() #inline comment for main_fix1
    except:
        logger.error(f"Extract: uncaught exception in main: {traceback.format_exc()}")

print('main_fix1 message1')