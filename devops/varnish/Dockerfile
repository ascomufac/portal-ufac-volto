# syntax=docker/dockerfile:1
FROM varnish:7.6

LABEL maintainer="AscomUfac <ascom@ufac.br>" \
      org.label-schema.name="portal-ufac-volto-varnish" \
      org.label-schema.description="ploneufac Varnish image." \
      org.label-schema.vendor="AscomUfac"

COPY etc/varnish.vcl /etc/varnish/default.vcl
