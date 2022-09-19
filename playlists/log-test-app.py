import logging
import loglib
import LogClass


def main():
    # logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    logging.info('Started')
    loglib.do_something()

    lc = LogClass.MyClass()
    # logging.info(lc.name)

    logging.info('Finished')


if __name__ == '__main__':
    main()
