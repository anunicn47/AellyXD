#==============×==============#
#      Created by: Aelly
#=========× AellyXD ×=========#

FROM AellyOfficial/AellyXD:buster

RUN git clone -b AellyXD https://github.com/AellyOfficial/AellyXD /home/aellyXD/ \
    && chmod 777 /home/AellyXD \
    && mkdir /home/AellyXD/bin/

COPY ./sample_config.env ./config.env* /home/AellyXD/

WORKDIR /home/AellyXD/

RUN pip install -r requirements.txt

CMD ["bash","start"]
