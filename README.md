Ein Webcrawler der namhafte deutsche Nachrichtenseiten crawlt. Der Crawler basiert auf Scrapy. Nähere Informationen und Installationshinweisen sind [hier](https://docs.scrapy.org/en/latest/index.html) zu finden.

Die Spiders können entweder direkt über die Kommandozeile angestoßen werden oder über die main.py automatisiert werden. Letzteres stößt die Spiders dreimal am Tag an und schreibt die Ergebnisse in ein lokales File (Prüfung ob der Artikel bereits zuvor gecrawlt wurde, findet in den Spiders statt).

Folgende Shell Befehle sind verfügbar: 
- getWeltArticle
- getTagesschauArticle
- getSpiegelArticle
- getNtvArticle
- getImages (crawled Artikel und Bilder aus allen Schlagzeilen von Welt und Spiegel)
