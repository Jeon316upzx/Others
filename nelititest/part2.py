# Tell us one thing you are very opinionated about as a developer and why.


1) Developers shouldn't shove down their opinions on others as best practice, the reason is that
   It leads to poor code quality, encourages poor standardization and affects morale.
   eg I have had a senior developer tell me to return not only the user and user token on login but
   all the models defined(transactions, activities, settings, profile) and his reason was that
   where he worked before, that was how they did it and it was a very bad practice because of the amount of
   task that gets done by the Database per request: (getting profile informaton meant that one would get transactions, settings etc.)



# Based on your understanding of our company, what do you think our biggest challenge is?

1) Efficiency and storage is one of the major issues in that storing
   and efficiently fetching data from the database can be quite tasking especially with millions of index journals and their metadata.

# What’s one cool feature or idea you’d like to implement if you came to work for us?

1) I as a user would like to see sample journals on getting to the landing page, maybe like
about 10 - 20 random journals to better give me a sense of what the platform is about just like zlibrary did.

2) I would love to be able to download journals in different formats eg Word, PDF, epub etc.

3) I would implement a more rich user interface that users would not only love but commend, I am already sourcing for a better UI for Neliti.

4) for Authenticated users which
   I don't think has been implemented yet, I would love to build a recommendation systems that uses their Hits to recommends journals and publications
