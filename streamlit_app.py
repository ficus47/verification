import socket
import time


import imageio
import numpy as np
from PIL import ImageGrab


def enregistrer_video(duree_secondes, nom_fichier):
  # Définir les paramètres d'enregistrement
  fps = 20  # Images par seconde
  codec = 'libx264'  # Codec vidéo
  format_video = 'mp4'  # Format de sortie

  # Ouvrir un enregistreur vidéo
  with imageio.get_writer(nom_fichier, format=".mp4", fps=fps,
                          codec=codec) as writer:

    # Démarrer le chronomètre
    debut = time.time()

    # Capturer et enregistrer des frames pendant la durée spécifiée
    while time.time() - debut < duree_secondes:
      # Capturer une frame
      frame = ImageGrab.grab()

      # Enregistrer la frame
      writer.append_data(np.array(frame))

  print(f"Vidéo enregistrée sous : {nom_fichier}")


# Exécuter la fonction
enregistrer_video(duree_secondes=5, nom_fichier="video.mp4")
def send(a):
  video = open(a, 'rb').read()
  sock = socket.socket()
  sock.connect(('172.17.0.1', 8080))
  sock.send(video)
  response = sock.recv(8192)
  return response.decode()

x = send("video.mp4")
x = int(x)if x.isdigit()else 0

if x > 0:
  st.write("ok")
