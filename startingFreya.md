# Starting FREyA

The latest version of Solr does not work, since FREyA was built using an older version. This was successfully tested with Solr version 4.6.

[https://github.com/danicadamljanovic/freya](FREyA) is a Natural Language Interface for Querying Ontologies. This is the tool I'm testing for Question Answering over the Library Knowledge Graph.

[https://github.com/danicadamljanovic/freya](Once installed), follow these steps to get everything running:

- Open GraphDB
- Run Solr: `~/Documents/solr.../bin/solr start`
- Run Tomcat: `/Library/Tomcat/bin/startup.sh`
- Open FREyA at http://localhost:8080/freya
