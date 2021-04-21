# LORD USERBOT
FROM koala21/kampangbot:buster

#
# Baby
#
RUN git clone -b Love https://github.com/dewi-rbtk/Babybot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/dewi-rbtk/Babybot/Love/requirements.txt

CMD ["python3","-m","userbot"]
