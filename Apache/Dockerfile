FROM httpd:2.4
COPY index.html /usr/local/apache2/htdocs/
RUN chmod 777 /usr/local/apache2/htdocs/index.html
EXPOSE 9999
COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf
ENV container=docker
ENTRYPOINT echo $container
