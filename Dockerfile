FROM python:3

WORKDIR /erptestjav

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "python", "/erptestjav/src/api_erp.py" ]