# Layer

Currently a giant heap of trash, Layer is the skeleton for an ETL???/BRMS???/something else?????? framework.

It is used to build and orchestrate Business Rule Integration Components (BRICs).

A BRIC is a plugin module, containing the logic and flow implementation for a business requirement.

### Getting Started

To initialize a new bric from template use:

    python bin/cli.py -c [name_of_new_bric]

Build your business logic inside your new bric, then load it:

    from lib.layer import Layer
    
    # initiate new layer app with environment level
    # or don't specify a level and set it in the config
    layer = Layer('dev')
    
    # load your desired plugins (leave empty to load all plugins)
    layer.mold_brics('name_of_new_bric', 'name_of_another_bric')
    
    # execute your plugins (build your house)
    layer.lay_bric('name_of_new_bric')
        --or--
    layer.lay_brics()
    
Or to use Layer as a package:
    
    from layer import Layer
    
    app = Layer.build()
    
    app.plugs.create_blob_client_stream(blob_query)


#### Goal
Build a distributed service, which is capable of handling the ETL of datasets sized 1-100GB.
Main architecture should:
   - stream all source data, data transformations and uploads
   - have parallelized data down- and up- load capabilities
   - support a wide range of data sources
   - support abstract data manipulation
   - support extensible configuration
   - vectorize data manipulation functions or enforce vectorization whenever possible
   - enforce use of functional programing paradigms:
         - pass by reference
         - no first-level object mutation or reassignment
   - make use of piping sugar to create easily understandable business workflows
   - easily compare requested business logic to code implementation [1]

#### Features
- Extensible config based on environment
- Colorful Logger
- Friendly intellisense and function source tracking
- Parallelizable and streamable I/O operations
- Multiple data source connectors
- Extensible data manipulation features
- Business workflows as plugins (BRICs)
- Template creation for new BRICs


#### Change Log
```
0.0.1 Oficially named the project 'Layer'

```


#### TODOs
- Optimizations:
     - stream dataframes
     - vectorize all transform functions
     - execute flows in parallel
     - wrap all calculations and filters in error handlers
     - move bric-builders to separate GIT projects with own their config
     - build brics as microservices
         eventually this could grow into a bric extender service
     - utilize bitwize operator to create flows
     - [1] draw business flow trees from business logic and from code - this is a way to compare logic provided by BAs
         with algorithms produced by developers. Ideally, generating JSON files with the business flow and expected outputs
         from the code and BA requirements, and comparing the results. This will also abstract business testing to a higher level
- API:
     - create API using Graphene
     - link microservices by message bus or REST and allow data transfer
     - allow access to other brics from current (app.get_bric(name).bricFunc());
         this can be used to get data (from any step in the flow!) from other brics with current config or the bric's original config,
         without building that whole bric, or calling it from the bric service;
- Functions:
     - have option to enforce vectorization wherever possible
     - set defaults on all end function params
     - add docstrings to functions
     - add type hints for idiots
- Config:
     - config additional properties in app.py
     - merge bric level config
- Logger:
     - set logger config based on environment
- Connectors:
     - merge bric level connectors
     - implement Oracle, MSSQL connectors
- Testing and error handling:
     - Ugh, yeah, do that, too, I guess...
     - write some tests (and yes, they have to go deep)
     - add error handling everywhere
- Security:
     - Yes, and also make it secure, somehow...
- Lint:
     - enforce lint by throwing errors at runtime
- Framer:
     - all dataframe columns to UPPERCASE // df.columns = map(str.upper, df.columns);
        this avoids accidentally overwriting DataFrame properties or getting errors for attempted overwriting
     - allow automatic indexing and reindexing of dataframes
     - export dataframes to CSV, JSON, etc.
- Docker:
     - build Docker images for each bric-builder - TBD
     - check if docker can deploy only altered brics
     - build docker auto-deploy service


####  Dev Tips and Good Practices
- Use PyCharm, it's just better
- Use TabNine with your IDE of choice. It provides great Intellisense support for this framework
- Enforce the pylintrc as a standard
- Write code for maximum re-usability; No piece of code should be declared twice
- When faced with a problem, try creating a global solution to solve it, not the easiest solution, 
    i.e problems should be solved on the highest level, not micro-managed
- Vectors, not iterators
- More immutables, less reassignment
- No side-effects on transforms 
- Stream, don't chunk or bulk
- Parallelize slow functions and I/O operations
- Always try: > catch: > finally for handling non-mutative/non-callable procedures 
- Use appropriate error types
- Follow the guides in the sources below for best practices

####  Sources and Guides
- https://github.com/sfermigier/awesome-functional-python
- https://pbpython.com/pandas_transform.html
- https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6
- http://www2.lawrence.edu/fast/GREGGJ/Python/numpy/numpy_vector.html
- https://jacquespeeters.github.io/2017/08/21/parallel-pandas-groupby/
- https://streamz.readthedocs.io/en/latest/dataframes.html
- https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1
- http://coconut-lang.org/
- https://stackoverflow.com/a/55951300
- https://www.diva-portal.org/smash/get/diva2:1308291/FULLTEXT01.pdf
- http://160592857366.free.fr/joe/ebooks/tech/Wiley%20Business%20Rules%20Management%20and%20Service%20Oriented%20Architecture.pdf
- https://en.wikipedia.org/wiki/Rete_algorithm

####  Miscellaneous