import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


class MysqlAdminer:

    @staticmethod
    def connect(
            host,
            username,
            password,
            database
    ):
        url = f"https://{host}/adminer/"

        session = requests.Session()
        session.get(url)  # load cookies

        resp = session.post(
            url,
            data={
                "auth[driver]": "server",
                "auth[server]": "",
                "auth[username]": username,
                "auth[password]": password,
                "auth[db]": database
            },
            allow_redirects=False
        )

        if resp.status_code != 302:
            raise Exception(f"Could not connect to database! code: {resp.status_code}")

        return MysqlAdminer(f"{url}?username={username}&db={database}", session)

    def __init__(self, url, session):
        self.url = url
        self.session: requests.Session = session

    def get_token(self):
        resp = self.session.post(
            self.url + "&sql="
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        return soup.find("input", {"name": "token"}).get("value")

    def query(self, sql) -> list:
        resp = self.session.post(
            f"{self.url}&sql={quote(sql)}",
            files={
                "query": (None, sql),
                "limit": (None, ""),
                "token": (None, self.get_token())
            },
            allow_redirects=False
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        p = soup.find("p", {"class": "error"})
        if p:
            raise Exception(p.getText())

        table = soup.select("#content .scrollable table")[0]

        array = []
        naming = []

        for th in table.select("thead tr th"):
            naming.append(th.get("title").split(".")[1])

        length = len(naming)

        tr = table.find("tr", recursive=False)

        i = 0
        obj = {}
        array.append(obj)

        # fucking hell
        for text in tr.find_all(recursive=True, text=True):

            if i >= length:
                i = 0
                obj = {}
                array.append(obj)

            obj[naming[i]] = text

            i += 1

        return array

    def close(self):
        return self.session.post(
            self.url + "&sql=",
            files={
                "logout": "Logout",
                "token": self.get_token()
            },
            allow_redirects=False
        ).status_code == 302

