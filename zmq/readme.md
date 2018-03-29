
# [ØMQ](http://zguide.zeromq.org/)

ZeroMQ is a high-performance asynchronous messaging library, aimed at use in distributed or concurrent applications.
It provides a message queue, but unlike message-oriented middleware, a ZeroMQ system can run without a dedicated message
broker. The library's API is designed to resemble that of Berkeley sockets.


## Request & Reply - [`request_reply/`](request_reply/)

- The _REQ-REP_ socket pair is in lockstep.
- The client issues `zmq_send()` and then `zmq_recv()`, in a loop (or once if that's all it needs). Doing any other
  sequence (e.g., sending two messages in a row) will result in a return code of -1 from the send or recv call.
- Server issues `zmq_recv()` and then `zmq_send()` in that order, as often as it needs to.

![Request & Reply Schematics](request_reply/schematics.png)

```bash
#!/bin/bash
python client.py &
python server.py
```

> - You could throw thousands of clients at this server, all at once, and it would continue to work happily and quickly.
>   For fun, try starting the client and then starting the server, see how it all still works, then think for a second
>   what this means.
> - Let us explain briefly what these two programs are actually doing. They create a ZeroMQ context to work with, and
>   a socket. Don't worry what the words mean. You'll pick it up. The server binds its REP (reply) socket to port 5555.
> - The server waits for a request in a loop, and responds each time with a reply. The client sends a request and reads
>   the reply back from the server.
> - If you kill the server (Ctrl-C) and restart it, the client won't recover properly. Recovering from crashing
>   processes isn't quite that easy.
> - There is a lot happening behind the scenes but what matters to us programmers is how short and sweet the code is,
>   and how often it doesn't crash, even under a heavy load. This is the request-reply pattern, probably the simplest
>   way to use ZeroMQ. It maps to RPC and the classic client/server model.


## Publish & Subscribe - [`publish_subscribe/`](publish_subscribe/)

- An example of one-way data distribution, in which a server publishes updates to a set of subscribers. Example that
  pushes out weather updates consisting of a zip code, temperature, and relative humidity.
- There's no start and no end to this stream of updates, it's like a never ending broadcast.
- Subsciber application, which listens to the stream of updates and grabs anything to do with a specified zip code,
  by default New York City.
- The _PUB-SUB_ socket pair is asynchronous. The client does `zmq_recv()`, in a loop (or once if that's all it needs).
  Trying to send a message to a _SUB_ socket will cause an error. Similarly, the service does `zmq_send()` as often as
  it needs to, but must not do `zmq_recv()` on a _PUB_ socket.
![Publish & Subscribe Schematics](publish_subscribe/schematics.png)

```bash
#!/bin/bash
python subscriber.py &
python subscriber.py &
python subscriber.py &
python publisher.py &
```

> - A subscriber can connect to more than one publisher, using one connect call each time. Data will then arrive and be
>   interleaved ("fair-queued") so that no single publisher drowns out the others.
> - If a publisher has no connected subscribers, then it will simply drop all messages.
> - If you're using TCP and a subscriber is slow, messages will queue up on the publisher. We'll look at how to
>   protect publishers against this using the "high-water mark" later.
> - You do not know precisely when a subscriber starts to get messages. Even if you start a subscriber, wait a while,
>   and then start the publisher, the subscriber will always miss the first messages that the publisher sends. This is
>   because as the subscriber connects to the publisher (something that takes a small but non-zero time), the publisher
>   may already be sending messages out.


## Parallel Processing Pipeline - [`parallel_pipeline/`](parallel_pipeline/)

- A ventilator that produces tasks that can be done in parallel
- A set of workers that process tasks
- A sink that collects results back from the worker processes

![Parallel Processing Pipeline Schematics](parallel_pipeline/schematics.png)

```bash
#!/bin/bash
python sink.py &
python worker.py &
python worker.py &
python worker.py &
python ventilator.py
```

> - The workers connect upstream to the ventilator, and downstream to the sink. This means you can add workers arbitrarily.
>   If the workers bound to their endpoints, you would need (a) more endpoints and (b) to modify the ventilator and/or
>   the sink each time you added a worker. We say that the ventilator and sink are stable parts of our architecture and
>   the workers are dynamic parts of it.
> - We have to synchronize the start of the batch with all workers being up and running. This is a fairly common gotcha in
>   ZeroMQ and there is no easy solution. The `zmq_connect` method takes a certain time. So when a set of workers
>   connect to the ventilator, the first one to successfully connect will get a whole load of messages in that short time
>   while the others are also connecting. If you don't synchronize the start of the batch somehow, the system won't run in
>   parallel at all. Try removing the wait in the ventilator, and see what happens.
> - The ventilator's PUSH socket distributes tasks to workers (assuming they are all connected before the batch start
>   s going out) evenly. This is called load balancing and it's something we'll look at again in more detail.
> - The sink's PULL socket collects results from workers evenly. This is called fair-queuing.
