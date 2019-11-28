# Public/Private Keys for the Cloud

## Whats the Big Deal

Lets say Alice and Bob are friend that live far from each other. 
Alice wants to email Bob a secret message, and Eve wants to read the message. 
Neither Alice nor Bob want Eve to eavesdrop on their message.  
Let us also say that Eve can intercept every message between the two.  
To ensure Eve can't read the message Alice needs to encrypt it, which requires  
a key that Alice is confident that Eve doesn't have (and can't figure out).  

If Alice and Bob both knew the key Alice could simply encrypt the message and
send it to Bob. Eve would have no way to know the key and thus the message is safe. 
However, Alice has never told Bob the key before so this case cannot occur. 

What if Alice emails Bob the key then encrypts the message? 
Unfortunately, Alice can't just email Bob the key.  
If she did, it wouldn't be encrypted. If it were Bob wouldn't be able to read it.  
Since the key would have to be sent as plain text Eve would be able to
intercept the key and read the secret message. 

Public/Private keys allow Alice to send the message. 

## Public & Private Key Pair

### General

Let's say Alice has a private key (called K^a\_r) and a public key (called
K^a\_u), and Bob has the private key (K^b\_r) and public key (K^b\_u) (the
details on how to generate these keys are left for later). Now when Alice 
wants to reach Bob she can look up his public key.   
After Alice has Bob's public key she can encrypt 


### RSA

### ECC

Superior to RSA in computation, security, flexibility, memory, communication,
etc. 
If possible use ECC. 

### Dangerous Enough to Hurt Someone

RSA is typically used to introduce public-private cryptography due to its ease
in understanding the concepts. With minimal skill you could write a small
program yourself to implement RSA. *DO NOT DO THIS*. This is said with the
utmost seriousness. RSA is *extremely* easy to implement incorrectly. Even
trained cryptographers have typed bugs. 

I repeat the credo of all security developers *NEVER. EVER. Roll your own
crypto*. You are dangerous enough to hurt yourself or others with
misimplementing this knowledge. 

Feel free however to utilize libraries that implement these functions. 

Whenever possible use ECC over RSA. 

Please note these articles to learn why. 

## How to Generate them

### RSA

### ECC

## Safeguarding the Message Content

Let's think further about Alice and Bob's messages. Eve can still intercept
every message between Alice and Bob. Eve cannot *read* the message content
since she does not have Bob's private key. She may not be able to read it, but
what is stopping her from tampering with it? Absolutely nothing. 

What's wrong with Eve tampering with the message? It'll just be a jumbled mess
right? Let's say Eve does tamper with the message and its a jumbled mess. Bob
may or may not be suspecious. The real danger occurs when the message isn't
jumbled. Let us assume Alice sent Bob "I Love You", and Eve intercepts the
message, changes random bits and it happens to transform into "I Hate You". Bob
is certain it came from Alice but has no way to know that Alice *didn't* send that text.   
Now we have a question of *Integrity* of messages. 

Resolved by HMAC.

## Roots of Trust

Public Private key pairs rely on some 'root of trust'.  

## Implications for the Cloud

The public/private key pair resolves the question of Identity. What if we want
a user to access a particular machine, or more interestingly automate a machine
to access another machine in a secure manner. 

## Relation to Cloudmesh

### Cloud Chameleon 

ssh requires a public private key pair

### cms key

### cms keygroup



