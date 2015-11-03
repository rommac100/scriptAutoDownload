__author__ = 'rommac100'
from splinter import Browser
with Browser('chrome') as browser:
    browser.visit("https://arlo.netgear.com/#/login")
    # Enter you Username/Email, replace the temp.
    browser.fill('userId', 'tempemail@tempemail.com')
    # Enter you password, replace the temp.
    browser.fill('password', 'tempPass')
    button = browser.find_by_id('loginButton')
    button.click()
    if browser.is_text_present('Settings'):
        print('')
    else:
        print("Found.")
        if browser.is_text_present('Library'):
            button2 = browser.find_by_id('footer_library')
            button2.click()
            if browser.is_text_present('Click on'):
                button3 = browser.find_by_id('day_ok')
                button3.click()
                if browser.is_text_present('Select'):
                    button4 = browser.find_by_id('day_ToggleSelectMode')
                    button4.click()
                    if browser.is_text_present('Select Alls'):
                        print('')
                    else:
                        button5 = browser.find_by_id('day_SelectAll')
                        button5.click()
                        if browser.is_text_present('Downloads'):
                            print("Download is present.")
                        else:
                            button6 = browser.find_by_id('footer_download')
                            button6.click()
                            print("Type:'delete' if you want to delete the files.")
                            x = input()
                            if x == "delete":
                                button7 = browser.find_by_id('footer_delete')
                                button7.click()
                                if browser.is_text_present('Are you sure'):
                                    button8 = browser.find_by_id('buttonConfirm')
                                    button8.click()
                                    if browser.is_text_present('Done'):
                                        button9 = browser.find_by_id('day_ToggleSelectMode')
                                        button9.click()
                                else:
                                    print("Did not delete it.")
                            else:
                                print("Done.")
            else:
                print("No.")