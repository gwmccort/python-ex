
# %%
import logging

# logging.basicConfig()
log = logging.getLogger()
print('\n\nlog.level (default):', log.level)
log.debug('debug message')
log.info('info message')
log.warning('warring message')

logging.basicConfig(level=logging.INFO)
print('\n\nlog.level (after config info):', log.level)
log.debug('debug message')
log.info('info message')
log.warning('warring message')


log.setLevel(logging.DEBUG)
print('log.level (new debug):', log.level)
log.debug('debug message')
log.info('info message')
log.warning('warring message')

# rl = logging.getLogger('root')
# print(rl)
# logging.basicConfig(level=logging.DEBUG)
# print(rl)

# logging.info('info')
# logging.warning('warn')

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s')

# logging.info('info mes')
# logging.warning('warn mes')

# log = logging.getLogger()
# print('log.level:', log.level)
# log.setLevel(logging.DEBUG)
# print('log.level:', log.level)

# log.info('info')
# log.warning('warning')
# log.error('error')

# print('logging.level:', logging.level)

# logging.basicConfig(level=logging.INFO)
# print('logging.level:', logging.level)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# %%
