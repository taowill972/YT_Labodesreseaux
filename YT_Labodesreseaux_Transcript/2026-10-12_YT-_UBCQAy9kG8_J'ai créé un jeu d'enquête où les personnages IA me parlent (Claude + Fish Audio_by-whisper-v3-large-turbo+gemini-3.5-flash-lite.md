# 🎬 J'ai créé un jeu d'enquête où les personnages IA me parlent (Claude + Fish Audio)

> **Chaîne** : [Labo Des Réseaux](https://www.youtube.com/@labodesreseaux)  
> **Lien YouTube** : [https://www.youtube.com/watch?v=_UBCQAy9kG8](https://www.youtube.com/watch?v=_UBCQAy9kG8)  
> **Date de publication** : 20261012  
> **Durée** : 11:59  
> **Identifiant vidéo** : `_UBCQAy9kG8`  
> **Modèles** : Audio: `whisper-v3-large-turbo` | Vision: `gemini-3.5-flash-lite`  

---

## 📌 Synthèse Exécutive & Outils

### 💡 Résumé
**Dans cette vidéo, le créateur de la chaîne Labo Des Réseaux présente la conception complète et le test d'un jeu d'enquête textuel et interactif inspiré des jeux point-and-click des années 90, baptisé « Les Mystères du Manoir Van Bergen ».** Le projet repose sur l'association de l'intelligence artificielle générative textuelle (Claude / Anthropic) pour le code et le scénario, de modèles d'images pour les assets graphiques, et d'une technologie avancée de synthèse vocale (Fish Audio) afin de donner vie aux suspects.

**Le tutoriel démontre comment un développeur ou un passionné peut orchestrer rapidement des API puissantes pour créer une expérience narrative immersive en local.** Grâce à l'utilisation conjointe de Claude Code pour le développement rapide de l'application et de l'API de Fish Audio (notamment le modèle S2.1 Pro, gratuit en accès API jusqu'en novembre 2026), chaque personnage du jeu dispose d'une voix sur mesure, d'une personnalité propre et d'une capacité à répondre dynamiquement en temps réel aux questions formulées par le joueur.

**Le créateur conclut sur la force de l'immersion vocale dans le jeu vidéo narratif, prouvant qu'il est possible de bâtir un prototype de jeu complexe en un temps record sans compétences avancées en programmation traditionnelle.** Bien que ce projet demeure une expérimentation non commercialisable en l'état, il illustre concrètement le potentiel des agents conversationnels vocaux et des outils de synthèse audio pour réinventer les interactions dans le divertissement numérique et les applications SaaS interactives.

### 🛠️ Outils, Modèles & Logiciels Présentés
- **Claude / Claude Code / Claude Opus 5.5** (Anthropic) : Assistant de développement et de génération de code en local, gestion du « cerveau » et de la logique conversationnelle des personnages.**
- **Fish Audio / Fish Audio S2.1 Pro** : Plateforme de synthèse vocale par IA, utilisée via son API pour générer les voix des personnages, les échantillons audio, et intégrer des balises de contrôle des émotions.**
- **GPT Image 2.5 / ChatGPT** : Outils de génération d'images et d'assets graphiques pour concevoir les décors et l'ambiance visuelle du jeu.**
- **Navigateur web & Environnement local (localhost)** : Plateforme d'exécution et de test du jeu stocké directement sur le bureau du créateur.**

### 🔑 Points Clés & Enseignements Stratégiques
- Concept du jeu** : Un jeu d'enquête de 40 minutes dans un manoir où le joueur incarne un inspecteur interrogeant librement des suspects dont le coupable est généré aléatoirement à chaque partie.
- Architecture technique hybride** : Association d'un modèle de langage lourd (Claude Opus) pour la logique conversationnelle et d'une API Text-to-Speech ultra-rapide (Fish Audio) pour l'oralisation.
- Avantage de l'API Fish Audio** : Le modèle S2.1 Pro est accessible gratuitement en API jusqu'à fin novembre 2026, permettant de tester et d'intégrer des voix réalistes sans frais.
- Gestion des émotions vocales** : Injection de documentation et de guides de balises audio spécifiques à l'IA vocale pour que les personnages adaptent le ton de leur voix (colère, ironie, neutralité) en fonction des propos du joueur.
- Workflow de développement assisté** : Utilisation d'un prompt long structuré pour guider Claude Code dans la création de l'architecture locale et du stockage des fichiers du jeu sur le bureau.
- Génération automatisée des assets** : Demande à Claude de rédiger un fichier de prompts visuels (style point-and-click des années 90) directement injecté dans ChatGPT pour obtenir un pack graphique cohérent au format zip.
- Personnalisation et choix des voix** : Génération d'échantillons audio directement dans le dossier du projet via l'API Fish Audio pour écouter et valider le timbre de chaque personnage avant le lancement de la partie.
- Sécurité des clés API** : Rppel indispensable de la suppression immédiate des clés API exposées lors de l'enregistrement pour éviter les utilisations malveillantes.
- Immersion narrative renforcée** : Le fait d'entendre les suspects répondre oralement du tac au tac crée une dynamique de rejouabilité et d'enquête psychologique bien supérieure à un simple chat textuel.
- Pistes d'amélioration du projet** : Possibilité d'étendre le concept à des enquêtes multi-actes, d'intégrer un inventaire d'objets cliquables et d'ajouter des animations graphiques plus poussées.

---

## ⏱️ Chronologie & Transcription Complète Audio & Visuelle (Mot pour Mot)

### ⏱️ `[00:00:01 - 00:00:20]` | Segment #01

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Allez, cette fois-ci, je vais me diriger vers le salon. On va aller questionner la comtesse. Et on va tenter un truc. Vous avez une belle tête de coupable. On va voir comment elle va réagir. Oula ! Je vous demande pardon ?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Jeu d'enquête textuel et visuel sur navigateur ou application.
**Contenu textuel & Code** : Dialogue entre le détective et la Comtesse Irène de Saint-Aymar, avec des options de questions proposées en bas.
**Action / Démonstration** : Le créateur navigue dans le manoir puis interroge la comtesse en lui posant des questions et des provocations.

**Captures d'écran :**
- ![Vue d'ensemble de la bibliothèque du manoir dans le jeu d'enquête, montrant le plan et les personnages présents.](../screenshots/_UBCQAy9kG8/frame_01_000002.jpg)  
  *⏱️ 00:00:02 — Vue d'ensemble de la bibliothèque du manoir dans le jeu d'enquête, montrant le plan et les personnages présents.*
- ![Interface d'interrogatoire avec la Comtesse Irène de Saint-Aymar, affichant les dialogues et les options de questions.](../screenshots/_UBCQAy9kG8/frame_01_000010.jpg)  
  *⏱️ 00:00:10 — Interface d'interrogatoire avec la Comtesse Irène de Saint-Aymar, affichant les dialogues et les options de questions.*
- ![Suite de l'interrogatoire où le joueur formule une remarque provocquante à la comtesse.](../screenshots/_UBCQAy9kG8/frame_01_000018.jpg)  
  *⏱️ 00:00:18 — Suite de l'interrogatoire où le joueur formule une remarque provocquante à la comtesse.*

---

### ⏱️ `[00:00:20 - 00:00:39]` | Segment #02

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Surveillez votre langage, mon brave. Vous ne parlez pas à une fille de cuisine. Une tête de coupable ? Voilà donc les méthodes de la police judiciaire. Le préfet dîne chez les Rochoirs jeudi. et je doute qu'il goûte votre sens de la physionomie. Oula, le préfet, je vais me retrouver dans la sauce. Je rigolais, je rigolais.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation orale ou séquence sans interface partagée.
**Contenu textuel & Code** : Explications et conseils de création de contenu / IA.
**Action / Démonstration** : Démonstration et mise en contexte pratique.

---

### ⏱️ `[00:00:40 - 00:00:59]` | Segment #03

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Bon, je ne suis pas en train de lancer une carrière de streamer. Je teste simplement le jeu que j'ai créé avec Claude et Fichodio. Sur le papier, ça ressemble à un jeu d'enquête classique. Plusieurs suspects, je dois trouver le coupable en les interrogeant. Sauf qu'il y a une particularité. Tous les personnages me répondent à l'oral en temps réel en fonction des questions que je leur pose.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Jeu d'enquête personnalisé développé avec Claude et Fichodio, interface graphique de type point-and-click.
**Contenu textuel & Code** : Noms des personnages (Colette Marchand, la comtesse, etc.), interface d'interrogatoire, bulles de dialogue, horloge du jeu, carte des pièces du manoir.
**Action / Démonstration** : Le créateur teste et présente son jeu d'enquête interactif avec des personnages dotés de réponses vocales en temps réel.

**Captures d'écran :**
- ![Interface principale du jeu d'enquête montrant un salon luxueux avec les différents suspects et le personnage du joueur.](../screenshots/_UBCQAy9kG8/frame_03_000041.jpg)  
  *⏱️ 00:00:41 — Interface principale du jeu d'enquête montrant un salon luxueux avec les différents suspects et le personnage du joueur.*
- ![Interface d'interrogatoire en gros plan avec un suspect (Colette Marchand) et des options de dialogue textuelles/vocales.](../screenshots/_UBCQAy9kG8/frame_03_000057.jpg)  
  *⏱️ 00:00:57 — Interface d'interrogatoire en gros plan avec un suspect (Colette Marchand) et des options de dialogue textuelles/vocales.*

---

### ⏱️ `[00:00:59 - 00:01:20]` | Segment #04

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pourquoi ce geste ? Vous et la baronne avez eu une liaison, je ne comprends pas bien le geste. Une liaison ? Et madame ? On ne me l'avait jamais faite, mon chou ! Dans cette vidéo, je vais te présenter le projet et t'expliquer comment j'ai donné une voix et un cerveau au personnage de mon jeu.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface utilisateur de jeu vidéo narratif textuel et illustré.
**Contenu textuel & Code** : Texte du dialogue d'interrogatoire avec Colette Marchand, options de questions et illustrations des personnages de profil.
**Action / Démonstration** : Le créateur présente le prototype de son jeu vidéo et fait écouter/lire les dialogues interactifs générés.

**Captures d'écran :**
- ![Interface du jeu montrant un dialogue d'interrogatoire avec le personnage Colette Marchand, l'inspecteur et le youtubeur en incrustation vidéo.](../screenshots/_UBCQAy9kG8/frame_04_000100.jpg)  
  *⏱️ 00:01:00 — Interface du jeu montrant un dialogue d'interrogatoire avec le personnage Colette Marchand, l'inspecteur et le youtubeur en incrustation vidéo.*
- ![Suite de l'interrogatoire textuel et vocal dans le jeu avec la réponse de Colette Marchand à la question sur la liaison.](../screenshots/_UBCQAy9kG8/frame_04_000109.jpg)  
  *⏱️ 00:01:09 — Suite de l'interrogatoire textuel et vocal dans le jeu avec la réponse de Colette Marchand à la question sur la liaison.*

---

### ⏱️ `[00:01:20 - 00:01:42]` | Segment #05

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pour ce projet, j'ai utilisé trois outils. Cloud Code pour le développement, avec aussi l'API de Claude, on y reviendra. GPT Image 2.5 pour les assets graphiques du jeu et Fiches Audio qui sponsorisent cette vidéo. C'est d'ailleurs l'élément clé du projet parce que c'est grâce à l'API de Fiche Audio que tous mes personnages vont prendre vie. Fiche Audio, c'est une plateforme de synthèse vocale avec beaucoup de fonctionnalités.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de Fish Audio et infographie graphique de présentation.
**Contenu textuel & Code** : Textes descriptifs des outils (Claude Code, GPT Image 2.5, Fish Audio) et menu principal du tableau de bord Fish Audio.
**Action / Démonstration** : Présentation des trois outils clés utilisés pour le développement du projet de jeu vidéo.

**Captures d'écran :**
- ![Infographie présentant les trois outils utilisés pour le projet : Claude Code, GPT Image 2.5 et Fish Audio (sponsor).](../screenshots/_UBCQAy9kG8/frame_05_000131.jpg)  
  *⏱️ 00:01:31 — Infographie présentant les trois outils utilisés pour le projet : Claude Code, GPT Image 2.5 et Fish Audio (sponsor).*
- ![Capture d'écran du tableau de bord de l'interface Fish Audio montrant les options de création audio, texte en parole et clonage de voix.](../screenshots/_UBCQAy9kG8/frame_05_000140.jpg)  
  *⏱️ 00:01:40 — Capture d'écran du tableau de bord de l'interface Fish Audio montrant les options de création audio, texte en parole et clonage de voix.*

---

### ⏱️ `[00:01:42 - 00:02:04]` | Segment #06

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Génération de voix IA avec une large bibliothèque, création de voix sur mesure, changement de voix, création d'effets sonores, séparation de voix. Il y a même un accès à des modèles IA de génération d'images et vidéos, la possibilité de créer des agents vocaux. Bref, un outil très complet. Ce qui nous intéresse aujourd'hui, c'est la partie développeur. utiliser Fiche Audio en API pour donc donner une voix à nos personnages.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Fish Audio (application web SaaS)
**Contenu textuel & Code** : Menus de navigation (Créatif, Développeur, Agents, Synthèse vocale, Image et vidéo), champs de texte, réglages audio, graphiques de statistiques d'utilisation API.
**Action / Démonstration** : Le présentateur navigue à travers les différentes fonctionnalités de la plateforme Fish Audio, de la génération vocale au tableau de bord développeur.

**Captures d'écran :**
- ![Interface de synthèse vocale de Fish Audio montrant un champ de texte avec des balises d'émotion et les paramètres audio.](../screenshots/_UBCQAy9kG8/frame_06_000143.jpg)  
  *⏱️ 00:01:43 — Interface de synthèse vocale de Fish Audio montrant un champ de texte avec des balises d'émotion et les paramètres audio.*
- ![Section 'Image et vidéo' de l'application Fish Audio affichant des avatars générés par IA et des outils de création visuelle.](../screenshots/_UBCQAy9kG8/frame_06_000153.jpg)  
  *⏱️ 00:01:53 — Section 'Image et vidéo' de l'application Fish Audio affichant des avatars générés par IA et des outils de création visuelle.*
- ![Tableau de bord développeur de Fish Audio affichant les statistiques d'utilisation, les clés API et le solde de crédits.](../screenshots/_UBCQAy9kG8/frame_06_000202.jpg)  
  *⏱️ 00:02:02 — Tableau de bord développeur de Fish Audio affichant les statistiques d'utilisation, les clés API et le solde de crédits.*

---

### ⏱️ `[00:02:04 - 00:02:24]` | Segment #07

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et bonne nouvelle, le modèle Fiche Audio S21 Pro est entièrement gratuit en accès en API jusqu'à la fin novembre 2026. Pour mon projet, il m'a suffi de créer un compte gratuitement sur Fiche Audio, d'aller dans l'espace développeur et de créer une clé API. J'ai obtenu toutes les voix de mon jeu sans dépenser un seul centime. Si comme moi tu veux en profiter, le lien est en description et commentaire épinglé.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant le site officiel et l'espace développeur de Fish Audio (Fish Audio S21 Pro).
**Contenu textuel & Code** : Pages web décrivant la gratuité de l'API de synthèse vocale S21 Pro et fenêtre contextuelle de génération de clé API.
**Action / Démonstration** : Le créateur montre la page d'annonce officielle puis l'interface de création d'une clé API sur la plateforme Fish Audio.

**Captures d'écran :**
- ![Capture d'écran du site web de Fish Audio présentant l'annonce de l'API gratuite S21 Pro pour les développeurs, avec le présentateur en bas à droite.](../screenshots/_UBCQAy9kG8/frame_07_000205.jpg)  
  *⏱️ 00:02:05 — Capture d'écran du site web de Fish Audio présentant l'annonce de l'API gratuite S21 Pro pour les développeurs, avec le présentateur en bas à droite.*
- ![Interface du tableau de bord développeur de Fish Audio affichant une fenêtre modale pour créer une clé API avec le nom 'api key', signalée par une grande flèche rose.](../screenshots/_UBCQAy9kG8/frame_07_000223.jpg)  
  *⏱️ 00:02:23 — Interface du tableau de bord développeur de Fish Audio affichant une fenêtre modale pour créer une clé API avec le nom 'api key', signalée par une grande flèche rose.*

---

### ⏱️ `[00:02:24 - 00:02:43]` | Segment #08

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> L'idée de mon jeu est la suivante. Tu incarnes un inspecteur de police qui enquête sur un meurtre qui vient d'avoir lieu dans un manoir, celui de la baronne Van Bergen. Le but, interroger tous les suspects encore sur place pour trouver le coupable. Et pour ça, il faut donner à chaque personnage la capacité de nous répondre.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Vidéo explicative animée (motion design sur fond uni).
**Contenu textuel & Code** : Texte 'L'idée du jeu', icônes d'enquête, de meurtre, de manoir et de dialogue.
**Action / Démonstration** : Le créateur présente le concept de son jeu d'enquête policière en voix off face caméra avec des illustrations graphiques.

---

### ⏱️ `[00:02:43 - 00:03:07]` | Segment #09

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et pour qu'un personnage puisse nous répondre, il lui faut deux choses, un cerveau et une voix. Le cerveau, ça sera Claude Opus 5.5 via API, et la voix, ça sera l'API de fiche audio. Ensuite, chaque personnage a sa personnalité, son histoire, ses relations avec les autres personnages. Le gameplay est plutôt simple, on se balade dans le manoir pour interroger chaque personnage, on pose les questions qu'on veut sans aucune limite, et le personnage nous répond en temps réel.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Graphismes animés et schémas explicatifs intégrés à la vidéo YouTube de 'Labo Des Réseaux'.
**Contenu textuel & Code** : Textes illustrant le concept : 'Le gameplay simple', 'Où étiez-vous hier soir ?', et une forme d'onde audio.
**Action / Démonstration** : Le créateur explique le fonctionnement du jeu, les interactions possibles avec les personnages et la liberté des questions posées aux PNJ.

**Captures d'écran :**
- ![Schéma explicatif du gameplay montrant une grille représentant les salles du manoir et un exemple de dialogue avec transcription audio.](../screenshots/_UBCQAy9kG8/frame_09_000306.jpg)  
  *⏱️ 00:03:06 — Schéma explicatif du gameplay montrant une grille représentant les salles du manoir et un exemple de dialogue avec transcription audio.*

---

### ⏱️ `[00:03:08 - 00:03:31]` | Segment #10

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> A chaque début de partie, un coupable est désigné de façon aléatoire, donc impossible de savoir à l'avance qui c'est. Le coupable va chercher à nous mentir, ce sera donc nos compétences d'inspecteur et notre capacité à poser les bonnes questions qui vont nous permettre de l'identifier en recoupant les témoignages. On a 40 minutes pour poser autant de questions qu'on veut, et dès qu'on a une idée du coupable, on appelle le commissaire pour lui donner le nom du suspect.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Vidéo YouTube avec incrustations graphiques minimalistes et animations de type motion design.
**Contenu textuel & Code** : Graphismes explicatifs illustrant la désignation aléatoire d'un coupable, des mensonges et un chronomètre d'enquête.
**Action / Démonstration** : Le créateur présente les mécaniques du jeu d'enquête en utilisant des infographies animées.

---

### ⏱️ `[00:03:32 - 00:03:52]` | Segment #11

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Deux essais possibles, on a gagné, on reçoit une médaille, on s'est trompé, on est viré. J'ai déjà élaboré mon prompt pour guider Claude Code dans la réalisation du jeu. Il est plutôt long, donc je ne vais pas le détailler ici, mais si tu veux le récupérer, je mets le lien en description. Je précise, j'ai demandé à Claude de créer le jeu en local, donc tous les fichiers sont créés et stockés dans un même dossier sur mon bureau.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de l'application Claude et explorateur de fichiers macOS.
**Contenu textuel & Code** : Texte du prompt décrivant le cadre du jeu (manoir des années 1920, meurtre de la baronne Van Bergen) et arborescence de fichiers du projet.
**Action / Démonstration** : Le créateur montre le prompt utilisé pour guider l'IA dans le développement du jeu d'enquête et l'arborescence des dossiers générés.

**Captures d'écran :**
- ![Affichage du prompt détaillé pour la création du jeu d'enquête avec Claude Code et l'API Fish Audio.](../screenshots/_UBCQAy9kG8/frame_11_000342.jpg)  
  *⏱️ 00:03:42 — Affichage du prompt détaillé pour la création du jeu d'enquête avec Claude Code et l'API Fish Audio.*
- ![Superposition d'une fenêtre de gestionnaire de fichiers macOS montrant l'arborescence du projet créé (dossiers docs, assets, data, server, etc.).](../screenshots/_UBCQAy9kG8/frame_11_000351.jpg)  
  *⏱️ 00:03:51 — Superposition d'une fenêtre de gestionnaire de fichiers macOS montrant l'arborescence du projet créé (dossiers docs, assets, data, server, etc.).*

---

### ⏱️ `[00:03:52 - 00:04:16]` | Segment #12

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Pour que le jeu soit beau, j'ai également demandé à Claude de me préparer des prompts pour mes assailles. Et côté style et gameplay, je voulais quelque chose inspiré des point and click des années 90, style les chevaliers de Baphomet. C'est joli et ça a l'avantage d'être léger en animation et en affichage. J'ai précisé à Claude que les prompts étaient destinés à GPT-Image 2.5 et tu vois, il m'a préparé un fichier avec tous les prompts directement dans le dossier du jeu.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de l'assistant IA Claude / application de développement (Game Fish API) et affichage du jeu en cours de test.
**Contenu textuel & Code** : Texte de prompt demandant des styles graphiques rétro inspirés des jeux d'aventure classiques, et aperçu visuel des dialogues entre personnages avec décors dessinés.
**Action / Démonstration** : Le créateur montre le résultat visuel obtenu grâce à Claude pour son jeu de type point-and-click.

**Captures d'écran :**
- ![Interface de Claude montrant les instructions pour générer des prompts d'images de style point-and-click des années 90, avec un aperçu du jeu vidéo inspiré des Chevaliers de Baphomet.](../screenshots/_UBCQAy9kG8/frame_12_000404.jpg)  
  *⏱️ 00:04:04 — Interface de Claude montrant les instructions pour générer des prompts d'images de style point-and-click des années 90, avec un aperçu du jeu vidéo inspiré des Chevaliers de Baphomet.*

---

### ⏱️ `[00:04:16 - 00:04:36]` | Segment #13

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> je n'ai eu qu'à donner ce fichier à ChatGPT pour qu'il me crée tous les assets. Et pendant que ChatGPT me générait mes assets, j'ai demandé à Claude de commencer à me coder le jeu. Après quelques minutes de travail, j'ai eu une première version. Ce n'est pas mal, même si pour l'instant rien ne fonctionne vraiment, parce que je n'ai pas encore donné accès aux API qui alimentent les conversations avec les personnages.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Explorateur de fichiers, Interface de l'assistant IA (Claude/ChatGPT), Navigateur web (localhost:3000)
[DESC_IMAGE_1] Fichiers : ASSETS.md, GDD.md, PROMPTS.md.
[DESC_IMAGE_2] Titre « Meurtre au Manoir Van Bergen », code source, console de génération.
[DESC_IMAGE_3] « Carnet d'enquête », « Faits établis par la police », description de l'affaire et personnages.
**Contenu textuel & Code** : Explications et conseils de création de contenu / IA.
**Action / Démonstration** : Le créateur montre l'arborescence des fichiers du projet, puis l'avancement du code généré par l'IA et le test de l'interface du jeu d'enquête dans le navigateur.

**Captures d'écran :**
- ![Explorateur de fichiers montrant les différents dossiers et assets générés pour le projet (ASSETS.md, GDD.md, PROMPTS.md).](../screenshots/_UBCQAy9kG8/frame_13_000417.jpg)  
  *⏱️ 00:04:17 — Explorateur de fichiers montrant les différents dossiers et assets générés pour le projet (ASSETS.md, GDD.md, PROMPTS.md).*
- ![Interface de l'assistant de code IA montrant les interactions en cours avec le projet « Meurtre au Manoir Van Bergen » et le rendu dans le navigateur.](../screenshots/_UBCQAy9kG8/frame_13_000426.jpg)  
  *⏱️ 00:04:26 — Interface de l'assistant de code IA montrant les interactions en cours avec le projet « Meurtre au Manoir Van Bergen » et le rendu dans le navigateur.*
- ![Aperçu de l'interface du jeu dans le navigateur affichant le carnet d'enquête avec les faits établis par la police.](../screenshots/_UBCQAy9kG8/frame_13_000435.jpg)  
  *⏱️ 00:04:35 — Aperçu de l'interface du jeu dans le navigateur affichant le carnet d'enquête avec les faits établis par la police.*

---

### ⏱️ `[00:04:36 - 00:04:56]` | Segment #14

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mais côté gameplay, on a déjà une bonne première impression. Entre temps, ChatGPT a fini par créer tous mes assets. Le style est très sympa, je suis plutôt content du résultat. ChatGPT m'a préparé un zip avec l'ensemble des assets. Je donne simplement ce zip à Claude pour qu'il intègre les assets dans le dossier du jeu et qu'il attribue chaque asset à l'élément correspondant.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web (localhost), interface de l'assistant IA (Codex / ChatGPT) et environnement de développement.
**Contenu textuel & Code** : Interface de jeu "Meurtre au Manoir", liste des 56 assets générés (images de personnages, décors) et modification de fichiers JSON.
**Action / Démonstration** : Le créateur montre le résultat du jeu en cours d'exécution, la liste des assets générés par l'IA et l'intégration du fichier ZIP dans le projet.

**Captures d'écran :**
- ![Aperçu du jeu en cours de test sur un navigateur web local (localhost:3000) montrant une interface de sélection des suspects.](../screenshots/_UBCQAy9kG8/frame_14_000437.jpg)  
  *⏱️ 00:04:37 — Aperçu du jeu en cours de test sur un navigateur web local (localhost:3000) montrant une interface de sélection des suspects.*
- ![Interface de l'outil de génération d'IA montrant la création et le regroupement des 56 designs demandés dans une archive ZIP.](../screenshots/_UBCQAy9kG8/frame_14_000446.jpg)  
  *⏱️ 00:04:46 — Interface de l'outil de génération d'IA montrant la création et le regroupement des 56 designs demandés dans une archive ZIP.*
- ![Interface de développement montrant le transfert et l'intégration du fichier ZIP contenant les assets graphiques dans le projet du jeu.](../screenshots/_UBCQAy9kG8/frame_14_000454.jpg)  
  *⏱️ 00:04:54 — Interface de développement montrant le transfert et l'intégration du fichier ZIP contenant les assets graphiques dans le projet du jeu.*

---

### ⏱️ `[00:04:56 - 00:05:15]` | Segment #15

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> J'ai maintenant mon gameplay, mes assets, et il ne me reste plus qu'à donner vie à mes personnages. Pour ça, je donne à Claude Code un accès à l'API d'Opus 5.5. Très facile, il te suffit de créer une clé API depuis ton compte Claude Platform. A noter, tu auras aussi besoin de créditer un peu ton compte pour que cette clé API fonctionne.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Claude Console (plateforme Anthropic), navigateurs web.
**Contenu textuel & Code** : Fenêtre pop-up "Créer une clé API", champs de nom ("marko-api-key", "game-marko"), options d'expiration et URL "platform.claude.com".
**Action / Démonstration** : Le créateur montre comment générer une clé API sur la plateforme Claude pour connecter l'outil.

**Captures d'écran :**
- ![Interface de Claude Console montrant une fenêtre modale pour créer une clé API avec les champs de nom et de configuration.](../screenshots/_UBCQAy9kG8/frame_15_000506.jpg)  
  *⏱️ 00:05:06 — Interface de Claude Console montrant une fenêtre modale pour créer une clé API avec les champs de nom et de configuration.*
- ![Interface de Claude Console avec la fenêtre de création de clé API, comportant l'URL platform.claude.com affichée en surimpression.](../screenshots/_UBCQAy9kG8/frame_15_000514.jpg)  
  *⏱️ 00:05:14 — Interface de Claude Console avec la fenêtre de création de clé API, comportant l'URL platform.claude.com affichée en surimpression.*

---

### ⏱️ `[00:05:15 - 00:05:34]` | Segment #16

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Moi j'ai mis 20$, ça devrait me suffire. Et pour donner une voix à mes personnages, cette fois-ci je vais utiliser l'API de Fiche Audio. Comme je te le disais, le modèle Fiche Audio S1.pro est gratuit en API jusqu'à fin novembre 2026. Tu te connectes à ton compte Fiche Audio, tu vas dans l'onglet développeur et tu crées une nouvelle clé API.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Site web Fish Audio, interface développeur et tableau de bord de gestion des clés API.
[DESC_IMAGE_1] Article de blog intitulé 'Fish Audio S2.1 Pro: Free Text-to-Speech API for Developers' avec le présentateur en bas à droite.
[DESC_IMAGE_2] Menu latéral pointant vers l'onglet 'Développeur' et la page 'Clés API' avec une flèche rouge explicative.
**Contenu textuel & Code** : Explications et conseils de création de contenu / IA.
**Action / Démonstration** : Le créateur montre la page de présentation du modèle gratuit Fish Audio S2.1 Pro puis navigue vers l'onglet développeur pour expliquer comment créer une clé API.

**Captures d'écran :**
- ![Le site web de Fish Audio présentant l'API gratuite S2.1 Pro pour les développeurs.](../screenshots/_UBCQAy9kG8/frame_16_000525.jpg)  
  *⏱️ 00:05:25 — Le site web de Fish Audio présentant l'API gratuite S2.1 Pro pour les développeurs.*
- ![Le tableau de bord du compte Fish Audio montrant l'onglet développeur et la section des clés API.](../screenshots/_UBCQAy9kG8/frame_16_000532.jpg)  
  *⏱️ 00:05:32 — Le tableau de bord du compte Fish Audio montrant l'onglet développeur et la section des clés API.*

---

### ⏱️ `[00:05:34 - 00:06:13]` | Segment #17

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le lien pour créer gratuitement ton compte Fiche Audio est en description et commentaire. Je donne ensuite directement cette clé API à Claude. Petite précision si tu t'inquiètes pour moi, toutes les clés API utilisées dans cette vidéo ont été supprimées depuis. Donc si tu envoies une s'afficher à l'écran, elle ne fonctionne plus au moment où tu regardes cette vidéo. En plus de la clé API fiche audio, j'ai donné de la documentation à Claude, notamment le guide édité par fiche audio sur le contrôle des émotions dans la voix et les tags audio. Ça va lui permettre de bien utiliser utiliser les tags avec mes personnages pour qu'ils répondent avec le ton adapté. Voilà j'ai tout ce qu'il me faut alors j'ai ouvert une première version du jeu pour faire quelques corrections.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de gestion de clés API avec fenêtre modale.
**Contenu textuel & Code** : Fenêtre modale "Créer une clé API", champs "Nom de la clé", options d'expiration ("Jamais", "7 jours", "30 jours", "90 jours"), et flèche rouge pointant vers le bas.
**Action / Démonstration** : Le créateur montre le tableau de bord et la fenêtre modale permettant de configurer et générer une nouvelle clé API.

**Captures d'écran :**
- ![Interface de création d'une clé API avec une modale affichant les options de nommage et d'expiration, le créateur apparaissant en incrustation.](../screenshots/_UBCQAy9kG8/frame_17_000535.jpg)  
  *⏱️ 00:05:35 — Interface de création d'une clé API avec une modale affichant les options de nommage et d'expiration, le créateur apparaissant en incrustation.*

---

### ⏱️ `[00:06:13 - 00:06:33]` | Segment #18

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> En effet Claude m'avait choisi des voix qui ne me plaisait pas forcément. Je lui ai demandé d'autres suggestions et ce qui est pratique c'est que toujours via l'API de fiche audio il m'a généré des échantillons dans le dossier du jeu. Je les ai écoutés et j'ai pu comme ça choisir de nouvelles voix. Alors j'ai demandé aussi quelques petites améliorations sur le gameplay au niveau de l'affichage.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de l'assistant IA Claude, Finder macOS, interface web du jeu.
**Contenu textuel & Code** : Fichiers audio .mp3 nommés pour les voix de personnages (ex: '0-actuelle-le-penseur.mp3', '1-voix-masculine-anxieuse.mp3'), prompt demandant une voix peureuse.
**Action / Démonstration** : Le créateur montre la génération et la sélection de fichiers audio de propositions de voix via l'API.

**Captures d'écran :**
- ![Affichage d'une fenêtre de l'explorateur de fichiers macOS (Finder) montrant des échantillons audio MP3 générés pour un personnage.](../screenshots/_UBCQAy9kG8/frame_18_000623.jpg)  
  *⏱️ 00:06:23 — Affichage d'une fenêtre de l'explorateur de fichiers macOS (Finder) montrant des échantillons audio MP3 générés pour un personnage.*

---

### ⏱️ `[00:06:33 - 00:06:52]` | Segment #19

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Mon jeu fonctionne, je te propose, on lance une petite partie ensemble pour voir à quoi ça ressemble. On est sur l'écran du jeu, on va rentrer notre nom. On va choisir inspecteur Aspectrice. On va aller sur inspecteur Marco, let's go. Paris, octobre 1926. Il est presque minuit, qu'à des orfèvres.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de développement (IDE/chat IA) et interface du jeu "Meurtre au Manoir Van Bergen".
**Contenu textuel & Code** : Code JavaScript, prompts de modification audio, écran de démarrage du jeu, nom "Marko", choix "Inspecteur", et texte d'introduction textuel ("Paris, octobre 1926...").
**Action / Démonstration** : Le créateur montre son code de gestion de la musique, lance son jeu, saisit son nom, choisit son rôle et découvre l'introduction narrative.

**Captures d'écran :**
- ![Interface de l'outil de développement montrant le code JavaScript pour la gestion audio et un aperçu du jeu "Meurtre au Manoir Van Bergen".](../screenshots/_UBCQAy9kG8/frame_19_000634.jpg)  
  *⏱️ 00:06:34 — Interface de l'outil de développement montrant le code JavaScript pour la gestion audio et un aperçu du jeu "Meurtre au Manoir Van Bergen".*
- ![Écran d'accueil du jeu "Meurtre au Manoir Van Bergen" avec le champ pour saisir le nom de l'inspecteur et choisir le genre.](../screenshots/_UBCQAy9kG8/frame_19_000643.jpg)  
  *⏱️ 00:06:43 — Écran d'accueil du jeu "Meurtre au Manoir Van Bergen" avec le champ pour saisir le nom de l'inspecteur et choisir le genre.*
- ![Scène d'introduction narrative du jeu montrant un bureau d'enquêteur avec les sous-titres de l'histoire.](../screenshots/_UBCQAy9kG8/frame_19_000650.jpg)  
  *⏱️ 00:06:50 — Scène d'introduction narrative du jeu montrant un bureau d'enquêteur avec les sous-titres de l'histoire.*

---

### ⏱️ `[00:06:52 - 00:07:14]` | Segment #20

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et l'inspecteur Marco s'apprête enfin à rentrer chez lui. C'est cool, il a prononcé mon nom. Marco, laissez tomber votre paperasse. Je vous envoie de toute urgence sur une affaire. La baronne Van Bergen a été assassinée dans son manoir, en pleine réception. Cinq invités, trois domestiques, et l'un d'eux est notre assassin.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface d'un jeu narratif ou d'enquête avec option "Passer l'intro" et sous-titres en bas de l'écran.
**Contenu textuel & Code** : Texte à l'écran : "Marko ! Laissez tomber votre paperasse..." puis "La baronne Van Bergen a été assassinée dans son manoir...".
**Action / Démonstration** : Le créateur teste et commente l'introduction narrative d'un jeu d'enquête interactif.

**Captures d'écran :**
- ![Scène narrative d'un jeu vidéo d'enquête montrant le commissaire s'adressant à l'inspecteur Marco.](../screenshots/_UBCQAy9kG8/frame_20_000703.jpg)  
  *⏱️ 00:07:03 — Scène narrative d'un jeu vidéo d'enquête montrant le commissaire s'adressant à l'inspecteur Marco.*
- ![Scène narrative montrant la victime (la baronne Van Bergen) au sol entourée des suspects, avec les sous-titres du dialogue.](../screenshots/_UBCQAy9kG8/frame_20_000713.jpg)  
  *⏱️ 00:07:13 — Scène narrative montrant la victime (la baronne Van Bergen) au sol entourée des suspects, avec les sous-titres du dialogue.*

---

### ⏱️ `[00:07:18 - 00:07:37]` | Segment #21

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Le corps a été emporté et nos hommes ont bouclé le périmètre. Mais sans la moindre preuve, impossible d'inculper qui que ce soit. Votre meilleure chance, c'est de trouver le coupable. Faites vite, on ne pourra pas les retenir éternellement. Vous avez 40 minutes. Allez, c'est parti.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Jeu d'enquête textuel et visuel en ligne (type escape game / visual novel).
**Contenu textuel & Code** : Texte d'introduction du jeu, dialogues du commissaire, minuterie de 40 minutes, plan du manoir et boutons interactifs (Carnet, Téléphone, Quitter).
**Action / Démonstration** : Le créateur découvre l'introduction narrative du jeu d'enquête avant d'arriver dans le hall principal et de lancer le compte à rebours de 40 minutes.

**Captures d'écran :**
- ![Vue extérieure d'un manoir la nuit avec les forces de l'ordre, accompagnée de dialogues textuels du commissaire.](../screenshots/_UBCQAy9kG8/frame_21_000719.jpg)  
  *⏱️ 00:07:19 — Vue extérieure d'un manoir la nuit avec les forces de l'ordre, accompagnée de dialogues textuels du commissaire.*
- ![Gros plan sur le commissaire montrant une montre à gousset, fixant le temps limite de l'enquête.](../screenshots/_UBCQAy9kG8/frame_21_000727.jpg)  
  *⏱️ 00:07:27 — Gros plan sur le commissaire montrant une montre à gousset, fixant le temps limite de l'enquête.*
- ![Vue intérieure du hall d'entrée du manoir avec le minuteur de 40 minutes et les différentes options de déplacement.](../screenshots/_UBCQAy9kG8/frame_21_000736.jpg)  
  *⏱️ 00:07:36 — Vue intérieure du hall d'entrée du manoir avec le minuteur de 40 minutes et les différentes options de déplacement.*

---

### ⏱️ `[00:07:37 - 00:07:59]` | Segment #22

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> On a 40 minutes, on voit bien dans le coin le chronomètre s'afficher. On a notre inspecteur et on va pouvoir se déplacer dans les différentes pièces du manoir. On va commencer par le salon. Alors, je vais me diriger vers le premier personnage et on va lui parler. Bonsoir, Anselm, c'est ça ?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Jeu d'enquête interactive sur navigateur ou application web.
**Contenu textuel & Code** : Chronomètre à 39:48, plan du manoir, personnages (Anselme, la comtesse, l'inspecteur), interface de dialogue textuel ("Bonsoir, Anselme, c'est ça ?").
**Action / Démonstration** : Le créateur explore le salon du manoir puis engage la conversation avec le personnage d'Anselme en tapant un message dans l'interface d'interrogatoire.

**Captures d'écran :**
- ![Vue d'ensemble du salon dans un jeu d'enquête interactive au manoir, avec le chronomètre de 40 minutes et les personnages visibles.](../screenshots/_UBCQAy9kG8/frame_22_000748.jpg)  
  *⏱️ 00:07:48 — Vue d'ensemble du salon dans un jeu d'enquête interactive au manoir, avec le chronomètre de 40 minutes et les personnages visibles.*
- ![Interface d'interrogatoire avec le majordome Anselme et l'inspecteur, affichant les options de dialogue et le champ de saisie du joueur.](../screenshots/_UBCQAy9kG8/frame_22_000757.jpg)  
  *⏱️ 00:07:57 — Interface d'interrogatoire avec le majordome Anselme et l'inspecteur, affichant les options de dialogue et le champ de saisie du joueur.*

---

### ⏱️ `[00:07:59 - 00:08:17]` | Segment #23

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Bonsoir, monsieur l'inspecteur. Anselm, oui, pour vous servir. Majordome de cette maison depuis 35 ans, Si monsieur l'inspecteur veut bien s'asseoir, Anselme répondra de son mieux.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation orale ou séquence sans interface partagée.
**Contenu textuel & Code** : Explications et conseils de création de contenu / IA.
**Action / Démonstration** : Démonstration et mise en contexte pratique.

---

### ⏱️ `[00:08:17 - 00:08:36]` | Segment #24

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Bon, c'est pas trop mal, ça répond vraiment presque du tac au tac. On va lui poser une autre question. Vous parlez toujours de vous la troisième personne. Pardonnez-moi monsieur l'inspecteur, c'est une vieille habitude de la maison.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation orale ou séquence sans interface partagée.
**Contenu textuel & Code** : Explications et conseils de création de contenu / IA.
**Action / Démonstration** : Démonstration et mise en contexte pratique.

---

### ⏱️ `[00:08:37 - 00:08:56]` | Segment #25

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Madame la baronne n'aimait guère qu'un domestique dise « je ». Il faudra m'excuser, ce soir l'habitude revient toute seule. Ok ok bon allez on va aller interroger la deuxième personne la comtesse de Saint-Emmard. Bonsoir madame vous connaissiez bien la victime ?

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Jeu d'enquête textuel et visuel sur navigateur ou application, avec incrustation webcam du créateur.
**Contenu textuel & Code** : Scène de salon bourgeois avec des personnages interactifs (« Parler à Anselme », « La comtesse »), un plan du manoir en bas à gauche, un chronomètre en haut à droite (36:33) et des options de menu en bas à droite (Carnet, Téléphone, Quitter).
**Action / Démonstration** : Le créateur navigue dans le jeu et interagit avec les personnages du manoir pour mener son enquête.

**Captures d'écran :**
- ![Capture d'écran montrant le jeu d'enquête interactif avec le créateur en incrustation vidéo dans le coin supérieur gauche.](../screenshots/_UBCQAy9kG8/frame_25_000846.jpg)  
  *⏱️ 00:08:46 — Capture d'écran montrant le jeu d'enquête interactif avec le créateur en incrustation vidéo dans le coin supérieur gauche.*

---

### ⏱️ `[00:08:56 - 00:09:21]` | Segment #26

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Bonsoir mon brave si je connaissais Hélène nous avons usé les mêmes bancs de pensionnat il y a plus d'un demi-siècle. Nous nous voyons chaque semaine nous détestions cordialement et aucune de nous deux n'aurait su s'en passer. C'est ce qu'on appelle une amitié dans notre monde.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de jeu web ou application de rôle/enquête interactive de type text-based mystery game.
**Contenu textuel & Code** : Textes d'interrogatoire, noms des personnages ("Comtesse Irène de Saint-Aymar"), indices ("Pistes"), champ de saisie "Votre question..." et bouton "Demander".
**Action / Démonstration** : Le créateur mène une session de jeu d'enquête interactive en lisant et posant des questions à un personnage non-joueur.

**Captures d'écran :**
- ![Interface d'un jeu d'enquête textuel montrant le dialogue avec la Comtesse Irène de Saint-Aymar, avec des options de questions et un encadré de saisie.](../screenshots/_UBCQAy9kG8/frame_26_000857.jpg)  
  *⏱️ 00:08:57 — Interface d'un jeu d'enquête textuel montrant le dialogue avec la Comtesse Irène de Saint-Aymar, avec des options de questions et un encadré de saisie.*
- ![Progression de l'interrogatoire où la Comtesse répond textuellement à la question de l'enquêteur sur sa relation avec la victime.](../screenshots/_UBCQAy9kG8/frame_26_000908.jpg)  
  *⏱️ 00:09:08 — Progression de l'interrogatoire où la Comtesse répond textuellement à la question de l'enquêteur sur sa relation avec la victime.*
- ![Affichage de la suite de la réponse de la Comtesse détaillant son amitié de longue date et sa rivalité avec la victime.](../screenshots/_UBCQAy9kG8/frame_26_000919.jpg)  
  *⏱️ 00:09:19 — Affichage de la suite de la réponse de la Comtesse détaillant son amitié de longue date et sa rivalité avec la victime.*

---

### ⏱️ `[00:09:21 - 00:09:40]` | Segment #27

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Bon je vais pas te montrer les 40 minutes de gameplay. Alors j'ai vraiment interrogé tous les suspects. J'ai parlé à tout le monde. Ce qui est vraiment cool c'est qu'on peut vraiment leur poser n'importe quelle question. Alors selon les questions ils vont ou se braquer ou être collaboratifs. Ils vont pouvoir s'énerver aussi ça c'est super marrant. Ils ont tous une personnalité différente.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de jeu vidéo d'enquête policière interactive textuelle avec IA, incrustation vidéo du créateur.
**Contenu textuel & Code** : Écrans d'interrogatoire de suspects (Maître Henri Duclos et Colette Marchand), champ de saisie de texte libre "Demander", pistes d'enquête textuelles.
**Action / Démonstration** : Le créateur présente le système de discussion libre et d'interrogatoire des suspects dans le jeu d'enquête.

**Captures d'écran :**
- ![Interface du jeu montrant l'interrogatoire du suspect Maître Henri Duclos, avec une boîte de saisie pour poser des questions personnalisées et le présentateur en incrustation en bas à droite.](../screenshots/_UBCQAy9kG8/frame_27_000930.jpg)  
  *⏱️ 00:09:30 — Interface du jeu montrant l'interrogatoire du suspect Maître Henri Duclos, avec une boîte de saisie pour poser des questions personnalisées et le présentateur en incrustation en bas à droite.*
- ![Interface du jeu montrant l'interrogatoire d'un autre suspect, Colette Marchand, avec des suggestions de questions et un champ de texte libre pour l'interrogatoire.](../screenshots/_UBCQAy9kG8/frame_27_000938.jpg)  
  *⏱️ 00:09:38 — Interface du jeu montrant l'interrogatoire d'un autre suspect, Colette Marchand, avec des suggestions de questions et un champ de texte libre pour l'interrogatoire.*

---

### ⏱️ `[00:09:40 - 00:10:13]` | Segment #28

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> Et ils se balancent tous un petit peu les uns les autres avec des méfiances, des amitiés. Donc la dynamique est assez sympa. Et voilà je te résume un peu. A force de parler à tout le monde j'ai trouvé le coupable. En fait c'est le cuisinier. Gustave qui a fait le coup et en gros ce qu'il l'a trahi c'est qu'il m'a affirmé qu'il n'avait pas quitté la cuisine de toute la soirée. La bonne m'a dit qu'il est sorti fumer une cigarette mais qu'il n'est pas sorti par la porte de service qu'il prend d'habitude qu'il est sorti par le couloir. En recoupant les témoignages je l'ai ensuite reporté à mon commissaire et j'ai gagné

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface de jeu vidéo d'enquête textuelle/graphique avec incrustation vidéo du créateur en bas à droite.
**Contenu textuel & Code** : Titre "Affaire résolue", texte détaillant l'aveu de Gustave Morel, le mobile, l'élément déclencheur de sa trahison, et les boutons de choix "Oui" ou "Non".
**Action / Démonstration** : Le créateur présente l'écran de conclusion du jeu après avoir résolu l'enquête.

**Captures d'écran :**
- ![Écran de fin de jeu montrant la résolution d'une enquête policière avec un texte explicatif sur le coupable et le mobile.](../screenshots/_UBCQAy9kG8/frame_28_001011.jpg)  
  *⏱️ 00:10:11 — Écran de fin de jeu montrant la résolution d'une enquête policière avec un texte explicatif sur le coupable et le mobile.*

---

### ⏱️ `[00:10:13 - 00:10:47]` | Segment #29

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> j'ai été récompensé d'une médaille Bon alors sur ce projet il y aurait plein de choses à pousser. On pourrait ajouter des enquêtes découper en plusieurs actes et même intégrer d'autres mécanismes de point and click avec des objets, un inventaire, ajouter aussi des animations, mais c'est déjà beaucoup pour un projet monté aussi vite. Et surtout, pouvoir parler en direct avec les suspects et entendre de leur voix la réponse à mes questions niveau immersion, ça fait une vraie différence. Bien sûr, ce n'est qu'un projet parmi d'autres, je ne compte pas commercialiser ce jeu. Si c'était le but, j'aurais sûrement eu une approche différente. Ce projet sert à te montrer

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Présentation vidéo au format face caméra avec infographie épurée.
**Contenu textuel & Code** : Textes de conclusion : 'Déjà beaucoup pour un projet monté aussi vite', 'Un projet parmi d'autres' et 'Pas à vendre'.
**Action / Démonstration** : Le créateur conclut son projet en faisant le bilan et en affichant des éléments textuels de synthèse à l'écran.

---

### ⏱️ `[00:10:47 - 00:11:25]` | Segment #30

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> avant tout un exemple concret de l'utilisation de l'API de fiches audio. Mais avec cette API, on pourrait mener à bien d'autres projets, des applications, des outils pédagogiques et je pense à un dernier cas d'usage qu'on a vu récemment sur la chaîne, utiliser Claude Opus 5.5 pour créer des vidéos en motion design et ajouter l'API de fiches audio pour la voix off. Pour ce dernier cas d'usage, je ne résiste pas à faire un test rapide. J'ai demandé à Claude de me créer une vidéo verticale de 30 secondes en motion design sur les abeilles et je lui ai donné une clé api fiche audio en lui demandant de sélectionner une voix adaptée à la narration et d'utiliser

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Interface web de Claude (Anthropic) et lecteur vidéo intégré.
**Contenu textuel & Code** : Schéma d'architecture avec Claude Opus 5.5, script avec des balises textuelles émotionnelles ([curious], [soft tone], [break]) et aperçu vidéo de motion design sur les abeilles.
**Action / Démonstration** : Le présentateur explique comment combiner Claude Opus 5.5 avec une API audio pour créer et calibrer des vidéos en motion design de manière automatisée.

**Captures d'écran :**
- ![Schéma explicatif montrant l'association entre Claude Opus 5.5 et une API audio pour générer une vidéo en motion design.](../screenshots/_UBCQAy9kG8/frame_30_001106.jpg)  
  *⏱️ 00:11:06 — Schéma explicatif montrant l'association entre Claude Opus 5.5 et une API audio pour générer une vidéo en motion design.*
- ![Interface de l'outil Claude affichant un script avec des balises audio textuelles et un lecteur vidéo intégré montrant une animation de motion design.](../screenshots/_UBCQAy9kG8/frame_30_001123.jpg)  
  *⏱️ 00:11:23 — Interface de l'outil Claude affichant un script avec des balises audio textuelles et un lecteur vidéo intégré montrant une animation de motion design.*

---

### ⏱️ `[00:11:25 - 00:11:59]` | Segment #31

**🔊 Audio (Transcription Intégrale Mot pour Mot en Français) :**
> les tags audio pour mettre la bonne émotion en fonction du texte voici le résultat cette goutte de miel représente le travail de toute une vie une abeille vit environ cinq semaines elle visite des milliers de fleurs et à la fin voilà ce qu'elle laisse un douzième de cuillère à café Pour remplir cette cuillère, il faut 12 abeilles. Alors la prochaine fois que tu mets du miel dans ton thé, tu sais que 12 abeilles y ont passé leur vie. A toi de jouer, je te rappelle l'API de Fiches Audio est gratuite jusqu'à la fin novembre 2026. Pour en profiter, le lien est en description et commentaire épingué. Merci et à bientôt sur le Labo des réseaux.

**👁️ Analyse Visuelle d'Écran (gemini-3.5-flash-lite) :**
**Interface & Outils** : Navigateur web affichant le site Fish Audio
**Contenu textuel & Code** : Page web Fish Audio S2.1 Pro: Free Text-to-Speech API for Developers, bannière colorée indiquant "S2.1 PRO IS NOW FREE to all developers", menus de navigation (Products, Solutions, Resources, Developers, Enterprise, Pricing, Contact Sales)
**Action / Démonstration** : Le présentateur commente la mise à disposition gratuite de l'API text-to-speech Fish Audio S2.1 Pro pour les développeurs.

**Captures d'écran :**
- ![Capture d'écran du site Web de Fish Audio montrant la présentation de l'API Text-to-Speech S2.1 Pro gratuite, avec le présentateur visible en bas à droite.](../screenshots/_UBCQAy9kG8/frame_31_001158.jpg)  
  *⏱️ 00:11:58 — Capture d'écran du site Web de Fish Audio montrant la présentation de l'API Text-to-Speech S2.1 Pro gratuite, avec le présentateur visible en bas à droite.*

---
