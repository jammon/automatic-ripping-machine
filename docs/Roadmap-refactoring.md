# Roadmap for refactoring ARM

## tl;dr
I want to make the code easier to read and to understand. For this it should become more structured, some functionality should be moved into different functions, modules or classes and some names should be changed.

## Description
Currently the code is - out of obvious historical reasons - mostly in a linear, imperative style. E.g. `ripper/main.py` looks roughly like this:

```
import <whatever>
import ...
...

def some_function():
    ...

def some_other_function():
    ...

def main(some, parameters):
    # long
    # list
    # of 
    # detailed
    # instructions
    # and
    # if
        # constructs
    # with
        # many
        # branches
    # ...

if __name__ == "__main__":
    # do some setup
    # 10 loc about logging
    # get arguments
    # initialize some variable
    # initialize Job using that variable
    # more about logging
    if (something with cdrom_status):
        # 2 loc, finally exit
    if (something with logging):
        # exit
    
    # again logging
    
    # something with database
    # change 2 variables in job
    
    # again database in 5 loc
    
    # again logging in 8 loc

    # some database query about Jobs

    # do something with the result in 10 loc

    # again logging

    try:
        main(logfile, job)
    except Exception as e:
        # logging
        # notifying
        # set job variables
    else:
        # set job variable
    finally:
        # 6 loc calculations
        # something with database
```

For somebody new to the project (like me) this is hard to grasp and find my way through it. It is not easy to find the spot in the code, where the concept I'm looking for is dealt with. Some variables or functions have names that don't speak to me.

I want to refactor the code, so that it is more structured and divided in more obvious sections. Anything that modifies e.g. a job should be in a method of Job. Probably it would be wise to subclass Job for music, dvd, blueray etc. to get rid of long if-elif-statements.

`ripper/main.py` should then maybe look like this:

```
import <whatever>
import ...
...

def main(some, parameters):
    do_some_setup()
    initialize_logging()
    manage_previous_jobs_in_database()
    job = job_factory()
    job.do_the_ripping()
    maybe_write_something_to_the_database()
    log_exit_status()

def do_some_setup():
    ...

def initialize_logging():
    ...

if __name__ == "__main__":
    main()
```

Maybe it could also be a good idea to add the name of the function to the logging if it's a kind of error message.

Now this was mostly about `ripper/main.py`, but the other parts of the code should be treated in the same way.