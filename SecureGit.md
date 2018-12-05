# Securing Git: Signing Commits

On the Internet, how would one know that a commit is really made by the person claiming to be?

For Git, we use a tool called GPG, which helps you declare yourself has the true author, and verify the work of others. But first, lets see how it works. 

## Signing Commits

Public key encryption is type of encryption that uses two keys: a private and a public key. To have another person send messages to you, you hand them your public keys. Now, they encrypt the message with the public key, and send the encrypted text to you. Now, using your private key, you could decrypt the message. Public encryption only allows the person with the private key to decrypt the message; anyone with public key could encrypt stuff, but never decrypt. 

What happens if you run this scheme in reverse, "encrypting" a particular message with your private key? When somebody "decrypts" this message with the corresponding public key, they can get the original message. What interesting is that the only person that could create this special "encrypted" message is the person with the private key, or you. This process of reversing the normal sequence of encryption is called **signing**.

![CMU Document Signing](https://users.ece.cmu.edu/~adrian/630-f04/PGP-intro_files/fig1-6.gif)	

## Using GPG

GPG, short for GnuPG, is a open source tool for encrypting and signing files. 