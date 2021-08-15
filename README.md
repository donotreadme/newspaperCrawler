Kleinere Spielerei um den Umgang mit Scrapy etwas zu üben. (https://docs.scrapy.org/en/latest/index.html)

Mit *scrapy crawl getHeadlines* können die Urls der Ticker-News von den Nachrichtenseiten Welt und Spiegel geladen werden und werden in .txt Dateien zwischen gespeichert.

Mit *scrapy crawl getWeltArticle* (bzw. getSpiegelArticle) lassen sich anschließend alle relevanten Daten crawlen (mit * -o "name.jl"* ergänzen um in json-File zu speichern)
