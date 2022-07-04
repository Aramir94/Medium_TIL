WORKDIR /
ADD requirements.txt /
RUN pip install -r requirements.txt

RUN apt install wget
RUN wget http://magnitude.plasticity.ai/word2vec/GoogleNews-vectors-negative300.magnitude

CMD [ "python", "./service.py" ]

