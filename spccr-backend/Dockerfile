FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "spccr", "/bin/bash", "-c"]

COPY . .

EXPOSE 5000

CMD ["conda", "run", "--no-capture-output", "-n", "spccr", "python", "app.py"]
