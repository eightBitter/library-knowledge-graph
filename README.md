Library Knowledge Graph Project
===============================

This is a personal attempt at creating a library knowledge graph that represents NCSU Libraries (collections, people, services, events, spaces, technology, etc).

## Plan

- [x] Design templates for each entity type
- [x] Come up with a taxonomy for connecting entities
- [x] Create 10 example records for each entity
- [x] Convert JSON-LD to TTL
- [ ] Resolve conversion problems
- [ ] Ingest records into GraphDB and run some queries to explore relationships
- [ ] Install question-answer software (check earlier research notes for particular software)
- [ ] Create use-case examples
  - Related content (Amazon)
  - Smart search
  - Research tracks?

## To Do Next

- Figure out why the script is converting certain URIs to strings. See
  - schema:makesOffer (want a )
  - schema:provider (want a URI)
  - workLocation (want a URI)
  - worksFor (want a URI)
  - address (want a URI)
  - propertyID (want a literal)
  - genre (want literal)
  - availability (want URI)
  - containedInPlace (want URI)
  - dayOfWeek (want URI)
  - photo (want URI)
  - containsPlace (want URI)
  - isRelatedTo (want URI)
  - availableAtOrFrom (want URI)
  - Will need to explicitly specify data type. See JMHaynes.json

## Goals for week of June 4

  - Get data cleaned and into GraphDB
  - Explore the data and come up with a list of natural questions and corresponding SPARQL queries
  - Install QA extension
