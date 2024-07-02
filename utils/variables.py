import os

from dotenv import load_dotenv

load_dotenv()


def convert_time(duration: float):
    minutes = int(duration)
    seconds = int((duration - minutes) * 60)
    return minutes, seconds


FREECEL = {
    "CAIQUE": "61999273832",
    "LUCAS ANDRE": "61999197779",
    "LUCAS ANDRE 2": "61998813220",
    "LUCAS BRITO": "61998581582",
    "LUCAS JESUS": "61998056355",
    "LUCIANA": "61999455221",
    "MARIANE": "61998171094",
    "ORLANDO": "61998174859",
    "PEDRO HENRIQUE": "61999174422",
    "VICTOR GABRIEL": "61996969544",
    "ELIAB": "61998854422",
    "DANIEL": "61996994786",
    "THALES": "61982010708",
    "RONALD": "61996941701",
    "PAULO WENDELL": "61998742182",
    "MATHEUS": "61996915979"
}

VALPARAISO = {
    "ANA CLARA": "61996184016",
    "DEIVID": "61982012100",
    "KAUAN": "61996683502",
    "LUCAS": "61999231754",
    "MATEUS": "61998623254",
    "NAIYARA": "61996882374",
    "VANESSA": "61996121748",
    "KAREN": "61999160935",
    "SDR 1": "61999077254",
    "SDR 2": "61998243834",
    "SDR 3": "61996174224",
}

SAMAMBAIA = {
    "RICARDO": "61998413910",
    "GUSTAVO": "61996865698",
    "ANA ALICE": "61999178648",
    "RUTH": "61999714455",
    "PAULO": "61981164007",
}

LOGIN_URL = (
    "https://vivogestao.vivoempresas.com.br/Portal/api/" +
    "datapackcompanyinfo"
)
RELATORIO_URL = (
    "https://vivogestao.vivoempresas.com.br/" +
    "Portal/api/voicereports?action=getCallHistory&msisdn={telefone}" +
    "&startDate={startDate}" +
    "&endDate={endDate}" +
    "&startRow=1&fetchSize=50" +
    "&sessionId={sessionId}" +
    "&remoteHost=gateway" +
    "&remoteIp={remoteIp}" +
    "&acessLogin=santosegomes"
)

PAYLOAD = {
    "action": "login",
    "user": os.getenv("user"),
    "password": os.getenv("password"),
}
