![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/3646eb02de6527ca5d83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230920%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230920T093721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a16061403db66817ad257733a20c1f9aa1ecfab33cd908a5694276e8dcd5fa38) ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/746187b76bea1f46030e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230920%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230920T093721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=02ccbaa82aa41a4558f000e0a4d9f4674f627dec8f113cff094dff37c5cbd325) ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/665ce871c2ecc66a8e71.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230920%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230920T093721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=45fd1aa136b5e69a82fd95dd96bc766fa0fe9ae7f446225f38097e9ee7cfe91c)

Resources
---------

**Read or watch:**

*   [REST API Design: Pagination](/rltoken/VeL1Cbu_NVNND6WKJrECbg "REST API Design: Pagination")
*   [HATEOAS](/rltoken/Mqk-KBxLRtJaQuWZO-oeAQ "HATEOAS")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/cTaCEqXO09xize9ePftDXg "explain to anyone"), **without the help of Google**:

*   How to paginate a dataset with simple page and page\_size parameters
*   How to paginate a dataset with hypermedia metadata
*   How to paginate in a deletion-resilient manner

Requirements
------------

*   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5.\*)
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions and coroutines must be type-annotated.

Setup: `Popular_Baby_Names.csv`
-------------------------------

[use this data file](/rltoken/7IKLZ7i4pO4MJ9CQoGHfVw "use this data file") for your project
