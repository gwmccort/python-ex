import logging

log = logging.getLogger(__name__)


class MyClass:
    log = logging.getLogger(__name__ + '.MyClass')

    def __init__(self) -> None:
        # self.log = logging.getLogger(self.__name__)
        # self.log = logging.getLogger('MyClass')
        # print('__name__:', __name__)
        # print('class:', str(__class__))
        print('in MyClass.init')
        self.log.info('in MyClass.__init__')
