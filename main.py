if __name__ == '__main__':
    try:
        logger.info('ETL Process Initialized for main_fix1')
        main() #inline comment for main_fix1
    except:
        logger.error(f"Extract: uncaught exception in main: {traceback.format_exc()}")

<<<<<<< HEAD

print('master message1')




def func2:
	print('master added func2')
=======
print('main_fix1 message1')


def func1:
	print('main_fix1 added func1')
>>>>>>> main_fix1
