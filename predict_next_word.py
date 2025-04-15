# 1. Crée un dossier et déplace le fichier
mkdir predict-next-word
cd predict-next-word
mv /chemin/vers/predict_next_word.py .

# 2. Initialise Git
git init

# 3. Ajoute le script
git add predict_next_word.py
git commit -m "🧠 Ajout du script de prédiction de mot suivant avec LSTM"

# 4. Lien avec le dépôt distant
git remote add origin https://github.com/TON_UTILISATEUR/predict-next-word.git

# 5. Pousse le tout
git push -u origin master

