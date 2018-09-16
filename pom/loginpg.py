
class LoginPage(object):
    base_url="http://118.31.19.120:3000/"
    login_link_text = "登录"
    username_id="name"
    pass_id="pass"
    login_btn_css_selector=".span-primary"

    fail_tag_name="Strong"
    success_css_selector='span.user_name > a'

    def check_login(self,driver,username,password,status):
        driver.get(self.base_url)
        driver.find_element_by_link_text(self.login_link_text).click()
        driver.find_element_by_id(self.username_id).send_keys(username)
        driver.find_element_by_id(self.pass_id).send_keys(password)
        driver.find_element_by_css_selector(self.login_btn_css_selector).click()

        # error_msg
        if status=='fail':
            result_text = driver.find_element_by_tag_name(self.fail_tag_name).text 
        else:
            result_text = driver.find_element_by_css_selector(self.success_css_selector).text
        
        return result_text

    