# Imagen base con soporte Windows
FROM mcr.microsoft.com/windows/servercore:ltsc2022

WORKDIR /app

COPY BINARIES/ ./BINARIES/
COPY RAWSCRIPT/ ./RAWSCRIPT/

EXPOSE 1024

CMD ["BINARIES\\ChatScript.exe"]
