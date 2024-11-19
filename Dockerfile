# Verison du python avec laquelle je travaille
FROM python:3.13.0

# Les deux lignes ci-dessous ajoutent un groupe d'utilisateurs, un utilisateur avec le nom user
# répertoire personnel sous le répertoire /home/user
RUN useradd -ms /bin /bash user
USER user

# pour ne pas avoir à spécifier le répertoire personnel de travail à chaque commande (par défaut /):
WORKDIR /home/user

# On copie ce qu'il y a dans requirements.txt dans le Dockerfile :
COPY requirements.txt .

# On fait appel à pip pour faire les installations
RUN pip install -r requirements.txt && rm requirements.txt

# On copie le code source
COPY src .

# Pour démarrer l'application
ENTRYPOINT ["python", "app.py"]