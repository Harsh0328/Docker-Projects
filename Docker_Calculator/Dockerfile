FROM python

COPY requirements.txt .
COPY calculatorapp.py .
RUN mkdir templates
COPY templates/form.html templates/.
RUN pip3 install -r requirements.txt

CMD ["python", "calculatorapp.py"]
