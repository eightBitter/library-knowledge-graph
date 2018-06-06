# Note on conversion from JSON-LD to TTL

The conversion runs kind of slow based on the small amount of records I’m converting.

Some of Schema.org’s vocabulary definitions have multiple ranges. What this means is that it confuses conversion scripts. For example, schema:genre always converts to a URI; schema:provider converts to a literal. The way to work around this is by explicitly specifying data types. However, this makes the JSON data look a little wonky. Here’s a list of the terms I’ve come across so far:

schema:makesOffer
schema:provider
workLocation
worksFor
address
propertyID (want a literal)
genre (want literal)
availability (want URI)
containedInPlace (want URI)
dayOfWeek (want URI)
photo (want URI)
containsPlace (want URI)
isRelatedTo
availableAtOrFrom
