# Despliegue de FastAPI en AWS EC2

Este README explica cómo desplegar y probar una aplicación FastAPI en una instancia EC2 de AWS.

---

## 1. Preparar la instancia EC2
1. Lanza una instancia Ubuntu en AWS EC2.  
2. Conéctate vía SSH:
```bash
chmod 400 finalSO_punto_2.pem
ssh -i finalSO_punto_2.pem ubuntu@<EC2_PUBLIC_IP>
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn boto3
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

