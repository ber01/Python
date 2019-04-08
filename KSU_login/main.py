import pkg_resources, pip

data = list()
with open('./KSU_login/inputForm') as f:
    data = f.readlines()

id, pwd = data[0].rstrip(), data[1].rstrip()

package_list = [str(l).split()[0] for l in pkg_resources.working_set]

if not 'selenium' in package_list:
    print('selenium을 다운로드 합니다.')
    pip.main(['install', 'selenium'])

from selenium import webdriver

# 크롬 드라이버 지정
driver = webdriver.Chrome('./KSU_login/chromedriver')

# 경성포탈 접속
driver.get('https://portal.ks.ac.kr')

driver.implicitly_wait(3)

# 설치가 되어 있지 않은 경우
try:
    # 현재 driver의 alert 창 받아오기
    alert = driver.switch_to.alert
    # 경성포탈 alert 창은 2개가 뜨기 때문에 dismiss() 두 번
    alert.dismiss()
    alert.dismiss()
except:
    pass

# 학생 로그인 창 클릭
driver.find_element_by_xpath('//*[@id="tabImg1"]').click()

# 아이디 입력 .send_keys('아이디'), 문자열로 지정
driver.find_element_by_xpath('//*[@id="id"]').send_keys(id)

# 비밀번호 입력 .send_keys('비밀번호'), 문자열로 지정
driver.find_element_by_xpath('//*[@id="pw"]').send_keys(pwd)

# 로그인 버튼
driver.find_element_by_xpath('//*[@id="tabArea1Img"]').click()

# LMS 접속
driver.get('https://canvas.ks.ac.kr/')

# 통합 로그인
driver.find_element_by_xpath('//*[@id="integrated_login_link_area"]/div/a').click()