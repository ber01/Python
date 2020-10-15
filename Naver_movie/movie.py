from flask import Flask
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/test")
def test():
    return "Hello test"

@app.route("/reple")
def crawling():
    dic = {}
    for i in range(1, 2):

        URL = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=136900&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=" + str(
            i)

        ua = UserAgent()
        header = {'user-agent': ua.chrome}
        response = requests.get(URL, headers=header)

        content = response.content
        soup = BeautifulSoup(content, 'html.parser')

        for li in soup.find('div', attrs={'class': 'score_result'}).find_all('li'):
            a = li.em.text.strip()
            b = li.p.text.strip().replace("관람객", "").strip()

            dic[b] = a
    return dic

if __name__ == "__main__":
    app.run()