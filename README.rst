InDesign Server SOAP Client
===========================
A simple python wrapper for the InDesign Server SOAP service for running InDesign scripts remotely.

Dependancies
------------

- suds>=0.4

Sample Usage
------------

::

    from indesign_server.client import InDesignServerClient
    wsdl = "http://myserver.com/service?wsdl"
    client = InDesignServerClient(wsdl)
    client.run_script("c:\path\to\script.jsx", script_language="javascript",
                script_args={"arg0":"some value"})
    
Notes
-----
The version of InDesign server I'm using (CS5.5) did not provide the correct endpoint in the
generated wsdl file.  You can use the `host` argument of `InDesignServerClient` to set the
correct endpoint.

Also, timeout errors are common because InDesign server sometimes performs long running tasks.
Set the `timeout` argument of `InDesignServerClient` to compensate.