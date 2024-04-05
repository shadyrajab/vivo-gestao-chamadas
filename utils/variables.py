import os

from dotenv import load_dotenv

load_dotenv()

CONSULTORES = {
    "CAIQUE": "61999273832",
    "GABRIEL JESUS": "61996527715",
    "LUCAS ANDRE": "61999197779",
    "LUCAS BRITO": "61998581582",
    "LUCAS ERICK": "61981128799",
    "LUCAS JESUS": "61998056355",
    "LUCIANA": "61999455221",
    "MARIANE": "61998171094",
    "ORLANDO": "61998174859",
    "PAMERA": "61998923424",
    "PEDRO HENRIQUE": "61999174422",
    "PEDRO LUCAS": "61999214045",
    "THATILA": "61998071389",
    "VICTOR GABRIEL": "61996969544",
}

LOGIN_URL = "https://vivogestao.vivoempresas.com.br/Portal/api/datapackcompanyinfo"
RELATORIO_URL = "https://vivogestao.vivoempresas.com.br/Portal/api/voicereports?action=getCallHistory&msisdn={telefone}&startDate={startDate}&endDate={endDate}&startRow=1&fetchSize=50&sessionId={sessionId}&remoteHost=gateway&remoteIp={remoteIp}&acessLogin=santosegomes"

PAYLOAD = {
    "action": "login",
    "user": os.getenv("user"),
    "password": os.getenv("password"),
}
