Title: Book Review: System Design Interview
Date: 2022-03-24 20:00
Category: systems architecture
Slug: system-design-interview
Status: published
Summary: My key takeaways from the book System Design Interview: An Insider’s Guide

This book is about designing highly scalable, reliable, distributed backend systems. I recently finished reading
<u>[Designing Data-Intensive Applications (Martin Kleppmann)](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable-ebook/dp/B06XPJML5D)</u>
and Amazon recommended me another one, that seemed to be quite promising -
<u>[System Design Interview (Alex Xu)](https://www.amazon.com/System-Design-Interview-Insiders-Guide/dp/1736049119)</u>.
I decided to give it a go.

My motivation was to enrich my overall engineering and system design toolbox by getting a better perspective on architecture and design of software systems
(mostly backend / distributed systems) and to systemize my approach.

[TOC]

How to think during the overall process of system design (I tried to think beyond an interview as I was reading the book, because many good principles
from the book can be applied in real life as well), how to identify the functional and non-functional requirements, how to think more pragmatically,
how to identify bottlenecks, how to think about scaling, and much more.

Mastering system design is difficult. I'm not talking only about the initial design, but about the whole software development lifecycle - the confirmation that the design
actually works in real life - all major functional and non-functional requirements have been fulfilled, the cost of development was reasonable, and the maintenance / extensibility
is acceptable. If you were already participating or making software design and architecture decisions in the past, it might or might not mean that you are universally good in
this and that you can design a back-end system for another product in another company. It's always good to broaden your knowledge; it's easier in coding because you have
tons of open source projects and you get feedback pretty quickly. But getting a good feedback on your design is not as easy and quick in real life - it can take months to
design and implement the system (even if it's a MVP).

## Thoughts On The Book

The book offers a framework for the system design and then it applies it to several case studies. There is also a nice
[online course](https://courses.systeminterview.com/courses/system-design-interview-an-insider-s-guide) that has the same content as the book.

The book is, in my opinion, quite practical, but can be sometimes rather superficial - it doesn't cover all the reasoning and theory behind the decisions
and it sometimes doesn't go very deep. But I don't mean it in a bad way - after all, this book is supposed to be a 'preparation' for a system design
interview, not a comprehensive manual for designing software systems in real life.

Generally speaking, I recommend this book to people who are: preparing for the systems design interview, or are yet about to design and
implement a distributed system at scale, but also to more experienced engineers who would like to extend their knowledge and stretch their muscles
in this area.

## System Design Interview Framework

A proposed framework for the systems design interview is below. The author claims that a great system design interview is open-ended and there is no one-size-fits-all
solution. I tend to agree - bear in mind that unnecessarily complex, over-engineered solution that doesn't communicative intentions and trade-offs very well is a big
red flag - not just during the interview, but also in the real life.

### 1. **Understand the problem and establish design scope**

A quote from the book: *"In a systems design interview, giving out an answer quickly does not give you you bonus points."*

Slow down, think and ask proper, high-level questions. Make proper assumptions and write down your learnings.
Think about the main functional features, the usage of the system and make constraints clear.

### 2. **Propose high-level design and get buy-in**

Iteratively confirm that your approach satisfies the requirements and constraints of the system. Use a whiteboard or paper for capturing the ideas (the format can be
a couple of box diagrams that are somehow connected - these can represent web servers, clients, databases, load balancers, cache, DNS systems, etc) and the main
parts of the system. Have a two-way conversation, not a monologue.

### 3. **Design deep dive**

At this step, you should already know what the overall goals and boundaries of the systems are and you should have a high-level blueprint for the overall design.
You should have some ideas/parts of the systems/algorithms where to focus more. Work with the interviewer to identify and prioritize components of the system.
The objective here is to dig into details of some system components. This can be the most time consuming and technically challenging part of the process.

### 4. **Wrap up**

Once the design seems to be sensible, the last part is to wrap up the session. This can include identification of the bottleneck, discuss potential improvements,
re-iterating again by recapping the design, but also some non-functional requirements such as scalability (e.g. in network requests), reliability
(software, hardware, or human errors), and maintenance (future development, monitoring and operations) of the system.


## Back On The Envelope Estimation

You'll sometimes be asked to do 'back-of-the-envelope' estimates. These can be helpful for estimating system capacity or performance requirements.

### Power Of Two

<center>

|     Power      |          Exact Value          |        Approximate Value        |     Bytes     |
|:--------------:|------------------------------:|:-------------------------------:|--------------:|
|       7        |                           128 |                                 |          16 B |
|       8        |                           256 |                                 |          32 B |
|      10        |                          1024 |            1 thousand           |          1 KB |
|      20        |                     1,048,576 |            1 million            |          1 MB |
|      30        |                 1,073,741,824 |            1 billion            |          1 GB |
|      40        |             1,099,511,627,776 |            1 trillion           |          1 TB |
|      50        |         1,125,899,906,842,624 |            1 quadrillion        |          1 PB |

</center>

### Latency Numbers Every Programmer Should Know

Take these numbers with pinch of salt - many of them can be outdated as computers become faster and more powerful. However, they
can be very useful anyway, because they can give us a rough idea about the performance of the entire system or some of its part.

<center>

| Operation Name                              |                Time               |
|:--------------------------------------------|:---------------------------------:|
| L1 cache reference                          |             0.5 ns                |
| Branch mispredict                           |               5 ns                |
| L2 cache reference                          |               7 ns                |
| Mutex lock/unlock                           |              25 ns                |
| Main memory reference                       |             100 ns                |
| Compress 1K bytes with Zippy                |          10,000 ns = 10 μs        |
| Send 1 KB bytes over 1 Gbps network         |          10,000 ns = 10 μs        |
| Read 4 KB randomly from SSD                 |         150,000 ns = 150 μs       |
| Read 1 MB sequentially from memory          |         250,000 ns = 250 μs       |
| Round trip within same datacenter           |         500,000 ns = 500 μs       |
| Read 1 MB sequentially from SSD             |       1,000,000 ns = 1,000 μs     |
| HDD seek                                    |      10,000,000 ns = 10,000 μs    |
| Read 1 MB sequentially from 1 Gbps network  |      10,000,000 ns = 10,000 μs    |
| Read 1 MB sequentially from HDD             |      30,000,000 ns = 30,000 μs    |
| Send packet CA -> Netherlands -> CA         |     150,000,000 ns = 150,000 μs   |

</center>

Where:

* 1 ns = 10^-9 seconds
* 1 us = 10^-6 seconds = 1,000 ns

Some conclusions:

* Memory is fast but the disk is slow.
* Avoid disk seeks if possible.
* Simple compression algorithms are fast.
* Compress data before sending it over the internet if possible.
* Data centers are usually in different regions, and it takes time to send data between them.

### Availability Numbers

High availability is the ability of a system to be continuously operational for a desirably long period of time.
This is measured as a percentage, where 100% means a service that has zero downtime. Most services fall between 99% and 100%,
big cloud providers usually set this at 99.9%.

This number can be a part of an agreement between a service provider and its customer. This agreement is called a service level agreement (SLA).

<center>

| Availability | Acceptable Downtime Per Day | Acceptable Downtime Per Year |
|:-------------|:---------------------------:|:----------------------------:|
| 99%          |          14.40 min          |           3.65 days          |
| 99.9%        |           1.44 min          |          8.77 hours          |
| 99.99%       |           8.64 sec          |           52.60 min          |

</center>

## Further Resources

* <u>[System Design Primer](https://github.com/donnemartin/system-design-primer)</u>: A great resource for designing large scale systems

* <u>[Designing Data-Intensive Applications](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable-ebook/dp/B06XPJML5D)</u>:
  A must read book on scalable, distributed systems. The book contains many concepts and is both theoretical and practical. It's quite detailed, technical, and
  even quite challenging sometimes. I heavily recommend it to everyone who is dealing with systems where the biggest bottleneck is data

* <u>[Martin Fowler's Blog](https://www.martinfowler.com/architecture/)</u>: One of the best technical blogs out there. I'm sure that you'd agree with me if you are already
  familiar with it. If this is the first time you hear about it, well...you can thank me later

* <u>[High Scalability Blog](http://highscalability.com/)</u>: Case studies and discussions of real systems such as Uber, Instagram, Netflix, and much more.

* Depending on technology you use, there is an amazing content on other blogs (including corporate blogs, such as
  <u>[AWS Blog](https://aws.amazon.com/blogs/)</u>, <u>[Netflix Blog](https://netflixtechblog.com/)</u>,
  <u>[Databricks Blog](https://databricks.com/blog)</u>, etc, check the platform/technology of your interest, maybe they publish something
  related to this topic) and video content on YouTube (especially various conferences) or other platforms
  (such as <u>[AlgoExpert](https://www.algoexpert.io/product)</u> which seems to be quite interesting although I don't have a personal experience with it)
