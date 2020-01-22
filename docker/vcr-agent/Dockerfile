FROM bcgovimages/aries-cloudagent:py37-1.11-2_0.4.1

#FROM bcgovimages/von-image:py36-dev 

#RUN pip3 install aries-cloudagent

RUN pip3 install --no-cache-dir -e "git+https://github.com/ianco/indy-catalyst.git@test-issuer-bug#egg=subdir&subdirectory=server/message_families/issuer_registration"
COPY ./debug-logger.cfg .