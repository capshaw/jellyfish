# jellyfish

Stream of consciousness writing repository. The point of jellyfish is to make the writing and maintaining of notes painless. Less clutter and thought concerning the medium, more thought about the writing.

Supports markdown and will eventually have a robust API for accessing public entries.

## Thoughts, Motivations, FAQ

+ Jellyfish is intentionally feature-minimal and ridiculously basic. For now each entry has exactly two fields: an owner and a blob of content.
+ *"Stream of consciousness writing repository."? Isn't that just a blog?* Kind of, but not really. Blogging has certain objectives: to reach an audience and make it easy for the readers to interact with the writers. I want to build something a little different: a container for thoughts that may or may not be revisited later (that would be forgotton otherwise), and may or may not be publically discoverable. Basically, a more introspective blog.
+ Security through obscurity is not an option. The APIs are public (by definition). Angular.js and a public repo make this especially obvious. Because of this, the APIs shouldn't take *anything* for granted. Everyone should be assumed to be a malicious client. 

## Dependencies
+ Flask
    * SQLAlchemy
+ Angular.js

## License

MIT License

