import logging

def debug_log():
    logging.debug('Ha-ha!')


def main():
    log_format = "%(asctime)s %(levelname)s %(message)s"
    logging.basicConfig( filename='way.txt'
                        ,level=logging.DEBUG
                        ,filemode='a'
                        ,format=log_format)
                        )
    debug_log()

if __name__ != '__main__':
    main()
