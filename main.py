if __name__ == '__main__':
    try:
        logger.info('ETL Process Initialized')
        main()
    except:
        logger.error(f"Extract: uncaught exception in main: {traceback.format_exc()}")
