# FROM bcgovimages/aries-cloudagent:py36-1.15-1_0.6.0
FROM bcgovimages/aries-cloudagent:py36-1.16-0_0.6.1

RUN pip3 install --no-cache-dir -e "git+https://github.com/bcgov/aries-vcr.git#egg=issuer-registration&subdirectory=server/message_families/issuer_registration"

COPY ./debug-logger.cfg .
