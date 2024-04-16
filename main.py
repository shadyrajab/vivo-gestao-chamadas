import threading
from datetime import datetime, time

import pandas as pd
import requests

from utils.variables import CONSULTORES, LOGIN_URL, PAYLOAD, RELATORIO_URL

date = datetime(2024, 4, 15)

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
    called_numbers = []
    call_to_any_consul_number = False
    if json["totalRecordCount"] > 0:
        for call in json["result"]:
            called_number = call["calledMsisdn"]
            if called_numbers in list(CONSULTORES.values()):
                called_numbers.append(called_number)
                call_to_any_consul_number = True

    result = {
        "CONSULTOR": consultor,
        "TELEFONE": telefone,
        "CHAMADAS": json["totalRecordCount"],
        "LIGOU PARA OUTRO CONSULTOR": call_to_any_consul_number,
        "QUEM RECEBEU A LIGAÇÃO": str(called_numbers)
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
