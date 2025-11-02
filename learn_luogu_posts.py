import requests
import ptext
import sqlite3

con = sqlite3.connect("graph.db")

for i in range(1001175, 1002000):
    try:
        req = requests.get(
            f"https://luogu.com.cn/discuss/{i}",
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
                "x-lentille-request": "content-only",
            },
            cookies={
                "_uid": "",
                "__client_id": "",
            },
        )
        data = req.json()["data"]
        # print(data)
        s = data["post"]["content"]
        ptext.text_input(con, s, 6000000, commit=False)
        for it in data["replies"]["result"]:
            it["content"]
            ptext.text_input(con, it["content"], 6000000, commit=False)
            ptext.text_input(con, s[-3:] + it["content"][0], 6000000, commit=False)
        con.commit()
        print(f"已严肃学习贴子 {i}！")
    except Exception as e:
        print(f"贴子 {i} 学习失败：{str(e)}")
