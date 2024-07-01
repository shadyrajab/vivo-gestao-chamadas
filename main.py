import threading
from datetime import datetime, time

import pandas as pd
import requests

from utils.variables import (FREECEL, LOGIN_URL, PAYLOAD, RELATORIO_URL,
                             VALPARAISO)

date = datetime.now()

start_date = int(datetime.combine(date, time.min).timestamp()) * 1000
end_date = int(datetime.combine(date, time.max).timestamp()) * 1000 - 1


def login_vivo_gestao(url: str, payload: dict):
    response = requests.post(url, json=payload)
    json = response.json()

    return json["sessionId"], json["remoteIp"]


def get_total_record_count(
        url: str,
        consultor: str,
        telefone: str,
        RECORDS: list):
    response = requests.get(url)
    json = response.json()
    result = {
        "CONSULTOR": consultor,
        "TELEFONE": telefone,
        "CHAMADAS": json["totalRecordCount"],
    }
    RECORDS.append(result)


def get_threads(consultores: dict):
    RECORDS = []
    threads = []
    for consultor, telefone in consultores.items():
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
                RECORDS
            ),
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return pd.DataFrame(RECORDS)


session_id, remote_ip = login_vivo_gestao(LOGIN_URL, PAYLOAD)

get_threads(FREECEL).to_excel(
    f"relatorio chamadas {date.strftime("%d-%m-%Y")}.xlsx",
    index=False)

get_threads(VALPARAISO).to_excel(
    f"relatorio chamadas {date.strftime("%d-%m-%Y")} valparaiso.xlsx",
    index=False)
