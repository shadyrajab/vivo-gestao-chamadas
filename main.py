import threading
from datetime import datetime, time

import pandas as pd
import requests

from utils.variables import CONSULTORES, LOGIN_URL, PAYLOAD, RELATORIO_URL

date = datetime(2024, 4, 5)

start_date = int(datetime.combine(date, time.min).timestamp()) * 1000
end_date = int(datetime.combine(date, time.max).timestamp()) * 1000 - 1

RECORDS = []


def login_vivo_gestao(url: str, payload: dict):
    response = requests.post(url, json=payload)
    json = response.json()

    return json["sessionId"], json["remoteIp"]


def get_total_record_count(url: str, consultor: str, telefone: str):
    response = requests.get(url)
    json = response.json()
    result = {
        "CONSULTOR": consultor,
        "TELEFONE": telefone,
        "CHAMADAS": json["totalRecordCount"]
    }
    RECORDS.append(result)


session_id, remote_ip = login_vivo_gestao(LOGIN_URL, PAYLOAD)

threads = []
for consultor, telefone in CONSULTORES.items():
    url = RELATORIO_URL.format(
        telefone=telefone,
        startDate=start_date,
        endDate=end_date,
        sessionId=session_id,
        remoteIp=remote_ip,
    )
    thread = threading.Thread(
        target=get_total_record_count,
        args=(
            url,
            consultor,
            telefone,
        ),
    )
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()


dataframe = pd.DataFrame(RECORDS)
dataframe.to_excel(f"relatorio chamadas {date.strftime("%d-%m-%Y")}.xlsx")
