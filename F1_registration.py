__author__ = 'zengc'

import unittest
from selenium import webdriver

class RegistrationTest(unittest.TestCase):
        
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.username = "register"
        self.email = "register@rose-hulman.edu" 
        self.password = 12345
        self.short_password = 123
        self.diff_password = 13245
        self.delete = 1;
        
    def tearDown(self):
        if(self.delete == 1):
            #delete account
            self.driver = webdriver.Chrome()
            #Login
            self.driver.get("http://localhost:8000")
            self.driver.find_element_by_id('loginlink').click()
            self.driver.find_element_by_name('email').send_keys(self.email)
            self.driver.find_element_by_name('password').send_keys(self.password)
            self.driver.find_element_by_id('btn-login').click()
    
            #Delete
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul[1]/li[3]/a").click()
            self.driver.find_element_by_id('deletacctlink').click()
            self.driver.find_element_by_id('passField').send_keys(self.password)
            self.driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/button").click()
            self.driver.quit()
            
       
    def test_1_registration_centerbutton(self):
        #Open main page
        self.driver.get("http://localhost:8000")
        #Click register button
        self.driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/input[2]").click()
        #Verify page redirect
        self.assertIn("http://localhost:8000/registration/", self.driver.current_url)
        #Fill test data
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('confirm').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        #Check that the registration is complete, page redirect to success_page
        self.assertIn("http://localhost:8000/registration/register_user", self.driver.current_url)
        self.assertIn("Registration successful, please login to continue.", self.driver.page_source)
        #Close browser
        self.driver.quit()
        
    def test_2_registration_navbar(self):
        #Open another main page
        self.driver.get("http://localhost:8000")
        self.driver.find_element_by_id('registerlink').click()
        #Verify page redirect
        self.assertIn("http://localhost:8000/registration/", self.driver.current_url)
        #Fill test data
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('confirm').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        #Check that the registration is complete, page redirect to login_page
        self.assertIn("http://localhost:8000/registration/register_user", self.driver.current_url)
        self.assertIn("Registration successful, please login to continue.", self.driver.page_source)
        #Close browser
        self.driver.quit()
    
    def test_3_exsisting_account(self):
        #Open main page
        self.driver.get("http://localhost:8000")
        #Click register button
        self.driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/input[2]").click()
        #Verify page redirect
        self.assertIn("http://localhost:8000/registration/", self.driver.current_url)
        #Fill test data
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('confirm').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        #Check that registration failed and gives fail message
        self.assertIn("http://localhost:8000/registration/register_user", self.driver.current_url)
        self.assertIn("Registration successful, please login to continue.", self.driver.page_source)
        
        #Open new main page
        self.driver.get("http://localhost:8000")
        #Click register button
        self.driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/input[2]").click()
        #Verify page redirect
        self.assertIn("http://localhost:8000/registration/", self.driver.current_url)
        #Fill test data
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('confirm').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        #Check that registration failed and gives fail message
        self.assertIn("http://localhost:8000/registration/register_user", self.driver.current_url)
        self.assertIn("Registration failed: Account already registered", self.driver.page_source)
        #Close browser
        self.driver.quit()
    
    def test_4_short_password(self):
        #Don't run delete account
        self.delete = 0
        
        #Open new main page
        self.driver.get("http://localhost:8000")
        #Click register button
        self.driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/input[2]").click()
        #Verify page redirect
        self.assertIn("http://localhost:8000/registration/", self.driver.current_url)
        #Fill test data
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('password').send_keys(self.short_password)
        self.driver.find_element_by_id('confirm').send_keys(self.short_password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        #Check that registration failed and gives fail message
        self.assertIn("http://localhost:8000/registration/register_user", self.driver.current_url)
        self.assertIn("Password needs to be at least 4 characters long", self.driver.page_source)
        #Close browser
        self.driver.quit()
    
    def test_5_diff_password(self):
        #Don't run delete account
        self.delete = 0
        
        #Open new main page
        self.driver.get("http://localhost:8000")
        #Click register button
        self.driver.find_element_by_xpath("//*[@id='login']/div/div/div/div/input[2]").click()
        #Verify page redirect
        self.assertIn("http://localhost:8000/registration/", self.driver.current_url)
        #Fill test data
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_id('confirm').send_keys(self.diff_password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        #Check that registration failed and gives fail message
        self.assertIn("http://localhost:8000/registration/register_user", self.driver.current_url)
        self.assertIn("Passwords need to match", self.driver.page_source)
        #Close browser
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()