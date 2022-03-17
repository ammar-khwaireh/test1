if __name__ == '__main__':
    try:
        logger.info('ETL Process Initialized for main_fix1')
        main()
    except:
        logger.error(f"Extract: uncaught exception in main: {traceback.format_exc()}")
