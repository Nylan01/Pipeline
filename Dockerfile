# Image de base : un serveur web Nginx déjà prêt (version légère "alpine")
FROM nginx:alpine

# On copie notre page dans le dossier que Nginx sert par défaut
# --chmod=644 : rend le fichier lisible par Nginx, quels que soient les droits sur le disque
COPY --chmod=644 site/index.html /usr/share/nginx/html/index.html

# Nginx écoute sur le port 80 dans le conteneur
EXPOSE 80
