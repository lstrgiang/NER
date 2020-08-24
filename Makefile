
server/run:
	uvicorn app.main:app



build:
	docker-compose build 

up:
	docker-compose up

ssh:
	docker exec -it nlp-enner /bin/ash


vi/run:
	cd packages
	vncorenlp -Xmx2g VnCoreNLP-1.1.1.jar -p 9001 -a "wseg,pos,ner,parse"


en/run:
	cd packages	
	java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,ner,parse,depparse -status_port 9000 -port 9000 -timeout 60000 &
