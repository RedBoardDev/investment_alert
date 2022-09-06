import schedule
from time import sleep
from main_lib import request_json
from lib_file import utils_file

def compare_value(i_1:int, i_2:int) -> bool:
    if (i_1 != i_2):
        return (False)
    return (True)

def evmos_alert():
    req = request_json("https://proxy.atomscan.com/evmos-lcd/staking/delegators/evmos1y225ugph305lmgl0lkt9k7gcn4ugtnvxgezzvr/delegations")
    actual_balance:int = int(req['result'][0]['balance']['amount'])
    utils_file_fct = utils_file()
    utils_file_fct.load_file('data.json')
    data_balance:int = utils_file_fct.f_read('balance')
    if (compare_value(data_balance, actual_balance) == True):
        utils_file_fct.f_write("balance", actual_balance)
        difference_balance:int = actual_balance - data_balance
        print(difference_balance)

schedule.every().day.at("02:10").do(evmos_alert)

while True:
    schedule.run_pending()
    sleep(1)