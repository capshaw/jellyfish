# jellyfish

Stream of consciousness writing repository. The point of jellyfish is to make the writing and maintaining of notes painless. Less clutter and thought concerning the medium, more thought about the writing.

Supports markdown and will eventually have a robust API for accessing public entries.

## Running jellyfish

*As a note, the following process will eventually be made easier and more automated.*

To run jellyfish you'll need to create a new file called `config.py` that contains two keys: a `secret_key` used for maintaining secure sessions and a `hash_key` used as an extra salt when hashing passwords (used along with the user-specific salts).

You'll also need to instantiate a database, and create an initial user. (There's currently no user-friendly way of creating users or signing up.)  Your bootstrapping function could look something like this:

```python
from models import User
import util
import database

salt = util.generate_salt(64)
user = User('User Name', 'user.email@email.com', 'Password', salt)
util.hash_user_password(user)

database.init_db()
database.db_session.add(user)
database.db_session.commit()
User.query.all()
```

After that, you should be able to run `main.py` and be on your way!

## Thoughts, Motivations, FAQ

+ Jellyfish is intentionally feature-minimal and ridiculously basic. For now each entry has exactly two fields: an owner and a blob of content.
+ *"Stream of consciousness writing repository."? Isn't that just a blog?* Kind of, but not really. Blogging has certain objectives: to reach an audience and make it easy for the readers to interact with the writers. I want to build something a little different: a container for thoughts that may or may not be revisited later (that would be forgotton otherwise), and may or may not be publically discoverable. Basically, a more introspective blog.
+ Security through obscurity is not an option. The APIs are public (by definition). Angular.js and a public repo make this especially obvious. Because of this, the APIs shouldn't take *anything* for granted. Everyone should be assumed to be a malicious client. 

## Dependencies
+ Flask (0.10.1)
+ SQLAlchemy (0.9.1)
+ Angular.js (1.0.7)

## License

MIT License

