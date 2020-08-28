from selenium import webdriver
import time

class MeetBot:
    def __init__(self, code):
        self.driver = webdriver.Chrome()
        self.driver.get('https://accounts.google.com')
        input('Login to account... [Press enter to continue]')
        self.driver.get('https://meet.google.com/' + code)
    
    def SendInvites(self):
        self.driver.refresh()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[4]/div[1]/div/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[4]/div[2]/div/div').click()
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]').click()

### SETUP ###
print('Google Meet Flooder\n')
code = input('Code?: ')
bot = MeetBot(code)
print('Preparing...')
input('Give access to microphone: [Press enter to continue]')
timeout = float(input('Timeout?: '))

### MAIN LOOP ###
while True:
    invite = 1
    str_quantity = input('Number of invites?: ')
    try:
        quantity = int(str_quantity)
        for i in range(quantity):
            bot.SendInvites()
            print('Sending invite ' + str(invite) + '...')
            invite += 1
            time.sleep(timeout)
    except:
        if str_quantity == 'infinite':
            while True:
                bot.SendInvites()
                print('Sending invite ' + str(invite) + '...')
                invite += 1
                time.sleep(timeout)