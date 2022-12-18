FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#RUN pip3 install git
#RUN pip3 install cython
#RUN git clone https://github.com/numpy/numpy.git
#RUN cd numpy
#RUN python3 setup.py install
#RUN git clone https://github.com/pandas-dev/pandas.git
#RUN cd pandas
#RUN python3 setup.py install pandas

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]