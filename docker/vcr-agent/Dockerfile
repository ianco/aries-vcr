FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.6.0

#RUN pip3 install --no-cache-dir -e "git+https://github.com/bcgov/aries-vcr.git#egg=subdir&subdirectory=server/message_families/issuer_registration"
RUN pip3 install --no-cache-dir -e "git+https://github.com/ianco/aries-vcr.git#egg=subdir&subdirectory=server/message_families/issuer_registration"

COPY ./debug-logger.cfg .
