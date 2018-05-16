from cases.helper import utils

account = utils.get_account()
print('account-->' + str(account))

utils.save_password('123456789')
account = utils.get_account()
print('account-->' + str(account))
