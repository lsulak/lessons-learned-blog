Title: Book Recommendation: Designing Data-Intensive Applications
Date: 2022-03-15 20:00
Category: systems architecture
Slug: designing-data-intensive-applications
Status: draft
Summary: My key takeaways from the book Designing Data-Intensive Applications.

These days, the importance of data and its usefulness in our professional as well as in our
personal lives is more and more prevalent. Simply put, data matters, if it can be consumed, interpreted,
and used in a meaningful way - we can optimize for things that
actually matter based on reality, not just our intuition, and make informed decision.

Besides making data-driven decisions, reporting is no easy task without data, stored somewhere in computer - take,
for example Amazon. In 2020, they had over 200 million regularly paying Amazon Prime members worldwide
[link](https://www.statista.com/statistics/829113/number-of-paying-amazon-prime-members/), they had around
1.3 millions employees [link](https://www.statista.com/statistics/234488/number-of-amazon-employees/),
and they were selling over 350 million products [link](https://www.nchannel.com/blog/amazon-statistics/).
Can you imagine how impossible would be to manually manage and make payments for such a big number of employees
each month, manage the whole portfolio of products, manage orders and calculate the overall revenue from their
e-commerce site effectively and efficiently?

Ever-increasing data volumes come hand in hand with technological innovation that enabled the storage to be
cheap and the computation resources to no longer be a primary bottleneck in many applications. For some applications,
data is the primary challenge there: the complexity, volume, or the speed at which it's changing. This leads to
an increasing complexity of the systems and applications that utilize the data, not to mention a massive development
and a very broad spectrum of technologies that emerge each year. It can be very challenging
to understand and master all sorts of technologies, programming languages, frameworks, and platforms - on both,
technical level as well as on broader, more architectural level. Let me steal a quote from the book:

*"However, as software engineers and architects, we also need to
have a technically accurate and precise understanding of the various technologies and
their trade-offs if we want to build good applications."*

If you develop applications that have some kind of backend for storing and processing data,
then this book is a must-read for you.

Increasingly many applications now have such demanding or wide-ranging
requirements that a single tool can no longer meet all of its data processing and storage needs.
Instead, the work is broken down into tasks that can be performed efficiently on a single tool,
and those different tools are stitched together using application code.

# Foundations Of Data Systems

## The Most Important Non-Functional Requirements Of Software Systems

An application has to meet various requirements in order to be useful. There are:

* **functional requirements**: what the system should do, such as allowing data to be stored,
  retrieved, searched, and processed in various ways, and
* **nonfunctional requirements**: general properties like security, reliability, compliance, scalability,
  compatibility, and maintainability.

This book starts with the explanation of three concerns that are important in most software systems:
* **Reliability**. The system should continue to work correctly (performing the correct function at
  the desired level of performance) even in the face of adversity (hardware or software faults, and
  even human error).

* **Scalability**. As the system grows (in data volume, traffic volume, or complexity), there should
  be reasonable ways of dealing with that growth.

  The author explains how to describe load and performance
  of your system. This is illustrated on an example of a service that sends data to a client.
  In this example, the author details that usually, measuring response time using medium (instead of the arithmetic mean)
  and percentiles (for being able to spot outliers) can be a good idea; in practical terms, for monitoring
  dashboards of your application, you need to calculate them on an ongoing basis, for example as a rolling window
  of response times of requests in the last 10 minutes. Every minute, you'd calculate the median and various
  percentiles over the values in that window and plot those metrics on a graph - for example using **heatmaps**
  (i.e. histograms collected over time, see
  (this excellent article)[https://orangematter.solarwinds.com/2016/11/18/why-percentiles-dont-work-the-way-you-think/]
  for more details).

  The author then continues with explaining ways of coping with increasing load with **scaling up** (=vertical scaling, moving
  to more powerful machine) and **scaling out** (=horizontal scaling, distributing the load across many machines, i.e.
  shared-nothing architecture).

  *"A system that can run on a single machine is often simpler, but high-end machines can become very expensive, so very intensive workloads often can't avoid scaling out. In reality, good architectures usually involve a pragmatic mixture of approaches: for example, using several fairly powerful machines can still be simpler and cheaper than a large number of small virtual machines."*

* **Maintainability**. Over time, many different people will work on the system (engineering and operations,
  both maintaining current behavior and adapting the system to new use cases), and they should all be
  able to work on it productively.

  *"It is well known that the majority of the cost of software is not in its initial development, but in its ongoing maintenance—fixing bugs, keeping its systems operational, investigating failures, adapting it to new platforms, modifying it for new use cases, repaying technical debt, and adding new features."*

  We should design software in such a way that it will hopefully minimize pain during maintenance. Particular
  attention should be paid to these three design principles:
  * **Operability**. Make it easy for operations teams to keep the system running smoothly.

    *Focus on:* having good visibility into the system’s health, and having effective ways of managing it.

  * **Simplicity**. Make it easy for new engineers to understand the system, by removing as much
    complexity as possible from the system. When complexity makes maintenance hard, budgets and schedules are often
    overrun. In complex software, there is also a greater risk of introducing bugs when making a change.

    *"Making a system simpler does not necessarily mean reducing its functionality; it can also mean removing accidental complexity. (Moseley and Marks)[https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.93.8928] define complexity as accidental if it is not inherent in the problem that the software solves (as seen by the users) but arises only from the implementation."*

    *Focus on:* a good abstraction can hide a great deal of implementation detail behind a clean,
    simple-to-understand facade, hopefully resulting in removing accidental complexity.

  * **Evolvability**. Make it easy for engineers to make changes to the system in the future, adapting
    it for unanticipated use cases as requirements change.

    It's extremely unlikely that your system’s requirements will remain unchanged forever.
    They are much more likely to be in constant flux: you learn new facts, previously unanticipated use
    cases emerge, business priorities change, users request new features, new platforms replace old platforms,
    legal or regulatory requirements change, growth of the system forces architectural changes, etc.

    *Focus on:*
    * organizational point of view: agile working patterns provide a framework for adapting to change.

    * technical perspective: simplicity and its abstractions: simple and easy-to-understand
      systems are usually easier to modify than complex ones.

## Data Models

Data models are perhaps the most important part of developing software, because they have such a profound effect:
not only on how the software is written, but also on how we think about the problem that we are solving.

Historically, data started out being represented as one big tree (the hierarchical model), but that wasn’t good
for representing many-to-many relationships, so the relational model was invented to solve that problem.
More recently, developers found that some applications don’t fit well in the relational model either.
New nonrelational “NoSQL” datastores have diverged in two main directions:

* Document databases target use cases where data comes in self-contained documents and relationships between one document and another are rare.

* Graph databases go in the opposite direction, targeting use cases where anything is potentially related to everything.

All three models (document, relational, and graph) are widely used today, and each is good in its respective domain.
Generally speaking, relational databases generalize very well to all kinds of (increasingly) diverse purposes.

One thing that document and graph databases have in common is that they typically
don’t enforce a schema for the data they store, which can make it easier to adapt
applications to changing requirements. However, your application most likely still
assumes that data has a certain structure; it’s just a question of whether the schema is
explicit (enforced on write) or implicit (handled on read).

The author goes into history and describes the following data models:

* Hierarchical model (1970s, the most popular was IBM’s Information Management System, IMS):
  It represented all data as a tree of records nested within records, much like
  the JSON structure. Like document databases, this worked well for one-to-many relationships, but it
  made many-to-many relationships difficult, and it didn’t support joins.
  Various solutions were proposed to solve the limitations of the hierarchical model.
  The two most prominent were the relational model (which became SQL, and took
  over the world) and the network model (which initially had a large following but
  eventually faded into obscurity).

* Network model: standardized by a committee called the Conference on Data Systems Languages (CODASYL) and
  implemented by several different database vendors; it is also known as the CODASYL model. The CODASYL
  model was a generalization of the hierarchical model. In the tree structure of the hierarchical model,
  every record has exactly one parent; in the network model, a record could have multiple parents.
  This allowed many-to-one and many-to-many relationships to be modeled.

  A query in CODASYL was performed by moving a cursor through the database by
  iterating over lists of records and following access paths. If a record had multiple
  parents (i.e., multiple incoming pointers from other records), the application code
  had to keep track of all the various relationships. The problem was that they made the code for querying
  and updating the database complicated and inflexible. With both the hierarchical and the network model, if
  you didn’t have a path to the data you wanted, you were in a difficult situation. You could change the
  access paths, but then you had to go through a lot of handwritten database query code and rewrite it to
  handle the new access paths. It was difficult to make changes to an application’s data model.

  The links between records in the network model were not foreign keys, but more like
  pointers in a programming language (while still being stored on disk). The only way
  of accessing a record was to follow a path from a root record along these chains of
  links - this is called an access path.

* Relational model: data is organized into relations (tables) and
  each relation is a collection of tuples (rows).

  In a relational database, the query optimizer automatically decides which parts of the
  query to execute in which order, and which indexes to use. Those choices are effectively
  the “access path,” but the big difference is that they are made automatically by the query optimizer,
  not by the application developer, so we rarely need to think about them.

  If you want to query your data in new ways, you can just declare a new index, and
  queries will automatically use whichever indexes are most appropriate. The relational model thus made it much easier to add
  new features to applications.

* Document databases: Document databases reverted back to the hierarchical model in one aspect: storing
nested records within their parent record rather than in a separate
table.

* NoSQL model (Not Only SQL): the main driving forces behind the adoption of these databases include
  a need for greater scalability than relational databases offer, specialized query operations not well
  supported  by the relational model, less restrictive and more dynamic and expressive data model.

  If the database itself does not support joins, you have to emulate a join in application code by making
  multiple queries to the database. Moreover, even if the initial version of an application fits well
  in a join-free document model, data has a tendency of becoming more interconnected as features are added
  to applications.

* Graph-Like Data Models
  We saw earlier that many-to-many relationships are an important distinguishing feature between different
  data models. If your application has mostly one-to-many relationships (tree-structured data) or no
  relationships between records, the document model is appropriate. If many-to-many relationships are
  very common in your data? The relational model can handle simple cases of many-to-many relationships,
  but as the connections within your data become more complex, it becomes more natural to start
  modeling your data as a graph.

Database normalization: Literature on the relational model distinguishes several different normal forms,
but the distinctions are of little practical interest. As a rule of thumb, if you’re duplicating values
that could be stored in just one place, the schema is not normalized.

### Relational Versus Document Databases Today

The main arguments in favor of the document data model are schema flexibility, bet‐
ter performance due to locality, and that for some applications it is closer to the data
structures used by the application. The relational model counters by providing better
support for joins, and many-to-one and many-to-many relationships.

If the data in your application has a document-like structure (i.e., a tree of one-to-many relationships,
where typically the entire tree is loaded at once), then it’s probably a good idea to use a document model.

However, if your application does use many-to-many relationships, the document
model becomes less appealing. It’s possible to reduce the need for joins by denormalizing, but then the application
code needs to do additional work to keep the denormalized data consistent. Joins can be emulated in application code
by making multiple requests to the database, but that also moves complexity into the application
and is usually slower than a join performed by specialized code inside the database.
In such cases, using a document model can lead to significantly more complex application code and worse performance.

It’s not possible to say in general which data model leads to simpler application code;
it depends on the kinds of relationships that exist between data items. For highly
interconnected data, the document model is awkward, the relational model is accept‐
able, and graph models are the most natural.

Most document databases, and the JSON support in relational databases, do not
enforce any schema on the data in documents. No schema means that arbitrary keys
and values can be added to a document, and when reading, clients have no guaran‐
tees as to what fields the documents may contain.

schema-on-read (the structure of the data is implicit, and only interpreted when the
data is read), in contrast with schema-on-write (the traditional approach of relational databases, where the schema is explicit and the database ensures all written data con‐
forms to it)

The schema-on-read approach is advantageous if the items in the collection don’t all
have the same structure for some reason (i.e., the data is heterogeneous)—for exam‐
pl there is a biv variety of objects, or the structure of data is determined by external systems over which you have
no control and which might change over time. In cases where all records are
expected to have the same structure, schemas are a useful mechanism for document‐
ing and enforcing that structure.

It seems that relational and document databases are becoming more similar over
time, and that is a good thing: the data models complement each other. v If a database
is able to handle document-like data and also perform relational queries on it, appli‐
cations can use the combination of features that best fits their needs.

## Storage And Retrieval

Motivation: you need to select a storage engine that is appropriate for your application, from
the many that are available. In order to tune a storage engine to perform well on your kind of
workload, it's important to have a rough idea of what the storage engine is doing under the hood.

In particular, there is a big difference between storage engines that are optimized for
transactional workloads and those that are optimized for analytics.

On a high level, we saw that storage engines fall into two broad categories: those optimized for transaction processing (OLTP),
and those optimized for analytics (OLAP). The biggest difference between them is in the access patterns:

* OLTP systems are typically user-facing, which means that they may see a huge
  volume of requests. In order to handle the load, applications usually only touch a
  small number of records in each query. The application requests records using
  some kind of key, and the storage engine uses an index to find the data for the
  requested key. Disk seek time is often the bottleneck here.

* Data warehouses and similar analytic systems are primarily used by business analysts, not by end users.
  They handle a much lower volume of queries than OLTP systems, but each query is typically very
  demanding, requiring many millions of records to be scanned in a short time.
  Disk bandwidth (not seek time) is often the bottleneck here, and column-
  oriented storage is an increasingly popular solution for this kind of workload.

On the OLTP side, we saw storage engines from two main schools of thought:
* The log-structured school, which only permits appending to files and deleting obsolete files, but never updates a file that has been written. Bitcask, SSTables,
  LSM-trees, LevelDB, Cassandra, HBase, Lucene, and others belong to this group.

* The update-in-place school, which treats the disk as a set of fixed-size pages that can be overwritten. B-trees are the biggest example of this philosophy,
  being used in all major relational databases and also many nonrelational ones.

The author goes into details of log-structured storage engines and page-oriented storage engines.

An index is an additional structure that is derived from the primary data. Maintaining additional structures
incurs overhead, especially on writes. For writes, it’s hard to beat the performance of
simply appending to a file, because that’s the simplest possible write operation. Any
kind of index usually slows down writes, because the index also needs to be updated
every time data is written.

This is an important trade-off in storage systems: well-chosen indexes speed up read
queries, but every index slows down writes. For this reason, databases don’t usually
index everything by default, but require you—the application developer or database
administrator—to choose indexes manually, using your knowledge of the application’s typical query patterns.

The author talks, into detail with al ot of practical examples and lists of database systems that utilize the individual techniques.
There are key-value indexes, which are like a primary key index in the relational model. A primary key uniquely
identifies one row in a relational table, or one document in a document database, or one vertex in a graph database.
Other records in the database can refer to that row/document/vertex by its primary key (or
ID), and the index is used to resolve such references.

It is also very common to have secondary indexes. A secondary index can easily be constructed from a key-value index.

There are Hash Indexes, SSTables and LSM-Trees, B-Trees

## Transaction Processing or Analytics?

An application typically looks up a small number of records by some key, using an index. Records
are inserted or updated based on the user’s input. Because these applications are
interactive, the access pattern became known as online transaction processing (OLTP).
However, databases also started being increasingly used for data analytics, which has
very different access patterns. Usually an analytic query needs to scan over a huge
number of records, only reading a few columns per record, and calculates aggregate
statistics (such as count, sum, or average) rather than returning the raw data to the
user.

A transaction needn’t necessarily have ACID properties. Transaction processing just means allowing clients
to make low-latency reads and writes - as opposed to batch processing jobs, which only run periodically (e.g. once a day).

| Property             | OLTP                                              | OLAP                                      |
| -------------------- | ------------------------------------------------- |
| Main read pattern    | Small number of records per query, fetched by key | Aggregate over large number of records    |
| Main write pattern   | Random-access, low-latency writes from user input | Bulk import (ETL) or event stream         |
| Primarily used by    | End user/customer, via web application            | Internal analyst, for decision support    |
| What data represents | Latest state of data (current point in time)      | History of events that happened over time |
| Dataset size         | Gigabytes to terabytes                            | Terabytes to petabytes                    |

At first, the same databases were used for both transaction processing and analytic
queries. SQL turned out to be quite flexible in this regard: it works well for OLTP-type
queries as well as OLAP-type queries. Nevertheless, in the late 1980s and early 1990s, there
was a trend for companies to stop using their OLTP systems for analytics purposes, and
to run the analytics on a separate database instead. This separate database was called a data warehouse.

### Data Warehousing
An enterprise may have dozens of different transaction processing systems: e.g. systems powering the
customer-facing website, tracking inventory in warehouses, planning routes for vehicles, managing suppliers,
etc. Each of these systems is complex and needs a team of people to maintain it, so the systems end up
operating mostly autonomously from each other.

These OLTP systems are usually expected to be highly available and to process trans‐
actions with low latency, since they are often critical to the operation of the business.
Letting business analysts run ad hoc analytic queries on OLTP systems can be often too expensive - they
need to scan a large parts of the dataset, which can harm performance of concurrently executing transactions.

This problem can be solved by a data warehousing. A data warehouse is a separate database that analysts can
query, without affecting OLTP operations. The data warehouse contains a read-only copy of the data
in all the various OLTP systems in the company. Data is extracted from OLTP databases
(using either a periodic data dump or a continuous stream of updates), transformed into an
analysis-friendly schema, cleaned up, and then loaded into the data warehouse. The process
of getting data into the data warehouse is called ETL (Extract-Transform-Load).

The data model of a data warehouse is most commonly relational, because SQL is
generally a good fit for analytic queries. On the surface, a data warehouse and a relational OLTP database look similar,
because they both have a SQL query interface. However, the internals of the systems can look quite different, because
they are optimized for very different query patterns. Some databases, such as Microsoft SQL Server, have support for
transaction processing and data warehousing in the same product.

### Stars and Snowflakes: Schemas for Analytics

As explored in Chapter 2, a wide range of different data models are used in the realm
of transaction processing, depending on the needs of the application. On the other
hand, in analytics, there is much less diversity of data models. Many data warehouses
are used in a fairly formulaic style, known as a star schema (dimensional modeling). Usually, facts are captured as individual events,
because this allows maximum flexibility of analysis later. However, this means that the fact table can become extremely
large (in practical terms, they can have over hundred of columns or even much more, and trillions of rows).
Some columns in the fact tables are attributes (e.g. price of product) and others are references to
dimensional tables. As each row in the fact table represents an event,
the dimensions represent the who, what, where, when, how, and why of the event (dimensions can be also very wide, but have usually much smaller number of records).

The name “star schema” comes from the fact that when the table relationships are
visualized, the fact table is in the middle, surrounded by its dimension tables; the
connections to these tables are like the rays of a star.
A variation of this template is known as the snowflake schema, where dimensions are
further broken down into subdimensions. Snowflake schemas are more normalized than star schemas,
but star schemas are often preferred because they are simpler for analysts to work
with.

Although fact tables are often over 100 columns wide, a typical data warehouse query
only accesses 4 or 5 of them at one time. In most OLTP databases, storage is laid out in a row-oriented fashion: all the values
from one row of a table are stored next to each other. The idea behind column-oriented storage is simple: don’t store all the values from one
row together, but store all the values from each column together instead. If each col‐
umn is stored in a separate file, a query only needs to read and parse those columns
that are used in that query, which can save a lot of work. An example of columnar storage format is Parquet.
The column-oriented storage layout relies on each column file containing the rows in
the same order. This type of storage can be efficiently compressed, especially if the column values
are repetitive (these systems often use bitmap encoding or Run-length encoding).

Most of the load consists of large read-only queries run by analysts. Column-oriented storage,
compression, and sorting all help to make those read queries faster. However, they have the
downside of making writes more difficult. An update-in-place approach, like B-trees use, is not possible with compressed col‐
umns. If you wanted to insert a row in the middle of a sorted table, you would most
likely have to rewrite all the column files. As rows are identified by their position
within a column, the insertion has to update all columns consistently.
Fortunately, we have already seen a good solution earlier in this chapter: LSM-trees.
All writes first go to an in-memory store, where they are added to a sorted structure
and prepared for writing to disk. It doesn’t matter whether the in-memory store is
row-oriented or column-oriented. When enough writes have accumulated, they are
merged with the column files on disk and written to new files in bulk. Queries need to examine both the column data on disk and the recent writes in mem‐
ory, and combine the two. However, the query optimizer hides this distinction from
the user.

Not every data warehouse is necessarily a column store: traditional row-oriented
databases and a few other architectures are also used. However, columnar storage can
be significantly faster for ad hoc analytical queries, so it is rapidly gaining popularity.

Another aspect of data warehouses that is worth mentioning briefly is materialized
aggregates. As discussed earlier, data warehouse queries often involve an aggregate
function, such as COUNT, SUM, AVG, MIN, or MAX in SQL. If the same aggregates are used
by many different queries, it can be wasteful to crunch through the raw data every
time. Why not cache some of the counts or sums that queries use most often?
When the underlying data changes, a materialized view needs to be updated, because
it is a denormalized copy of the data. The database can do that automatically, but
such updates make writes more expensive, which is why materialized views are not
often used in OLTP databases. In read-heavy data warehouses they can make more
sense. A common special case of a materialized view is known as a data cube or OLAP cube.
It is a grid of aggregates grouped by different dimensions. The advantage of a materialized
data cube is that certain queries become very fast because they have effectively been precomputed.
For example, if you want to know the total sales per store yesterday, you just need to look at the
totals along the appropriate dimension—no need to scan millions of rows.

## Encoding And Evolution

There are many ways of turning data structures into bytes on the
network or bytes on disk. The details of such encodings affect not only
their efficiency, but more importantly also the architecture of applications and your
options for deploying them. Schema evolution is a property that is hugely beneficial for evolvability of the overall system.

The encoding formats can be generally classified into the following groups:
* Programming language–specific encodings are restricted to a single programming language and often fail to
  provide forward and backward compatibility.

  They are usually very convenient, but they are usually intended for quick and easy encoding of data,
  so data versioning is often neglected - so they usually don't offer schema evolution for backward and forward compatibility.
  Efficiency (CPU time as well as resulting size of the encoded structure) is often not as optimal as some other alternatives.

  Usually this category of encodings isn't a very suitable solution for more complex systems on production that are working with bigger
  datasets. But it can be sufficient enough for smaller datasets, data used only internally within the organization, or for transient purposes.

* Textual formats like JSON, XML, and CSV are widespread, and their compatibility depends on how you use them.
  These formats are somewhat vague about datatypes, so you have to be careful with things like numbers and
  binary strings.

  Regarding schema support, CSV does not have any schema, so it is up to the application to define the meaning of each
  row and column. There is optional schema support for both XML and JSON. These schema languages are quite powerful, and
  thus quite complicated to learn and implement.

  JSON, XML, and CSV are good enough for many purposes. It’s likely that they will remain popular,
  especially as data interchange formats (i.e., for sending data from one organization to another).
  In these situations, as long as people agree on what the format is, it often doesn’t matter how
  pretty or efficient the format is. The difficulty of getting different organizations to agree on
  anything outweighs most other concerns.

* Binary schema–driven formats like Thrift, Protocol Buffers, and Avro allow compact, efficient encoding with clearly
  defined forward and backward compatibility semantics. The schemas can be useful for documentation and code generation
  in statically typed languages. However, they have the downside that data needs to be decoded before it is human-readable.

These days, backward/forward compatibility and rolling upgrades are quite achievable with appropriate choice of the technology.

In most cases, a change to an application’s features also requires a change to data that
it stores: perhaps a new field or record type needs to be captured, or perhaps existing
data needs to be presented in a new way. When a data format or schema changes, a corresponding change to application code
often needs to happen. However, in a large application, code changes often cannot happen instantaneously:
* With server-side applications you may want to perform a rolling upgrade (also
  known as a staged rollout), deploying the new version to a few nodes at a time,
  checking whether the new version is running smoothly, and gradually working
  your way through all the nodes.

* With client-side applications you’re at the mercy of the user, who may not install
  the update for some time.

This means that old and new versions of the code, and old and new data formats, may potentially all coexist
in the system at the same time. In order for the system to continue running smoothly, we need to maintain
compatibility in both directions: backward and forward compatibility.

### Modes Of Dataflow

Whenever you want to send data over the network or write it to a file - you need to encode it as a
sequence of bytes. Who encodes the data and who decodes it? The most common ways how data flows between processes are:

* Via databases
* Via service calls (e.g. REST and RPC)
* Via asynchronous message passing

# Distributed Data

There are various reasons why you might want to distribute a database across multiple machines:

* Scalability. If your data volume, read load, or write load grows bigger than a single machine
  can handle, you can potentially spread the load across multiple machines.

* Fault tolerance/high availability. If your application needs to continue working even if one machine (or several
  machines, or the network, or an entire datacenter) goes down, you can use multiple machines to give you redundancy.
  When one fails, another one can take over.

* Latency. If you have users around the world, you might want to have servers at various locations worldwide so that
  each user can be served from a datacenter that is geographically close to them. That avoids the users having to wait
  for network packets to travel halfway around the world.

There are two common ways data is distributed across multiple nodes:
* Replication. Keeping a copy of the same data on several different nodes, potentially in different locations.
  Replication provides redundancy: if some nodes are unavailable, the data can still be served from the remaining
  nodes. Replication can also help improve performance.

  If the data that you’re replicating does not change over time, then replication is easy:
  you just need to copy the data to every node once, and you’re done. All of the difficulty in replication
  lies in handling changes to replicated data. There are three popular algorithms for replicating changes
  between nodes: single-leader, multi-leader, and leaderless replication. Almost all distributed databases use one of these three approaches.

  Every write to the database needs to be processed by every replica; otherwise, the replicas would no longer contain the same data.
  The most common solution for this is called leader-based replication (also known as active/passive or master–slave replication).

  1. One of the replicas is designated the leader (also known as master or primary). When clients want to write to the database, they must
     send their requests to the leader, which first writes the new data to its local storage.

  1. The other replicas are known as followers (read replicas, slaves, secondaries, or hot standbys).i Whenever the leader writes
     new data to its local storage, it also sends the data change to all of its followers as part of a replication log or change stream.
     Each follower takes the log from the leader and updates its local copy of the database accordingly, by applying all writes in the same
     order as they were processed on the leader.

  1. When a client wants to read from the database, it can query either the leader or any of the followers. However, writes are only accepted
     on the leader (the followers are read-only from the client’s point of view).

  An important detail of a replicated system is whether the replication happens synchronously or asynchronously. Synchronous: the leader
  waits until a follower has confirmed that it received the write before reporting success to the user, and before making the write visible to
  other clients. Asynchronous: the leader sends the message, but doesn’t wait for a response from the follower.

  In practice, if you enable synchronous replication on a database, it usually means that one of the followers is synchronous, and the others are
  asynchronous. If the synchronous follower becomes unavailable or slow, one of the asynchronous followers is made synchronous. This guarantees
  that you have an up-to-date copy of the data on at least two nodes: the leader and one synchronous follower. This configuration is sometimes also called
  semi-synchronous.

  Often, leader-based replication is configured to be completely asynchronous. In this case, if the leader fails and is not recoverable, any writes
  that have not yet been replicated to followers are lost. This means that a write is not guaranteed to be durable, even if it has been confirmed to
  the client. However, a fully asynchronous configuration has the advantage that the leader can continue processing writes, even if all of its
  followers have fallen behind. Weakening durability may sound like a bad trade-off, but asynchronous replication is nevertheless widely used,
  especially if there are many followers or if they are geographically distributed.

* Partitioning. Splitting a big database into smaller subsets called partitions so that different partitions can be
  assigned to different nodes (also known as sharding).

## Replication

Replication can serve several purposes: high availability (keeping the system running even when one machine is down),
disconnected operation (allowing an application to continue working when there is a network interruption),
latency (placing data geographically close to users), and scalability (being able to handle a higher volume of reads
than a single machine could handle, by performing reads on replicas).

There are three approaches to replication:
* single-leader: clients send all writes to a single node (the leader), which sends a stream of data
  change events to the other replicas (followers). Reads can be performed on any replica, but reads from followers might be stale.

* multi-leader: clients send each write to one of several leader nodes, any of which can accept writes. The leaders send
  streams of data change events to each other and to any follower nodes.

* leaderless replication: clients send each write to several nodes, and read from several nodes in parallel
  in order to detect and correct nodes with stale data.


Each approach has advantages and disadvantages. Single-leader replication is popular because it is fairly easy to understand and there is no
conflict resolution to worry about. Multi-leader and leaderless replication can be more robust in the presence of faulty nodes, network
interruptions, and latency spikes—at the cost of being harder to reason about and providing only very weak consistency guarantees.

### Failures

* Follower: on its local disk, each follower keeps a log of the data changes it has received from the leader. If a follower crashes and is restarted, or if the network between the leader and the follower is temporarily interrupted, the follower can recover quite easily: from its log, it knows the last transaction that was processed before the fault occurred. Thus, the follower can connect to the leader and request all the data changes that occurred during the time when the follower was disconnected. When it has applied these changes, it has caught up to the leader and can continue receiving a stream of data changes as before.

* Leader: handling a failure of the leader is trickier: one of the followers needs to be promoted to be the new leader, clients need to be reconfigured to send their writes to the new leader, and the other followers need to start consuming data changes from the new leader. This process is called failover.

### Implementation of Replication Logs

* Statement-based replication; non-determinism is the main problem, functions like NOW() or queries relying on existing data in the DB, side effects of the statements, etc)

* Write-ahead log (WAL) shipping; the main problem is that the log describes the data on a very low level: a WAL contains details of which bytes were changed in which disk blocks. This makes replication closely coupled to the storage engine. If the database changes its storage format from one version to another, it is typically not possible to run different versions of the database software on the leader and the followers. This can have a big operational impact.

* Logical (row-based) log replication; this doesn't have the same problem as WAL shipping-based replication - since a logical log is decoupled from the storage engine internals, it can more easily be kept backward compatible, allowing the leader and the follower to run different versions of the database software, or even different storage engines. This technique is called change data capture and is also useful for other applications, because the log can be parsed by external system, for example data warehouse for analysis.

* Trigger-based replication; it offers flexibility but there are a few downsides: it has greater overheads than other replication methods, and is more prone to bugs (since it requires a custom application code) and limitations than the database’s built-in replication.

### Replication Lag

If an application reads from an asynchronous follower, it may see outdated information if the follower has fallen behind. This leads to apparent inconsistencies in the database: if you run the same query on the leader and a follower at the same time, you may get different results, because not all writes have been reflected in the follower. This inconsistency is just a temporary state—if you stop writing to the database and wait a while, the followers will eventually catch up and become consistent with the leader. For that reason, this effect is known as eventual consistency. In general, there is no limit to how far a replica can fall behind. In normal operation, the delay between a write happening on the leader and being reflected on a follower—the replication lag—may be only a fraction of a second, and not noticeable in practice. However, if the system is operating near capacity or if there is a problem in the network, the lag can easily increase to several seconds or even minutes.

When working with an eventually consistent system, it is worth thinking about how the application behaves if the replication lag increases to several minutes or even
hours. If the answer is “no problem,” that’s great. However, if the result is a bad experience for users, it’s important to design the system to provide a stronger guarantee,
such as read-after-write. Pretending that replication is synchronous when in fact it is asynchronous is a recipe for problems down the line.

The next sections highlight three examples of problems that are likely to occur when there is replication lag.

#### Reading Your Own Writes

A user makes a write, followed by a read from a stale replica. But in asynchronous replication, new data may not yet have reached the replica.
To prevent this anomaly, we need *read-after-write* consistency - users should always see data that they submitted themselves.
It makes no promises about other users: other users’ updates may not be visible until some later time.
However, it reassures the user that their own input has been saved correctly.

#### Monotonic Reads

An anomaly can occur when reading from asynchronous followers - it's possible for a user to see things moving backward in time.
This can happen if a user makes several reads from different replicas.

One way of achieving monotonic reads is to make sure that each user always makes
their reads from the same replica. For example, the replica can be chosen based on a hash of the user ID, rather than
randomly. However, if that replica fails, the user’s queries will need to be rerouted to another replica.

#### Consistent Prefix Reads

This replication lag anomaly concerns violation of causality. Users should see the data in a state that makes causal sense: for example, seeing a
question and its reply in the correct order.

If the database always applies writes in the same order, reads always see a consistent prefix, so this anomaly cannot happen.
However, in many distributed databases, different partitions operate independently, so there is no global ordering of writes:
when a user reads from the database, they may see some parts of the database in an older state and some in a newer state.

Preventing this kind of anomaly requires another type of guarantee: consistent prefix reads. This guarantee says that if a sequence
of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.
One solution is to make sure that any writes that are causally related to each other are written to the same partition.

### Multi-Leader Replication

Leader-based replication has one major downside: there is only one leader, and all writes must go through it. iv If you can’t connect to
the leader for any reason, for example due to a network interruption between you and the leader, you can’t write to the database.
A natural extension of the leader-based replication model is to allow more than one node to accept writes. Replication still happens
in the same way: each node that processes a write must forward that data change to all the other nodes. We call this a multi-leader
configuration (also known as master–master or active/active replication). In this setup, each leader simultaneously acts as a follower to the other leaders.

It rarely makes sense to use a multi-leader setup within a single datacenter, because the benefits rarely outweigh the added complexity. Typical
use-cases of this approach involve e.g. multi-datacenter operation, clients with offline operation (e.g. calendar apps on your mobile phone, your laptop, and
other devices need to function even without the Internet - you must be able to see the data in your calendar and even sync any changes to servers whenever you
are back online), or collaborative editing (e.g. Google Docs).

As multi-leader replication is a somewhat retrofitted feature in many databases, there are often subtle configuration pitfalls and surprising
interactions with other database features. For example, autoincrementing keys, triggers, and integrity constraints can be problematic.
For this reason, multi-leader replication is often considered dangerous territory that should be avoided if possible.

The biggest problem with multi-leader replication is that write conflicts can occur, which means that conflict resolution is required.
There is a few possible solutions for this problem, most of them involve conflict resolution by converging toward a consistent state,
or custom (programmatic, using application code) conflict resolution (this application code can be executed on write or on read).
The research on the topic of automatic conflict resolution is still ongoing.
Note that conflict resolution usually applies at the level of an individual row or document, not for an entire transaction.

**Multi-Leader Replication Topologies**: a replication topology describes the communication paths along which writes are propagated from one node to another.
Three example topologies are circular topology, star topology, and all-to-all topology.

### Leaderless Replication

### Concurrency

An operation A happens before another operation B if B knows about A, or depends on A, or builds upon A in some way. Whether one operation happens
before another operation is the key to defining what concurrency means. In fact, we can simply say that two operations are concurrent if neither
happens before the other (i.e., neither knows about the other). Thus, whenever you have two operations A and B, there are three possibilities: either
A happened before B, or B happened before A, or A and B are concurrent.

## Partitioning

For very large datasets, or very high query throughput, replication is not sufficient: we need to break the data up into partitions, also known as sharding.

Scalability is the main goal here: different partitions can be placed on different nodes in a shared-nothing cluster. So a large dataset can be distributed
across many disks, and the query load can be distributed across many processors.

Partitioning is usually combined with replication so that copies of each partition are stored on multiple nodes. This means that, even though each
record belongs to exactly one partition, it may still be stored on several different nodes for fault tolerance.

There are several ways how to partition data . The goal with partitioning is to spread the data and the query load evenly across
nodes. If every node takes a fair share, then—in theory—10 nodes should be able to handle 10 times as much data and 10 times the read and write
throughput of a single.

If the partitioning is unfair, so that some partitions have more data or queries than others, we call it skewed. The presence of skew makes
partitioning much less effective. In an extreme case, all the load could end up on one partition, so 9 out of 10 nodes are idle and your
bottleneck is the single busy node. A partition with disproportionately high load is called a hot spot.

There are two main approaches to partitioning:
* Key range partitioning: assign a continuous range of keys to eac partition, from min to max).
  If you know the boundaries between the ranges, you can easily determine which partition contains a given key.

  Here, keys are sorted, and a partition owns all the keys from some minimum up to some maximum. Sorting has the advantage that efficient
  range queries are possible, but there is a risk of hot spots if the application often accesses keys that are close together in the sorted order.

* Hash partitioning: a good hash function takes skewed data and makes it uniformly distributed. Once you have a suitable hash function for keys,
  you can assign each partition a range of hashes (rather than a range of keys), and every key whose hash falls within a partition’s range will be stored
  in that partition. These hash functions don't need to be cryptographically strong, for example, Cassandra and MongoDB use MD5.
  Unfortunately, range queries won't be efficient because the keys are now scattered across all the partitions, so their sort order is lost.

  Here a hash function is applied to each key, and a partition owns a range of hashes. This method destroys the ordering of keys, making range
  queries inefficient, but may distribute load more evenly. When partitioning by hash, it is common to create a fixed number of partitions in
  advance, to assign several partitions to each node, and to move entire partitions from one node to another when nodes are added or removed.
  Dynamic partitioning can also be used.

"Fully automated rebalancing can be convenient, because there is less operational work to do for normal maintenance. However, it can be unpredictable.
Rebalancing is an expensive operation, because it requires rerouting requests and moving a large amount of data from one node to another. If it is
not done carefully, this process can overload the network or the nodes and harm the performance of other requests while the rebalancing is in progress."

The author also discussed the interaction between partitioning and secondary indexes. A secondary index also needs to be partitioned, and there are two methods:
* Document-partitioned indexes (local indexes), where the secondary indexes are stored in the same partition as the primary key and value.
  This means that only a single partition needs to be updated on write, but a read of the secondary index requires a scatter/gather across all partitions.

* Term-partitioned indexes (global indexes), where the secondary indexes are partitioned separately, using the indexed values. An entry in the
  secondary index may include records from all partitions of the primary key. When a document is written, several partitions of the secondary
  index need to be updated; however, a read can be served from a single partition.

## Transactions

A transaction is a way for an application to group several reads and writes together into a logical unit. Conceptually, all the reads and writes
in a transaction are executed as one operation: either the entire transaction succeeds ( commit) or it fails (abort, rollback).

Not every application needs transactions, and sometimes there are advantages to weakening transactional guarantees or abandoning them entirely
(for example, to achieve higher performance or higher availability).

The idea of ACID consistency depends on the application’s notion of invariants, and it’s the application’s responsibility to define its
transactions correctly so that they preserve consistency. This is not something that the database can guarantee: if you write bad data
that violates your invariants, the database can’t stop you. Atomicity, isolation, and durability are properties of the database,
whereas consistency (in the ACID sense) is a property of the application. The application may rely on the database’s atomicity
and isolation properties in order to achieve consistency, but it’s not up to the database alone. Thus, the letter C doesn’t
really belong in ACID.

A note on ACID durability: In a single-node database, durability typically means that the data has been written to
nonvolatile storage such as a hard drive or SSD. It usually also involves a write-ahead log or similar which allows
recovery in the event that the data structures on disk are corrupted. In a replicated database, durability may mean
that the data has been successfully copied to some number of nodes. In order to provide a durability guarantee,
a database must wait until these writes or replications are complete before reporting a transaction as successfully committed.

### Isolation Anomalies

* Dirty reads
* Dirty writes
* Phantom read: this occurs when, in the course of a transaction, two identical queries are executed, and the collection of rows
  returned by the second query is different from the first.
* Non-repeatable read: this error occurs, when during the course of a transaction, a row is retrieved twice and the values
  within the row differ between reads. This is okay in many situations, but there are some which cannot tolerate it, such as
  backups, analytic queries, or integrity checks.
* The lost update problem: this can occur if an application reads some value from the database, modifies it, and writes back
  the modified value (a read-modify-write cycle). If two transactions do this concurrently, one of the modifications can
  be lost, because the second write does not include the first modification.

  An example of this problem is this: two users editing a wiki page at the same time, where each user saves their
  changes by sending the entire page contents to the server, overwriting whatever is currently in the database.
* Write skew: is neither a dirty write nor a lost update, because the two transactions are updating two different objects.
  You can think of write skew as a generalization of the lost update problem. Write skew can occur if two transactions read
  the same objects, and then update some of those objects (different transactions may update different objects). In the
  special case where different transactions update the same object, you get a dirty write or lost update anomaly (depending on the timing).

  Write skew phantoms usually follow the pattern of:
  a) select query checks whether some requirement is satisfied by searching for rows that match some search condition,
  b) depending on the result of the select query, the application code decides how to continue,
  c) if the application decides to go ahead, it makes a write to the database and commits the transaction. The effect of this
  write changes the precondition of the decision of step 2. In other words, if you were to repeat the SELECT query from step 1
  after committing the write, you would get a different result, because the write changed the set of rows matching the search condition.

  This effect, where a write in one transaction changes the result of a search query in another transaction, is called a phantom.
  Snapshot isolation avoids phantoms in read-only queries, but in read-write transactions, phantoms can lead to particularly
  tricky cases of write skew.


### Weak Isolation Levels

Isolation levels are hard to understand, and inconsistently implemented in different databases. Strong isolation level means serializability,
see the next section. This section will talk about weaker isolation levels.

* Read Uncommitted. It prevents dirty writes, but does not prevent dirty reads. Some databases support this rather weak isolation level.

* Read Committed, it has two guarantees:
  * When reading from the database, you will only see data that has been committed (no dirty reads).
  * When writing to the database, you will only overwrite data that has been committed (no dirty writes).

  Read committed is a very popular isolation level. It is the default setting in Oracle 11g, PostgreSQL, SQL Server 2012, MemSQL,
  and many other databases.

  Most commonly, databases prevent dirty writes by using row-level locks: when a transaction wants to modify a particular
  object (row or document), it must first acquire a lock on that object. It must then hold that lock until the transaction
  is committed or aborted. Only one transaction can hold the lock for any given object; if another transaction wants to
  write to the same object, it must wait until the first transaction is committed or aborted before it can acquire the lock and continue.

  Most databases prevent dirty reads using the following approach: for every object that is written, the database remembers both the
  old committed value and the new value set by the transaction that currently holds the write lock. While the transaction is ongoing,
  any other transactions that read the object are simply given the old value. Only when the new value is committed do transactions
  switch over to reading the new value.

  This is pretty good, but there still can be of ways in which you can have concurrency bugs when using this isolation level, such as
  non-repeatable read or a phantom read. More on this below.

* Snapshot Isolation (aka, in Oracle it is called serializable, and in PostgreSQL and MySQL it is called repeatable read).
  Snapshot isolation is the most common solution to the non-repeatable read problem. The idea is that each transaction reads
  from a consistent snapshot of the database—that is, the transaction sees all the data that was committed in the database
  at the start of the transaction. Even if the data is subsequently changed by another transaction, each transaction sees only
  the old data from that particular point in time.

  Snapshot isolation is a boon for long-running, read-only queries such as backups and analytics. It is very hard to reason about
  the meaning of a query if the data on which it operates is changing at the same time as the query is executing. When a transaction
  can see a consistent snapshot of the database, frozen at a particular point in time, it is much easier to understand. From a performance
  point of view, a key principle of snapshot isolation is readers never block writers, and writers never block readers.

  To implement snapshot isolation, databases use a generalization of the Read Committed mechanism. The database must potentially keep several
  different committed versions of an object, because various in-progress transactions may need to see the state of the database at
  different points in time. Because it maintains several versions of an object side by side, this technique is known as multi-version
  concurrency control (MVCC).

  If a database only needed to provide read committed isolation, but not snapshot isolation, it would be sufficient to keep two
  versions of an object: the committed version and the overwritten-but-not-yet-committed version. However, storage engines that
  support snapshot isolation typically use MVCC for their read committed isolation level as well. A typical approach is that read
  committed uses a separate snapshot for each query, while snapshot isolation uses the same snapshot for an entire transaction.
  MVCC-based snapshot isolation is implemented in Postgres in a way that when a transaction is started, it is given a unique,
  always-increasing vii transaction ID. Whenever a transaction writes anything to the database, the data it writes is tagged
  with the transaction ID of the writer. When a transaction reads from the database, transaction IDs are used to decide
  which objects it can see and which are invisible. By carefully defining visibility rules, the database can present a consistent
  snapshot of the database to the application. By never updating values in place but instead creating a new version every time a value
  is changed, the database can provide a consistent snapshot while incurring only a small overhead.

* Preventing Lost Updates
  The read committed and snapshot isolation levels we’ve discussed so far have been primarily about the guarantees of
  what a read-only transaction can see in the presence of concurrent writes. We have mostly ignored the issue of two
  transactions writing concurrently. Because this is such a common problem, a variety of solutions have been developed:

  * Atomic write operations: taking an exclusive lock on the object when it is read so that no other transaction can
    read it until the update has been applied. Another option is to simply force all atomic operations to be executed on a single thread.
  * Explicit locking: if the database’s built-in atomic operations don’t provide the necessary functionality, another option is for the
    application to explicitly lock objects that are going to be updated.
  * Automatically detecting lost updates: atomic operations and locks are ways of preventing lost updates by forcing the read-modify-write
    cycles to happen sequentially. An alternative is to allow them to execute in parallel and, if the transaction manager
    detects a lost update, abort the transaction and force it to retry its read-modify-write cycle.
  * Compare-and-set: the purpose of this operation is to avoid lost updates by allowing an update to happen only if the value
    has not changed since you last read it. If the current value does not match what you previously read, the update has no
    effect, and the read-modify-write cycle must be retried.
  * Conflict resolution and replication: in replicated databases (see Chapter 5 ), preventing lost updates takes on another
    dimension: since they have copies of the data on multiple nodes, and the data can potentially be modified concurrently on
    different nodes, some additional steps need to be taken to prevent lost updates. A common approach in such replicated databases
    is to allow concurrent writes to create several conflicting versions of a value (also known as siblings), and to use application
    code or special data structures to resolve and merge these versions after the fact.

### Serializability

This guarantees that even though transactions may execute in parallel, the end result is the same as if they had executed one at a time,
serially, without any concurrency. Thus, the database guarantees that if the transactions behave correctly when run individually,
they continue to be correct when run concurrently—in other words, the database prevents all possible race conditions.

But if serializable isolation is so much better than the mess of weak isolation levels, then why isn’t everyone using it? To answer
this question, we need to look at the options for implementing serializability, and how they perform. They are usually implemented as either:
* Literally executing transactions in a serial order.
  The approach of executing transactions serially is implemented in VoltDB/H-Store, Redis, and Datomic.

  A system designed for single-threaded execution can sometimes perform better than a system that supports concurrency,
  because it can avoid the coordination overhead of locking. However, its throughput is limited to that of a single CPU core.
  In order to make the most of that single thread, transactions need to be structured differently from their traditional form.

* Two-phase locking.
* Optimistic concurrency control techniques such as serializable snapshot isolation.


